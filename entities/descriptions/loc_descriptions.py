import random
from entities.descriptions.base import Descriptions
from utilities.state_utils import iterate_states, iterate_keys

from config.logging_config import desc_logger


class Loc_Descriptions(Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, is_outdoors)
        """description has:
                approaching
                at_entity
                leaving
                times 
                weather 
            + connections
            + will query for at_scene
                """

    def set_scene(self, suspects_present, items_present, connections):
        desc_logger.debug(f"Loc_Desc/set_scene(): setting scene with suspects {suspects_present}, items {items_present}, connections {connections}")
        player_last_loc = self.game_state.player.location_history[-2]
        #can have some logic for player last loc, if its the same location (ie they just interacted with a suspect or item)
        #   make description shorter or just a recap!

        scene_description = []
        #AT ENTITY
        at_ent_desc = self.get_description("at_entity")
        scene_description.append(at_ent_desc)
        desc_logger.debug(f"Loc_Desc/set_scene(): got at ent{at_ent_desc}")
        #TIMES
        time_desc = self.get_description("times")
        scene_description.append(time_desc)
        desc_logger.debug(f"Loc_Desc/set_scene(): got times{time_desc}")
        #WEATHER IF OUTDOORS
        if self.is_outdoors:
            weather_desc = self.get_description("weather")
            scene_description.append(weather_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got outdoors:{weather_desc}")
        #DECORATE TAGS SEPARATELY, NOT IN AT_ENTITY.
        # this way, system decorations (like weather) come after all the specific descriptions from the id, but before the present suspects/items.
        #either before or after? decide later.
        desc_decorations = self.decorate_description_tags()
        scene_description.append(desc_decorations)
        desc_logger.debug(f"Loc_Desc/set_scene() :desc_decorations {desc_decorations}")
        for suspect_id, suspect_data in suspects_present.items(): #get descriptions from objevct for each obeject?@@?@?@22
            sus_desc = suspect_data.descriptions.get_description("at_scene")
            scene_description.append(sus_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got sus desc AT SCENE :{sus_desc}")
        for item_id, item_data in items_present.items():
            item_desc = item_data.descriptions.get_description("at_scene")
            scene_description.append(item_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got item desc AT SCENE : {item_desc}")

        #GET INTRO PHRASE?!?!

        #query from the actual connected location, so that you get descriptions based on their state!
        for connection_id in connections:
            if connection_id != player_last_loc.id:
                connected_location = self.game_state.location_manager.get_entity(connection_id)
                if connected_location:
                    conn_desc = connected_location.descriptions.get_connection_descriptions(self.id)
                    scene_description.append(conn_desc)
                    desc_logger.debug(f"Loc_Desc/set_scene():got connected loc desc {conn_desc}")
        desc_logger.debug(f"LOC_DESC set scene: returnins {scene_description}")
        return scene_description

    def get_connection_descriptions(self, loc_id_querying_from):
        conn_desc_dic = iterate_states(self.game_state, self.entity_state, self.descriptions, "connections")
        if conn_desc_dic:
            if loc_id_querying_from in conn_desc_dic:
                description = iterate_keys(self.game_state, conn_desc_dic[loc_id_querying_from])
                if description:
                    desc_logger.debug(f"LOC DESC/ get connection desctripsion: returning random {description}")
                    return random.choice(description)
        #raise ValueError("No connection descriptions available; should have defaulted")




class Door_Descriptions(Loc_Descriptions): #difference is only for setting scene/at entity, handles door open/close / lid logic
    def __init__(self, id, name, entity_state, game_state, id_descriptions, default_descriptions, lid_component, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, None, is_outdoors)
        self.descriptions = id_descriptions
        self.default_descriptions = default_descriptions
        self.lid_component = lid_component

    def set_scene(self, suspects_present, items_present, connections):
        # Call the inherited set_scene method with an empty connections list
        scene_description = super().set_scene(suspects_present, items_present, [])
        desc_logger.debug(f"door desc setting scene - super = {scene_description}")

        # Modify the connection logic for the lid-specific condition
        if self.lid_component.is_open:
            desc_logger.debug(f"door desc setting scene - IS OPEN")
            player_last_loc = self.game_state.player.location_history[-2]
            for connection_id in connections:
                if connection_id != player_last_loc.id:
                    connected_location = self.game_state.location_manager.get_entity(connection_id)
                    if connected_location:
                        conn_desc = connected_location.descriptions.get_connection_descriptions(self.id)
                        scene_description.append(conn_desc)
                        desc_logger.debug(f"Loc_Desc/DOOR DESCRIPTIONS/ set_scene() : got connected loc desc "
                                     f"{conn_desc}")

        desc_logger.debug(f"door setting scene returning scene {scene_description}")
        return scene_description

    def get_description(self, description_type):
        if description_type == "at_entity":
            #lid stuff
            lid_description = self.lid_component.get_description(description_type) #return description based on state.

            desc_decorations = self.decorate_description_tags()

            description = [lid_description, desc_decorations]
            desc_logger.debug(f"doors desc AT ENTITY: get  description returning {description}")
            return description
        else:
            return super().get_description(description_type)