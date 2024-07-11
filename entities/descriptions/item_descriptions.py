from entities.descriptions.base import Mobile_Descriptions
from utilities.state_utils import iterate_vibe_keys
from config.logging_config import desc_logger
class Item_Descriptions(Mobile_Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, current_location, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, current_location, is_outdoors)
    # later, may have unique mobile description methods; or suspects/items will inherit this and add methods accordingly
        self.component = None

    def set_scene(self, suspects_present=None, items_present=None, connections=None, optional_key = None):
        desc_logger.debug(f"ITE_DESC set scene: data {suspects_present} {items_present}")
        scene_description = []
        scene_description.append(super().set_scene(optional_key = optional_key))
        # Could prob combine mobile ents, but whateva
        scene_description.append(super().get_at_scene(suspects_present, items_present, self.id))
        desc_logger.debug(f"ITE_DESC set scene: returnins {scene_description}")
        return scene_description

    def set_drawer_scene(self, suspects_present=None, items_present=None, hidden_items_present=None, optional_key = None):
        desc_logger.debug(f"ITE_DESC set drawer scene: data {suspects_present} {items_present}")
        scene_description = []

        #gets desk only if drawer is closed:
        if not self.component.is_open:
            scene_description.append(super().set_scene(optional_key = optional_key))

        #get desk at scene
        if not self.component.is_open:
            scene_description.append(super().get_at_scene(suspects_present, items_present, self.id))

        if self.component:
            #get drawer
            comp_desc = self.component.get_description("at_entity")
            if comp_desc:
                scene_description.append(comp_desc)
            #get drawer at scene if open
            if self.component.is_open:
                scene_description.append(super().get_at_scene(suspects_present, hidden_items_present, self.id))

        desc_logger.debug(f"ITE_DESC set drawer scene: returnins {scene_description}")
        return scene_description

