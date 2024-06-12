
from config.settings import EXIT_COMMANDS, ENTER_COMMANDS

#CHECK EVENTS ALWAYS AFTER A PLAYER INPUT, U CAN INTERRUPT IMMEDIATELY AND THEN CALL WHATEVER IS NEEDED AFTER

import logging

logger = logging.getLogger('my_game')

class Game:
    def __init__(self, game_state, ui):
        self.game_state = game_state
        self.ui = ui

    def run(self):
        # intro sequence
        logger.debug("running game")
        while True:
            self.exploration_handler()  # time/effects directly change gamestate; causes effects
        #outro sequence



    def exploration_handler(self):
        while True:
            #only locations break loop by returning command - is that true?

            matched_command = self.game_state.player.current_location.start_loop(self.ui) #handles approach/leave descriptiosn

            # should CHECK EVENTS HERE so can break before regular processing happens
            self.game_state.event_system.check_events()
            logger.debug(f"Game.game matched command is {matched_command}")

            if matched_command in self.game_state.player.current_location.get_connections():

                self.game_state.player.move(matched_command, self.ui)
                break
            elif matched_command in self.game_state.player.current_location.suspects_present:
                self.dialogue_handler(matched_command)
                break
            elif matched_command in self.game_state.player.current_location.items_present:
                self.item_handler(matched_command)
                break
            else:
                # handle whimsical command
                raise ValueError("validated command with no handler")

    def dialogue_handler(self, command_id):
        # check with player first to verify breaking convo, to prevent mistakes from choosing topic
        #announce here?
        try:
            current_suspect = self.game_state.suspect_manager.get_entity(command_id)
            logger.debug(f"game.game sus handler starting loop with {current_suspect.id}")
            current_suspect.start_loop(self.ui)

        except:
            # should not be passed if not validated
            raise ValueError("ERROR: ID passed to dialogue handler, no matching object")

    def item_handler(self, command_id):
        try:

            current_item = self.game_state.item_manager.get_entity(command_id)
            logger.debug(f"game.game item handler starting loop with {current_item.id}")
            current_item.start_loop(self.ui)

        except:
            # should not be passed if not validated
            raise ValueError("ERROR: ID passed to item handler, no matching object")
