from entity_managers.base import Entity_Manager
from entities.entities.items import Item, Clue, Drawer
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
        for item_id, item_data in self.entity_data["drawers"].items():
            self.entities[item_id] = Drawer(id=item_id,
                                        game_state=self.game_state,
                                        descriptions=self.description_data[item_id],

                                        #any components get unpacked from the data
                                        **item_data)



    def spawn_items(self):
        #spawn entities in locations
        for item_id, item in self.entities.items():
            spawn_data = item.spawn_data
            locations_always_spawn = spawn_data.get("locations_always_spawn")
            if locations_always_spawn:
                ent_logger.info(
                    f"Spawning locations always spawn \n item {item_id} in all {locations_always_spawn} \nwith state {self.entities[item_id].entity_state}")
                self.game_state.location_manager.spawn_entities(self.entities[item_id], locations_always_spawn)

            #PROCEED AS NORMAL WITH THE REGULAR DATSET
            #get the locations first so you can pass it to the stat tracker.
            number_to_spawn = spawn_data.get("count", 1)

            spawn_locations = spawn_data.get("locations")
            random.shuffle(spawn_locations)
            ent_logger.debug(f"item: {item_id}, spawn_locations: {spawn_locations}\n{spawn_data}")
            spawn_locations = spawn_locations[:number_to_spawn]
            #end of location logic

            #CHECK FREQUENCY:
            if random.random() < self.entities[item_id].spawn_frequency: #default vs custom spawn frequency handled in entity (makes CLUES vs ITEMS logic easier)
                #CHECK DESPAWN_CONDITIONS, else, proceed as regular.
                #lets you have mutually exclusive items with different IDS.
                despawn_conditions = spawn_data.get('conditions_despawn', {})
                if despawn_conditions:
                    if self.check_conditions(despawn_conditions, item_id, "spawn", spawn_locations):
                        continue
                #else:
                if self.check_conditions(spawn_data.get('conditions', {}), item_id, "spawn", spawn_locations):

                    self.game_state.location_manager.spawn_entities(self.entities[item_id], spawn_locations)
                    ent_logger.info(f"Spawning item {item_id} in all {spawn_locations} \nwith state {self.entities[item_id].entity_state}")



    def check_conditions(self, conditions_dic, item_id, query_type=None, spawn_or_state_id=None): #last two are for stat tracker, state vs spawn and relevant ids
        if not conditions_dic:
            return True
        murderer_profile = self.game_state.suspect_manager.murderer.profile
        for condition, values in conditions_dic.items():
            if condition == "traits":
                if all(cond in murderer_profile.values() for cond in values):
                    # means that an item was set based on the murderer, therefore:
                    #can add the STORY TRACKER and STATS tracker stuff here!item_id
                    #can add a -1 tag to related dialogue?
                    ent_logger.info(f"{item_id} is MURDERER CLUE: {condition}, {values}")
                    if query_type != "despawn":
                        self.game_state.stat_tracker.track_murderer(item_id, values, query_type, spawn_or_state_id)
                    return True
            # can have other conditions as needed
        return False



