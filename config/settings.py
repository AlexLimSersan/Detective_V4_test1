# Game Settings
#PLAYER
PLAYER_STARTING_LOCATION = "cab_01"
#TIME SYSTEM
START_PHASE = "morning"
ALL_PHASES = ["morning", "midday", "evening", "night"]
TICKER_MULTIPLIER = 1
PHASE_TIME_INTERVAL = 10 #time between phases
#ACTION TIME
MOVE_TIME = 2
#speak time, interact time

#WEATHER SYSTEM
START_WEATHERS = ["sunny"]
""" 
weather notes:
GOOD
    sunny = sunny and clear
NEUTRAL, BAD
    grey = chilly + grey
    rain = rain + storm
"""
ALL_WEATHERS = ["sunny", "grey", "rain"]
GOOD_WEATHER = ["sunny"]

#SPAWN DATA DEFAULT VALUES
CLUE_SPAWN_FREQUENCY = 0.8
ITEM_SPAWN_FREQUENCY = 1
ITEM_STATE_FREQUENCY = 0.8


# Mood Keys
AMBIANCE_KEYS = ['good', 'neutral', 'bad']
AMBIANCE_VALUES = {'good': 10, 'neutral': 0, 'bad': -10}
DEFAULT_STARTING_AMBIANCE = 0
#SUSPECTS
SUSPECT_STARTING_MOOD = 0
MURDER_STRESS_MULTIPLIER = 2

#EVENTS
EVENT_TRIGGER_CAP = 2 #before murder!


# UI SETTINGS
MESSAGE_SLEEP_TIME = 0.4
# Command Identifiers
EXIT_COMMANDS = ["return", "leave", "exit", "back", "turn"]
ENTER_COMMANDS = ["enter", "go", "continue", "forward", "down", "cont", "walk"]