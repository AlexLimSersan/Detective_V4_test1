from entity_managers.base import Entity_Manager
from entities.entities.items import Item, Clue
import random

from config.settings import ITEM_SPAWN_FREQUENCY, ITEM_STATE_FREQUENCY
from config.logging_config import ent_logger



murderer_profile_all_possibilities = {
            "murderer": ["bertha", "gibbs", "phil", "bob", "maxwell"],
            "weapon_type": ["knife", "gun", "blunt"],
            "fight_type": ["strong", "weak"],
            "outfit_type": ["leather", "denim"],
            "smoke_type": ["cigs", "tobacco", "none"],
            #maybe at bar just for dialogue and story YES
            "match_type": ["new_matches", "old_matches", "none"],
            "drink_type": ["whiskey", "rum", "none"],
            "hair_type": ["hair", "bald"],
            "shoe_type": ["shoes", "boots"],
        }

# STATE DEFALT FREQdefault is 0.8, maybe clues different. When default is selected, 80% chance of default, else a random other state (ie goes back to cleaned)
item_data = {
    "item_id": {
        "name": "name",
        "state_data": {
            #states keyed to data
            "default": {
                "frequency": 0.8 #KEEP AT THIS VALUE PLEASE.
            },
            "cleaned": {
                "conditions": {"traits": "bertha"} #IGNORE FOR NOW PLEASE:conditions that if all met will set this state to starting state, else default
            }
        },
        "spawn_data": {
            "locations": ["loc_1", "loc_2"], #list of possible locations
            "frequency": 1, #item default spawn freq is 1, please keep like this please
            "count": 1, #number of times the item spawns. please keep as one for now 1
            "conditions": {"traits": ["bertha", "leather"], #IGNORE FOR NOW PLEASE ; murderer traits (or other conditions) that MUST be present for spawn
        }
    }
}
}

class Item_Manager(Entity_Manager):
    def __init__(self, entity_data, description_data, game_state):
        super().__init__(entity_data, description_data, game_state)

    def load_entities(self):
        #load items (and clues)
        for item_id, item_data in self.entity_data["clues"].items():
            self.entities[item_id] = Clue(id=item_id,
                                        game_state=self.game_state,
                                        descriptions=self.description_data[item_id],
                                        #any components get unpacked from the data
                                        **item_data)
            ent_logger.debug(f"loading clue {item_id}, {item_data}")
        for item_id, item_data in self.entity_data["items"].items():
            self.entities[item_id] = Item(id=item_id,
                                        game_state=self.game_state,
                                        descriptions=self.description_data[item_id],
                                        #any components get unpacked from the data
                                        **item_data)
            ent_logger.debug(f"loading item {item_id}, {item_data}")

    def spawn_items(self):
        #spawn entities in locations
        for item_id, item in self.entities.items():
            spawn_data = item.spawn_data
            state_data = item.state_data

            #CHECK FREQUENCY:
            if random.random() < self.entities[item_id].spawn_frequency: #default vs custom spawn frequency handled in entity (makes CLUES vs ITEMS logic easier)
                #CHECK SPAWN_CONDITIONS
                if self.check_conditions(spawn_data.get('conditions', {})):
                    #DETERMINE STARTING STATE
                    self.entities[item_id].entity_state = self.determine_state(state_data)

                    #SPAWN ITEM
                    number_to_spawn = spawn_data.get("count", 1)
                    spawn_locations = spawn_data.get("locations")
                    spawn_locations = spawn_locations[:number_to_spawn]
                    self.game_state.location_manager.spawn_entities(self.entities[item_id], spawn_locations)
                    ent_logger.info(f"Spawning item {item_id} in all {spawn_locations} \nwith state {self.entities[item_id].entity_state}")

    def determine_state(self, state_data):
        if state_data:
            for state, data in state_data.items():
                if state != "default" and self.check_conditions(data.get("conditions", {})):
                    if random.random() <= data.get("frequency", ITEM_STATE_FREQUENCY):
                        return state
        return "default"

    def check_conditions(self, conditions_dic):
        if not conditions_dic:
            return True
        murderer_profile = self.game_state.suspect_manager.murderer.profile
        for condition, values in conditions_dic.items():
            if condition == "traits":
                if all(cond in murderer_profile.values() for cond in values):
                    # means that an item was set based on the murderer, therefore:
                    #can add the STORY TRACKER and STATS tracker stuff here!
                    return True
            # can have other conditions as needed
        return False



