
from abc import ABC, abstractmethod
import random
from utilities.state_utils import iterate_states, iterate_keys
from config.logging_config import desc_logger

class Descriptions(ABC):
    def __init__(self, id, name, entity_state, game_state, descriptions, is_outdoors=False):
        self.id = id
        self.name = name
        self.entity_state = entity_state
        self.game_state = game_state
        self.descriptions = descriptions
        self.is_outdoors = is_outdoors

    def get_description(self, description_type):
        desc_logger.debug(f"Base Descriptions/ get_description() : description type: {description_type}")
        descriptions = iterate_states(self.game_state, self.entity_state, self.descriptions, description_type)
        if descriptions:
            return self.fetch_random_description(description_type, descriptions)
        desc_logger.warning(f"Base Description/get_description(): No descriptions found after iterating states for description type {description_type}")
        #raise ValueError("No description available")

    def fetch_random_description(self, description_type, descriptions_dic):
        desc_logger.debug(f"base descriptions - fetch random desc, type = {description_type}, dic = {descriptions_dic}")
        descriptions = self.handle_description_keying(description_type, descriptions_dic)
        # ITERATE AMBIANCE KEYS (returns input if not found)
        descriptions = iterate_keys(descriptions, self.game_state.vibe_system.ranked_keys)
        if descriptions:
            if not isinstance(descriptions, list):
                desc_logger.error(
                    f"base descriptions : \n type: {description_type}, descriptions not list: {descriptions}")
                raise ValueError(f"descriptions not list")

            description = random.choice(descriptions)
            return description
        desc_logger.warning(f"Base desc/ No valid description found for type '{description_type}' in ranked keys")

    def handle_description_keying(self, description_type, descriptions_dic):
        temp_dic = None
        if isinstance(descriptions_dic, dict):
            if description_type in ["1", "2", "3", "at_entity"]:
                temp_dic = descriptions_dic  # just to avoid the warning log below
            if description_type == "approaching": #ALREADY CHANGED PLAYER LOC
                temp_dic = descriptions_dic.get(self.game_state.player.location_history[-2].id)
            if description_type in ["leaving", "connections", "at_scene"]:
                temp_dic = descriptions_dic.get(self.game_state.player.current_location.id)
        if not temp_dic:
            temp_dic = descriptions_dic
        descriptions_dic = self.check_nested_weather_or_time_keys(temp_dic)

        return descriptions_dic

    def check_nested_weather_or_time_keys(self, descriptions_dic):
        if isinstance(descriptions_dic, dict):
            # ALWAYS key weather, time. or just time. but never time, weather!!!
            current_weather = self.game_state.weather_system.current_weather
            current_time = self.game_state.time_system.current_phase

            # try weather key, time key. then try time key. then finally, iterate mood keys.
            weather_keyed_dic = descriptions_dic.get(current_weather)
            time_keyed_dic = descriptions_dic.get(current_time)
            if weather_keyed_dic: #optionally check if there is nested time key in the weather key dic
                descriptions_dic = weather_keyed_dic
                if isinstance(weather_keyed_dic, dict):
                    time_keyed_weather_dic = weather_keyed_dic.get(current_time)
                    if time_keyed_weather_dic:
                        descriptions_dic = time_keyed_weather_dic

            elif time_keyed_dic: #optionally check if there is nested weather keys in the time keyed dic
                descriptions_dic = time_keyed_dic
                if isinstance(time_keyed_dic, dict):
                    weather_keyed_time_dic = time_keyed_dic.get(current_weather)
                    if weather_keyed_time_dic:
                        descriptions_dic = weather_keyed_time_dic

        return descriptions_dic


    def set_scene(self, *args, **kwargs):
        # Initialize with an empty string to add a separating line
        scene_description = [" "]
        #just for now so you can still play, later remove non 123
        for _ in ["1", "2", "3", "weather", "times", "at_entity"]:
            scene_description.append(self.get_description(_))
        # TAGS
        scene_description.append(self.decorate_description_tags())
        return scene_description

    def decorate_description_tags(self):
        desc_decorations = []
        #get tags by iterating states
        tags = iterate_states(self.game_state, self.entity_state, self.descriptions, "tags")
        # can have frequency logic here
        decor = self.game_state.weather_system.decorate_tags(tags)
        desc_decorations.append(decor)

        desc_logger.debug(
                    f"Base Description/ decorate_description_tags() : decorating weather with tags: {tags}; decor: {decor}")

        #other tags can be added as needed, like maybe late game, she greets you like an old friend?
        #desc_decorations.append(self.game_state.event_system.decorate_tags(tags))

        if desc_decorations:
            return desc_decorations
        desc_logger.warning(
            f"base description class DECORATE TAGS() NO DESC_DECor {desc_decorations}")


class Mobile_Descriptions(Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, current_location, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, is_outdoors)
        self.current_location = current_location
    # later, may have unique mobile description methods; or suspects/items will inherit this and add methods accordingly
