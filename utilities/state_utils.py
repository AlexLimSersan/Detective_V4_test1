# utils/state_utils.py
import random
from config.logging_config import app_logger
def iterate_states(game_state, entity_state, data, to_get=None):
    current_events = game_state.event_system.current_events
    #print(f"iterating states on {data}")
    #print(f" iterate states: getting {to_get}")
    # Check for event-specific
    for event_id in current_events:
        if event_id in data:
            found_dic = data[event_id] if to_get is None else data[event_id].get(to_get)
            if found_dic:
                return found_dic

    # Check for state-specific
    found_dic = data.get(entity_state, {}) if to_get is None else data.get(entity_state, {}).get(to_get)
    if found_dic:
        return found_dic

    # Check for default
    found_dic = data.get("default", {}) if to_get is None else data.get("default", {}).get(to_get)
    if found_dic:
        return found_dic
    #raise ValueError(f"ITERATE STATES: no found dictionary; to_get : {to_get}")

def iterate_vibe_keys(dictionary, ranked_keys): #for mood keys
    try:
        for key in ranked_keys:
            #fails if a list
            keyed_descriptions = dictionary.get(key)
            if keyed_descriptions:
                app_logger.info(f"returning {key} keyed descriptions {keyed_descriptions} ")
                return keyed_descriptions
        app_logger.warning(f"tried all keys, didnt fail. not returning anything?")
    except:
        app_logger.info(f"failed try, exception: returning {dictionary}")
        return dictionary #if cant find key, just return dic anyways

def check_nested_weather_or_time_keys(descriptions_dic, game_state):
    if isinstance(descriptions_dic, dict):
        current_weather = game_state.weather_system.current_weather
        current_time = game_state.time_system.current_phase

        for desc_key, nested_dic in descriptions_dic.items():

            if isinstance(nested_dic, list):
                pass
        #if current_weather in list(descriptions_dic.keys()

        weather_keyed_dic = descriptions_dic.get(current_weather)
        time_keyed_dic = descriptions_dic.get(current_time)
        #CHECK WEATHER, TIME
        if weather_keyed_dic:
            descriptions_dic = weather_keyed_dic
            if isinstance(weather_keyed_dic, dict):
                time_keyed_weather_dic = weather_keyed_dic.get(current_time)
                if time_keyed_weather_dic:
                    descriptions_dic = time_keyed_weather_dic
        #CHECK TIME, WEATHER
        elif time_keyed_dic:
            descriptions_dic = time_keyed_dic
            if isinstance(time_keyed_dic, dict):
                weather_keyed_time_dic = time_keyed_dic.get(current_weather)
                if weather_keyed_time_dic:
                    descriptions_dic = weather_keyed_time_dic
    # keyed by mood keys, or might just be a list
    return descriptions_dic

