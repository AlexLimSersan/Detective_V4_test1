from entities.components.base import Interaction
from entities.descriptions.base import Descriptions
from abc import ABC, abstractmethod
from utilities.state_utils import iterate_states, iterate_vibe_keys
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS

from config.logging_config import ent_logger

class LockMechanism(ABC):
    def __init__(self, id, name, game_state, entity_state, is_outdoors, lock_type, outside, is_locked = True, lock_descriptions = None, ):
        self.id = id
        self.name = name
        self.game_state = game_state
        self.entity_state = entity_state
        self.is_outdoors = is_outdoors
        self.lock_type = lock_type
        self.outside = outside #loc id the side the mechanism is NOT on. if accessed from this side, you cant just turn the knob
        self.is_locked = is_locked
        self.descriptions = lock_descriptions or {} #action:description pairs, check this else return default scattered below
        ent_logger.debug(f"LOCK MECHANISM DESCRIPTIONS = {self.descriptions}, lock desc = {lock_descriptions}")

    @abstractmethod
    def get_description(self, type):
        pass
    @abstractmethod
    def get_options(self):
        pass
    @abstractmethod
    def lock(self, ui):
        pass
    @abstractmethod
    def unlock(self, ui):
        pass



class KeyLock(LockMechanism): #only keylocks for now. maybe padlocks later
    def __init__(self, id, name, key, game_state, entity_state, is_outdoors, lock_type, outside, is_locked = True, lock_descriptions = None, ):
        super().__init__(id, name, game_state, entity_state, is_outdoors, lock_type, outside, is_locked, None)
        self.key = key #id for key needed to open from lock_side
        self.descriptions = Descriptions(id, name, entity_state, game_state, lock_descriptions, is_outdoors)
        self.default_descriptions = {
            "outside_locking": "You turn the key, locking it.",
            "outside_unlocking": "You turn the key. It unlocks.",
            "inside_locking": "You turn the knob to the lock position.",
            "inside_unlocking": "You turn the knob to the unlock position.",

            "cant_open": "It's locked.",
            "key_dont_fit": "The key doesn't fit.",

            "already_locked": "It's already locked.",
            "already_unlocked": "It's already unlocked.",


            "outside_locked": "It's locked. The keyhole faces you.",
            "outside_unlocked": "It's unlocked.",
            "inside_locked": "The knob is in the lock position.",
            "inside_unlocked": "The knob is in the unlock position."
        }

    def get_description(self, description_type): #could work in lock mechanism base class
        ent_logger.debug(f"LOCKS.PY/KEYLOCK/get_description() description_type = {description_type}")
        player_side = self.game_state.player.location_history[-2].id

        if description_type != "at_entity":
            raise ValueError(f"locks.get_description no matching description type {description_type}")
        if player_side == self.outside:
            description_type = "outside_locked" if self.is_locked else "outside_unlocked"
        else:
            description_type = "inside_locked" if self.is_locked else "inside_unlocked"

        description = self.descriptions.get_description(description_type)
        ent_logger.debug(f"keylock/get desc, toget = {description_type}\n descriptions = {description}")
        return description or self.default_descriptions.get(description_type)

    def get_options(self):
        player_side = self.game_state.player.location_history[-2].id
        if player_side == self.outside:
            if self.is_locked:
                return {"unlock": "choose key..."}
            else:
                return {"lock": "choose key..."}
        else:
            if self.is_locked:
                return {"unlock": "turn knob"}  # or none if bolt lock
            else:
                return {"lock": "turn knob"}

    def lock(self, ui):
        player_side = self.game_state.player.location_history[-2].id
        text = None

        if self.is_locked:
            text = self.get_description("already_locked")
            ui.display(text)
            return

        if player_side == self.outside:
            command_id = self.game_state.player.ask_inv_type("key", ui)
            if command_id != self.key:
                text = self.get_description("key_dont_fit")
                ui.display(text)
                return
            else:
                text = self.get_description("outside_locking")
        if not text:
            text = self.get_description("inside_locking")

        self.is_locked = True
        ui.display(text)

    def unlock(self, ui):
        player_side = self.game_state.player.location_history[-2].id

        if not self.is_locked:
            text = self.get_description("already_unlocked")
            ui.display(text)
            return

        if player_side == self.outside:
            command_id = self.game_state.player.ask_inv_type(ui, "key")
            if not command_id:
                return
            if command_id == self.key:
                ui.announce(command_id, self.lock_type)
                text = self.get_description("outside_unlocking")
            else:
                ui.display(f"{command_id} doesn't fit.")
                return
        else:
            text = self.get_description("inside_unlocking")

        self.is_locked = False
        ui.display(text)


class BoltLock(LockMechanism):
    def __init__(self, name, game_state, entity_state, lock_type, outside, lock_descriptions = None, is_locked = True):
        super().__init__(name, game_state, entity_state, lock_type, outside, lock_descriptions, is_locked)
        #not implemented yet
