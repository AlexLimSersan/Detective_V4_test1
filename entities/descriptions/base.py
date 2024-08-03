
from abc import ABC, abstractmethod
import random
from utilities.state_utils import iterate_states, iterate_vibe_keys, check_nested_weather_or_time_keys
from config.logging_config import desc_logger
from utilities.general_utils import merge_dicts
class Descriptions(ABC):
    def __init__(self, id, name, entity_state, game_state, descriptions, is_outdoors=False):
        self.id = id
        self.name = name
        self.entity_state = entity_state
        self.game_state = game_state
        self.descriptions = descriptions
        self.is_outdoors = is_outdoors
        #approaching, leaving, at entity, connections, at_scene

    def get_description(self, description_type, optional_key = None):
        desc_logger.debug(f"Base Descriptions/ get_description() : description type: {description_type}\n{self.entity_state}")
        descriptions = iterate_states(self.game_state, self.entity_state, self.descriptions, description_type)
        description_to_return = []
        # just for now, later always list of dics
        # can be keyed for time, weather, mood, as desired

        if isinstance(descriptions, dict):
            description_to_return.append(self.fetch_random_description(description_type, descriptions, optional_key))
        # later always list: ; for each dic in list, handle keys and get a description
        elif isinstance(descriptions, list):
            for desc_dic in descriptions:
                if isinstance(desc_dic, dict):  # safety
                    description_to_return.append(self.fetch_random_description(description_type, desc_dic, optional_key))

        if not description_to_return and descriptions:
            desc_logger.debug(f"{description_to_return}, {descriptions}")
            return descriptions
        if description_to_return:
            desc_logger.debug(f"{description_to_return}")
            return description_to_return
        #desc_logger.warning(f"Base Description/get_description(): No descriptions found after iterating states for description type {description_type}\n{self.descriptions}")
        #raise ValueError("No description available")

    def fetch_random_description(self, description_type, descriptions_dic, optional_key = None):
        desc_logger.debug(f"base descriptions - fetch random desc, type = {description_type}, dic = {descriptions_dic}")
        descriptions = self.handle_description_keying(description_type, descriptions_dic, optional_key)
        # ITERATE AMBIANCE KEYS (returns input if not found)
        desc_logger.debug(f"base descriptions - ITERATING descriptions {descriptions}")
        descriptions = iterate_vibe_keys(descriptions, self.game_state.vibe_system.ranked_keys)
        if descriptions:
            if not isinstance(descriptions, list):
                desc_logger.error(
                    f"base descriptions : \n type: {description_type}, descriptions not list: {descriptions}")
                raise ValueError(f"descriptions not list")
            while isinstance(descriptions, list):
                descriptions = random.choice(descriptions)
            #description = random.choice(descriptions) #so would either get a random str descriptioin, or a random list of strs, each str in the list would have a pause time.
            if isinstance(descriptions,str):
                descriptions.format(current_phase=self.game_state.time_system.current_phase)
            #i think this was getting messed up in set scene
            #actually, if i do the scroll text as it prints, then wouldnt really need this?
            return descriptions
        #desc_logger.warning(f"Base desc/ No valid description found for type '{description_type}' in ranked keys")

    def handle_description_keying(self, description_type, descriptions_dic, optional_key = None):
        #iterated states and have the "desc type" eg approaching dictionary with whatever nested keys...
        #check first for default, which is the {"neutral": [] } -> will get merged to the nested keys if present.
        #
        default_to_add = descriptions_dic.get("default")
        desc_logger.debug(f"desc_base {description_type}; default to add:\n{default_to_add}; ")
        temp_dic = None
        if isinstance(descriptions_dic, dict):
            if description_type in ["at_entity", "times", "weather"]:
                temp_dic = descriptions_dic.get(self.game_state.player.current_location.id)#GOING TO TRY THIS, NOW CAN HAVE DIFFERENT at ent DESCRIPTIONS BASED ON LOCATION!  # just to avoid the warning log below
                if optional_key and not temp_dic:
                    temp_dic = descriptions_dic.get(optional_key, descriptions_dic)
            # ALREADY CHANGED PLAYER LOC
            elif description_type == "approaching":  # approaching from
                temp_dic = descriptions_dic.get(self.game_state.player.location_history[-2].id)
                if optional_key and not temp_dic:
                    temp_dic = descriptions_dic.get(optional_key, descriptions_dic)
            elif description_type in ["leaving", "connections", "at_scene"]:  # leaving to
                from entities.entities.items import Drawer
                drawer_dic = None
                drawer = self.game_state.item_manager.get_entity(self.id)
                if isinstance(drawer, Drawer):
                    if drawer.components.is_open:
                        drawer_dic = descriptions_dic.get("open")
                    else:
                        drawer_dic = descriptions_dic.get("closed")
                if drawer_dic:
                    descriptions_dic = drawer_dic
                temp_dic = descriptions_dic.get(self.game_state.player.current_location.id)
                desc_logger.debug(f"at scene temp = {temp_dic}")
                if optional_key and not temp_dic:
                    temp_dic = descriptions_dic.get(optional_key, descriptions_dic)

            elif optional_key:
                temp_dic = descriptions_dic.get(optional_key, temp_dic)
            else:
                ...
                #desc_logger.warning(f"base/handle description keying(): unaccounted description type {description_type}; \n dic = {descriptions_dic}")
        if not temp_dic:
            temp_dic = descriptions_dic
            desc_logger.debug(f"at scene temp = {temp_dic}")

        descriptions_dic = check_nested_weather_or_time_keys(temp_dic, self.game_state)
        desc_logger.debug(f"RETURNING = {descriptions_dic}")
        if default_to_add:
            #this is weird lol but fuckit
            merged_dic = None
            if isinstance(default_to_add, dict) and isinstance(descriptions_dic, dict):
                merged_dic = merge_dicts(default_to_add, descriptions_dic)

                desc_logger.info(f"1\n{merged_dic},{default_to_add}, {descriptions_dic}")
            elif isinstance(default_to_add, list) and isinstance(descriptions_dic, list):
                merged_dic = []
                merged_dic.extend(descriptions_dic)
                merged_dic.extend(default_to_add)
                desc_logger.info(f"2\n{merged_dic},{default_to_add}, {descriptions_dic}")
            else:
                desc_logger.info(
                    f"3\n BASE / HANDLE KEYING: \nDEFAULT TO ADD = {default_to_add}\n merged_dic = {merged_dic}")
            if merged_dic:
                return merged_dic
            else:
                return descriptions_dic

        else:
            return descriptions_dic

    def set_scene(self, suspects_present=None, items_present=None, connections=None, optional_key = None):
        # Initialize with an empty string to add a separating line
        scene_description = [" "]
        #just for now so you can still play, later just get at_ent
        for _ in ["at_entity", "times", "weather"]:
            desc = self.get_description(_, optional_key = optional_key)
            if desc:
                scene_description.append(desc)
        # TAGS
        desc_decor = self.decorate_description_tags()
        if desc_decor:
            scene_description.append(desc_decor)
        return scene_description

    def get_at_scene(self, suspects_present, items_present, optional_key = None):
        scene_description = []
        desc_logger.debug(f"opt {optional_key}")
        for suspect_id, suspect_data in suspects_present.items():
            sus_desc = suspect_data.descriptions.get_description("at_scene", optional_key=optional_key)
            if sus_desc:
                scene_description.append(sus_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got sus desc AT SCENE :{sus_desc}")

        for item_id, item_data in items_present.items():
            item_desc = item_data.descriptions.get_description("at_scene", optional_key=optional_key)
            if item_desc:
                scene_description.append(item_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got item desc AT SCENE : {item_desc}")
        return scene_description
    def decorate_description_tags(self):
        desc_decorations = []
        # can have frequency logic here
        # get tags by iterating states
        tags = iterate_states(self.game_state, self.entity_state, self.descriptions, "tags")
        if not self.get_description("weather"):
            decor = self.game_state.weather_system.decorate_tags(tags)
            desc_decorations.append(decor)

            desc_logger.info(
                    f"Base Description/ decorate_description_tags() : decorating weather with tags: {tags}; decor: {decor}")

        # other tags can be added as needed, like maybe late game, she greets you like an old friend?
        # desc_decorations.append(self.game_state.event_system.decorate_tags(tags))

        if desc_decorations:
            return desc_decorations
        desc_logger.warning(
            f"base description class DECORATE TAGS() NO DESC_DECor {desc_decorations}")


class Mobile_Descriptions(Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, current_location, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, is_outdoors)
        self.current_location = current_location
    # later, may have unique mobile description methods; or suspects/items will inherit this and add methods accordingly
