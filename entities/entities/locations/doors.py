from entities.components.lids import Lid
from entities.descriptions.loc_descriptions import Door_Descriptions
from entities.entities.locations.locations import Location
from utilities.general_utils import names_to_ids
from config.logging_config import ent_logger

class Door(Location): #NEED TO SET SCENE FOR CONNECTIONS? WHEN DOOR IS OPEN.
    def __init__(self, id, name, game_state, descriptions, connections, component_descriptions = None, is_open=False, lock_mechanism = None, entity_state = "default", is_outdoors=False):
        super().__init__(id, name, game_state, None, connections, entity_state, is_outdoors)
        # uses loc descriptions, should still work. state is things like default, burned, broken, etc.
        self.components = Lid(id, name, entity_state, game_state, is_outdoors, connections, component_descriptions, is_open, lock_mechanism)
        self.descriptions = Door_Descriptions(id, name, entity_state, game_state, descriptions, is_outdoors, lid_component=self.components)

    def get_connections(self):
        if self.components.is_open:
            return self.connections
        else:
            return [self.game_state.player.location_history[-2].id] #location player came from!

    def start_loop(self, ui):
        #approaching in player move, because if command is mobile entity, you dont approach once done with entity loop
        ui.display(self.set_scene())
        ent_logger.debug("Locations start loop: entering self.loop()")
        matched_command = self.loop(ui)  # dialogue or interactions
        #leaving description in player move, because if command is item or sus, you dont leave!
        return matched_command

    def loop(self, ui):
        while True:

            suspects, items, locations, actions = self.get_options()

            # options are ids; always pass ids to ui
            ui.display_menu(self.game_state, suspects, items, locations, actions)
            command = ui.get_input()
            command_id = names_to_ids(command, self.game_state)
            ent_logger.debug(f"DOORS.py/loop: command_id : {command_id}")
            locations = self.get_connections()

            if isinstance(command_id, list):
                command_id = self.handle_command_id_list_logic(command_id, locations)

            if self.components.process_command(command_id, ui): #need to handle action matching in components, then skip action matching here
                for connection in self.get_connections():
                    if connection != self.game_state.player.location_history[-2].id:
                        conn_obj = self.game_state.location_manager.get_entity(connection)

                        ui.display(conn_obj.descriptions.get_connection_descriptions(self.id))

            else:

                result = self.process_command(command_id, ui, suspects, items, locations, actions)
                #if u want could override the enter checker here for descs
                ent_logger.debug(f"DOOR/LOOP() result = {result}")
                if isinstance(result, list):
                    result = self.handle_command_id_list_logic(result, locations)
                ent_logger.info(f"result: {result}")
                #RESULT HANDLING
                whimsical_handlers = {"enter": self.bump}
                if result:
                    return result
                elif command_id in whimsical_handlers:
                    whimsical_handlers[command_id](ui)
                    #THIS IS WHERE YOU WOULD HANDLE WHIMSICALS! (there wouldnt be a result)
                else:
                    ui.bad_input()

    def get_options(self):#can have items or suspects at doors this way
        # returns options to display
        suspects = [suspect.id for suspect in self.suspects_present.values()]
        items = [item.id for item in self.items_present.values()]
        locations = None #for doors, all in actions
        actions = {}

        #handling front end enter/return type stuff:
        #get leads to and add to actions
        connections = self.get_connections()

        player_last_loc_id = self.game_state.player.location_history[-2].id
        ent_logger.debug(f"door connections :{connections}, playerlastloc id {player_last_loc_id}")
        for connection in connections:
            if connection != player_last_loc_id:
                actions["Enter"] = f"{connection}" #formatting handled in UI
        actions.update(self.components.get_options())
        actions[player_last_loc_id] = "" #formatting handled in UI
        ent_logger.debug(f"doors.py/getoptions {actions}")
        #no connection locations for doors, all in actions!
        return suspects, items, locations, actions

    def bump(self, ui):
        if not self.components.is_open:
            bump_text = self.descriptions.get_description(f"enter") or f"You bump into the {self.name}."
            ui.display(bump_text)
