import difflib
import copy
from utilities.general_utils import names_to_ids, flatten_list, ids_to_names
from config.logging_config import app_logger
from collections import defaultdict
def get_command(ui, game_state):
    #possible_multiple_option_type is LOCATIONS
    command = ui.get_input()


    return command

def handle_command_id_list_logic(command_ids, game_state):
    app_logger.debug(f"command_utils.PY/handling command_id_list_logic() \n "
                     f"COMMAND IDS: {command_ids} ")
    if len(command_ids) == 1:
        return command_ids[0]
    # remove ids that are not in locations (which is current connections)
    command_ids = [id for id in command_ids if id in game_state.player.current_location.get_connections()]
    # Flatten the list but avoid splitting strings into characters
    possible_ids = flatten_list(command_ids)

    if not possible_ids:
        raise ValueError(
            "no possible ids, great.")
    if len(possible_ids) == 1:
        command_id = possible_ids[0]
        app_logger.debug(f"command_utils.PY/handlecommand_id_list_logic; possible ids {possible_ids}")
        return command_id
    elif len(possible_ids) > 1:
        possible_ids = [id for id in possible_ids if id != game_state.player.location_history[-2].id]
        if not len(possible_ids) == 1:
            raise ValueError(f"FFFFFFFFÙCK")
        app_logger.debug(f"command_utils.PY/handlecommand_id_list_logic; possible ids {possible_ids}")
        return possible_ids[0]
    else:
        raise ValueError("len of possible ids not accounted for")


def match_command_to_option(command, game_state, suspects=None, items=None, locations=None, actions=None):
    suspects = copy.deepcopy(suspects) if suspects else []
    items = copy.deepcopy(items) if items else []
    locations = copy.deepcopy(locations) if locations else []
    actions = copy.deepcopy(actions) if actions else []
    app_logger.info(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION: command = {command}\n suspects = {suspects}\nitems={items}\n locs={locations}\nactions={actions}\n")
    matched = False

    if isinstance(command, list):
        app_logger.warning(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION: command = {command}\n suspects = {suspects}\nitems={items}\n locs={locations}\nactions={actions}\n")
        command = command[0]

    # Convert actions to list if it is a dict
    if isinstance(actions, dict):
        action_values = list(actions.values())
        action_keys = list(actions.keys())
        app_logger.info(f"general utils/ action_values {action_values}/action_keys {action_keys}")

        key_value_pairs = [f"{key}:{value}" for key, value in actions.items()]
        actions = flatten_list([action_keys, action_values, key_value_pairs])

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

    from entities.entities.locations.doors import Door
    if isinstance(game_state.player.current_location, Door):
        if game_state.player.current_location.components.is_open:
            actions.append("enter")

    #filter out current location id
    locations = [id for id in locations if id != game_state.player.current_location.id]

    # combine options
    combined_options = suspects + items + locations + actions
    app_logger.debug(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ; combined options = {combined_options}")
    # Convert to names
    option_names = ids_to_names(combined_options, game_state)
    app_logger.info(f"option_names  {option_names}")
    # Generate full names for all options
    # full_names = generate_full_names(option_names)
    # make item map
    option_map = defaultdict(list)

    for option_id in combined_options:
        # Get the name
        option_name = ids_to_names(option_id, game_state)

        # Split to parts (e.g., whiskey, bottle)
        option_parts = option_name.split()

        for part in option_parts:
            option_map[part].append(option_id)

        option_map[option_name].append(option_id)

    for key, values in option_map.items():
        if len(values) > 1:
            option_map[key] = [option_id for option_id in values if option_id != game_state.player.location_history[-2].id]

    app_logger.info(f"option_map = {option_map}")
    # Find the best match across all current options
    best_match = option_map.get(find_best_match(command, list(option_map.keys())))
    if isinstance(best_match, list):
        best_match = best_match[0]
    app_logger.debug(f"GENERAL_UTILS/MATCHCOMMAND_TO_OPTION: before if best match = {best_match}")
    if best_match:

        entity_ids = (
            game_state.location_manager.get_entity_ids(best_match) +
            game_state.item_manager.get_entity_ids(best_match) +
            game_state.suspect_manager.get_entity_ids(best_match)
        )
        matched = True
        entity_ids = [id for id in entity_ids if id in locations or id in suspects or id in items]
        app_logger.info(f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ;  \nbest_match = {best_match}\nentity_ids = {entity_ids}")
        if entity_ids:
            if len(entity_ids) > 1: #command maps to multiple entity ids that are in options. This means same name for multiple locs. so remove last loc so its like it defaults to forward
                player_last_loc_id = game_state.player.location_history[-2].id
                entity_ids = [id for id in entity_ids if id != player_last_loc_id]
            if len(entity_ids) > 1:
                raise ValueError(f"YOU THOUGHT WRONG")
            return entity_ids[0], matched
        else:
            app_logger.info(
                f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ;  \nbest_match = {best_match}\nentity_ids = {entity_ids}")
            return best_match, matched
    app_logger.info(
        f"GENERAL_UTILS.PY/MATCH_COMMAND_TO_OPTION() ;  \nno best match\nreturning {command}")
    return command, matched  # Return the original command if no matches found


def generate_full_names(names):
    return set(name.lower() for name in names)


def find_best_match(command, full_names, threshold=0.6):
    """NEED TO MATCH TO FIRST PART OF NAME LIKE RUM FOR RUM BOTTLE"""
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
