

#CLUE FREQUENCY: .8

#can change default frequency as needed
#for frequency, would need something like for count, %chance to spawn. other wise 80% of the time, 3 spawn. I want 80% of the time, 3 times, so you can have 0-3
clue_data = {
#WEAPON blood
    "knife_blood_01": {
#first is fatal/essential, 100% spawn
        "name": "pool of blood",
        "conditions": { #conditions for item to spawn
            "frequency": 1, #default 0.8, so 20% chance of not appearing
            "trait": ["knife"], #murderer traits that MUST be present for spawn
        },
        "spawns": {
            "location": ["crime_scene_01"], #list of possible locations
            "count": 1
        }
    },
    "knife_blood_02": {
        "name": "blood splatter",
        "conditions": {
            "trait": ["knife"],
        },
        "spawns": {
            "location": ["alley_02"], #different desc, for blood
        }
    },
    "gun_blood_01": {
        "name": "pool of blood", #BACK SPATTER descr
        "conditions": {
            "frequency": 1,
            "trait": ["gun"],
        },
        "spawns": {
            "location": ["crime_scene_01"],

        }
    },
    "gun_blood_02": {
        "name": "blood spatter", #mist
        "conditions": {
            "frequency": 1,
            "trait": ["gun"],
        },
        "spawns": {
            "location": ["crime_scene_01"],

        }
    },
    "gun_misc_01": {
        "name": "bullet casing",
        "conditions": {
            "trait": ["gun"],
        },
        "spawns": {
            "location": ["crime_scene_01"],

        }
    },
    #weapon wound
    "knife_wound_01": {

        "name": "stab wound",
        "conditions": { #conditions for item to spawn
            "frequency": 1, #default 0.8, so 20% chance of not appearing
            "trait": ["knife"], #murderer traits that MUST be present for spawn
        },
        "spawns": {
            "location": ["torso_01"], #list of possible locations
        },
    "knife_wound_02": {
        "name": "slashes",
        "conditions": { #conditions for item to spawn
            "trait": ["knife"],
        },
        "spawns": {
            "location": ["arms_01", "torso_01"],
        }
    },
    "knife_wound_03": {
        "name": "cuts",
        "conditions": {
            "trait": ["knife"],
        },
        "spawns": {
            "location": ["hands_01", "arms_01"],
            }
        }
    },
    "gun_wound_01": {
        "name": "bullet wound", #spatter vs splatter
        "conditions": {
            "frequency": 1,
            "trait": ["gun"],
        },
        "spawns": {
            "location": ["torso_01"],
        }
    },
    "gun_wound_02": {
        "name": "catastrophic cranial injury", #headshot #devastating
        "conditions": {
            "trait": ["gun"],
        },
        "spawns": {
            "location": ["head_01"],
        }
    },
#FIGHT TYPE STRONG, WEAK
"strong_bruise_01": {
        "name": "severe bruising",#contusions Fractures lacerations
        "conditions": {
            "frequency": 1,
            "trait": ["strong"],
        },
        "spawns": {
            "location": ["torso_01"],
        }
    },
"strong_bruise_02": {
        "name": "blunt force trauma",#defending , contusions Fractures lacerations
        "conditions": {
            "trait": ["strong"],
        },
        "spawns": {
            "location": ["arms_01, legs_01"],
        }
    },
"strong_bone_01": {
        "name": "crushed ribs", #beaten, crushing
        "conditions": {
            "trait": ["strong"],
        },
        "spawns": {
            "location": ["torso_01"],
        }
    },
"strong_bone_02": {
        "name": "fracture", #broken, snapped
        "conditions": {
            "trait": ["strong"],
        },
        "spawns": {
            "location": ["arms_01","legs_01"],
        }
    },#other strong clue but item/state: A pair of dented metal garbage cans, one tipped over with its contents spilling out onto the damp pavement.
"weak_bruise_01": {
        "name": "superficial bruise",#abrasions, #light discoloration
        "conditions": {
            "trait": ["weak"],
        },
        "spawns": {
            "location": ["crime_scene"],
        }
    },
"weak_bruise_02": {
        "name": "abrasions",#scrapes#abrasions, #light discoloration
        "conditions": {
        },
        "spawns": {
            "location": ["arms_01", "legs_01"],
        }
    },

#OUTFIT DENIM LEATHER

"leather_01": {
        "name": "leather scrap", #torn leather, torn fabric
        "conditions": {
            "trait": ["leather"],
        },
        "spawns": {
            "location": ["alley_turn_01"],
        }
    },
"denim_01": {
        "name": "denim scrap", #torn leather, torn fabric
        "conditions": {
            "trait": ["denim"],
        },
        "spawns": {
            "location": ["alley_turn_02"],
        }
    },
#SMOKE TYPE CIGS TOBacco NONE
"cigs_01": {
        "name": "cigarette butt",
        "conditions": {
            "trait": ["cigs"]
        },
        "spawns": {
            "location": ["alley_01"],
        }
    },
"tobacco_01": {
        "name": "tobacco ashes",
        "conditions": {
            "trait": ["tobacco"]
        },
        "spawns": {
            "location": ["alley_01"],
        }
    },
#matchbook new old
"new_matchbook_01": {
        "name": "black matchbook",
        "conditions": {
            "trait": ["new_matches"]
        },
        "spawns": {
            "location": ["alley_trip_01"],
        }
    },
"old_matchbook_01": {
        "name": "old matchbook",
        "conditions": {
            "trait": ["old_matches"]
        },
        "spawns": {
            "location": ["alley_trip_01"],
        }
    },
#DRINK TYPE WHISKEY RUM NONE
"whiskey_01": {
        "name": "spilled whiskey",
        "conditions": {
            "trait": ["whiskey"]
        },
        "spawns": {
            "location": ["alley_trip_01"],
        }
    },
"rum_01": {
        "name": "spilled rum",
        "conditions": {
            "trait": ["rum"]
        },
        "spawns": {
            "location": ["alley_trip_01"],
        }
    },
#hairtype hair bald
"hair_01": {
        "name": "strand of hair",
        "conditions": {
            "trait": ["hair", "strong"]
        },
        "spawns": {
            "location": ["hands_01"],
        }
    },
"hair_02": {
        "name": "strand of hair",
        "conditions": {
            "trait": ["hair"]
        },
        "spawns": {
            "location": ["ladder_01"],
        }
    },
#SHOE TYPE SHOES BOOT
"shoe_01": {
        "name": "footprint",
        "conditions": {
            "trait": ["shoe"]
        },
        "spawns": {
            "location": ["alley_mud_01"],
        }
    },
"boot_01": {
        "name": "footprint",
        "conditions": {
            "trait": ["boot"]
        },
        "spawns": {
            "location": ["alley_mud_01"],
        }
    },
},

#ITEM SPAWNS:100 (clues 80
#item STATE FREQ 0.8

item_data = {
    "item_id": {
        "name": "name",
        "states": {
            "default": {
                "conditions": { #conditions for item to spawn
                    "frequency": 1, #default 0.8, so 20% chance of not appearing
                    "trait": ["bertha"], #murderer traits that MUST be present for spawn
                }
            }
        },
        "spawns": {
            "location": ["loc_1", "loc_2"], #list of possible locations
            "count": 2, #number of times the item spawns. default is 1
        }
    }
}

item_data_template = {
    "kitchen_knife_01": {
        "name": "kitchen knife",
        "conditions": { #spawn conditions
            #trait, frequency, not trait, and state, if state, check conditions for state, conditions
                "not_trait": ["gibbs","bertha"],
        },
        "state_conditions": {
            "default": {#conditions here, if no conditions True. if conditions present evaluate traits/non_traits
                "trait": [""], #if trait in murderer traits, True -> set state @ frequency else proceed to evaluate other states. if none raise error
                "frequency": 0.8,
            },
            "cleaned": {}
        },
        "spawns": {
            "location": ["kitchen_01"],
        },
        "states": ["default", "cleaned"]
    },
    "butcher_knife_01": {
        "name": "butcher knife",
        "conditions": {
        },
        "state_conditions": {
            "cleaned": {
                "trait": ["bob"],
                "frequency": 1, #default frequency of 1 if trait in traits true
            },
            "default": { #if cleaned conditions false, eval default conditions. if true, default, else, random other condition, and you dont need to evaluate the other conditions
                "frequency" : 0.8
            },
        },
        "spawns": {
            "location": ["butchery_slaughterhouse_01"],
        },
    },
}