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

def iterate_keys(dictionary, ranked_keys): #for mood keys
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
