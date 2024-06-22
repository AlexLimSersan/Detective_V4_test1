from config.logging_config import app_logger

def format_list_as_sentence(list):
    if not list:
        return ""
    if len(list) == 1:
        return list[0]
    return ', '.join(list[:-1]) + f", and {list[-1]}"

def flatten_list(list_to_fix):
    fixed_list = []
    for sublist in list_to_fix:
        if isinstance(sublist, list):
            fixed_list.extend(sublist)
        else:
            fixed_list.append(sublist)
    return fixed_list


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