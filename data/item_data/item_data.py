





item_ent_data = {
    "clues": {

#ashes in alley
"alley_ash_cigs_01": {
    "name": "fine ashes",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["alcove_01"],
        "conditions": {"traits": ["cigs"]},
        "frequency": 0.2,
        "count": 1,
    }
},
"alley_ash_tobacco_01": {
    "name": "coarse ashes",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["alcove_01"],
        "conditions": {"traits": ["tobacco"]},
        "frequency": 0.5,
        "count": 1,
    }
},
"cig_butt_01": {
    "name": "roach",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "conditions": {"traits": ["cigs"]},
        "locations": ["alcove_01", "alley_02"],
        "frequency": 0.4,
        "count": 1,
    }
},


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
            "locations": ["dumpster_01", "dead_end_02"],
            "conditions": {"traits": ["knife", "at_bar"]},
            "frequency": 0.7,
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
            "locations": ["dumpster_01", "dead_end_02"],
            "conditions": {"traits": ["blunt"]},
            "frequency": 1,
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

"tooth_01": {
        "name": "tooth",
        "state_data": {
            "default": {
                "frequency": 1
            },
        },
        "spawn_data": {
            "locations": ["crime_scene_01", "crime_scene_02"],
            "conditions": {"traits": ["blunt, strong"]},
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
        "locations": ["debbie_01"],
        "frequency": 1,
        "count": 1,
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
        "locations": ["debbie_01"],
        "frequency": 1,
        "count": 1,
    }
},

#alley spill trip 05

"drink_stain_type_01": { #spilled onto garbage
    "name": "garbage",
    "state_data": {
        "default": { #not used
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
        "white": {
            "frequency": 1,
            "conditions": {"traits": ["white"]},
        },
        "red": {
            "frequency": 1,
            "conditions": {"traits": ["red"]},
        },
    },
    "spawn_data": {
        "locations": ["alley_05"], #could also put on scrap piece, or glass
        "frequency": 0.8,
        "count": 1,
    }
},

        #SMOKETYPE
"spilled_cigs_01": {
    "name": "loose cigarettes",
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["alley_05"],
        "conditions": {"traits": ["cigs"]},
        "frequency": 0.8,
        "count": 1,
    }
},
"spilled_tobacc_01": {
    "name": "loose tobacco",
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

"scrap_01": {
    "name": "torn fabric",
    "state_data": {
        "default": { #not used
            "frequency": 0
        },
        "denim": {
            "frequency": 1,
            "conditions": {"traits": ["denim"]},
        },
        "leather": {
            "frequency": 1,
            "conditions": {"traits": ["leather"]},
        },
        "suit": {
            "frequency": 1,
            "conditions": {"traits": ["suit"]},
        },
    },
    "spawn_data": {
        "locations": ["fire_escape_01", "fire_escape_02", "fire_escape_03"],
        "frequency": 0.8,
        "count": 1,
    }
},
"food_stain_01": {
    "name": "stain",
    "state_data": {
        "default": { #not used
            "frequency": 0
        },
        "mustard": {
            "frequency": 1,
            "conditions": {"traits": ["mustard"]},
        },
        "tomato": {
            "frequency": 1,
            "conditions": {"traits": ["tomato"]},
        },
        "grease": {
            "frequency": 1,
            "conditions": {"traits": ["grease"]},
        },
        "pie": {
            "frequency": 1,
            "conditions": {"traits": ["pie"]},
        },
    },
    "spawn_data": {
        "locations": ["scrap_01"],
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

"footprint_01": {
    "name": "mud",
    "state_data": {
        "default": { #not used
            "frequency": 1
        },
        "sneakers": {
            "frequency": 1,
            "conditions": {"traits": ["sneakers"]},
        },
        "dress_shoes": {
            "frequency": 1,
            "conditions": {"traits": ["dress_shoes"]},
        },
        "work_boots": {
            "frequency": 1,
            "conditions": {"traits": ["work_boots"]},
        },
    },
    "spawn_data": {
        "locations": ["alley_04"],
        "frequency": 0.8,
        "count": 1,
            }
        },


},

    "drawers": {
        ###
#ALL drinks for drink stain types!
"bar_cabinet_01" : {# behind the bar can access maybe if not bertha ; also maybe lowers mood?
            "name": "cabinet",
            "spawn_data": {
                "locations": ["bar_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "sliding doors", #gotta put stuff here?! lol
                "component_descriptions": {
                    "default": {
                        "opening":["You open the cabinet doors."],
                        "closing":["You close the cabinet doors."],
                        "closed": ["BEVERAGES, LIQUORS, WINES, BEERS, GLASSES, CANS, ETC... JUICES AND ICE TOOLS... NAPKINS, LEMONS/LIMES, FOOD!\n relates to something? deb?"],
                        "opened":["It's open."],
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
                        "opening":["You open the fridge."],
                        "closing":["You close the fridge."],
                        "closed": ["FOOD AND BEVERAGES?! relates to something like debbs?"],
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
                "count": 1,
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
"office_morgue_desk" : {
            "name": "steel desk",
            "spawn_data": {
                "locations": ["office_morgue_01"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "file cabinet", #gotta put stuff here?! lol
                "component_descriptions": {
                    "default": {
                        "opening":["office_morgue_desk open the cabinet doors."],
                        "closing":["You office_morgue_desk the cabinet doors."],
                        "closed": ["office_morgue_desk, LIQUORS, WINES, BEERS, GLASSES, CANS, ETC... JUICES AND ICE TOOLS... NAPKINS, LEMONS/LIMES, FOOD!\n relates to something? deb?"],
                        "opened":["It's office_morgue_desk."],
                    }
                }
            }
        },
"morgue_workbench" : {
            "name": "workbench",
            "spawn_data": {
                "locations": ["refrigeration_02"],
                "frequency": 1,
                "count": 1,
            },
            "state_data": {},
            "components": {
                "name": "compartment", #gotta put stuff here?! lol
                "component_descriptions": {
                    "default": {
                        "opening":["morgue_workbench open the cabinet doors."],
                        "closing":["You morgue_workbench the cabinet doors."],
                        "closed": ["morgue_workbench, LIQUORS, WINES, BEERS, GLASSES, CANS, ETC... JUICES AND ICE TOOLS... NAPKINS, LEMONS/LIMES, FOOD!\n relates to something? deb?"],
                        "opened":["It's morgue_workbench."],
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
                "default": {
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
                            "opening":["You pull the cloth away."],
                            "closing":[ "You throw the cloth over her."],
                            "closed": ["A white cloth covers the corpse."],
                            "opened":["Her corpse lays flat on the table."],
                        }
                }
            }
        },









},




"items": {



#MORTICIAN office stuff
"morgue_leather_jacket": { #on a hanger
            "name": "leather jacket", #its new ok?
            "state_data": {
                "default": { #normal
                    "frequency": 1
                },
            },
            "spawn_data": {
                "locations": ["office_morgue_01"],
                "frequency": 1,
                "count": 1,
            },
        },


#BACKROOM
"gambling_tables":{
    "name": "side tables", #put gibbs stuff here
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
"backroom_counter":{
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
"ledger":{
    "name": "ledger",  #gibbs secret
    "state_data": {
        "default": {
            "frequency": 1
        },
    },
    "spawn_data": {
        "locations": ["backroom_counter"],
        "frequency": 1,
        "count": 1,
    }
},

#ashtrays
"ashtray_01": {
    "name": "glass ashtray",  #public ashtrays
    "state_data": {
        "default": { #mix
            "frequency": 0.8
                },
        "empty": {
            "frequency": 0.2
                },
    },
    "spawn_data": {
        "locations": ["porch_table_01", "bar_01", "gambling_tables",],
        "frequency": 1,
        "count": 3,
    }
},


"ashtray_02": { #bertha office
    "name": "copper ashtray",
    "state_data": {
        "default": { #mix  #NEED TO ADD CONDITIONS
            "frequency": 0.8
                },
        "empty": {
            "frequency": 0.2
                },
        "tobacco": {
            "frequency": 0.8,
            "conditions": {"traits": ["bertha", "tobacco"]}
                },
        "cigarettes": {
            "frequency": 0.8,
            "conditions": {"traits": ["bertha", "cigs"]}
                },
    },
    "spawn_data": {
        "locations": ["bertha_office_drawer_01"],
        "frequency": 1,
        "count": 1,
    }
},

"ashtray_03": { #morgue
    "name": "wood ashtray",
    "state_data": {
        "default": { #mix
            "frequency": 0.8
                },
        "empty": {
            "frequency": 0.2
                },
        "tobacco": {
            "frequency": 0.8,
            "conditions": {"traits": ["mortician", "tobacco"]}
                },
        "cigarettes": {
            "frequency": 0.8,
            "conditions": {"traits": ["mortician", "cigs"]}
                },
    },
    "spawn_data": {
        "locations": ["office_morgue_desk"],
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

#   BERTHA CLUES
"bertha_clothes_01": {
    #CLOTHES AND FOOT COMBOS: if murderer - @ 80%,
        #64% chance both cleaned
        #32% chance one cleaned
        #4% chance neither
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

"porch_table_01": {
            "name": "table",
            "state_data": {
                "default": { #normal
                    "frequency": 1
                },
            },
            "spawn_data": {
                "locations": ["porch_01"],
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
        "locations": ["porch_table_01"],
        "frequency": 0.6,
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
        "conditions_despawn": {"traits": ["blunt"]}, #CAUSE THEN MURDER PIPE SPAWNS
        "locations": ["alcove_01"],
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
        "locations": ["kitchen_01", "backroom_01", "stage_02", "dumpster_01", "dead_end_01", "bar_01", "porch_table_01", "office_morgue_desk"],
        "frequency": 0.8,
        "count": 3,
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
        "locations": ["kitchen_01", "backroom_counter", "gambling_tables", "bar_01", "porch_table_01", "office_morgue_desk"],
        "frequency": 0.8,
        "count": 3,
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
        "locations": ["kitchen_01", "backroom_counter", "gambling_tables", "bar_01", "porch_table_01" ,"office_morgue_desk"],
        "frequency": 0.8,
        "count": 3,
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
        "locations_always_spawn": ["office_trash_01", "morgue_leather_jacket"],
        "locations": ["porch_table_01", "office_morgue_desk"],
        "frequency": 0.5,
        "count": 2,
    }
},


},
}

