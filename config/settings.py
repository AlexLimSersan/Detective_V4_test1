# Game Settings
#PLAYER
PLAYER_STARTING_LOCATION = "cab_01"
#TIME SYSTEM
START_PHASE = "morning"
ALL_PHASES = ["morning", "afternoon", "evening", "night"]
TICKER_MULTIPLIER = 1
PHASE_TIME_INTERVAL = 30 #time between phases
#ACTION TIME
MOVE_TIME = 2
#speak time, interact time

#WEATHER SYSTEM
START_WEATHERS = ["sun"]
""" 
weather notes:
GOOD
    sunny = sunny and clear
NEUTRAL, BAD
    grey = chilly + grey
    rain = rain + storm
"""
#GOING TO CHANGE: sun, rain, and storm. with a TRANSITION ANNOUNCEMENT...
#like the clouds darken, etc. maybe 2 announcements if detectable before changing.
#can have references to rain in the sun, but sparingly.
ALL_WEATHERS = ["sun", "rain"]# "grey",
GOOD_WEATHER = ["sun"]

#SPAWN DATA DEFAULT VALUES
CLUE_SPAWN_FREQUENCY = 0.8
ITEM_SPAWN_FREQUENCY = 1
ITEM_STATE_FREQUENCY = 0.8


# Mood Keys
"""Range is from [-10, 10]"""
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
EXIT_COMMANDS = ["return", "leave", "exit", "back","b"]
ENTER_COMMANDS = ["enter", "go", "continue", "forward", "down", "cont", "walk", "climb", "up", "e"]