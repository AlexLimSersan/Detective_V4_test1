
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
        """description has:
        approaching
        at_entity
        leaving
        times 
        weather 
        tags
        """

    def get_description(self, description_type):
        desc_logger.debug(f"Base Descriptions/ get_description() : description type: {description_type}")
        descriptions = iterate_states(self.game_state, self.entity_state, self.descriptions, description_type)
        desc_logger.debug(f"Base Description/ get_description() : iterated states gives: {descriptions}")
        if descriptions:
            return self.fetch_random_description(description_type, descriptions)
        desc_logger.warning(f"Base Description/get_description(): No descriptions found after iterating states for description type {description_type}")
        #raise ValueError("No description available")

    def fetch_random_description(self, description_type, descriptions_dic):
        desc_logger.debug(f"base descriptions - fetch random desc, type = {description_type}, dic = {descriptions_dic}")
        #description dic should be mood keys : [descriptions]
        if description_type in ["tags", "connections"]:
            #tags and connections are not in regular flow of descriptions, so break out without changing.
            #this is just a safeguard, should not come to this.
            return descriptions_dic

        #if additional keying needed:
        if description_type == "weather":
            if random.random() < 0.7:

                descriptions_dic = descriptions_dic.get(self.game_state.weather_system.current_weather)
                desc_logger.debug(f"Base Description/ fetch_random_description() : weather keyed dic {descriptions_dic}")
            else:
                desc_logger.info(f"BASE DESCRIPTIONS not ADDING WEATHER")
                return

        if description_type == "times":
            descriptions_dic = descriptions_dic.get(self.game_state.time_system.current_phase)
            desc_logger.debug(f"Base Description/ fetch_random_description() : time keyed dic {descriptions_dic}")

        if description_type == "at_scene":
            descriptions_dic = descriptions_dic.get(self.game_state.player.current_location.id)
            desc_logger.debug(f"Base Description/ fetch_random_description() : at_scene keyed dic {descriptions_dic}")
        #end of additional keying

        desc_logger.debug(f"Base Description/ fetch_random_description() : iterating keys on {descriptions_dic}")
        descriptions = iterate_keys(self.game_state, descriptions_dic)
        desc_logger.debug(f"Base Description/ fetch_random_description() : iterated keys, picking random on {descriptions}")
        # descriptions should be list

        if descriptions:
            description = random.choice(descriptions)
            desc_logger.debug(
                f"Base Description/ fetch_random_description() : returning {description}")
            return description
        desc_logger.warning(f"Base desc/ No valid description found for type '{description_type}' in ranked keys")
        #raise ValueError(f"No valid description found for type '{description_type}' in ranked keys")

    def decorate_description_tags(self):
        desc_decorations = []
        #gets tags by iterating states
        tags = iterate_states(self.game_state, self.entity_state, self.descriptions, "tags")
        # can have frequency logic here
        if self.is_outdoors:
            if random.random() < 0.6:
                decor = self.game_state.weather_system.decorate_tags(tags)
                desc_decorations.append(decor)
                desc_logger.debug(f"Base Description/ decorate_description_tags() : decorating weather with tags: {tags}; decor: {decor}")
            else:
                desc_logger.info(f"Base Description/ decorate_description_tags() : NOT DECORATING")
        #desc_decorations.append(self.game_state.event_system.decorate_tags(tags))

        #other tags can be added as needed, like maybe late game, she greets you like an old friend?
        if desc_decorations:
            if isinstance(desc_decorations, list):
                desc_logger.debug(f"base description class DECORATE TAGS() is a list: random choice from {desc_decorations}")
                return random.choice(desc_decorations)
            else:
                desc_logger.debug(f"base description class DECORATE TAGS() is NOT list: returning desc_decorations {desc_decorations}")
                return desc_decorations




class Mobile_Descriptions(Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, current_location, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, is_outdoors)
        self.current_location = current_location
    # later, may have unique mobile description methods; or suspects/items will inherit this and add methods accordingly

    def get_description(self, description_type):
        description = []
        if description_type == "at_entity":
            #if player is at the entity, add the clue id to the known clue ids, for topic generation in dialogue
            self.game_state.player.add_known_topic(self.id) #handles clue to topic logic
            desc_logger.info(f"mobile descriptions/at_entity adding {self.id} as known topic ")
            #known clues will later be used for the end game analysis!
        parent_description = super().get_description(description_type) #might need more conditions here, like if not in list of things to not talk about
        return parent_description

    def set_scene(self):
        scene_description = []
        # AT ENTITY
        at_ent_desc = self.get_description("at_entity")
        scene_description.append(at_ent_desc)
        desc_logger.debug(f"ITEM_DESC/set_scene(): got at ent{at_ent_desc}")
        # TIMES
        time_desc = self.get_description("times")
        scene_description.append(time_desc)
        desc_logger.debug(f"ITEM_DESC/set_scene(): got times{time_desc}")
        # WEATHER IF OUTDOORS
        if self.is_outdoors:
            weather_desc = self.get_description("weather")
            scene_description.append(weather_desc)
            desc_logger.debug(f"ITEM_DESC/set_scene(): got outdoors:{weather_desc}")
        # DECORATE TAGS SEPARATELY, NOT IN AT_ENTITY.
        # this way, system decorations (like weather) come after all the specific descriptions from the id, but before the present suspects/items.
        # either before or after? decide later.
        desc_decorations = self.decorate_description_tags()
        scene_description.append(desc_decorations)
        desc_logger.debug(f"ITEM_DESC/set_scene() :desc_decorations {desc_decorations}")
        return scene_description

