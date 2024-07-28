





item_ent_data = {
    "clues": {

"murder_matchbook_01": {
    "name": "bloody matchbook",
    "state_data": {
        "default": {
            "frequency": 0
        },
        "brown": {
            "frequency": 1, "conditions": {"traits": ["old"]},
        },
        "black": {
            "frequency": 1, "conditions": {"traits": ["new"]},
        },
    },
    "spawn_data": {
        "locations": ["alley_05"],
        "frequency": 0.8,
        "count": 1,
    }
},

#ashes in alley - its okay cig ashes are more common because debbie smokes
"murder_ash_01": {
    "name": "ashes",
    "state_data": {
        "default": { #cigs or premium
            "frequency": 1,
        },
        "tobacco": {
            "frequency": 1,
            "conditions": {"traits": ["tobacco"]},
        },
    },
    "spawn_data": {
        "locations": ["alcove_01"],
        "frequency": 0.8,
        "count": 1,
    }
},
"murder_roach_01": {
    "name": "squashed roach",
    "state_data": {
        "default": { #debbie with lipstick
            "frequency": 1
        },
        "cigs": {
            "frequency": 1,
            "conditions": {"traits": ["cigs"]},
        },
        "premium": {
            "frequency": 1,
            "conditions": {"traits": ["premium"]},
        },
    },
    "spawn_data": {
        "locations": ["alcove_01","alley_03", "alley_03_1","alley_02"],
        "frequency": 0.5,
        "count": 1,
    }
},

"roach_01": {
    "name": "roach",
    "state_data": {
        "default": { #generic vs premium in description keys
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["office_morgue_desk_01", "bertha_office_drawer_01"],
        "locations": ["porch_01", "bar_01",],
        "frequency": 0.4,
        "count": 2,
    }
},
#ashes in ashtray always mixed except for sus, fuckit

"blood_01": {
        "name": "blood",
        "state_data": {
            "default": {
                "frequency": 1
            },
            "knife": {
                "frequency": 1,
                "conditions": {"traits": ["knife"]},
                        },
            "gun": {
                "frequency": 1,
                "conditions": {"traits": ["gun"]},
                        },
            "blunt": {
                "frequency": 1,
                "conditions": {"traits": ["blunt"]},
                        },
        },
        "spawn_data": {
            "locations_always_spawn": ["crime_scene_01","crime_scene_02"],
            "locations": [],
            "frequency": 1,
            "count": 1,
        }
    },

"tooth_01": {
        "name": "tooth",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["crime_scene_01", "crime_scene_02"],
            "conditions": {"traits": ["void"]}, #fails the condition check so that it doesnt spawn, then moves to conditions any
            "conditions_any": {"traits": ["blunt, strong"]},
            "frequency": 0.7,
            "count": 1,
        }
    },
"bruising_01": { #to be on limbs and what not later
    "name": "bruising",
    "is_hidden": True,
    "state_data": {
        "default": { #weak
            "frequency": 1
        },
        "strong": {
            "frequency": 1,
            "conditions": {"traits": ["strong"]},
                    },
    },
    "spawn_data": {
        "locations_always_spawn": ["debbie_01"],
        "locations": ["limbs_01","torso_01","head_01"],
        "frequency": 1,
        "count": 3,
    }
},

"wounds_01": { #to be on limbs and what not later
    "name": "wounds",
    "is_hidden": True,
    "state_data": {
        "default": { #weak
            "frequency": 1
        },
        "knife": {
            "frequency": 1,
            "conditions": {"traits": ["knife"]},
                    },
        "gun": {
            "frequency": 1,
            "conditions": {"traits": ["gun"]},
                    },
        "blunt": {
            "frequency": 1,
            "conditions": {"traits": ["blunt"]},
                    },
    },
    "spawn_data": {
        "locations_always_spawn": ["debbie_01"],
        "locations": ["limbs_01","head_01","torso_01"],
        "frequency": 1,
        "count": 3,
    }
},

#WEAPONS

"murder_knife_01": { #can be missing, in alley, (or returned to kitchen with no one the wiser)
    #should have exact same desc as kitchen knife -> at bar knife
    #maybe state could be the murders knife, so the dialogue is conditional or whatever?
        "name": "bloody knife",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["dumpster_01", "roof_top_01"],
            "conditions": {"traits": ["knife"]},
            "frequency": 0.7,
            "count": 1,
        }
    },

"murder_gun_01": {
        "name": "bullet casing",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["crime_scene_01","crime_scene_02","alley_03_1"],
            "conditions": {"traits": ["gun"]},
            "frequency": 0.3,
            "count": 2,
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
            "locations": ["dumpster_01", "dead_end_02"],
            "conditions": {"traits": ["blunt"]},
            "frequency": 1,
            "count": 1,
        }
    },

#alley spill trip 05

"garbage_01": { #spilled onto garbage
    "name": "garbage",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["alley_05"], #could also put on scrap piece, or glass
        "frequency": 1,
        "count": 1,
    }
},

"scent_01": {  # spilled onto garbage
        "name": "scent",
        "state_data": {
            "default": {  # regular stinky? should never be used?
                "frequency": 1
            },
            "rum": {
                "frequency": 1,
                "conditions": {"traits": ["rum"]},
            },
            "whiskey": {
                "frequency": 1,
                "conditions": {"traits": ["whiskey"]},
            },
            "gin": {
                "frequency": 1,
                "conditions": {"traits": ["gin"]},
            },
        },
        "spawn_data": {
            "locations": ["garbage_01"],  # could also put on scrap piece, or glass
            "frequency": 0.8,
            "count": 1,
        }
    },

        #SMOKETYPE
#need spill different because of name
"spilled_cigs_01": {
    "name": "loose cigarettes",
    "state_data": {
        "default": {
            "frequency": 0,#should never be used
        },
        "cigs": {
            "frequency": 1,
            "conditions": {"traits": ["cigs"]},
        },
        "premium": {
            "frequency": 1,
            "conditions": {"traits": ["premium"]},
        },
    },
    "spawn_data": {
        "locations": ["alley_05"],
        "conditions": {"traits": ["void"]},
        "conditions_any": {"traits": ["cigs","premium"]},
        "frequency": 0.8,
        "count": 1,
    }
},
"spilled_tobacc_01": {
    "name": "spilled tobacco",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["alley_05"],
        "conditions": {"traits": ["tobacco"]},
        "frequency": 0.8,
        "count": 1,
    }
},

"scrap_leather_01": {
    "name": "torn leather",
    "state_data": {
        "default": { #no stain
            "frequency": 1
        },
        "mustard": {
            "frequency": 0.8,
            "conditions": {"traits": ["mustard"]},
        },
        "tomato": {
            "frequency": 0.8,
            "conditions": {"traits": ["tomato"]},
        },
        "pie": {
            "frequency": 0.8,
            "conditions": {"traits": ["pie"]},
        },
    },
    "spawn_data": {
        "locations": ["fire_escape_01", "fire_escape_02", "fire_escape_03"],

        "conditions": {"traits": ["leather"]},
        "frequency": 0.8,
        "count": 1,
    }
},
"scrap_denim_01": {
    "name": "torn denim",
    "state_data": {
        "default": { #no stain
            "frequency": 1
        },
        "mustard": {
            "frequency": 0.8,
            "conditions": {"traits": ["mustard"]},
        },
        "tomato": {
            "frequency": 0.8,
            "conditions": {"traits": ["tomato"]},
        },
        "pie": {
            "frequency": 0.8,
            "conditions": {"traits": ["pie"]},
        },
    },
    "spawn_data": {
        "locations": ["fire_escape_01", "fire_escape_02", "fire_escape_03"],
        "conditions": {"traits": ["denim"]},
        "frequency": 0.8,
        "count": 1,
    }
},
"scrap_suit_01": {
    "name": "torn suit",
    "state_data": {
        "default": { #no stain
            "frequency": 1
        },
        "mustard": {
            "frequency": 0.8,
            "conditions": {"traits": ["mustard"]},
        },
        "tomato": {
            "frequency": 0.8,
            "conditions": {"traits": ["tomato"]},
        },
        "pie": {
            "frequency": 0.8,
            "conditions": {"traits": ["pie"]},
        },
    },
    "spawn_data": {
        "locations": ["fire_escape_01", "fire_escape_02", "fire_escape_03"],
        "conditions": {"traits": ["suit"]},
        "frequency": 0.8,
        "count": 1,
    }
},

"hair_01": {
    "name": "hair",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["fire_escape_01", "fire_escape_02", "fire_escape_03"],
        "frequency": 0.5,
        "count": 1,
        "conditions": {"traits": ["hair"]},
    }
},

"footprint_01": { #later + debbie to sort through!!
    "name": "mud",
    "state_data": {
        "default": { #debbie
            "frequency": 1
        },
        "sneakers": {
            "frequency": 0.8,
            "conditions": {"traits": ["sneakers"]},
        },
        "dress_shoes": {
            "frequency": 0.8,
            "conditions": {"traits": ["dress_shoes"]},
        },
        "work_boots": {
            "frequency": 0.8,
            "conditions": {"traits": ["work_boots"]},
        },
    },
    "spawn_data": {
        "locations": ["crime_scene_02"], #to allow #later + debbie to sort through!!
        "frequency": 0.8,
        "count": 1,
            }
        },
        ###
#ALL drinks for drink stain types!
"bar_cabinet_01" : {# behind the bar can access maybe if not bertha ; also maybe lowers mood?
            "name": "shelf",
            "spawn_data": {
                "locations": ["bar_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
        },
},

    "drawers": {

"office_morgue_desk_01" : {
            "name": "workbench",
            "spawn_data": {
                "locations": ["morgue_office_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "drawer", #gotta put stuff here?! lol
                "component_descriptions": {
                    "default": {
                        "opening":["You pull the drawer open."],
                        "closing":["You slide the drawer closed."],
                        "closed": [""],
                        "opened":[""],
                    }
                }
            }
        },
"morgue_shelf_01" : {
            "name": "cabinet",
            "spawn_data": {
                "locations": ["morgue_office_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "sliding doors", #gotta put stuff here?! lol
                "component_descriptions": {
                    "default": {
                        "opening":["You slide the doors open."],
                        "closing":["You slide the doors closed."],
                        "closed": [""],
                        "opened":[""],
                    }
                }
            }
        },
        ###
#ALL ingredients for food stain types!
"fridge_01" : {# behind the bar can access maybe if not bertha ; also maybe lowers mood?
            "name": "fridge",
            "spawn_data": {
                "locations": ["kitchen_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "fridge", #gotta put stuff here?! lol
                "component_descriptions": {
                    "default": {
                        "opening":["It takes a bit more force than you expected.","The vacuum makes you have to pull it twice."],
                        "closing":["The door's weight makes the fridge sway."],
                        "closed": ["It's closed"],
                        "opened":["It's open."],
                    }
                }
            }
        },

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
                "component_descriptions": {
                    "default": {
                        "opening":["You have to shimmy it while pulling.","It gets caught as you pull, but eventually gives way.", "It's sides scrape against the wood."],
                        "closing":["You have to jamble it around to close it.","It resists, but eventually slides inwards.", "It's sides scrape against the wood."],
                        "closed": ["The drawer is shut."],
                        "opened":["The drawer hangs open."],
                    }
                }
            }
        },
"bertha_office_closet_01": {
            "name": "closet",
            "spawn_data": {
                "locations": ["bertha_office_01"],
                "frequency": 1,
                "count": 0,
            },
            "state_data": {},
            "components": {
                "name": "closet",
                "component_descriptions": {
                        "default": {
                            "opening":["You grab the handles and pull.",
                                       "The hinges grate.", "The hinges groan."],
                            "closing":[ "You push the doors closed.",
                                        "The hinges grate.", "The hinges groan.",],
                            "closed": ["The doors face you.","It's closed."],
                            "opened":["The doors hang by your sides.", "It's open."],
                        }
                }
            }
        },

        ### tbh head, torso, arms, etc, feels good here. purse, cardigan..
"debbie_01": { #
            "name": "debbie",
            "spawn_data": {
                "locations": ["refrigeration_02"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {
                "default": { #could have weapon?
                    "frequency": 1
                },
            },
            "components": {
                "name": "Debbie",
                "option_titles": {
                    "open_title": "pull",
                    "close_title": "cover",
                    "open_desc": "remove cloth",
                    "close_desc": "with cloth"
                },
                "component_descriptions": {
                        "default": {
                            "opening":["You pull the cloth away.","You remove the cover.",
                                       "The fabric drags as you pull.","You peel the cloth away.",""],
                            "closing":[ "You throw the cloth over her.","It lowers as air escapes.",
                                        "You drape the cloth across her.","You cover her with the cloth."],
                            "closed": ["A white cloth forms subtle, alternating curves.",
                                       "A cloth traces a still form with concave and convex slopes.",
                                       "A white cloth covers a body.",
                                       "The cloth drapes, its edges gently brushing the floor."],
                            "opened":[
                                "Glassy, fixed eyes stare into the void.\n"
                                "Long, brown hair forms a tangled mess, framing a waxy, pale face.",

                                "Brown hair splays around a bloody figure.\n"
                                "Her limbs are locked at awkward angles, her skin abnormally pale. "
                                ,
                                "A sunken, gaunt face looks through you.\n"
                                "Her muscles are rigid and stiff, her hair brown and bloodied.; "
                                ,
                                "Brown strands of hair lace across bloody features.\n"
                                "Her eyes are sunken and dry, her lips parted, chapped and blue."
                                ,
                                "Her face is locked in terror.\n"
                                "Glassy, unseeing eyes are framed by tangled, brown hair."

                                      ],
                        }
                }
            }
        },



},



"items": {

"morgue_tools_01":{
    "name": "tools",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["morgue_office_01"],
        "frequency": 1,
        "count": 1,
    }
},

#BACKROOM
"backroom_counter_01":{
    "name": "counter",  #more gibbs stuff here
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["backroom_01"],
        "frequency": 1,
        "count": 1,
    }
},
"backroom_table_01":{
    "name": "gambling tables",  #more gibbs stuff here
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["backroom_01"],
        "frequency": 1,
        "count": 1,
    }
},
"secret_01":{
    "name": "ledger",  #gibbs secret
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["backroom_counter_01"],
        "frequency": 1,
        "count": 1,
    }
},

#ashtrays
"ashtray_01": {
    "name": "ashtray",  #public ashtrays
    "state_data": {
        "default": { #mix
            "frequency": 0.8
                },
        "empty": {
            "frequency": 0.2
                },
    },
    "spawn_data": {
        "locations_always_spawn": ["office_morgue_desk_01","bertha_office_drawer_01"],
        "locations": [ "bar_01", "backroom_counter_01",],
        "frequency": 1,
        "count": 1,
    }
},


"dumpster_01": {
        "name": "dumpster",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["dead_end_02"],
            "frequency": 1,
            "count": 1,
        }
    },


"kitchen_knife_01": { #regular kitchen knife, always be in kitchen
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
"revolver_02": {
    "name": "pistol",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations": ["leather_jacket_02","office_morgue_desk_01"],
        "frequency": 1,
        "count": 1,
    }
},
"bullets_01": {
    "name": "bullets",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations": ["bertha_office_drawer_01","office_morgue_desk_01"],
        "frequency": 1,
        "count": 2,
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
        "locations": ["bertha_office_01"],
        "frequency": 1,
        "count": 1,
    }
},

"porch_table_01": {
            "name": "table",
            "state_data": {
                "default": { #normal
                    "frequency": 1
                },
            },
            "spawn_data": {
                "locations": [],
                "frequency": 1,
                "count": 1,
            },
        },
"matches_01": {
    "name": "black matchbook",
    "state_data": {
        "default": {
            "frequency": 0.8,
        },
        "used": {
            "frequency": 0.8,
        }
    },
    "spawn_data": {
        "locations_always_spawn": ["bertha_office_drawer_01", "bar_01"],
        "locations": ["porch_01", "leather_jacket_01", "suit_jacket_02"],
        "frequency": 0.6,
        "count": 1,
    }
},

"matches_02": {
    "name": "brown matchbook",
    "state_data": {
        "default": {
            "frequency": 0.4
        },
        "used": {
            "frequency": 0.8
        }
    },
    "spawn_data": {
        "locations_always_spawn": ["office_trash_01", "leather_jacket_02"],
        "locations": ["porch_01", "office_morgue_desk_01","backroom_counter_01","suit_jacket_02"],
        "frequency": 0.5,
        "count": 2,
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
        "conditions_despawn": {"traits": ["blunt"]}, #CAUSE THEN MURDER PIPE SPAWNS
        "locations": ["alcove_01","alley_03","alley_02"],
        "frequency": 0.8,
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
        "locations": ["kitchen_01", "backroom_01", "stage_02", "dumpster_01", "office_trash_01",
                      "dead_end_01", "bar_01", "porch_01", "office_morgue_desk_01"],
        "frequency": 0.6,
        "count": 2,
    }
},

"flask_01": {
    "name": "flask",
    "state_data": {
        "default": {
            "frequency": 0
        },
        "1": { #1 gin, 2 other
            "frequency": 1,
            "conditions": {"traits": ["gin"]}
        },
        "2": {
            "frequency": 1,
        },
    },
    "spawn_data": {
        "locations": ["bertha_office_01","morgue_shelf_01"],
        "frequency": 1,
        "count": 2,
    }
},

"gin_01": {
    "name": "gin",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "opened": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["bar_cabinet_01","morgue_shelf_01"],
        "locations": [ "stage_02", "porch_01"],
        "frequency": 1,
        "count": 1,
    }
},
"whiskey_01": {
    "name": "whiskey",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "opened": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["bar_cabinet_01", "morgue_shelf_01"],
        "locations": [ "backroom_counter_01",],
        "frequency": 1,
        "count": 1,
    }
},

"rum_01": {
    "name": "rum",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "opened": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["bar_cabinet_01"],
        "locations": ["backroom_counter_01", "porch_01"],
        "frequency": 1,
        "count": 1,
    }
},

"tomato_01": {
    "name": "tomato soup",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["fridge_01"],
        "locations": ["bar_01","stage_02"],
        "frequency": 1,
        "count": 1,
    }
},

"mustard_01": {
    "name": "sandwich",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["fridge_01", "morgue_shelf_01"],
        "locations": ["backroom_counter_01","backroom_01","bar_01"],
        "frequency": 1,
        "count": 1,
    }
},

"pie_01": {
    "name": "pie",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["fridge_01",  "morgue_shelf_01"],
        "locations": ["stage_02"],
        "frequency": 1,
        "count": 1,
    }
},


"lighter_01": { #maybe not always debbies later?
    "name": "lighter",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["cardigan_01", "crime_scene_01", "crime_scene_02"],
        "frequency": 1,
        "count": 1,
    }
},
"cardigan_01": {
    "name": "clothing",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 0.8
        },
        "torn": {
            "frequency": 1,
            "conditions": {"traits": ["strong"]}
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["debbie_01"],
        "locations": ["torso_01"],
        "frequency": 1,
        "count": 1,
    }
},

"cardigan_scraps_01": {
    "name": "wool fibers",
    "state_data": {
        "default": {
            "frequency": 0.8
        },
    },
    "spawn_data": {
        "locations": [ "crime_scene_01", "crime_scene_02", "alley_04"],
        "conditions": {"traits": ["strong"]},
        "frequency": 0.8,
        "count": 1,
    }
},

"glass_01": {
    "name": "wine glass",
    "state_data": {
        "default": {
            "frequency": 0
        },
        "white": {
            "frequency": 0.5
        },
        "red": {
            "frequency": 0.5
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["stage_02"],
        "locations": ["bar_01", "porch_01", "backroom_01","morgue_office_01"],
        "frequency": 1,
        "count": 1,
    }
},

"ticket_01": {
    "name": "bus ticket",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["stage_02","stage_02","stage_02","crime_scene_01", "crime_scene_02", "alley_03_1", "alley_04","cardigan_01"],
        "frequency": 1,
        "count": 1,
    }
},

"lipstick_01": { #debbies lipstick for the cig + cups/handkerchief?
    "name": "lipstick",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["crime_scene_01", "crime_scene_02", "alley_03_1", "cardigan_01", "stage_02"],
        "frequency": 1,
        "count": 1,
    }
},

"purse_01": {
    "name": "purse",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["crime_scene_01", "crime_scene_02", "alley_03_1", "alley_04","debbie_01"],
        "frequency": 1,
        "count": 0,#why have purse?
    }
},


"cigs_01": { #could make pack vs loose by item vs clue then state/spawn logic
    "name": "cigarettes",
    "state_data": {
        "default": {#loose
            "frequency": 0.6
        },
        "pack": {
            "frequency": 0.6
        },
    },
    "spawn_data": {
        "locations_always_spawn" : [], #can have jackets or whateva?
        "locations": ["porch_01", "leather_jacket_01",  "backroom_counter_01", "morgue_shelf_01"],
        "frequency": 0.8,
        "count": 2,
    }
},
"cigs_02": {
    "name": "premium cigarettes",
    "state_data": {
        "default": {#loose
            "frequency": 0.6
        },
        "pack": {
            "frequency": 0.6
        },
    },
    "spawn_data": {
        "locations_always_spawn" : ["office_morgue_desk_01"], #can have jackets or whateva?
        "locations": ["leather_jacket_02"], #maybe gibbs coat?
        "frequency": 0.6,
        "count": 1,
    }
},

"smoke_pipe_01": {
    "name": "tobacco pipe",
    "state_data": {
        "default": {
            "frequency": 0.6
        },
    },
    "spawn_data": {
        "locations_always_spawn" : ["bertha_office_drawer_01"], #can have jackets or whateva?
        "locations": ["office_morgue_desk_01", "morgue_shelf_01"],
        "frequency": 1,
        "count": 1,
    }
},


"tobacco_01": {
    "name": "tobacco pouch",
    "state_data": {
        "default": {
            "frequency": 0.6
        },
    },
    "spawn_data": {
        "locations_always_spawn" : ["bertha_office_drawer_01"], #can have jackets or whateva?
        "locations": ["office_morgue_desk_01", "leather_jacket_02"],
        "frequency": 1,
        "count": 1,
    }
},

"fibers_01": { #under debbies fingernails
    "name": "fingernails",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1 #general dirt and debris, smokes descs
        },
        "hair": {
            "frequency": 0.8,
            "conditions": {"traits": ["hair","strong"]},
        },
        "denim": { #somnething maybe like ; a few fibers, could be denim or cotton; or something like that?
            "frequency": 0.8,
            "conditions": {"traits": ["denim","strong"]},
        },
        "leather": {
            "frequency": 0.8,
            "conditions": {"traits": ["leather","strong"]},
        },
        "suit": {
            "frequency": 0.8,
            "conditions": {"traits": ["suit","strong"]},
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["debbie_01"],
        "locations": ["limbs_01"],
        "conditions": {"traits": ["strong"]},
        "frequency": 1,
        "count": 1,
    }
},

"earring_01": {
    "name": "ear ring",
    "is_hidden": True,
    "state_data": {
        "default": { #both
            "frequency": 1
        },
        "single": { #only 1
            "frequency": 1,
            "conditions": {"traits": ["strong"]},
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["debbie_01"],
        #"locations_always_spawn": ["head_01"], #can match earing to her ear
        "locations": ["crime_scene_01", "crime_scene_02"],
        "conditions": {"traits": ["strong"]},
        "frequency": 0.6,
        "count": 1,
    }
},

"shoe_rack_01": { #all shoe types
    "name": "shoe rack",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["lounge_01"],
        "frequency": 1,
        "count": 1,
    }
},

"hanger_01": { #all jacket types
    "name": "coat rack",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["lounge_01"],
        "frequency": 1,
        "count": 1,
    }
},

"denim_jacket_01": {  #BERTHA
    "name": "denim jacket",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["hanger_01"],
        "frequency": 1,
        "count": 1,
    }
},
"leather_jacket_01": { #BERTHA ; wearing denim, has leather jacket
    "name": "leather jacket",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["hanger_01"],
        "frequency": 1,
        "count": 1,
    }
},
"leather_jacket_02": { #MORTICIAN ; classic clean
    "name": "leather coat",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["reception_02"],
        "frequency": 1,
        "count": 1,
    }
},
"suit_jacket_02": { #GIBBS
    "name": "formal blazer",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["hanger_01"],
        "frequency": 1,
        "count": 1,
    }
},

"high_heels_01": { #debbie
    "name": "high heels",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["limbs_01"],
        "frequency": 1,
        "count": 1,
    }
},
"sneakers_01": { #bertha wearing, gibbs on rack
    "name": "sneakers",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["shoe_rack_01"],
        "locations": [],
        "frequency": 1,
        "count": 1,
    }
},
"dress_shoes_01": { #mort wearing, gibbs wearing
    "name": "dress shoes",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["shoe_rack_01"],
        "locations": [], #MORT also WEARING DRESS SHOES
        "frequency": 0.5,
        "count": 0,
    }
},
"workboots_01": { #
    "name": "work boots",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations_always_spawn": ["shoe_rack_01", "reception_02"],
        "locations": [],
        "frequency": 0.5,
        "count": 1,
    }
},


"head_01": { #
    "name": "head",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        #"locations_always_spawn": ["debbie_01"],
        "locations": [],
        "frequency": 0.5,
        "count": 1,
    }
},

"torso_01": { #
    "name": "torso",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        #"locations_always_spawn": ["debbie_01",],
        "locations": [],
        "frequency": 0.5,
        "count": 1,
    }
},

"limbs_01": { #
    "name": "limbs",
    "is_hidden": True,
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        #"locations_always_spawn": ["debbie_01"],
        "locations": [],
        "frequency": 0.5,
        "count": 1,
    }
},

},
}

