
import random

from config.settings import START_WEATHERS, ALL_WEATHERS, GOOD_WEATHER
import logging
# Get the logger configured in the main script
logger = logging.getLogger('my_game')

class Weather_System:
    def __init__(self, weather_data, game_state):
        #weather attributes
        self._current_weather = random.choice(START_WEATHERS)
        self.all_weathers = ALL_WEATHERS
        self.good_weathers = GOOD_WEATHER
        #weather descriptions
        self.weather_descriptions = weather_data
        #gamestate
        self.game_state = game_state

    @property
    def current_weather(self):
        return self._current_weather

    @current_weather.setter
    def current_weather(self, value):
        if value in self.all_weathers:
            self._current_weather = value
            logger.info(f"Setting weather: {value}")
        else:
            raise ValueError(f"Invalid weather type: {value}")

    def set_weather(self, new_weather):
        self.current_weather = new_weather


    def roll_weather(self):
        chance = random.random()
        logger.info(f"weather system generating chance: {chance}") #for now, will comment out later
        if chance < 0.8:
            keys = self.game_state.vibe_system.ranked_keys
            #if current gamevibe is good
            if keys[0] == "good":
                new_weather = random.choice(self.good_weathers)
            else:
                not_good_weathers = [weather for weather in self.all_weathers if weather not in self.good_weathers]
                new_weather = random.choice(not_good_weathers)
        else:
            new_weather = random.choice(self.all_weathers)
        self.current_weather = new_weather

    def decorate_tags(self, description_tags):
        logger.info(f"weather_system decorate tags: all description_tags: {description_tags}")
        if not description_tags:
            return []
        # Get current time of day and weather type
        time_of_day = self.game_state.time_system.current_phase
        current_weather = self.current_weather
        logger.info(f"weather_system decorate tags: time_of_day: {time_of_day}")
        logger.info(f"weather_system decorate tags: weather_type {current_weather}")

        # Initialize lists to collect descriptions for the current time of day and default
        specific_descs = [] #descriptions matching tag/time
        default_descs = [] #still matched to time of day!

        # Fetch descriptions for each tag
        for tag in description_tags:
            logger.info(f"weather_system decorate tags: tag : {tag}")

            # FORMAT: weather/tag/time of day

            #get weather
            weather_dic = self.weather_descriptions[current_weather]

            # DONT COMBINE WITH DEFAULT IF INDOORS
            if tag in ["indoors"]:
                tag_descriptions = weather_dic.get(tag,{}).get(time_of_day)
                logger.info(f"weather_system decorate tags: indoor tag descriptions: {tag_descriptions}")
                return random.choice(tag_descriptions)
            #getting default descriptions for weighted output below
            #default is keyed to weather type, not to tag
            if "default" in weather_dic:
                default_descs.extend(weather_dic["default"].get(time_of_day))

            if tag in weather_dic:
                specific_descs.extend(weather_dic[tag].get(time_of_day))
        # Create a pool of descriptions by combining specific time of day and default descriptions
        combined_descs = specific_descs + default_descs
        weights = [2.0] * len(specific_descs) + [1.0] * len(default_descs)  # Adjust weights as needed

        # Return a random description from the combined pool using weights
        if combined_descs:
            returning = random.choices(combined_descs, weights=weights, k=1)
            logger.info(f"weather_system decorate tags: returning {returning}")
            return returning
        logger.info("weather_system decorate tags: returning EMPTY LIST; nothing found")
        # If no descriptions are found, return an empty list
        return []