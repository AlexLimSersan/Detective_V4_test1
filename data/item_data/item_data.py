





item_ent_data = {
    "clues": {},
    "drawers": {
        "bertha_office_drawer_01": {
            "name": "desk",
            "spawn_data": {
                "locations": ["kitchen_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "drawer",
                "component_descriptions":{},
                "lock_mechanism": {
                    "id": "not needed lol",
                    "name": "bebe lock",
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
        }
    },
"items": {
    "kitchen_knife_01": {
        "name": "knife",
        "state_data": {
            "default": {
                "frequency": 0.8
            },
            "cleaned": {
                "conditions": {"traits": ["bertha"]}
            }
        },
        "spawn_data": {
            "locations": ["kitchen_01"],
            "frequency": 1,
            "count": 1,
        }
    },
"revolver_01": {
    "name": "revolver",
    "state_data": {
        "default": {
            "frequency": 0.8
        },

    },
    "spawn_data": {
        "locations": ["bertha_office_01"],
        "frequency": 1,
        "count": 1,
    }
},
"rum_01": {
    "name": "rum bottle",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "opened": {

        }
    },
    "spawn_data": {
        "locations": ["bar_01", "lounge_01"],
        "frequency": 1,
        "count": 1,
    }
},
"whiskey_01": {
    "name": "whiskey bottle",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "opened": {

        }
    },
    "spawn_data": {
        "locations": ["lounge_01", "porch_01"],
        "frequency": 1,
        "count": 1,
"conditions": {"traits": ["bertha"]}
    }
},
"matches_01": {
    "name": "engraved matchbook",
    "state_data": {
        "default": {
            "frequency": 0.8
        },

    },
    "spawn_data": {
        "locations": ["lounge_01", "porch_01"],
        "frequency": 1,
        "count": 1,
        "conditions": {"traits": ["bertha"]}
    }
},
"apple_01": {
    "name": "apple",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "rotten": {

        }
    },
    "spawn_data": {
        "locations": ["kitchen_01", "backroom_01", "stage_02"],
        "frequency": 1,
        "count": 2,
    }
}


}}
