clue_data = {
    # WEAPON blood
    "knife_blood_01": {
        "name": "pool of blood",
        "state_data": {
            "default": {
                "frequency": 1
            }
        },
        "spawn_data": {
            "locations": ["crime_scene_01"],
            "frequency": 1,
            "count": 1,
            "conditions": {
                "trait": "knife"
            }
        }
    },
    "knife_blood_02": {
        "name": "blood splatter",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["alley_02"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "knife"
            }
        }
    },
    "gun_blood_01": {
        "name": "pool of blood",
        "state_data": {
            "default": {
                "frequency": 1
            }
        },
        "spawn_data": {
            "locations": ["crime_scene_01"],
            "frequency": 1,
            "count": 1,
            "conditions": {
                "trait": "gun"
            }
        }
    },
    "gun_blood_02": {
        "name": "blood spatter",
        "state_data": {
            "default": {
                "frequency": 1
            }
        },
        "spawn_data": {
            "locations": ["crime_scene_01"],
            "frequency": 1,
            "count": 1,
            "conditions": {
                "trait": "gun"
            }
        }
    },
    "gun_misc_01": {
        "name": "bullet casing",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["crime_scene_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "gun"
            }
        }
    },
    # weapon wound
    "knife_wound_01": {
        "name": "stab wound",
        "state_data": {
            "default": {
                "frequency": 1
            }
        },
        "spawn_data": {
            "locations": ["torso_01"],
            "frequency": 1,
            "count": 1,
            "conditions": {
                "trait": "knife"
            }
        }
    },
    "knife_wound_02": {
        "name": "slashes",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["arms_01", "torso_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "knife"
            }
        }
    },
    "knife_wound_03": {
        "name": "cuts",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["hands_01", "arms_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "knife"
            }
        }
    },
    "gun_wound_01": {
        "name": "bullet wound",
        "state_data": {
            "default": {
                "frequency": 1
            }
        },
        "spawn_data": {
            "locations": ["torso_01"],
            "frequency": 1,
            "count": 1,
            "conditions": {
                "trait": "gun"
            }
        }
    },
    "gun_wound_02": {
        "name": "catastrophic cranial injury",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["head_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "gun"
            }
        }
    },
    # FIGHT TYPE STRONG, WEAK
    "strong_bruise_01": {
        "name": "severe bruising",
        "state_data": {
            "default": {
                "frequency": 1
            }
        },
        "spawn_data": {
            "locations": ["torso_01"],
            "frequency": 1,
            "count": 1,
            "conditions": {
                "trait": "strong"
            }
        }
    },
    "strong_bruise_02": {
        "name": "blunt force trauma",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["arms_01", "legs_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "strong"
            }
        }
    },
    "strong_bone_01": {
        "name": "crushed ribs",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["torso_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "strong"
            }
        }
    },
    "strong_bone_02": {
        "name": "fracture",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["arms_01", "legs_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "strong"
            }
        }
    },
    "weak_bruise_01": {
        "name": "superficial bruise",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["crime_scene"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "weak"
            }
        }
    },
    "weak_bruise_02": {
        "name": "abrasions",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["arms_01", "legs_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "weak"
            }
        }
    },
    # OUTFIT DENIM LEATHER
    "leather_01": {
        "name": "leather scrap",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["alley_turn_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "leather"
            }
        }
    },
    "denim_01": {
        "name": "denim scrap",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["alley_turn_02"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "denim"
            }
        }
    },
    # SMOKE TYPE CIGS TOBACCO NONE
    "cigs_01": {
        "name": "cigarette butt",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["alley_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "cigs"
            }
        }
    },
    "tobacco_01": {
        "name": "tobacco ashes",
        "state_data": {
            "default": {
                "frequency": 0.8
            }
        },
        "spawn_data": {
            "locations": ["alley_01"],
            "frequency": 0.8,
            "count": 1,
            "conditions": {
                "trait": "tobacco"
            }
        }
    },
}