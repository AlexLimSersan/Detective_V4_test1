
from entities.entities.base import Mobile_Entity

from config.settings import ITEM_SPAWN_FREQUENCY, CLUE_SPAWN_FREQUENCY, EXIT_COMMANDS
from config.logging_config import ent_logger
from utilities.general_utils import match_command_to_option
from entities.descriptions.item_descriptions import Item_Descriptions

class Item(Mobile_Entity):
    # routine hack: event->move mobile entity wherever, then event descriptions-> can be tailored for that location. default is default routine
    def __init__(self, id, name, game_state, descriptions, spawn_data, state_data = None, components = None, item_type = None, entity_state="default", is_outdoors=False, current_location=None, spawn_frequency = ITEM_SPAWN_FREQUENCY, ):
        super().__init__(id, name, game_state, None, entity_state, is_outdoors, current_location)
        self.item_type = item_type
        self.descriptions = Item_Descriptions(id, name, entity_state, game_state, descriptions, current_location, is_outdoors)
        self.state_data = state_data
        self.spawn_data = spawn_data
        self.components = components
        self.spawn_frequency = spawn_frequency
    #need type for inv by type?
    def loop(self, ui):
        #approach and leave desc already shown
        ui.display(self.descriptions.set_scene())
        while True:
            actions = self.get_options()
            ui.display_menu(self.game_state, actions = actions)
            #you pick up, put down, ??
            command = ui.get_input()
            if self.components:
                if self.components.process_command(command, ui):
                    continue
            result = self.process_command(command, ui, actions = actions)
            if result:
                return result
            ui.bad_input()

    def process_command(self, command_id, ui, actions):
        if isinstance(actions, dict):
            actions = list(actions.keys())
        if command_id in EXIT_COMMANDS:
            return command_id  # game handles switching handlers
        matched_command, matched = match_command_to_option(command_id, self.game_state, actions = actions)
        if matched:
            if ui.confirm(matched_command, self.game_state):
                return matched_command
        return None

    def get_options(self):
        actions = {}
        if self.components:
            actions.update(self.components.get_options())
        actions["return"] = ""
        return actions

    def update_location(self):
        raise NotImplementedError
        #item move logic not defined, maybe later with player inventory and dropping, or suspects moving items, etc
        #self.game_state.location_manager.move_entity(self, loc_id)


class Clue(Item):
    def __init__(self, id, name, game_state, descriptions, spawn_data, state_data = None, components = None, item_type = None, entity_state="default", is_outdoors=False, current_location=None, spawn_frequency = CLUE_SPAWN_FREQUENCY, ):
        super().__init__(id, name, game_state, descriptions, spawn_data, state_data, components, item_type, entity_state, is_outdoors, current_location, None )
        self.spawn_frequency = spawn_frequency







