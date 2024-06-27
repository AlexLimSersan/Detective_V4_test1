from entities.components.base import Interaction
from entities.descriptions.base import Descriptions
from abc import ABC, abstractmethod
from utilities.state_utils import iterate_states, iterate_vibe_keys
from utilities.command_utils import match_command_to_option
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from entities.components.locks import KeyLock, BoltLock

from game.game_state import Game_State

from config.logging_config import ent_logger
import random

class Lid(Interaction): #can refactor this for sure
    def __init__(self, id, name, entity_state, game_state, is_outdoors, connections, component_descriptions = None, is_open = False, lock_mechanism = None):
        super().__init__(id, name, game_state, entity_state, is_outdoors)
        self.is_outdoors = is_outdoors
        self.connections = connections
        self.descriptions = Descriptions(id, name, entity_state, game_state, component_descriptions, is_outdoors)
        self.is_open = is_open
        self.lock_mechanism = self.create_lock_mechanism(lock_mechanism)
        # Dictionary mapping commands to their corresponding methods
        self.option_handlers = {
            "open": self.open,
            "close": self.close,
            "lock": self.lock,
            "unlock": self.unlock,
        }
        assert isinstance(self.game_state, Game_State)

    def create_lock_mechanism(self, lock_mechanism):
        ent_logger.debug(f"creating lock mechanism {lock_mechanism}")
        if lock_mechanism:
            lock_type = lock_mechanism.get("lock_type")
            if lock_type == "key_lock":
                ent_logger.debug(f"LIDS.py/creating lock mechanism: {lock_mechanism}")
                return KeyLock(
                    id = lock_mechanism["id"],
                    name= lock_mechanism["name"],
                    key = lock_mechanism["key"],
                    game_state=self.game_state,
                    entity_state= self.entity_state,
                    is_outdoors = self.is_outdoors,
                    lock_type=lock_mechanism["lock_type"],
                    outside=lock_mechanism["outside"],
                    is_locked=lock_mechanism.get("is_locked", True),
                    lock_descriptions = lock_mechanism["lock_descriptions"]
                )
            elif lock_type == "bolt_lock":
                return BoltLock(entity_state= self.entity_state, game_state= self.game_state, **lock_mechanism)
            else:
                ent_logger.warning("ERROR MAKING LID - LOCK NOT RECOGNIZED")
        return None

    def get_description(self, description_type): #for at_entity
        ent_logger.debug(f"Lids.py/Get_description() ; starting. type = {description_type} \n lockmech = {self.lock_mechanism}")
        description = []
        to_get_dic = {
            "opened": "It's open.",
            "closed": "It's closed.",
            "opening": "The {name} swings open.",
            "closing": "The {name} swings shut."
        }
        if description_type in ["at_entity"]:
            if self.lock_mechanism:
                description.append(self.lock_mechanism.get_description(description_type))
                ent_logger.debug(f"lids at entity lock mechanism desc {description}")
            if self.is_open:
                #example specific desc = the wooden door hangs slightly open
                to_get_key = "opened"
            else:
                to_get_key = "closed"
        elif description_type in ["opening", "closing"]:
            to_get_key = description_type
        else:
            raise ValueError("lid get description; type not accounted for")
        result = None
        try:
            description_value = self.descriptions.get_description(to_get_key)
            if description_value:
                if isinstance(description_value, list):
                    description_value = random.choice(description_value)
                description.append(description_value)

                if description:
                    result = description

        finally:
            if result is None:
                result = [to_get_dic.get(to_get_key).format(name=self.name)]

        ent_logger.info(f"lids returning {result}, desc value {description_value} \n self.desc.desc {self.descriptions.descriptions}")
        return result

    def get_options(self):
        #remember, lid isnt directional
        options = {}
        if self.is_open:
            options["close"] = f"the {self.name}"
        else:
            options["open"] = f"the {self.name}"
            if self.lock_mechanism:
                lock_options = self.lock_mechanism.get_options()
                options.update(lock_options)
        return options

    def process_command(self, command, ui):
        if command in self.option_handlers:
            self.option_handlers[command](ui)
            return True
        else:
            current_options = list(self.get_options().keys()) # because else it would correct to all options
            matched_command, matched = match_command_to_option(command, game_state=self.game_state, actions=current_options)
            if matched:
                if ui.confirm(matched_command):
                    if matched_command in self.option_handlers:
                        self.option_handlers[matched_command](ui)
                return True
            #whimsicals possible here?
        return False

    def open(self, ui):
        if self.lock_mechanism and self.lock_mechanism.is_locked:
                text = self.lock_mechanism.get_description("cant_open")
                ui.display(text)
        elif not self.is_open:
            self.is_open = True
            text = self.get_description("opening")
            ui.display(text)
        else:
            ui.display("It's already open.")

    def close(self, ui):
        if self.is_open:
            self.is_open = False
            text = self.get_description("closing")
            ui.display(text)
        else:
            ui.display(f"It's already closed.")

    def lock(self, ui):
        # Define what happens when the player locks the door
        if self.is_open:
            ui.display("You can't lock it while its open.")
        elif not self.is_open and self.lock_mechanism:
            self.lock_mechanism.lock(ui)
        else:
            ui.display("There is no mechanism to lock")

    def unlock(self, ui):
        if self.is_open:
            ui.display("You cant unlock it while its open.")
        elif not self.is_open and self.lock_mechanism:
            self.lock_mechanism.unlock(ui)
        else:
            ui.display("There is no mechanism to unlock")



