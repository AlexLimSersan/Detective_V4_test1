item_description_data = {
"bertha_office_drawer_01": {
"default": {
        "approaching": ["You walk up to the desk."],
        "at_scene": {
                "bertha_office_01": {
                    "neutral": ["The middle of the room hosts a large desk",
                                "A desk sits in the middle of the room."],
                },
        },
        "at_entity": { #sturdy oak scratched
            "neutral": ["Scratches run across the wood grains.", "The surface is coarse and rough.",
                        "It's quite sturdy.", "The surface pricks your palm.",
                        "The desk's surface is coarse oak."],
             },
    },
},
"dumpster_01": {
        "default": {
            "at_scene": {
                "dead_end_01": {
                    "neutral": ["A dumpster is here."],

                }
            },
            "approaching": {
                "neutral": ["It stinks."],
            },
            "at_entity": {
                "neutral": [""],
            },
            "leaving": {
                "neutral": ["You turn around."],
            },
            "times": {
            },
            "weather": {
            }
        },
},
    "kitchen_knife_01": {
        "default": {
            "at_scene": {
                "kitchen_01": {
                    "neutral": ["Kitchen knives are stacked on a knife rack.", "Kitchen knives lie on the counter."],
                }
            },
            "approaching": {
                "neutral": ["Your hand grips the handle.", "Your fingers curl around the hilt."],
            },
            "at_entity": {
                "neutral": ["It's sharp.", "It's been used.", "The blade shines in the light."],
            },
            "leaving": {
                "neutral": ["You put the knife back.", "You place the knife back where it was."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
"murder_knife_01": { #kitchen knife?
        "default": {
            "at_scene": {
                "dumpster_01" : {
                    "neutral": ["You notice a knife buried in the trash.", "A knife is stashed under some trash."],
                },
                "dead_end_01": {
                    "neutral": ["A knife lies next to the dumpster.", "You notice a knife nearby."],
                }
            },
            "approaching": {
                "neutral": ["You hunch over, and grip the handle.","You kneel down and pick it up."],
            },
            "at_entity": {
                "neutral": ["It's blade is bloody and dented. It's handle is cracked.", "It's bloody.","The blade has a few dents, but its nonetheless quite sharp."],
            },
            "leaving": {
                "neutral": ["You put it back.", "You place the knife back."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
    "revolver_01": { #3 shots fired IN THE MRUDER!
        "default": { #unloaded
            "at_scene": {
                "bertha_office_drawer_01": { "neutral": ["There's a revolver and some bullets here."]
                }
            },
            "approaching": {
                "bertha_office_drawer_01": {
                "neutral": ["Your fingers curl around the handle.", "The barrel gleams under the light.", "You pick up the revolver."],
                }
            },
            "at_entity": [{
                "neutral": ["You swing the chamber back.", "You slide the chamber back.",
                            "The chamber slides back with a click.", "The chamber swings back."],
            },
                {
                "neutral": ["It's not loaded.", "It's empty."],
            },
            ],
            "leaving": {
                "neutral": ["You place the revolver back.", "You put it back.", "It clunks on the wood."],
            },
            "times": {
            },
            "weather": {
            }
        },
        "loaded": { #loaded with 3 shots
            "at_scene": {
                "bertha_office_drawer_01": {
                }
            },
            "approaching": {
            },
            "at_entity": {
                "neutral": ["It's loaded, with three shots fired.", "Three bullets are loaded.",
                            "Three bullets are missing from an otherwise full chamber."],
            },
            "leaving": {
            },
            "times": {
            },
            "weather": {
            }
        },
    },
"bullets_01": {
        "default": {
            "at_scene": {
                "bertha_office_drawer_01": {
                    "neutral": [""],
                },
            },
            "approaching": {
                "neutral": ["You pick one of the bullets up.", "You pick up one of the bullets."],
            },
            "at_entity": {
                "neutral": ["It glistens in the light.","It's got some weight to it.","" ],
            },
            "leaving": {
                "neutral": ["You place the bullet back.", "The bullet rattles as you drop it."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
    "rum_01": { #WARM, SWEETT, SYRUP, MOLASSES, CARAMEL, SWEET, fruity? dark, amber,
        "default": { #unsused
            "at_scene": {
                "bar_01": {
                    "neutral":["A bottle of rum sits atop the bar."],
                },
                "bertha_office_01": {
                    "sun": {"neutral":["A bottle of rum is caught in the sunlight.","The sun casts a bottle of rum in dramatic lighting.","A bottle of rum is on a nearby shelf."],},
                    "rain": {"neutral":["A bottle of rum is on a nearby shelf."],},
                    "storm": {"neutral":["A bottle of rum is on a nearby shelf."],},

                },
                "backroom_01": {
                    "neutral":["A bottle of rum is on a nearby shelf."],
                },
            },
            "approaching": {
                    "sun": {"neutral":["It's warm.","The bottle feels warm.", "It's contents glow in the light.","It has a rich, amber glow."],},
                    "rain": {"neutral":["It's cool and heavy in your hand", "It's cool to the touch"],},
                    "storm": {"neutral":["It's cool and heavy in your hand", "It's cool to the touch"],},

                },
            "at_entity": {
                "neutral": ["It hasn't been opened.","The seal is still on, covering the cap."],
            },
            "leaving": {
                "neutral": ["The bottle clunks as you set it back.", "You set the bottle back."],
            },
            "times": {
            },
            "weather": {
            }
        },
        "opened": {
            "at_scene": {
                "bar_01": {
                },
                "bertha_office_01": {
                },
                "backroom_01": {
                },
            },
            "approaching": {
            },
            "at_entity": {
                "neutral": ["A cloy, caramel sweetness hits your nose.","It has a dark, sugary scent.",
                            "The bottle is sticky, with a slight honey scent."],
            },
            "leaving": {
                "neutral": ["You set the bottle back, it's fragrance lingering."],
            },
            "times": {
            },
            "weather": {
            }
        }
    },
"whiskey_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND VODKA IS MORE CONTRASTING
        "default": {#not opened - CAN OPEN TO SMELL IT? WOULD BE EPIC!
            "at_scene": {
                "bar_01": {
                    "neutral": ["A whiskey bottle stands on a nearby shelf."],
                },
                "backroom_01": {
                    "neutral": ["A whiskey bottle sits atop a small table."],
                }
            },
            "approaching": {
                "neutral": ["You grab the bottles neck."],
            },
            "at_entity": {
                "neutral": ["It's not opened.","The cap is screwed down tight."],
            },
            "leaving": {
                "neutral": ["You leave the whiskey bottle behind."],
            },
            "times": {
            },
            "weather": {
            }
        },
        "opened": {
            "at_scene": {
                "lounge_01": {
                },
                "porch_01": {
                }
            },
            "approaching": {
            },
            "at_entity": { #OAK, SPICED, VANILLA, SMOKED OAK #maybe vodka is more contrasting?
                "neutral": ["It has a zesty, fruity scent.", "Notes of vanilla mix with a fresh, fruity scent."],
            },
            "leaving": {
                "neutral": ["You leave the bottle behind, it's aroma lingering."],
            },
            "times": {
            },
            "weather": {
            }
        }
    },
    "matches_01": {
        "default": {
            "at_scene": {
                "bertha_office_01": {
                    "neutral": ["A matchbook lies on her desk."],
                },
                "porch_01": {
                    "rain": {"neutral": ["A matchbook lies soaked on an armrest."],},
                    "storm": {"neutral": ["A matchbook lies soaked on an armrest."],},
                    "sun": {"neutral": ["A matchbook basks in the sun.", "A matchbook lies on an armrest."],}

                },
                "bar_01": {
                    "neutral": ["You see a bowl with some matchbooks in it."],
                },
            },
            "approaching": {
                "neutral": ["You pick it up."],
            },
            "at_entity": [{
                "neutral": ["You thumb the engraving. It's the pub's logo.","It has an engraving of the pub logo."],
            },
                {
                "neutral": ["It's in pristine condition.","It looks very new, practically unblemished."],
            },
            ],
            "leaving": {
                "neutral": ["You leave it behind."],
            },
            "times": {
            },
            "weather": {
            }
        },
        "used": {
            "at_scene": {
            },
            "approaching": {
            },
            "at_entity": [{
                "neutral": ["You thumb the pub's engraved logo.","It has an engraving of the pub logo."],
            },
                {
                "neutral": ["It's in pristine condition, despite missing a few matches.","Although missing some matches, the cover is practically unblemished."],
            },
            ],
            "leaving": {
            },
            "times": {
            },
            "weather": {
            }
        }
    },
"matches_02": { #black vs faded black?
        "default": {
            "at_scene": {
                "office_trash_01": {
                    "neutral": ["You notice a matchbook in the trash."],
                },
                "porch_01": {
                    "rain": {"neutral": ["A matchbook lies soaked on a table nearby."],},
                    "storm": {"neutral": ["A matchbook lies soaked on a table nearby."],},
                    "sun": {"neutral": ["A matchbook is perched on a table nearby."],},

                },
                "stage_02": {
                    "neutral": ["You spot a matchbook in the clutter."],
                },
            },
            "approaching": {
                "neutral": ["You pick it up."],
            },
            "at_entity": [{
                "neutral": ["It's worn, with a faded brown color.","The brown colour has faded over time."],
            },
            ],
            "leaving": {
                "neutral": ["You leave it behind."],
            },
            "times": {
            },
            "weather": {
            }
        },
        "used": {
            "at_scene": {
            },
            "approaching": {
            },
            "at_entity": [{
                "neutral": ["It's worn, with a faded brown color.","The brown colour has faded over time."],
            },
                {
                "neutral": ["It's completely empty.","There isn't a single match left."],
            },
            ],
            "leaving": {
            },
            "times": {
            },
            "weather": {
            }
        }
    },
"apple_01": {
        "default": {
            "at_scene": {
                "kitchen_01": {
                    "neutral": ["An apple sits on the counter."],
                },
                "backroom_01": {
                    "neutral": ["An apple is on a nearby table."],
                },
                "stage_02": {
                    "neutral": ["An apple sits on a prop table."],
                },
                "dumpster_01": {
                    "neutral": ["You notice an apple buried in the trash."],
                },
                "dead_end_01": {
                    "neutral": ["An apple is next to the dumpster."],
                }
            },
            "approaching": {
                "neutral": ["You grab the apple"],
            },
            "at_entity": {
                "good": ["The apple feels firm and ripe in your hand."],
                "bad": ["The apple feels soft and bruised."]
            },
            "leaving": {
                "neutral": ["You leave the apple behind."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
"office_trash_01": {
        "default": {
            "at_scene": {
                "bertha_office_01": {
                    "neutral": ["A trashcan is in the corner."],
                },
            },
            "approaching": {
                "neutral": ["You walk up to the trash."],
            },
            "at_entity": {
                "neutral": ["It's full of miscellaneous garbage."]
            },
            "leaving": {
                "neutral": ["You step back."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
"pipe_01": {
        "default": {
            "at_scene": {
                "alcove_01": {
                    "neutral": ["A metal pipe is propped against the wall."],
                },
            },
            "approaching": {
                "neutral": ["You grab the pipe, feeling its weight."],
            },
            "at_entity": {
                "neutral": ["It's solid lead.", "It's quite heavy."]
            },
            "leaving": {
                "neutral": ["You place the pipe back."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
"murder_pipe_01": {
        "default": {
            "at_scene": {
                "dumpster_01": {
                    "neutral": ["A bloody pipe lies on top some garbage."],
                },
                "dead_end_01": {
                    "neutral": ["A metal pipe, colored red, is behind some garbage."],
                },
            },
            "approaching": {
                "neutral": ["You kneel down and grab the pipe.", "It's cold to the touch."],
            },
            "at_entity": {
                "neutral": ["It's got a few bloodied dents.","The pipe is bloodied.", "Clumps of skin and blood lace a concave dent.",
                            "It's heavy, with red colored indents on it's head."]
            },
            "leaving": {
                "neutral": ["You place the pipe back."],
            },
            "times": {
            },
            "weather": {
            }
        },
    },

"bertha_clothes_01": {
        "default": {
            "at_scene": {
                "bertha_office_closet_01": {
                    "neutral": ["Identical denim jackets hang over an equal mix of shoes and boots."],
                },
            },
            "approaching": {
                "neutral": ["You sift through the jackets.", "The hangers rattle as you sift through them."],
            },
            "at_entity": {
                "neutral": ["They have slight style variations, but are otherwise identical.",
                            "They are all thick blue denim jackets. Some have more wear and tear than others."]
            },
            "leaving": {
                "neutral": [],
            },
            "times": {
            },
            "weather": {
            }
        },
        "cleaned": { #from murder, cooking/bar, mob 'accident', or whateva
            "at_scene": {
                },
            "approaching": {
            },
            "at_entity": [
                {"neutral": ["They have slight style variations, but are otherwise identical...",
                            "They are all thick blue denim jackets. Some have more wear and tear than others..."]},
                {"neutral": ["One of the jackets is has been forcibly cleaned, it's fibers brittle and color stripped.",
                             "One of the jackets is tattered, with white smears. It's been vigorously cleaned.",
                             "One of the jackets is faded and torn. Blanched patches form stripes.",
                             "One of the jackets is frayed, with some discoloration.\nIt's been bleached."]},
            ],
            "leaving": {
                "neutral": [""],
            },
            "times": {
            },
            "weather": {
            }
        },

    },
"bertha_footwear_01": {
        "default": {
            "at_scene": {
                "bertha_office_closet_01": {
                    "neutral": [],
                },
            },
            "approaching": {
                "neutral": ["You kneel down.", "You hunch over..."],
            },
            "at_entity": {
                "neutral": ["The footwear is a mix of average sized shoes and boots.",
                            "Shoes and boots of varying designs are loosely arranged in a row.",]
            },
            "leaving": {
                "neutral": [],
            },
            "times": {
            },
            "weather": {
            }
        },
        "cleaned_shoes": { #from murder, cooking/bar, mob 'accident', or whateva
            "at_scene": {
                "bertha_office_closet_01": {
                },
            },
            "approaching": {
            },
            "at_entity": [
                {"neutral": ["The footwear is a mix of average sized shoes and boots...",
                            "Shoes and boots of varying designs are loosely arranged in a row...",]},
                {"neutral": ["One pair of shoes is noticeably cleaner than the others.",
                             "One pair of shoes has been recently scrubbed, it's seams unraveling."]},
            ],
            "leaving": {
                "neutral": [""],
            },
            "times": {
            },
            "weather": {
            }
        },
    "cleaned_boots": { #from murder, cooking/bar, mob 'accident', or whateva - RECENTLY POLISHED/CLEANED
            "at_scene": {
                "bertha_office_closet_01": {
                },
            },
            "approaching": {
            },
            "at_entity": [
                {"neutral": ["The footwear is a mix of average sized shoes and boots...",
                            "Shoes and boots of varying designs are loosely arranged in a row...",]},
                {"neutral": ["One pair of boots is noticeably more polished than the others. Shallow scratches run across it's heel.",
                             "One pair of boots has been thoroughly scrubbed, and recently polished."]},
            ],
            "leaving": {
                "neutral": [""],
            },
            "times": {
            },
            "weather": {
            }
        },
    },
"bertha_office_closet_01": {
        "default": {
            "at_scene": {
                "bertha_office_01": {
                    "neutral": ["A closet is on the far wall."],
                },
            },
            "approaching": {
                "neutral": ["You approach the far wall.", "You come up to the closet."],
            },
            "at_entity": {
                "neutral": []
            },
            "leaving": {
                "neutral": ["You step back."],
            },
            "times": {
            },
            "weather": {
            }
        },
    }


}