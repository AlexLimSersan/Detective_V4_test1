from entities.descriptions.base import Mobile_Descriptions
from utilities.state_utils import iterate_keys
from config.logging_config import desc_logger
class Item_Descriptions(Mobile_Descriptions):
    def __init__(self, id, name, entity_state, game_state, descriptions, current_location, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, current_location, is_outdoors)
    # later, may have unique mobile description methods; or suspects/items will inherit this and add methods accordingly



