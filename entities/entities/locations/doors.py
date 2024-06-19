from entities.components.lids import Lid
from entities.descriptions.loc_descriptions import Door_Descriptions
from entities.entities.locations.locations import Location
from utilities.general_utils import names_to_ids
from utilities.command_utils import get_command
from config.logging_config import ent_logger

class Door(Location): #NEED TO SET SCENE FOR CONNECTIONS? WHEN DOOR IS OPEN.
    def __init__(self, id, name, game_state, descriptions, connections, component_descriptions = None, is_open=False, lock_mechanism = None, entity_state = "default", is_outdoors=False):
        super().__init__(id, name, game_state, None, connections, entity_state, is_outdoors)
        # uses loc descriptions, should still work. state is things like default, burned, broken, etc.
        self.components = Lid(id, name, entity_state, game_state, is_outdoors, connections, component_descriptions, is_open, lock_mechanism)
        self.descriptions = Door_Descriptions(id, name, entity_state, game_state, descriptions, is_outdoors, lid_component=self.components)
        self.whimsical_handlers = {
            "enter": self.bump
        }
    def get_connections(self):
        if self.components.is_open:
            return self.connections
        else:
            return [self.game_state.player.location_history[-2].id] #location player came from!

    def loop(self, ui):
        while True:
            suspects, items, locations, actions = self.get_options()
            # Door locations are displayed as actions (enter, return) ; locations still used for moving/connections
            ui.display_menu(suspects, items, None, actions)
            #get all ids that you want to pass to components as actions
            actions = list(self.components.option_handlers.keys())
            command_id = get_command(ui, self.game_state)
            result = self.process_command(command_id, ui, suspects, items, locations, actions)
            if result:
                return result
            elif command_id in self.whimsical_handlers:
                self.whimsical_handlers[command_id](ui)
            ui.display(self.descriptions.set_scene(self.suspects_present, self.items_present, self.get_connections()))

    def process_action(self, command_id, ui):
        if self.components.process_command(command_id, ui):
            #possible door specific logic here
            pass
    def get_actions(self):
        actions = {}
        # handling front end enter/return type stuff:
        # get leads to and add to actions
        connections = self.get_connections()

        player_last_loc_id = self.game_state.player.location_history[-2].id
        for connection in connections:
            if connection != player_last_loc_id:
                actions["Enter"] = f"{connection}"
        actions.update(self.components.get_options())
        actions[player_last_loc_id] = ""  # formatting handled in UI
        # no connection locations for doors, all in actions!
        return actions

    def bump(self, ui):
        if not self.components.is_open:
            bump_text = self.descriptions.get_description(f"enter") or f"You bump into the {self.name}."
            ui.display(bump_text)
