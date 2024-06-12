from entities.components.base import Interaction
from entities.descriptions.base import Descriptions
from abc import ABC, abstractmethod
from utilities.state_utils import iterate_states, iterate_keys
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS

from config.logging_config import ent_logger

class LockMechanism(ABC):
    def __init__(self, name, game_state, entity_state, lock_type, outside, is_locked = True, lock_descriptions = None, ):
        self.name = name
        self.game_state = game_state
        self.entity_state = entity_state
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
    def __init__(self, name, key, game_state, entity_state, lock_type, outside, is_locked = True, lock_descriptions = None, ):
        super().__init__(name, game_state, entity_state, lock_type, outside, is_locked, lock_descriptions)
        self.key = key #id for key needed to open from lock_side

    def get_description(self, description_type):
        ent_logger.debug(f"LOCKS.PY/KEYLOCK/get_description() description_type = {description_type}")
        #ALREADY ITERATED STATES IN LID
        player_side = self.game_state.player.location_history[-2].id
        default_descriptions = {
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



        to_get = description_type
        if description_type == "at_entity":
            if player_side == self.outside:
                to_get = "outside_locked" if self.is_locked else "outside_unlocked"
            else:
                to_get = "inside_locked" if self.is_locked else "inside_unlocked"
        ent_logger.debug(f"toget = {to_get}\n descriptions = {self.descriptions}")
        state_description_dic = iterate_states(self.game_state, self.entity_state, self.descriptions, to_get)
        if state_description_dic:
            description = iterate_keys(self.game_state, state_description_dic)
            return description
        else:
            desc = default_descriptions.get(to_get)
            if not desc:
                ent_logger.warning(f"LOCK/GET_descriptin - no default desc !! keys get desc ")
            return desc

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
            command_id = self.game_state.player.ask_inv_type("key", ui)
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
