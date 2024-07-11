
#clue and item have same format/template below.
#clues and items behave the same from the player/mechanics point of view.
#but i organized clues vs items for me:
#clues are items that are conditional based on the selected murderer trait (ie knife, gun, etc).
#items are based on the totality of possible murderer traits (ie a character has access to a knife AND a gun, a leather AND denim jacket, etc).

lock_template = {"lock_mechanism": {
                    "id": "brass_lock_01",
                    "name": "brass lock",
                    "key": "brass_key_01",
                    "lock_type": "key_lock",
                    "outside": "bertha_office_01",
                    "is_locked": False,
                    "lock_descriptions": {
                        "default": {
                            "outside_locking": ["You insert the brass key, feeling it click into place. The lock turns with a solid clunk."],
                            "outside_unlocking": ["You turn the brass key. The lock gives way with a soft click."],
                            "inside_locking": ["You turn the brass knob, hearing the lock slide into place."],
                            "inside_unlocking": ["You turn the brass knob, feeling the lock disengage."],
                            "cant_open": ["The door doesn't budge. It's brass locked."],
                            "key_dont_fit": ["You try the key. It doesn't fit. Must be the wrong one."],
                            "already_locked": ["The lock's already in place. No need to turn it again."],
                            "already_unlocked": ["It's already unlocked. No resistance at all."],
                            "outside_locked": ["The lock's in place. The keyhole faces you."],
                            "outside_unlocked": ["The lock's undone. The door's ready to open."],
                            "inside_locked": ["The knob's turned to lock. The door's secure."],
                            "inside_unlocked": ["The knob's in the open position. The door's free."]
                            }
                        }
                    }
                }

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
