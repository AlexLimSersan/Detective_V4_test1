
from entities.entities.base import Mobile_Entity
from entities.entities.suspects import Suspect
from config.settings import ITEM_SPAWN_FREQUENCY, CLUE_SPAWN_FREQUENCY, EXIT_COMMANDS, ITEM_STATE_FREQUENCY
from config.logging_config import ent_logger
from utilities.command_utils import match_command_to_option
from entities.descriptions.item_descriptions import Item_Descriptions
import random
from entities.components.lids import Lid
from entities.components.locks import KeyLock
from utilities.general_utils import names_to_ids

class Item(Mobile_Entity):
    # routine hack: event->move mobile entity wherever, then event descriptions-> can be tailored for that location. default is default routine
    def __init__(self, id, name, game_state, descriptions, spawn_data, state_data = None, components = None, item_type = None, entity_state="default", is_outdoors=False, current_location=None, spawn_frequency = ITEM_SPAWN_FREQUENCY, ):
        super().__init__(id, name, game_state, None, entity_state, is_outdoors, current_location)
        self.item_type = item_type#need type for inv by type?
        self.descriptions = Item_Descriptions(id, name, entity_state, game_state, descriptions, current_location, is_outdoors)
        self.state_data = state_data
        self.spawn_data = spawn_data
        self.components = components
        self.spawn_frequency = spawn_frequency
        self.entity_state = self.determine_state() #this is actually irrelevant outside of initialization due to iterate states?

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

    def determine_state(self):
        for state, data in self.state_data.items():
            if random.random() <= data.get("frequency", ITEM_STATE_FREQUENCY):
                if state != "default" and self.game_state.item_manager.check_conditions(data.get("conditions", {}), self.id, "state", state):
                    return state
        return "default"

    def start_loop(self, ui):
        ui.display(self.descriptions.get_description("approaching", optional_key=self.game_state.current_handler))
        ui.beat()
        self.add_player_topic()
        matched_command = self.loop(ui) #dialogue or interactions
        ui.display(self.descriptions.get_description("leaving", optional_key=self.game_state.current_handler))
        ui.beat()
        return matched_command

    def set_scene(self):
        scene_desc = []
        if self.components:
            comp_desc = self.components.get_description("at_entity")
            if comp_desc:
                scene_desc.append(comp_desc)
        scene_desc.append(self.descriptions.set_scene(self.suspects_present, self.items_present, optional_key=self.id))
        return scene_desc

    def loop(self, ui):
        #approach and leave desc already shown

        while True:
            ui.display(self.set_scene())
            actions = self.get_options()
            ui.display_menu_type_2(options = actions, title=self.name)
            #you pick up, put down, ??
            command = ui.get_input()
            if self.components:
                if self.components.process_command(command, ui):
                    ent_logger.debug(f"components processed {command}")
                    continue
            result = self.process_command(command, ui, actions = actions)
            if result == "pass":
                continue
            if result:
                return result
            ui.bad_input()

    def process_command(self, command, ui, actions):
        command_id = names_to_ids(command, self.game_state)
        if isinstance(command_id, list):
            command_id = command_id[0]
        if isinstance(actions, dict):
            actions = list(actions.keys())
        ent_logger.debug(f"com {command}, com id {command_id}, actions {actions}")
        if command_id in EXIT_COMMANDS:
            return command_id  # game handles switching handlers
        elif command_id in actions:
            ent_logger.debug(f"command id {command_id} in actions {actions}")
            if command_id in self.items_present:
                self.items_present[command_id].start_loop(ui)
                return "pass"
        matched_command, matched = match_command_to_option(command, self.game_state, actions = actions)
        if matched:
            if ui.confirm(matched_command):
                return self.process_command(matched_command, ui, actions)
        return None

    def get_options(self):
        actions = {}

        if self.items_present:
            for item_id, obj in self.items_present.items():
                actions[item_id] = "_None"
        if self.components:
            actions.update(self.components.get_options())
        actions["return"] = ""
        return actions #ITERATE OVER ITEMS PRESENT! THEN DRAWERS OVERWRITES IT COMPONENTS IS OPEN

    def update_location(self):
        raise NotImplementedError
        #item move logic not defined, maybe later with player inventory and dropping, or suspects moving items, etc
        #self.game_state.location_manager.move_entity(self, loc_id)


class Clue(Item):
    def __init__(self, id, name, game_state, descriptions, spawn_data, state_data = None, components = None, item_type = None, entity_state="default", is_outdoors=False, current_location=None, spawn_frequency = CLUE_SPAWN_FREQUENCY, ):
        super().__init__(id, name, game_state, descriptions, spawn_data, state_data, components, item_type, entity_state, is_outdoors, current_location, None )
        self.spawn_frequency = spawn_frequency

class Drawer(Item):
    def __init__(self, id, name, game_state, descriptions, spawn_data, state_data=None, components=None, item_type=None,
                 entity_state="default", is_outdoors=False, current_location=None, spawn_frequency=1):
        super().__init__(id, name, game_state, descriptions, spawn_data, state_data, components, item_type,
                         entity_state, is_outdoors, current_location, spawn_frequency)

        # Ensure 'components' is a dictionary with necessary keys
        if components is None:
            components = {"component_descriptions": {}, "lock_mechanism": None}

        # Initialize self.components as a Lid object
        self.components = Lid(
            id,
            components.get("name", self.name),
            entity_state,
            game_state,
            is_outdoors,
            None,
            component_descriptions=components.get("component_descriptions", {}),
            is_open=False,
            lock_mechanism=components.get("lock_mechanism", None)
        )
        self.descriptions.component = self.components
        assert isinstance(self.components, Lid)


    def get_options(self):
        actions = {}
        if self.components.is_open:
            if self.items_present:
                for item_id, obj in self.items_present.items():
                    actions[item_id] =  "_None"
        actions.update(self.components.get_options())
        actions["return"] = ""
        return actions  # ITERATE OVER ITEMS PRESENT! THEN DRAWERS OVERWRITES IT COMPONENTS IS OPEN
