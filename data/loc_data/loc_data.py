
loc_ent_data = {
    "locations": {
        "cab_01": {
            "name": "cab",
            "connections": ["alley_01", "porch_01", "morgue_01"],  #, "butcher_01", "docks_01", "morgue_01"
            "is_outdoors": True
        },
        #PUB
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
            "is_outdoors": True,
        },
        "backroom_01": {
            "name": "backroom",
            "connections": ["backroom_door_01"],
            "is_outdoors": True
        },
        #ALLEY

"alcove_01": {
            "name": "alcove", #smoketype
            "connections": ["alley_02"],
            "is_outdoors": True
        },




        #MORGUE
    },
    "halls": {
        #PUB
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
        # ALLEY
"dead_end_01": {
            "name": "corner", #dumpster, possible weapon, etc secret mobster or occult lore?!
            "connections": ["alley_04"],
            "is_outdoors": True,
"direction_labels": {
                 "forward": "down alley",
                 "backward": "towards the cab"
            },
        },
"alley_01": { #alley entrance
            "name": "sidewalk",
            "connections": ["cab_01", "alley_02"],
            "is_outdoors": True,
            "direction_labels": { #FUCK
                 "forward": "the alley",
                 "backward": "the cab",
                 "continue_title": "Enter:",
                 "return_title": "Return: to"
            },
        },
"alley_02": { #start of actually in alley , with alcove
            "name": "alley",
            "connections": ["alley_01", "alcove_01","alley_03"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "down alley",
                 "backward": "towards the cab"
            },
        },
"alley_03": { #regular alley. NO event trip, booze spill - > makes more sense after crime as panic.
    #narrows
            "name": "alley",
            "connections": ["alley_02", "alley_03_1"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "down alley",
                 "backward": "towards the cab"
            },
        },
"alley_03_1": { #regular alley with little desc, just to make crime feel more epic.
    #narrows
            "name": "alley",
            "connections": ["alley_03", "crime_scene_01"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "down alley",
                 "backward": "towards the cab"
            },
        },

"crime_scene_01": { #murder scene
    #widens to an open space/back court/square
            "name": "alley",
            "connections": ["alley_03_1", "alley_04"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "deeper into alley",
                 "backward": "towards the cab"
            },
        },
"alley_04": {
    #narrows again, -> muddy ground, shoetype
            "name": "alley",
            "connections": ["crime_scene_01", "dead_end_01", "alley_05"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "deeper into alley",
                 "backward": "towards the cab"
            },
        },
"alley_05": {
    #falls here.
            "name": "turn",
            "connections": ["alley_04", "alley_06"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "deeper into alley",
                 "backward": "towards the cab"
            },
        },
"alley_06": { #get up from fall, come to 3 way branch
            "name": "alley",
            "connections": ["alley_05", "fire_escape_01", "alley_07"],
            "is_outdoors": True,
            "direction_labels": {
                "forward": "deeper into alley",
                "backward": "towards the cab"
            },
        },

"fire_escape_01": { #AT BASE OF LADDER.
#event janked metal rail, scrap type AND fire escape here
            "name": "fire escape",
            "connections": ["alley_06", "fire_escape_02"],
            "is_outdoors": True,
            "direction_labels": {
                "forward": "up the ladder",
                "backward": "to alley",
                "continue_title": "Climb:",
                "continue_title_backward": "Continue:"
            },
        },
"fire_escape_02": { #ON LADDER
            "name": "fire escape",
            "connections": ["fire_escape_01", "fire_escape_03"],
            "is_outdoors": True,
            "direction_labels": {
                "forward": "up the ladder",
                "backward": "downwards",
                "continue_title": "Climb:"
            },
        },
"fire_escape_03": { #ON LADDER, JUST BENEATH ROOF
            "name": "fire escape",
            "connections": ["fire_escape_02", "roof_top_01"],
            "is_outdoors": True,
            "direction_labels": {
                "forward": "up onto the roof",
                "backward": "downwards",
                "continue_title": "Climb:"
            },
        },

"roof_top_01": {
            "name": "roof top",
            "connections": ["fire_escape_03"],
            "is_outdoors": True,
            "direction_labels": {
                "forward": "shouldnt ever print this",
                "backward": "downwards",
                "continue_title": "shouldnt:"
            },
        },
"alley_07": { #the alley continues to the residential area. turn back...
            "name": "alleyway",
            "connections": ["alley_06"],
            "is_outdoors": True,
            "direction_labels": {
                 "forward": "deeper into alley",
                 "backward": "towards the cab"
            },
        },
        # MORGUE
    },
    "doors": {
        "backroom_door_01": {
            "name": "iron door",
            "connections": ["backroom_01", "hallway_04"], #2connections max for doors
            "component_descriptions": {"default": {"opening": {"neutral": ["The hinges squeal."]},
                                                   "closing": {"neutral": ["The door slams shut.", ]},
                                                   "closed": {"neutral": ["The iron door faces you."]},
                                                   }}
        },
        "bertha_office_door_01": {
            "name": "wooden door",
            "connections": ["hallway_04", "bertha_office_01"],

            "component_descriptions": {"default": {"opening": {"neutral": ["It slides open effortlessly.", "It swings open."]},
                                                   "closing": {"neutral": ["It closes with a satisfying click.", "It swings shut."]},
                                                   "closed": {"neutral": ["The door leads to Bertha's office.", "The door faces you.",
                                                                          "It's the door to Bertha's office.","A wooden door faces you."]},
                                                   }},
            "lock_mechanism": {
                "id": "office_lock_01",
                "name": "brass lock",
                "key": "brass_key_01",
                "lock_type": "key_lock",
                "outside": "hallway_04",
                "is_locked": False,
                "lock_descriptions": {
                    "default": {
                        "outside_locking": ["The key clicks into place.", "The lock turns with a solid clunk."],
                        "outside_unlocking": ["You hear a clunk as the lock disengages.", "The lock gives way with a soft click."],
                        "inside_locking": ["You turn the knob, hearing the bolt slide into place."],
                        "inside_unlocking": ["The bolt disengages."],
                        "cant_open": ["The door doesn't budge.", "The brass lock holds the door still.", "You pull, but the door remains closed."],
                        "outside_locked": ["A brass keyhole faces you."],
                        "outside_unlocked": ["It's unlocked."],
                        "inside_locked": ["A brass knob is in the lock position."],
                        "inside_unlocked": ["A brass knob is in the unlock position."]
                        }
                    }
                }
            }
        # ALLEY

        # MORGUE
        },

}
