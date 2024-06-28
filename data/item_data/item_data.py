





item_ent_data = {
    "clues": {},
    "drawers": {
        "bertha_office_drawer_01": {
            "name": "desk",
            "spawn_data": {
                "locations": ["bertha_office_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "drawer",
                "component_descriptions": {"default": {"opening":["You pull the drawer open."], "closing":["You push the drawer closed."],
                                                       "closed": ["The drawer is closed."], "opened":["The drawer hangs open."],
                                                       }},
                "lock_mechanism": {
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
        },
    "bertha_office_closet_01": {
            "name": "closet",
            "spawn_data": {
                "locations": ["bertha_office_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "closet door",
                "component_descriptions": {"default": {
                    "opening":["The doors creak open.","The closet opens.",
                               "The hinges grate.", "The hinges groan."],
                    "closing":["The doors swing shut.",
                               "The hinges grate.", "The hinges groan.",],
                }},

        }
    },
},
"items": {
#   bertha
"bertha_clothes_01": {
            "name": "jackets",
            "is_hidden": True,
            "state_data": {
                "default": { #normal
                    "frequency": 0.8
                },
                "cleaned": { #cleaned,
                    "frequency": 0.8,
                    "conditions": {"traits": ["bertha"]},
                },
            },
            "spawn_data": {
                "locations": ["bertha_office_closet_01"],
                "frequency": 1,
                "count": 1,
            },
        },
"bertha_footwear_01": {
            "name": "footwear",
            "is_hidden": True,
            "state_data": {
                "default": { #normal
                    "frequency": 0.8
                },
                "cleaned_shoes": {
                    "frequency": 0.8,
                    "conditions": {"traits": ["bertha", "shoes"]},
                },
                "cleaned_boots": {
                    "frequency": 0.8,
                    "conditions": {"traits": ["bertha", "boots"]},
                }
            },
            "spawn_data": {
                "locations": ["bertha_office_closet_01"],
                "frequency": 1,
                "count": 1,
            },
        },
    "dumpster_01": {
        "name": "dumpster",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["dead_end_01"],
            "frequency": 1,
            "count": 1,
        }
    },

    "kitchen_knife_01": {
        #but always want in kitchen. - regular kitchen knife
        "name": "kitchen knife",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["kitchen_01"],
            "frequency": 1,
            "count": 1,
        }
    },
"murder_knife_01": { #can be missing, in alley, (or returned to kitchen with no one the wiser)
    #should have exact same desc as kitchen knife -> at bar knife
    #maybe state could be the murders knife, so the dialogue is conditional or whatever?
        "name": "bloodied knife",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["dumpster_01", "dead_end_01"],
            "conditions": {"traits": ["knife", "at_bar"]},
            "frequency": 0.8,
            "count": 1,
        }
    },
"revolver_01": {
    "name": "revolver",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "loaded": {
            "frequency": 0.8,
            "conditions": {"traits": ["bertha", "gun"]},
        }
    },
    "spawn_data": {
        "locations": ["bertha_office_drawer_01"],
        "frequency": 1,
        "count": 1,
    }
},
"bullets_01": {
    "name": "bullets",
    "is_hidden": True,
    "state_data": {
        "default": { # closed pack
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations": ["bertha_office_drawer_01"],
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
            "frequency": 0.8,
            "conditions": {"traits": ["bertha", "rum"]},
        }
    },
    "spawn_data": {
        "locations_always_spawn": ["bertha_office_01"],
        "locations": ["bar_01", "backroom_01"],
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
        "opened": { #should have at least one open
            "frequency": 0.8,
            "conditions": {"traits": ["at_bar", "whiskey"]},
        }
    },
    "spawn_data": {
        "locations": ["bar_01", "backroom_01", "bar_01"],
        "frequency": 0.6,
        "count": 3,
    }
},
"matches_01": {
    "name": "engraved matchbook",
    "state_data": {
        "default": {
            "frequency": 0.8,
        },
        "used": {
            "frequency": 0.8,
        }
    },
    "spawn_data": {
        "locations_always_spawn": ["bertha_office_01", "bar_01"],
        "locations": ["porch_01"],
        "frequency": 0.8,
        "count": 1,
        "conditions": {"traits": ["bertha"]}
    }
},
"office_trash_01": {
    "name": "trash can",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": [],
        "locations": ["bertha_office_01"],
        "frequency": 1,
        "count": 1,
    }
},
"matches_02": {
    #CAN HAVE A DIALOGUE ID SYSTEM -> .GET DIALOGUE ID, ENT_ID ; so can have multiple spawning conditions, under the same name.
    "name": "brown matchbook",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "used": {
            "frequency": 0.8
        }
    },
    "spawn_data": {
        "locations_always_spawn": ["office_trash_01"],
        "locations": ["stage_02", "porch_01"],
        "frequency": 0.8,
        "count": 1,
    }
},
"pipe_01": {
    "name": "metal pipe",
    "state_data": {
        "default": {
            "frequency": 0.8
        },

    },
    "spawn_data": {
        "conditions_despawn": {"traits": ["blunt"]},
        "locations": ["alcove_01"],
        "frequency": 0.6,
        "count": 1,
    }
},
"murder_pipe_01": {
        "name": "bloody pipe",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["dumpster_01", "dead_end_01"],
            "conditions": {"traits": ["blunt"]},
            "frequency": 1,
            "count": 1,
        }
    },
"apple_01": {
    "name": "apple",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations": ["kitchen_01", "backroom_01", "stage_02", "dumpster_01", "dead_end_01"],
        "frequency": 0.8,
        "count": 3,
    }
},

}
}
