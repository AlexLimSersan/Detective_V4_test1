
#clue and item have same format/template below.
#clues and items behave the same from the player/mechanics point of view.
#but i organized clues vs items for me:
#clues are items that are conditional based on the selected murderer trait (ie knife, gun, etc).
#items are based on the totality of possible murderer traits (ie a character has access to a knife AND a gun, a leather AND denim jacket, etc).

clue_data = {
    "item_id": {
        "name": "name",
        "state_data": {
            #states keyed to data
            "default": {
                "frequency": 0.8 #default is 0.8, different between items/clues.
                # When default is selected, 80% chance of default, else a random other state (ie goes back to cleaned)
            },
            "state_2": { #example state: cleaned/washed
                "conditions": {
                    "traits": ["bertha"],  #list of traits, all must be met! check murderer profile.values
                    "current_weather": "rain"
                }, #conditions that if all are met, this state is starting state at the frequency, else not this state
                "frequency": 0.8 #default is 0.8, can be different between items/clues.
            }
        },
        "spawn_data": {
            "locations": ["loc_1", "loc_2"], #list of possible locations
            "frequency": 1, #spawn frequency, default 1
            "count": 1, #number of times the item spawns. default is 1
            "conditions": {"murderer": "bertha", "outfit_type": "leather"}, #murderer traits (or other conditions) that MUST be present for spawn
        }
    }
}



item_description_template = {
    "entity_id": {
        "default": { #default state
            "at_scene": {
                "insert_spawn_location_id": {"neutral": [], "good": [], "bad": [],}
            },
            "approaching": {
"neutral": [], "good": [], "bad": [],
            },
            "at_entity": {
"neutral": [], "good": [], "bad": [],
            },
            "leaving": {
"neutral": [], "good": [], "bad": [],
            },
            "times": {
                "morning": [""],
                "afternoon": [""],
                "evening": [""],
                "night": [""],
            },
            "weather": {
                "rain": [""],
                "sunny": [""],
                "grey": [""],
            },
        },
        #insert non default state here, according to the same template. PLEASE IGNORE FOR NOW.
    },
    #new entities starts here
}
