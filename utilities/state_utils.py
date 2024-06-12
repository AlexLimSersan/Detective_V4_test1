# utils/state_utils.py
import random
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

def iterate_keys(game_state, dictionary): #for mood keys
    ranked_keys = game_state.vibe_system.ranked_keys
    try:
        for key in ranked_keys:
            keyed_descriptions = dictionary.get(key)
            if keyed_descriptions:
                return keyed_descriptions
    except:
        return dictionary #if cant find key, just return dic anyways
