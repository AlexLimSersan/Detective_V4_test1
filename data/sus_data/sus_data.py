

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
            "outfit_type": ["denim"],
            "smoke_type": ["cigs"],
            "access_to": ["bar"],
            "match_type": ["new"],
            "drink_type": ["whiskey", "rum"],
            "hair_type": ["hair"],
            "shoe_type": ["shoes"],
        },
        "routine": { #routine management here
            "default": { #can have different states
                "morning": "porch_01",
                "afternoon": "bertha_office_01",
                "else": "bar_01" #ids!
            }
        }
    },
    "gibbs_01": {
        "name": "gibbs",
        "profile":{
            "murderer": ["gibbs"],
            "weapon_type": ["knife", "gun", "blunt"],
            "fight_type": ["strong", "weak"],
            "outfit_type": ["leather", "denim"],
            "smoke_type": ["cigs", "tobacco", "none"],
            "access_to": ["bar"],
            "match_type": ["new_matches", "old_matches", "none"],
            "drink_type": ["whiskey", "rum", "none"],
            "hair_type": ["hair", "bald"],
            "shoe_type": ["shoes", "boots"],
        },
        "routine": { #routine management here
            "default": { #can have different states
                "else": "backroom_01" #ids!
            }
        }
    }
}