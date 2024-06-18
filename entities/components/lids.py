from entities.components.base import Interaction
from entities.descriptions.base import Descriptions
from abc import ABC, abstractmethod
from utilities.state_utils import iterate_states, iterate_keys
from utilities.command_utils import match_command_to_option
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from entities.components.locks import KeyLock, BoltLock

from game.game_state import Game_State

from config.logging_config import ent_logger

"""
self.id = id
        self.name = name
        self.entity_state = entity_state
        self.game_state = game_state
"""

class Lid(Interaction):
    def __init__(self, id, name, entity_state, game_state, is_outdoors, connections, component_descriptions = None, is_open = False, lock_mechanism = None):
        super().__init__(id, name, game_state, entity_state, is_outdoors)

        self.is_outdoors = is_outdoors
        self.connections = connections
        self.descriptions = component_descriptions #default: type(opened, closed, etc); key:description
        self.is_open = is_open
        self.lock_mechanism = self.create_lock_mechanism(lock_mechanism)
        assert isinstance(self.game_state, Game_State)

    def create_lock_mechanism(self, lock_mechanism):
        ent_logger.debug(f"creating lock mechanism {lock_mechanism}")
        if lock_mechanism:
            lock_type = lock_mechanism.get("lock_type")
            if lock_type == "key_lock":
                ent_logger.debug(f"LIDS.py/creating lock mechanism: {lock_mechanism}")
                return KeyLock(entity_state= self.entity_state, game_state= self.game_state, **lock_mechanism)
            elif lock_type == "bolt_lock":
                return BoltLock(entity_state= self.entity_state, game_state= self.game_state, **lock_mechanism)
            else:
                ent_logger.warning("ERROR MAKING LID - LOCK NOT RECOGNIZED")
        return None

    def get_description(self, type): #for at_entity
        ent_logger.debug(f"Lids.py/Get_description() ; starting. type = {type} \n lockmech = {self.lock_mechanism}")
        description = []
        if type in ["at_entity"]:
            if self.lock_mechanism:

                description.append(self.lock_mechanism.get_description(type))
                ent_logger.debug(f"lids at entity lock mechanism desc {description}")
            if self.is_open:
                #example specific desc = the wooden door hangs slightly open
                to_get = "opened"
                default = "It's open."
            else:

                to_get = "closed"
                default = "It's closed."

        elif type in ["opening"]:
            to_get = "opening"
            default = "The {name} swings open."

        elif type in ["closing"]:
            to_get = "closing"
            default = "The {name} swings shut."

        else:
            raise ValueError("lid get description; type not accounted for")
        ent_logger.debug(f"LIDS.PY/ GET_DESCRIPTION()  toget = {to_get}, iterating states on : {self.descriptions}")
        state_description_dic = iterate_states(self.game_state, self.entity_state, self.descriptions, to_get) if self.descriptions else None
        if state_description_dic:
            description.append(iterate_keys(self.game_state, state_description_dic))
        else:
            description.append(default.format(name=self.name))
        ent_logger.info(f"LIDS.PY/ GET_DESCRIPTION() type: {type} -  returning {description}")
        return description


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
        # Dictionary mapping commands to their corresponding methods
        option_handlers = {
            "open": self.open,
            "close": self.close,
            "lock": self.lock,
            "unlock": self.unlock,

        }

        # Check if the command is in the options and in the handler dictionary
        #if command in options and
        if command in option_handlers:
            # Call the corresponding method and pass the UI object
            option_handlers[command](ui)
            return True

        else: #COULD PASS ACTIONS HERE
            actual_options = list(self.get_options().keys()) #because it would correct to not actual options
            matched_command, matched = match_command_to_option(command, game_state=self.game_state, actions=actual_options)
            if matched:
                if ui.confirm(matched_command, self.game_state):
                    if matched_command in option_handlers:
                        # Call the corresponding method and pass the UI object
                        option_handlers[matched_command](ui)
                return True
            return False

    def enter(self, ui):
        if not self.is_open:
            ui.display(self.get_description("enter_closed"))


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



