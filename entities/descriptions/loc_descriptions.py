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

        scene_description = []
        scene_description.append(super().set_scene())

        for suspect_id, suspect_data in suspects_present.items(): #get descriptions from objevct for each obeject?@@?@?@22
            sus_desc = suspect_data.descriptions.get_description("at_scene")
            scene_description.append(sus_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got sus desc AT SCENE :{sus_desc}")
        for item_id, item_data in items_present.items():
            item_desc = item_data.descriptions.get_description("at_scene")
            scene_description.append(item_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got item desc AT SCENE : {item_desc}")

        #GET INTRO PHRASE?!?!
        player_last_loc = self.game_state.player.location_history[-2]
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
        #iterate states to find connection dic
        conn_desc_dic = iterate_states(self.game_state, self.entity_state, self.descriptions, "connections")
        if conn_desc_dic:
            #if the loc you are querying form in connection dictionary (should be)
            if loc_id_querying_from in conn_desc_dic:
                description_dic = conn_desc_dic[loc_id_querying_from]
                desc_logger.debug(f"connection descriptions: desc_dic = {description_dic}")
                #ALWAYS key weather, time. or just time. but never time, weather!!!
                current_weather = self.game_state.weather_system.current_weather
                current_time = self.game_state.time_system.current_phase
                desc_logger.debug(f"connection descriptions: current_weather = {current_weather} ; current_time = {current_time}")
                #try weather key, time key. then try time key. then finally, iterate mood keys.
                weather_keyed_dic = description_dic.get(current_weather)
                time_keyed_dic = description_dic.get(current_time)
                desc_logger.debug(
                    f"connection descriptions: weather_keyed_dic = {weather_keyed_dic} ")
                desc_logger.debug(
                    f"connection descriptions: time_keyed_dic = {time_keyed_dic} ")
                if weather_keyed_dic:
                    desc_logger.info(
                        f"connection descriptions: weather_keyed_dic = {weather_keyed_dic} ")
                    if isinstance(weather_keyed_dic, dict):
                        time_keyed_weather_dic = weather_keyed_dic.get(current_time)
                        desc_logger.info(
                            f"connection descriptions: time_keyed_weather_dic = {time_keyed_weather_dic} ")
                        if time_keyed_weather_dic:
                            description_dic = time_keyed_weather_dic
                        else:
                            raise ValueError (f" weather_keyed keyed by time but no descriptions?!")
                    else:
                        description_dic = weather_keyed_dic
                if time_keyed_dic:
                    description_dic = time_keyed_dic
                desc_logger.debug(f"connection descriptions: desc_dic after keying = {description_dic}")
                description = iterate_keys(self.game_state, description_dic)
                if description:
                    desc_logger.debug(f"LOC DESC/ get connection desctripsion: returning random {description}")
                    return random.choice(description)
        desc_logger.warning(f"LOC_DESCRIPTIONS.PY/get_connection_descriptions(): no connection description dictionary for: \n id {self.id}, \n loc querying from {loc_id_querying_from}")
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

    def get_connection_descriptions(self, loc_id_querying_from):
        #iterate states to find connection dic
        conn_desc_dic = iterate_states(self.game_state, self.entity_state, self.descriptions, "connections")
        if conn_desc_dic:
            #if the loc you are querying form in connection dictionary (should be)
            if loc_id_querying_from in conn_desc_dic:
                description_dic = conn_desc_dic[loc_id_querying_from]
                desc_logger.debug(f"DOOR connection descriptions: desc_dic = {description_dic}")

                #FIRST, GET DOOR OPEN/CLOSED!
                if self.lid_component.is_open:
                    description_dic = description_dic["open"]
                else:
                    description_dic = description_dic["closed"]
                if isinstance(description_dic, dict):
                    #ALWAYS key weather, time. or just time. but never time, weather!!!
                    current_weather = self.game_state.weather_system.current_weather
                    current_time = self.game_state.time_system.current_phase
                    desc_logger.debug(f"connection descriptions: current_weather = {current_weather} ; current_time = {current_time}")
                    #try weather key, time key. then try time key. then finally, iterate mood keys.
                    weather_keyed_dic = description_dic.get(current_weather)
                    time_keyed_dic = description_dic.get(current_time)
                    desc_logger.debug(
                        f"connection descriptions: weather_keyed_dic = {weather_keyed_dic} ")
                    desc_logger.debug(
                        f"connection descriptions: time_keyed_dic = {time_keyed_dic} ")
                    if weather_keyed_dic:
                        desc_logger.info(
                            f"connection descriptions: weather_keyed_dic = {weather_keyed_dic} ")
                        if isinstance(weather_keyed_dic, dict):
                            time_keyed_weather_dic = weather_keyed_dic.get(current_time)
                            desc_logger.info(
                                f"connection descriptions: time_keyed_weather_dic = {time_keyed_weather_dic} ")
                            if time_keyed_weather_dic:
                                description_dic = time_keyed_weather_dic
                            else:
                                raise ValueError (f" weather_keyed keyed by time but no descriptions?!")
                        else:
                            description_dic = weather_keyed_dic
                    if time_keyed_dic:
                        description_dic = time_keyed_dic
                desc_logger.debug(f"connection descriptions: desc_dic after keying = {description_dic}")
                description = iterate_keys(self.game_state, description_dic)
                if description:
                    desc_logger.debug(f"LOC DESC/ get connection desctripsion: returning random {description}")
                    return random.choice(description)
        desc_logger.warning(f"LOC_DESCRIPTIONS.PY/get_connection_descriptions(): no connection description dictionary for: \n id {self.id}, \n loc querying from {loc_id_querying_from}")
        #raise ValueError("No connection descriptions available; should have defaulted")