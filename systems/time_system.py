
from config.settings import TICKER_MULTIPLIER, START_PHASE, PHASE_TIME_INTERVAL, ALL_PHASES
from config.logging_config import app_logger
#all times like move time, etc, here! i think its better 100%
class Time_System: #could add an event "late game" or similar, which can change descriptions accordingly
    def __init__(self, game_state):
        self.game_state = game_state
        self.ticker = 0 #tracks time, later can have the slow down time in option idea
        self.ticker_multiplier = TICKER_MULTIPLIER #can adjust speed of game as needed
        self.current_phase = START_PHASE
        self.all_phases = ALL_PHASES
        self.phase_time_interval = PHASE_TIME_INTERVAL #how long each phase is

    def elapse_time(self, time_value, ui):
        app_logger.info(f"time_system.py/elapsing time() : {time_value}")
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

        self.game_state.weather_system.roll_weather()
        #can have things like events, routines (remember hack).
        self.game_state.suspect_manager.update_entity_locations()
        ui.display(f"_____________________")
        ui.display(f"Time progresses... People move around you.\n #Current phase: {self.current_phase.capitalize()}")  # later will comment out
        ui.display(f"_____________________")
        ui.stall()

        """LIKE WEAHTER, NEED SOME WARNING/TRANSITION THING! TO ABRUPT FOR ROUTINES ESP EVENTS LIKE A SUSPECT VANISHES or appears in the room.."""
        #SUN, RAIN, TRANSITION ANNOUNCEMENT (THE SKY DARKENS, CLOUDS FORM, THE CLOUDS PART, THE RAIN starts to SLOWS DOWN...
        """
        simple like, it's almost nighttime.... halfway through the phase.and done need to stall..
        
        
        """



