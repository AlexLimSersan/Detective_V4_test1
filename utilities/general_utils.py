
import random
from config.settings import AMBIANCE_KEYS, AMBIANCE_VALUES
import difflib
import logging
from config.logging_config import app_logger


def rank_keys(current_value, keys=AMBIANCE_KEYS):
    """Rank mood keys based on the current game vibe, returning keys in the order of closest match."""

    def mood_distance(key):
        return abs(current_value - AMBIANCE_VALUES[key])

    sorted_mood_keys = sorted(keys, key=mood_distance)
    return sorted_mood_keys

#ui utils

def format_list_as_sentence(list):
    if not list:
        return ""
    if len(list) == 1:
        return list[0]
    return ', '.join(list[:-1]) + f", and {list[-1]}"

#FUZZY MATCHING

def generate_full_names(names):
    return set(name.lower() for name in names)

def find_best_match(command, full_names, threshold=0.5):
    #lower threshold = more likely to match
    command_lower = command.lower()
    best_match = None
    highest_ratio = 0
    for name in full_names:
        ratio = difflib.SequenceMatcher(None, command_lower, name).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = name
    if highest_ratio >= threshold:
        return best_match
    else:
        return None

def match_command_to_option(command, game_state, suspects=[], items=[], locations=[], actions=[]):
    app_logger.debug(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION: command = {command}\n suspects = {suspects}\nitems={items}\n locs={locations}\nactions={actions}\n")
    matched = False

    #sus, items, locs, actions, must be list, can not be none type!
    #note they are ids!

    #convert actions to list, as actions may be a dict of keys=command, values=description; (like this for UI purposes)
    if isinstance(actions, dict):
        actions = list(actions.keys())

    #logic for adding continue or return to command matching
    if locations: #add continue to command matching if name of adjacent location same as current location
        for location in locations:
            if location != game_state.player.location_history[-2].id:
                location_name = ids_to_names(location, game_state)
                # locations with same name as current loc
                if location_name == game_state.player.current_location.name:
                    actions.append("continue")
    if game_state.player.location_history[-2].id in locations or game_state.player.location_history[-2].id in actions: #might be in loc or actions if door
        actions.append("return")

    #filter out current location id
    locations = [id for id in locations if id != game_state.player.current_location.id]

    # combine options
    combined_options = suspects + items + locations + actions
    app_logger.debug(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ; combined options = {combined_options}")
    # Convert to names
    option_names = ids_to_names(combined_options, game_state)
    app_logger.debug(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ;  option names = {option_names}")

    # Generate full names for all options
    full_names = generate_full_names(option_names)
    app_logger.debug(f"GENERAL_UTILS/MATCHCOMMAND_TO_OPTION: full names = {full_names}")
    # Find the best match across all current options
    best_match = find_best_match(command, full_names)
    app_logger.debug(f"GENERAL_UTILS/MATCHCOMMAND_TO_OPTION: before if best match = {best_match}")
    if best_match:

        entity_ids = (
            game_state.location_manager.get_entity_ids(best_match) +
            game_state.item_manager.get_entity_ids(best_match) +
            game_state.suspect_manager.get_entity_ids(best_match)
        )
        matched = True
        entity_ids = [id for id in entity_ids if id in locations or id in suspects or id in items]
        app_logger.debug(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ;  \nbest_match = {best_match}\nentity_ids = {entity_ids}")
        if entity_ids:
            if len(entity_ids) > 1: #command maps to multiple entity ids that are in options. This means same name for multiple locs. so remove last loc so its like it defaults to forward
                player_last_loc_id = game_state.player.location_history[-2].id
                entity_ids = [id for id in entity_ids if id != player_last_loc_id]
            return entity_ids, matched
        else:
            return best_match, matched
    app_logger.debug(
        f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ;  \nno best match\nreturning {command}")
    return command, matched  # Return the original command if no matches found

def names_to_ids(texts, game_state):
    app_logger.debug(f"GENERAL UTILS: names to ids() ; going to replace with texts = {texts}")
    if isinstance(texts, list):
        return [replace_names_with_ids(text, game_state) for text in texts]
    elif isinstance(texts, dict):
        return {key: replace_names_with_ids(text, game_state) for key, text in texts.items()}
    else:
        return replace_names_with_ids(texts, game_state)

def replace_names_with_ids(text, game_state):
    #might have multiple ids matching to a given name
    ids = []
    loc_ids = game_state.location_manager.get_entity_ids(text)
    sus_ids = game_state.suspect_manager.get_entity_ids(text)
    item_ids = game_state.item_manager.get_entity_ids(text)
    matched_ids = loc_ids + sus_ids + item_ids

    if matched_ids:
        ids.extend(matched_ids)
    else:
        ids.append(text)  # If no match, keep the text
    app_logger.debug(f"GENERAL UTILS: replace names with ids() ; returning ids = {ids}")
    return ids

def ids_to_names(texts, game_state):
    app_logger.debug(f"GENERAL UTILS: ids to names ; texts = {texts}")
    if isinstance(texts, list):
        return [replace_ids_with_names(text, game_state) for text in texts]
    elif isinstance(texts, dict):
        return {key: replace_ids_with_names(text, game_state) for key, text in texts.items()}
    else:
        return replace_ids_with_names(texts, game_state)

def replace_ids_with_names(text, game_state):

    words = text.split()
    for i, word in enumerate(words):
        words[i] = game_state.location_manager.get_entity_name(word) or \
                   game_state.suspect_manager.get_entity_name(word) or \
                   game_state.item_manager.get_entity_name(word) or word
    fixed_text = ' '.join(words)
    app_logger.debug(f"GENERAL UTILS: replaced ids with names() ; returning = {fixed_text}")
    return fixed_text