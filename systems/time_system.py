
from config.settings import TICKER_MULTIPLIER, START_PHASE, PHASE_TIME_INTERVAL, ALL_PHASES

import logging
logger = logging.getLogger('my_game')
#all times like move time, etc, here! i think its better 100%
class Time_System:
    def __init__(self, game_state):
        self.game_state = game_state
        self.ticker = 0 #tracks time, later can have the slow down time in option idea
        self.ticker_multiplier = TICKER_MULTIPLIER #can adjust speed of game as needed
        self.current_phase = START_PHASE
        self.all_phases = ALL_PHASES
        self.phase_time_interval = PHASE_TIME_INTERVAL #how long each phase is



    def elapse_time(self, time_value, ui):
        logger.warning(f"time_system.py/elapsing time() : {time_value}")
        # Elapse time by the given value multiplied by the ticker multiplier
        self.ticker += time_value * self.ticker_multiplier
        # Check if the ticker has reached the interval to progress the phase
        while self.ticker >= self.phase_time_interval:
            self.progress_phase(ui)
            self.ticker -= self.phase_time_interval

    def progress_phase(self, ui):

        # Find the index of the current phase and move to the next phase
        current_index = self.all_phases.index(self.current_phase)
        next_index = (current_index + 1) % len(self.all_phases)
        #progress phase
        self.current_phase = self.all_phases[next_index]
        ui.display(f"Time phase has progressed to: {self.current_phase}") #later will comment out
        self.game_state.weather_system.roll_weather()
        #can have things like events, routines (remember hack).
        self.game_state.suspect_manager.update_entity_locations()
        # Routines could be a  class which just moves entities based on time and syncs event_ids or state_ids
        ui.display(f"PEOPLE MOOOOOVEEEE")



