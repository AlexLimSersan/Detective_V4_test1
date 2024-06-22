#entities
from entities.entities.base import Entity
from entities.entities.items import Item
from entities.entities.suspects import Suspect
#descriptions
from entities.descriptions.loc_descriptions import Loc_Descriptions
#components
#utils
from utilities.general_utils import ids_to_names, names_to_ids, flatten_list
from utilities.command_utils import get_command, match_command_to_option, handle_command_id_list_logic
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
    def get_actions(self):
        return {}
    def get_options(self):
        # returns options to display
        suspects = [suspect.id for suspect in self.suspects_present.values()]
        items = [item.id for item in self.items_present.values()]
        locations = self.get_connections()
        actions = self.get_actions()  # doors and other can overide like this
        # display option in options -> option = (entitymanager.get(option) or option) -> hasattr(option, na entity, if entity
        # should return option map? then:
        # get command ; if command in option map, return command, else fuzzy matching with option map.
        # return match or None
        # if not process command, bad input
        return suspects, items, locations, actions

    def start_loop(self, ui):
        ui.display(self.descriptions.set_scene(self.suspects_present, self.items_present, self.get_connections()))
        matched_command = self.loop(ui)  # dialogue or interactions
        return matched_command

    def loop(self, ui):  # command validation must be in loop, only break out if valid command
        while True:
            suspects, items, locations, actions = self.get_options()
            ui.display_menu(suspects, items, locations, actions)

            command_id = get_command(ui, self.game_state)
            result = self.process_command(command_id, ui, suspects, items, locations, actions)
            if result:
                return result
            elif command_id in self.whimsical_handlers:
                self.whimsical_handlers[command_id](ui)

    def process_command(self, command, ui, suspects = None, items = None, locations = None, actions = None):
        suspects = suspects or []
        items = items or []
        locations = locations or []
        actions = actions or []

        command_id = names_to_ids(command, self.game_state)  # returns a list

        # possibly multiple command_id matches, so handle which one here
        if isinstance(command_id, list):
            command_id = handle_command_id_list_logic(command_id, self.game_state)

        # RETURN COMMAND TO CHANGE HANDLER
        if command_id in suspects + items + locations:
            return command_id
        elif command_id in actions:
            return self.process_action(command_id, ui)
        elif command_id in EXIT_COMMANDS or command_id in ENTER_COMMANDS:
            return self.handle_command_id_check_enter_or_exit(command_id, ui)
            #if result:
            #    return result
        else:
            matched_command, matched = match_command_to_option(command, self.game_state,
                                                               suspects, items, locations, actions)
            if matched:
                if ui.confirm(matched_command):
                    ent_logger.info(f"confirmed matched {matched_command}, actions = {actions}")
                    return self.process_command(matched_command, ui, suspects, items, locations, actions)
                else:
                    return None
        ui.bad_input()
    def process_action(self, command_id, ui):
        pass
    def handle_command_id_check_enter_or_exit(self, command_id, ui):
        if command_id in EXIT_COMMANDS:
            previous_loc_id = self.game_state.player.location_history[-2].id
            if previous_loc_id in self.get_connections():
                return previous_loc_id
        elif command_id in ENTER_COMMANDS:
            return self.handle_enter_command_logic(ui)

    def handle_enter_command_logic(self, ui):
        # determine and move to "forward"
        ent_logger.debug(f"LOCATIONS loop:handle_enter_command_id; entering with enter commands ")
        previous_loc_id = self.game_state.player.location_history[-2].id
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
            ent_logger.debug(f"LOCATIONS loop:handle_enter_command_id; length possible locs above 1! \n {possible_locations}")
            for id in possible_locations:
                #enter commands will choose the ids that have the same name as current location name. example: continue down dock, continue down alley, etc
                possible_loc_name = ids_to_names(id, self.game_state)
                current_loc_name = self.game_state.player.current_location.name
                if current_loc_name == possible_loc_name:
                    ent_logger.debug(f"LOCATIONS loop:handle_enter_command_id; returning possible location {id}")
                    return id
            ui.bad_input()
        else:
            ent_logger.debug("LOCATIONS loop:handle_enter_command_id;returning NONE")
            return None
