#entities
from entities.entities.base import Entity
from entities.entities.items import Item
from entities.entities.suspects import Suspect
#descriptions
from entities.descriptions.loc_descriptions import Loc_Descriptions
#components
#utils
from utilities.general_utils import match_command_to_option, ids_to_names, names_to_ids
#commands and settings
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from config.logging_config import ent_logger

class Location(Entity):
    def __init__(self, id, name, game_state, descriptions, connections, entity_state = "default", is_outdoors=False):
        super().__init__(id, name, game_state, None, entity_state, is_outdoors)
        self.descriptions = Loc_Descriptions(id, name, entity_state, game_state, descriptions, is_outdoors)
        #connections
        self.connections = connections #can have door IDS!
        # entities present, managed in spawn
        self.suspects_present = {}
        self.items_present = {}

    def remove_entity(self, entity):
        """Remove entity from location"""
        if entity.id in self.suspects_present:
            del self.suspects_present[entity.id]
        elif entity.id in self.items_present:
            del self.items_present[entity.id]
        else:
            raise ValueError(f"Entity {entity.id} not found")

    def add_entity(self, entity_obj):
        if isinstance(entity_obj, Suspect):
            self.suspects_present[entity_obj.id] = entity_obj
        elif isinstance(entity_obj, Item):
            self.items_present[entity_obj.id] = entity_obj

    def get_connections(self):
        return self.connections

    def set_scene(self):
        scene_description = self.descriptions.set_scene(self.suspects_present, self.items_present, self.get_connections())
        return scene_description

    def start_loop(self, ui):
        #approaching in player move, because if command is mobile entity, you dont approach once done with entity loop
        ui.display(self.set_scene())
        ent_logger.debug("Locations start loop: entering self.loop()")
        matched_command = self.loop(ui)  # dialogue or interactions
        #leaving description in player move, because if command is item or sus, you dont leave!
        return matched_command

    def handle_command_id_list_logic(self, command_ids, locations):
        ent_logger.debug(f"LOCATIONS.PY/handling command_id_list_logic() COMMAND IDS: {command_ids}")
        if len(command_ids) == 1:
            return command_ids[0]
        #remove ids that are not in locations (which is current connections)
        command_ids = [id for id in command_ids if id in locations]
        # Flatten the list but avoid splitting strings into characters
        possible_ids = []
        for sublist in command_ids:
            if isinstance(sublist, list):
                possible_ids.extend(sublist)
            else:
                possible_ids.append(sublist)

        if not possible_ids:
            raise ValueError(
                "no possible ids, great.")
        if len(possible_ids) == 1:
            command_id = possible_ids[0]
            ent_logger.debug(f"LOCATIONS.PY/handlecommand_id_list_logic; possible ids {possible_ids}")
            return command_id
        elif len(possible_ids) > 1:
            possible_ids = [id for id in possible_ids if id != self.game_state.player.location_history[-2].id]
            if not len(possible_ids) == 1:
                raise ValueError(f"FFFFFFFFÙCK")
            ent_logger.debug(f"LOCATIONS.PY/handlecommand_id_list_logic; possible ids {possible_ids}")
            return possible_ids[0]
        else:
            raise ValueError("len of possible ids not accounted for")

    def loop(self, ui):  # command validation must be in loop, only break out if valid command
        while True:
            # get options returns ids, they are displayed as names
            suspects, items, locations, actions = self.get_options()
            ui.display_menu(self.game_state, suspects, items, locations, actions)

            command = ui.get_input()
            command_id = names_to_ids(command, self.game_state)  # returns a list

            ent_logger.debug(f"Locations.py/loop: command: {command};; command_id : {command_id}")

            # possibly multiple command_id matches, so handle which one here
            if isinstance(command_id, list):
                command_id = self.handle_command_id_list_logic(command_id, locations)

            result = self.process_command(command_id, ui, suspects, items, locations, actions)
            if result:
                if isinstance(result, list):
                    result = result[0]
                return result
            else:
                ui.bad_input()

    def process_command(self, command_id, ui, suspects, items, locations, actions):
        if isinstance(actions, dict):
            actions= list(actions.keys())

        if command_id in suspects + items + locations:# + actions: #no actions actually cause those go to door, doesnt change handler
            return command_id  # game handles switching handlers
        elif command_id in EXIT_COMMANDS or command_id in ENTER_COMMANDS:
            return self.handle_command_id_check_enter_or_exit(command_id)
        else:
            matched_command, matched = match_command_to_option(command_id, self.game_state, suspects, items, locations,
                                                               actions)
            if matched:
                if ui.confirm(matched_command, self.game_state):
                    if matched_command in EXIT_COMMANDS or matched_command in ENTER_COMMANDS:
                        return self.handle_command_id_check_enter_or_exit(matched_command)
                    return matched_command
        return None

    def handle_command_id_check_enter_or_exit(self, command_id):
        if command_id in EXIT_COMMANDS:
            previous_loc_id = self.game_state.player.location_history[-2].id
            if previous_loc_id in self.get_connections():
                return previous_loc_id
        elif command_id in ENTER_COMMANDS:
            return self.handle_enter_command_id()
    def handle_enter_command_id(self):
        # determine and move to "forward"
        ent_logger.debug(f"LOCATIONS loop:handle_enter_command_id; entering with enter commands ")
        previous_loc_id = self.game_state.player.location_history[-2].id
        current_loc_id = self.game_state.player.current_location.id

        connections = self.game_state.player.current_location.get_connections()

        possible_locations = []
        for connection_id in connections:
            # filter previous locations out of possible locations; you continue to location thats NOT behind
            if connection_id != previous_loc_id:
                possible_locations.append(connection_id)
        if len(possible_locations) == 1:
            ent_logger.debug(f"LOCATIONS loop:handle_enter_command_id; length possible locs == 1! returning {possible_locations[0]}")
            # if 1 possible location, return it
            return possible_locations[0]
        elif len(possible_locations) > 1:
            # if more than one
            ent_logger.debug("LOCATIONS loop:handle_enter_command_id; length possible locs above 1!")
            for id in possible_locations:
                # if the name is the same as current location name, return it (continue down dock, continue down alley, etc)
                possible_loc_name = ids_to_names(id, self.game_state)
                current_loc_name = self.game_state.player.current_location.name
                if current_loc_name == possible_loc_name:
                    ent_logger.debug(f"LOCATIONS loop:handle_enter_command_id; returning possible location {id}")
                    return id
        else:
            ent_logger.debug("LOCATIONS loop:handle_enter_command_id;returning NONE")
            return None
    def get_options(self):
        #returns options to display
        suspects = [suspect.id for suspect in self.suspects_present.values()]
        items = [item.id for item in self.items_present.values()]
        locations = self.get_connections()
        actions = [] #doors and other can overide like this

        return suspects, items, locations, actions


