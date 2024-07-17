import random

murderer_profile_all_possibilities = {
            "murderer": ["bertha", "gibbs", "phil", "bob", "maxwell"],
            "weapon_type": ["knife", "gun", "blunt"],
            "fight_type": ["strong", "weak"],
            "outfit_type": ["leather", "denim"],
            "smoke_type": ["cigs", "tobacco", "none"],
            "access_to": ["bar", "docks", "butchery"],
            "match_type": ["new_matches", "old_matches", "none"],
            "drink_type": ["whiskey", "rum", "none"],
            "hair_type": ["hair", "bald"],
            "shoe_type": ["shoes", "boots"],
        }

sus_ent_data = {
    "bertha_01": {
        "name": "bertha",
        "profile": {
            "murderer": ["bertha"],
            "weapon_type": ["knife", "gun", "blunt"],
            "fight_type": ["strong", "weak"],
            "hair_type": ["hair"],
            "scrap_type": ["denim","leather"],
            "smoke_type": ["cigs","tobacco"],
            "access_to": ["bar"],
            "match_type": ["new"],
            "drink_type": ["rum", "gin"],
            "stain_type": ["tomato", "pie"],
            "shoe_type": ["sneakers","work_boots"],
        },
        "routine": { #routine management here
            "default": { #can have different states
                "morning": "porch_01",
                "else": "bar_01" #ids!
            }
        }
    },
    "gibbs_01": {
        "name": "gibbs",
        "profile": {
            "murderer": ["gibbs"],
            "weapon_type": ["knife", "blunt"],
            "fight_type": ["strong"],
            "hair_type": ["bald"],
            "scrap_type": ["denim","suit"],
            "smoke_type": ["cigs","premium"],
            "access_to": ["bar"],
            "match_type": ["new","old"],
            "drink_type": ["rum", "whiskey"],
            "stain_type": ["tomato", "mustard"],
            "shoe_type": ["sneakers","dress_shoes"],
        },
        "routine": { #routine management here
            "default": { #can have different states
                "else": "backroom_01" #ids!
            }
        }
    },
    "mortician_01": {
        "name": "mortician",
        "profile": {
            "murderer": ["mortician"],
            "weapon_type": ["knife", "gun"],
            "fight_type": ["weak"],
            "hair_type": ["hair"],
            "scrap_type": ["suit","leather"],
            "smoke_type": ["premium","tobacco"],
            "access_to": ["morgue"],
            "match_type": ["old"],
            "drink_type": ["whiskey","gin"],
            "stain_type": ["mustard", "pie"],
            "shoe_type": ["dress_shoes","work_boots"],
        },
        "routine": { #routine management here
            "default": { #can have different states
                "night": "void_01",
                "else": "morgue_office_01" #ids!
            }
        }
    }
}