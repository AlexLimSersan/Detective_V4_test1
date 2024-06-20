from entities.descriptions.base import Mobile_Descriptions
from utilities.state_utils import iterate_vibe_keys

class Sus_Descriptions(Mobile_Descriptions):
    def __init__(self, id, name, mood, entity_state, game_state, descriptions, current_location, is_outdoors=False):
        super().__init__(id, name, entity_state, game_state, descriptions, current_location, is_outdoors)
        self.mood = mood

    # later, may have unique mobile description methods; or suspects/items will inherit this and add methods accordingly

