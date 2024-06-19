import random
from entities.descriptions.base import Descriptions
from utilities.state_utils import iterate_states, iterate_keys

from config.logging_config import desc_logger


class Loc_Descriptions(Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, is_outdoors)
        """description has:
                # approaching, leaving, at_scene, connections #keyed by their respective loc / at scene IS ACTUALLY THE SAME AS CONNECTIONS?
                #first, second, third, all can be nested keys time, weather, mood, or just a list.
                also you can definitely REFACTOR DOOR AND LOC DESCRIPTOINS FURTHER!
                """

    def set_scene(self, suspects_present, items_present, connections):
        desc_logger.debug(f"Loc_Desc/set_scene(): setting scene with suspects {suspects_present}, items {items_present}, connections {connections}")

        scene_description = []
        scene_description.append(super().set_scene())
        # Could prob combine mobile ents, but whateva
        for suspect_id, suspect_data in suspects_present.items():
            sus_desc = suspect_data.descriptions.get_description("at_scene")
            scene_description.append(sus_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got sus desc AT SCENE :{sus_desc}")

        for item_id, item_data in items_present.items():
            item_desc = item_data.descriptions.get_description("at_scene")
            scene_description.append(item_desc)
            desc_logger.debug(f"Loc_Desc/set_scene(): got item desc AT SCENE : {item_desc}")

        scene_description.append(self.get_connection_descriptions(connections))

        desc_logger.debug(f"LOC_DESC set scene: returnins {scene_description}")
        return scene_description

    def get_connection_descriptions(self, connections):
        conn_desc = []
        # GET INTRO PHRASE?!?!
        player_last_loc = self.game_state.player.location_history[-2]
        for connection_id in connections:
            if connection_id != player_last_loc.id:
                # query from the actual connected location, so that you get descriptions based on their state!
                obj = self.game_state.location_manager.get_entity(connection_id)
                if obj:
                    conn_desc.append(obj.descriptions.get_description("connections"))

                    desc_logger.debug(f"Loc_Desc/set_scene():got connected loc desc {conn_desc}")
                else:
                    desc_logger.warning(f"no obj for connection descriptions?")
        return conn_desc

class Door_Descriptions(Loc_Descriptions): #difference is only for setting scene/at entity, handles door open/close / lid logic
    def __init__(self, id, name, entity_state, game_state, descriptions, is_outdoors, lid_component):
        super().__init__(id, name, entity_state, game_state, None, is_outdoors)
        self.descriptions = descriptions
        self.lid_component = lid_component

    def set_scene(self, suspects_present, items_present, connections):
        # Call the inherited set_scene method with an empty connections list
        scene_description = super().set_scene(suspects_present, items_present, [])
        desc_logger.info(f"door desc setting scene - super = {scene_description}")
        scene_description.append(self.lid_component.get_description("at_entity"))

        #Connection descriptions:
        if self.lid_component.is_open:
            scene_description.append(self.get_connection_descriptions(connections))

        desc_logger.debug(f"door setting scene returning scene {scene_description}")
        return scene_description

    def handle_description_keying(self, description_type, descriptions_dic):
        descriptions_dic = super().handle_description_keying(description_type, descriptions_dic)
        if isinstance(descriptions_dic, dict):
            # FIRST, GET DOOR OPEN/CLOSED!
            if self.lid_component.is_open:
                descriptions_dic = descriptions_dic.get("open", descriptions_dic)
            else:
                descriptions_dic = descriptions_dic.get("closed", descriptions_dic)
        return descriptions_dic
