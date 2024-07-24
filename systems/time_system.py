
from config.settings import TICKER_MULTIPLIER, START_PHASE, PHASE_TIME_INTERVAL, ALL_PHASES
from config.logging_config import app_logger
#all times like move time, etc, here! i think its better 100%
import random


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
        self.display_weather_change(ui)

    def display_weather_change(self, ui):
        if self.game_state.weather_system.current_weather == "sun":
            if self.game_state.weather_system.weather_history[-2] == "sun":
                if self.current_phase == "night":
                    ui.display(random.choice([f"The moon shines brightly overhead...",
                               f"The clouds clear, and the stars come out..."]))
                else:
                    ui.display(random.choice([f"The sun beats down overhead...",
                               f"The sun shines brightly above..."]))
            else:
                ui.display(random.choice([f"The clouds part, and the rain dwindles...",
                                          f"The sun comes out, and the rain stops...",
                                          f"The rain stops, and the sun comes out..."]))
        else:
            if self.game_state.weather_system.weather_history[-2] == "sun":
                ui.display(random.choice([f"The clouds darken... It begins to rain.",
                           f"Rain clouds form overhead, obscuring the sun..."]))
            else:
                if self.game_state.weather_system.current_weather == "storm":
                    ui.display(random.choice([f"The rain worsens...",f"The rain intensifies..."]))
                else:
                    ui.display(random.choice([f"The rain continues...",
                               f"The rain shows no signs of stopping..."]))






