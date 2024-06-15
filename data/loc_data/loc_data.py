
"""

"""

loc_ent_data = {
    "locations": {
        "cab_01": {
            "name": "cab",
            "connections": ["alley_01", "porch_01"],  #, "butcher_01", "docks_01", "morgue_01"
            "is_outdoors": True
        },
        "porch_01": {
            "name": "porch",
            "connections": ["lounge_01", "cab_01"],
            "is_outdoors": True #default
        },
        "lounge_01": {
            "name": "lounge",
            "connections": ["porch_01", "bar_01", "kitchen_01", "stage_01", "hallway_01"],
            "is_outdoors": True #tag indoors
        },
        "bar_01": {
            "name": "bar",
            "connections": ["lounge_01",],
            "is_outdoors": True
        },
        "kitchen_01": {
            "name": "kitchen",
            "connections": ["lounge_01"],
        },
        "stage_01": {
            "name": "stage",
            "connections": ["lounge_01", "stage_02"],
        },
        "stage_02": {
            "name": "backstage",
            "connections": ["stage_01", "hallway_01"],
        },
        "bertha_office_01": {
            "name": "office",
            "connections": ["bertha_office_door_01"],
            "is_outdoors": True
        },
        "backroom_01": {
            "name": "backroom",
            "connections": ["backroom_door_01"],
            "is_outdoors": True
        },
    },
    "halls": {
        "hallway_01": {
            "name": "hallway",
            "connections": ["lounge_01", "stage_02", "hallway_02"],
            "direction_labels": {
                 "forward": "down hallway",
                 "backward": "towards Pub"
            },
        },
        "hallway_02": {
            "name": "hallway",
            "connections": ["hallway_01", "hallway_03"],
            "direction_labels": {
                 "forward": "down hallway",
                 "backward": "towards Pub"
            },
        },
        "hallway_03": {
            "name": "hallway",
            "connections": ["hallway_02", "hallway_04"],
            "direction_labels": {
                 "forward": "down hallway",
                 "backward": "towards Pub"
            },
        },
        "hallway_04": {
            "name": "hallway",
            "connections": ["hallway_03", "bertha_office_door_01", "backroom_door_01"],
            "direction_labels": {
                 "forward": "down hallway",
                 "backward": "towards Pub"
            },
        },
    },
    "doors": {
        "backroom_door_01": {
            "name": "iron door",
            "connections": ["backroom_01", "hallway_04"], #2connections max for doors
        },
        "bertha_office_door_01": {
            "name": "office door",
            "connections": ["hallway_04", "bertha_office_01"],
            "component_descriptions": {
                "default": {
                    "opening": ["The door clicks open, echoing softly."],
                    "closing": ["The door snaps shut with a finality."],
                    "opened": ["The office door hangs open.","The door is ajar."],
                    "closed": ["The door is firmly shut."]
                },
            },
            "lock_mechanism": {
                "name": "brass lock",
                "key": "brass_key_01",
                "lock_type": "key_lock",
                "outside": "hallway_04",
                "lock_descriptions": {
                    "default": {
                        "outside_locking": "You insert the brass key, feeling it click into place. The lock turns with a solid clunk.",
                        "outside_unlocking": "You turn the brass key. The lock gives way with a soft click.",
                        "inside_locking": "You turn the brass knob, hearing the lock slide into place.",
                        "inside_unlocking": "You turn the brass knob, feeling the lock disengage.",
                        "cant_open": "The door doesn't budge. It's brass locked.",
                        "key_dont_fit": "You try the key. It doesn't fit. Must be the wrong one.",
                        "already_locked": "The lock's already in place. No need to turn it again.",
                        "already_unlocked": "It's already unlocked. No resistance at all.",
                        "outside_locked": "The lock's in place. The keyhole faces you.",
                        "outside_unlocked": "The lock's undone. The door's ready to open.",
                        "inside_locked": "The knob's turned to lock. The door's secure.",
                        "inside_unlocked": "The knob's in the open position. The door's free."
                        }
                    }
                }
            }
        }
    }