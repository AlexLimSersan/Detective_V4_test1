
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS

#CHECK EVENTS ALWAYS AFTER A PLAYER INPUT, U CAN INTERRUPT IMMEDIATELY AND THEN CALL WHATEVER IS NEEDED AFTER
from config.logging_config import app_logger

class Game:
    def __init__(self, game_state, ui):
        self.game_state = game_state
        self.ui = ui
        self._current_handler = None

    @property
    def current_handler(self):
        return self._current_handler

    @current_handler.setter
    def current_handler(self, handler_name):
        self._current_handler = handler_name
        self.game_state.current_handler = handler_name
    def run(self):
        # intro sequence
        self.exploration_handler()  # time/effects directly change gamestate; causes effects

        #outro sequence

    def exploration_handler(self):
        self.current_handler = "location"
        while True:
            #only locations break loop by returning command - is that true?

            matched_command = self.game_state.player.current_location.start_loop(self.ui) #handles approach/leave descriptiosn

            # should CHECK EVENTS HERE so can break before regular processing happens
            self.game_state.event_system.check_events()
            #only announce here
            if matched_command in self.game_state.player.current_location.get_connections():
                self.ui.announce("moving_player", matched_command)
                self.game_state.player.move(matched_command, self.ui)

            elif matched_command in self.game_state.player.current_location.suspects_present:
                self.ui.announce("talking", matched_command)
                self.dialogue_handler(matched_command)

            elif matched_command in self.game_state.player.current_location.items_present:
                self.ui.announce("interacting", matched_command)
                self.item_handler(matched_command)

            elif matched_command == "EXIT_GAME":
                break
            else:
                # handle whimsical command
                raise ValueError(f"validated command with no handler: {matched_command}")

    def dialogue_handler(self, command_id):
        self.current_handler = "suspect"
        try:
            current_suspect = self.game_state.suspect_manager.get_entity(command_id)
            current_suspect.start_loop(self.ui)
        except:
            # should not be passed if not validated
            raise ValueError("ERROR: ID passed to dialogue handler, no matching object")

    def item_handler(self, command_id):
        self.current_handler = "item"
        try:
            current_item = self.game_state.item_manager.get_entity(command_id)
            current_item.start_loop(self.ui)
        except:
            # should not be passed if not validated
            raise ValueError("ERROR: ID passed to item handler, no matching object")
