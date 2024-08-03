item_description_data = {
"murder_matchbook_01": {
        "brown": {
            "at_scene": {
                "default": {
                    "neutral": ["A reddish brown matchbook is squashed into the mud."],
                },
            },
            "at_entity": {
                "neutral": ["Flecks of dried blood cover a faded brown matchbook."],
            },
        },
        "black": {
            "at_scene": {
                "default": {
                    "neutral": ["A reddish black matchbook is squashed into the mud."],
                },
            },
            "at_entity": {
                "neutral": ["Flecks of dried blood cover a matte, black matchbook."],
            },
        },
},
"murder_ash_01": {
        "default": { #cigs or premium
            "at_scene": {
                "default": {
                    "neutral": ["On a windowsill, you notice smeared, fine ashes."],
                },
            },
            "at_entity": {
                "neutral": ["A mix of black and white ashes surround a burn mark.","Ashes follow a scorch mark, each thin flake curling at the edges.", "A black circular imprint centers around streaks of thin, white ash."],
            },
        },
        "tobacco": {
            "at_scene": {
                "default": {
                    "neutral": ["On a windowsill, you notice a small pile of ashes. "],
                },
            },
            "at_entity": {
                "neutral": ["Soot mixes with bits of unburnt tobacco, forming sticky, granular clumps."],
            },
        },
},
"murder_roach_01": {
        "default": { #debs
            "at_scene": {
                "default": {
                    "neutral": ["Squashed into the ground lies a roach."],
                },
            },
            "at_entity": {
                "neutral": ["It's burned right down to the butt. Glossy, pink smears contrast against the crumpled white filter."],
            },
        },
        "cigs": {
            "at_entity": {
                "neutral": ["It's burned right down to the butt, the white filter crushed into a wrinkled fold."],
            },
        },
        "premium": {
            "at_entity": {
                "neutral": ["It's burned right down to the butt, the silver filter crushed into a wrinkled fold."],
            },
        },
},
"roach_01": {
        "default": {
            "at_scene": {
                "default": {
                    "neutral": ["Some cigarette butts rest near the edge."],
                },
            },
            "at_entity": {
                "morgue_office_01": {"neutral": ["Scorch marks form a symmetric circle around a solid, silver filter."]},
                "bertha_office_01": {"neutral": ["The paper is burned unevenly, down to the solid, white filter."],},
                "porch_01": ["The paper is burned unevenly, down to the solid, white filter."],
                "bar_01": ["The paper is burned unevenly, down to the solid, white filter."],
            },
        },
},
"blood_01": { #later, key to location
        "default": {
        },
        "knife": {
            "at_scene": {
                "crime_scene_01": {
                    "neutral": ["Streaks of blood mar the wall.",
                                "Blood patterns the walls in long, irregular arcs."],
                    },
                "crime_scene_02": {
                    "neutral": ["Long, tapering streaks of blood arc across the walls and floor.",
                                "Thick, curved lines of blood scatter against the walls and floor. "],
                },
            },
            "at_entity": {
                "crime_scene_01": {
                    "neutral": ["They form jagged rows, with large, disk-like dots beneath you.",
                                "They form a series of jagged sprays. Below, you see red, circular drops."
                                ],
                },
                "crime_scene_02": {
                    "neutral": ["Blood pools where the floor and walls meet, the edges smudged and crooked.",
                                "Below, you see a puddle of crimson, its edges irregular and smeared.",

                                "Below, you see a darker pool of blood, presumably where the body was."],
                }

            },
        },
        "gun": {
            "at_scene": {
                "crime_scene_01": {
                    "neutral": ["Blood covers the walls in a fine mist.",
                                "A thin spray of blood evenly coats the walls.",
                                "Small drops of red are spattered across the alley in a fine mist."],
                    },
                "crime_scene_02": {
                    "neutral": ["Diffuse specks of blood mar the walls..",
                                "Flecks of blood surround you."],
                    },
            },
            "at_entity": {
                "crime_scene_01": {
                    "neutral": ["Each drop is thin and small. The bricks are coated uniformly.",
                                ],
                    },
                "crime_scene_02": {
                    "neutral": ["Blood pools where the floor and walls meet, the edges smudged and crooked.",
                                "Below, you see a puddle of crimson, its edges irregular and smeared.",
                                "Below, you see a darker pool of blood, presumably where the body was."],
                    },
            },
        },
        "blunt": {
            "at_scene": {
                "crime_scene_01": {
                    "neutral": ["Blood covers the walls, splattered around unevenly.",
                                "Irregular arcs of blood streak the brick walls. "],
                    },
                "crime_scene_02": {#
                    "neutral": ["Long, tapering streaks of blood arc across the walls and floor.",
                                "Thick, curved lines of blood scatter the walls and floor. "],
                    },
                },
            "at_entity": {
                "crime_scene_01": {
                    "neutral": [
                        "Splotches of blood lie beneath thick, branching arcs.",
                        "The blood is cast across the walls in jagged strokes.",
                            ],
                },
                "crime_scene_02": {
                    "neutral": ["Blood pools where the floor and walls meet, the edges smudged and crooked.",
                                "Below, you see a puddle of crimson, its edges irregular and smeared.",

                                "Below, you see a darker pool of blood, presumably where the body was."],
                }
            },

            },
        },
"tooth_01": {
        "default": {
            "at_scene": {
                "neutral": ["The blood red forms a contrasting background to a white tooth."],
            },
            "at_entity": {
                "neutral": ["It's roots are jagged, it's crown chipped."],
            },
        },
},
"bruising_01": {
        "default": {
            "at_scene": {
                "neutral": ["Abrasions run across the front of her forearms and knees. LIVOR MORTIS?!?"],
            },
            "at_entity": {
                "neutral": ["They look like minor scrapes and bruises. SHOULD BE FROM GRAVITY 3HR/S"],
            },
        },
        "strong": {
            "at_scene": {
                "neutral": ["Mottled, purple bruising mark her ribs and limbs WHAT ABOUT HER CLOTHES?."],
            },
            "at_entity": {
                "neutral": ["The force of the impacts were clearly great. Alongside the bruising, her ribs are broken, and her forearm snapped in two. "
                            "FIST MARKS TO CONTRAST PIPE? also   boot prints?!!"],
            },
        },
},
"wounds_01": {
        "default": {
        },
        "knife": {
            "at_scene": {
                "neutral": ["Her flesh dangles at awkward angles - successive slices and stabs line her torso."
                            "\nYou can see right to the bone on some of them."],
            },
            "at_entity": {
                "neutral": [
                    "A deep cut, from the neck to the spine, separates her jugular by about 3 inches. \n...\nIt looks lethal."],
            },
        },
        "gun": {
            "at_scene": {
                "neutral": ["Bullets are embedded in her head, chest, and abdomen."],
            },
            "at_entity": {
                "neutral": ["Each wound forms a direct, straight line through her. "],
            },
        },
        "blunt": {
            "at_scene": {
                "neutral": ["Rows of indents form distinct, concave lines. The deepest runs from her ear, through her jaw, to her neck."],
            },
            "at_entity": {
                "neutral": ["Her jaw, neck, head, and nose are broken... Along with multiple ribs and some limbs."],
            },
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
                "neutral": ["It's blade is bloodied and dented. It's handle is cracked.","The blade has a few dents, but its nonetheless quite sharp."],
            },
            "leaving": {
                "neutral": ["You put it back.", "You place the knife back."],
            },
        },
    },
"murder_gun_01": {
        "default": {
            "at_scene": {
                "neutral": ["The glint from a bullet casing catches your eye."],
            },
            "approaching": {
                "neutral": ["You kneel down."],
            },
            "at_entity": {
                "neutral": ["It's the discarded shell that ejects when fired.\nIt looks like it belongs to a handgun."],
            },
            "leaving": {
                "neutral": ["You stand back up."],
            },
        },
},

"murder_pipe_01": {
        "default": {
            "at_scene": {
                "dumpster_01": {
                    "neutral": ["The edge of a pipe sticks out amidst the filth."],
                },
                "dead_end_01": {
                    "neutral": ["A metal pipe is in the far corner."],
                },
            },
            "approaching": {
                "neutral": ["You kneel down and grab the pipe.", "It's cold to the touch."],
            },
            "at_entity": {
                "neutral": ["Clumps of skin and blood lace a concave dent.",
                            "It's heavy, with red colored indents on it's head."]
            },
            "leaving": {
                "neutral": ["You place the pipe back."],
            },
        },
    },
"garbage_01": {
        "default": {
            "at_scene": {
                "neutral": ["A heap of old cardboard and garbage makes the alley awkward to traverse."],
            },
            "at_entity": {
                "neutral": ["It's miscellaneous, abandoned items - scrap materials, boxes, clothes...\n"
                            "There looks like a body shaped impression where someone has fallen..."],
            },
        },
},
"scent_01": {
        "default": {
            "at_scene": {
                "neutral": ["You notice an alcoholic scent, out of place amongst the rubbish. Something was spilled."],
            },
            "at_entity": {
                "neutral": ["ERROR - why is it default?."],
            },
        },
        "rum": {
            "at_entity": {
                "neutral": ["The scent is somewhere between molasses and sugarcane - with a hint of nutmeg."],
            },
        },
        "whiskey": {
            "at_entity": {
                "neutral": ["The scent is somewhere between vanilla and caramel - with a hint of oak."],
            },
        },
        "gin": {
            "at_entity": {
                "neutral": ["The scent is somewhere between pine and citrus - with floral undertones."],
            },
        },
},

"spilled_cigs_01": {
        "default": {
            "at_scene": {
                "alley_05": {"neutral": ["Loose cigarettes are sprawled in front of you."]} #could also put spill on them
                },
            "approaching": {
                "neutral": ["You take a closer look..."],
            },
        },
        "cigs": {
            "at_entity": {
                "alley_05": {"neutral": ["They look like generic, white cigarettes."]},
            },
        },
        "premium": {
            "at_entity": {
                "alley_05": {"neutral": ["Faint concentric rings run down the body, to a matte silver filter."]},
            },
        },
},

"spilled_tobacc_01": {
        "default": {
            "at_scene": {
                "alley_05": {"neutral": ["Loose, ground leaves of tobacco are sprawled out in front of you.", "Shreds of tobacco are sprawled out in front of you."]}
                },
            "approaching": {
                "neutral": ["You take a closer look..."],
            },
            "at_entity": {
                "alley_05": {"neutral": ["It's got a rich, sweet aroma.", "Each strip is a shade of brown, with a pliable texture."]},

            },
        },
},

"scrap_leather_01": {
        "default": {
            "at_scene": {
                "neutral": ["A piece of torn leather dangles, caught on a jagged metal rail."],
                },
            "at_entity":
                {"neutral": ["The leather has small tears and creases running through it, it's edges look uneven and frayed."]},

        },
        "mustard": {
            "at_entity": [
                {"neutral": ["The leather has small tears and creases running through it, it's edges look uneven and frayed."]},

                {"neutral": [
                    "You notice that aside from the blood stains, some yellow smears line the edge - mustard?"]},

            ]
        },
        "tomato": {
            "at_entity": [
                {"neutral": ["The leather has small tears and creases running through it, it's edges look uneven and frayed."]},

                {"neutral": [
                    "You notice that aside from the blood stains, some orange smears line the edge - tomato?"]},

            ]
        },
        "pie": {
            "at_entity": [
                {"neutral": ["The leather has small tears and creases running through it, it's edges look uneven and frayed."]},

                {"neutral": [
                    "You notice that aside from the blood stains, some blue smears line the edge - blueberry?"]},

            ]
        },
},

"scrap_denim_01": {
        "default": {
            "at_scene": {
                "neutral": ["A piece of torn denim dangles, caught on a jagged metal rail."],
                },
            "at_entity": {

                    "neutral": ["Blue and white threads form a tattered scrap, it's threads unraveling at the seams."]
}
        },
        "mustard": {
            "at_entity": [
                {
                    "neutral": ["Blue and white threads form a tattered scrap, it's threads unraveling at the seams."]
                },

                {"neutral": [
                    "You notice that aside from the blood stains, some yellow smears line the edge - mustard?"]},

            ]
        },
        "tomato": {
            "at_entity": [
                {
                    "neutral": ["Blue and white threads form a tattered scrap, it's threads unraveling at the seams."]
                },

                {"neutral": [
                    "You notice that aside from the blood stains, some orange smears line the edge - tomato?"]},

            ]
        },
        "pie": {
            "at_entity": [
                {
                    "neutral": ["Blue and white threads form a tattered scrap, it's threads unraveling at the seams."]
                },

                {"neutral": [
                    "You notice that aside from the blood stains, some blue smears line the edge - blueberry?"]},

            ]
        },
},
"scrap_suit_01": {
        "default": {
            "at_scene": {
                "neutral": ["A piece of torn fabric dangles, caught on a jagged metal rail."],
                },
            "at_entity":
                {
                "neutral": ["Finely weaved wool flutters in the wind - it looks like it's from formal wear."]
                },
        },
        "mustard": {
            "at_entity": [
                {
                "neutral": ["Finely weaved wool flutters in the wind - it looks like it's from formal wear."]
                },

                {"neutral": [
                    "You notice that aside from the blood stains, some yellow smears line the edge - mustard?"]},

            ]
        },
        "tomato": {
            "at_entity": [
                {
                "neutral": ["Finely weaved wool flutters in the wind - it looks like it's from formal wear."]
                },

                {"neutral": [
                    "You notice that aside from the blood stains, some orange smears line the edge - tomato?"]},

            ]
        },
        "pie": {
            "at_entity": [
                {
                "neutral": ["Finely weaved wool flutters in the wind - it looks like it's from formal wear."]
                },

                {"neutral": [
                    "You notice that aside from the blood stains, some blue smears line the edge - blueberry?"]},

            ]
        },
},


"footprint_01": {
        "default": {
            "at_scene": {
                "neutral": ["Printed in the mud is a distinct, singular footprint."],
            },
            "approaching":{"neutral": ["You kneel down..."]},
            "at_entity": {
                "neutral": ["It's a narrow imprint. A broad flat area tapers forward - behind it, a sharp dot forms a deep circular impression."],
            },
        },
        "sneakers": {
            "at_entity": {
                "neutral": ["It's a narrow imprint, with shallow, wavy grooves."],
            },
        },
        "work_boots": {
            "at_entity": {
                "neutral": ["It's a wide imprint, with deep, cross-hatched grooves."],
            },
        },
        "dress_shoes": {
            "at_entity": {
                "neutral": ["It's a narrow imprint with minimal, smooth grooves. It deepens at the heel."],
            },
        },
},

"hair_01": {
        "default": {
            "at_scene": {
                "neutral": ["A few locks of hairs are caught on the corner of the guard rails.",
                            "A few locks of hairs hang, snagged on the edge of the guard rails."]
                },
            "at_entity": {
                "neutral": ["They are black strands, medium in length..."]
            },
        },
},

#DRAWERS!!!!@@@@@@@@@@@@@
#morg
"morgue_shelf_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND gin IS MORE CONTRASTING
        "default": {#not opened - CAN OPEN TO SMELL IT? WOULD BE EPIC!
            "at_scene": {
                    "neutral": ["The corner of the room houses a shelf."],
            },
        },
    },
#bar
"bar_cabinet_01": {
        "default": {
            "at_scene": {
                "neutral": ["Where the counter meets the wall, a wide shelf hangs above."],
            },
        },
},

"fridge_01": {
        "default": {
            "at_scene": {
                "neutral": ["The refrigerator hums."]
                },
        }
},

"backroom_table_01": {
        "default": {
            "at_scene": {
                "neutral": ["Gambling tables take center stage.","The center of the room hosts the gambling tables."],
            },
            "at_entity": {
                "neutral": ["Old and worn felt cover the table."],
            },
        },
},
"backroom_counter_01": {
        "default": {
            "at_scene": {
                "neutral": ["To the side, there's a casual looking bar counter."],
            },
            "approaching": {
            },
            "at_entity": {
                "neutral": ["It's sturdy."],
            },
        },
},
"secret_01": {
        "default": {
            "at_scene": {
                "neutral": ["You see a small ledger."],
            },
            "approaching": {
            },
            "at_entity": {
                "neutral": ["It looks like something important is here."],
            },
        },
},



"ashtray_01": { #glass
        "default": {
            "at_scene": {
                "bertha_office_drawer_01": {
                            "neutral": ["A steel ashtray sits on the desk."],
                        },
                "neutral": ["Glass from an ashtray glints momentarily."]
                },
            "approaching": {
                "neutral": ["You take a closer look..."],
            },
            "at_entity": {
                "bertha_office_drawer_01": {
                    "neutral": ["Sticky, burned tobacco forms granular clumps.", "Bits of half burned tobacco form coarse, sticky lumps."]
                },
                "morgue_office_01": {
                    "neutral": ["It's filled with a mix of fine soot, and thick clumps of half burnt tobacco."],
                },
                "neutral": ["Cigarette butts are buried in their own thin ashes.", "A few roaches mingle in their own finely burned ashes."]

            },
        },
        "empty": {
            "at_entity": {
                "neutral": ["It's empty - it looks recently cleaned.","It's been emptied, with only tarry residue left."]
            },
        },
},
"porch_table_01": {
        "default": {
            "at_scene": {
                "neutral": ["A small, round table is surrounded with three seats.", "The corner of the deck has a small, round table."],
            },
        },
},
"office_morgue_desk_01": {
        "default": {
            "at_scene": {
                "neutral": ["The steel surface looks cold and clean.","Solid steel forms the surface of the workbench.","The desk looks sterile and clean."],
            },
            "approaching": {
                "neutral": [],
            },
            "at_entity": {
                "neutral": [""],
            },
            "leaving": {
                "neutral": [""],
            },
            "times": {
            },
            "weather": {
            }
        },
},
"bertha_office_drawer_01": { #actually desk lol
"default": {
        "approaching": ["You place your palms against the desk."],
        "at_scene": {
                "bertha_office_01": {
                    "sun": {"neutral": ["The middle of the room hosts a large desk",
                                "A desk sits in the middle of the room."],},
                    "rain": {"neutral": ["The middle of the room hosts a large desk",
                                "A desk sits in the middle of the room."],},
                    "storm": {"neutral": ["The middle of the room hosts a large desk",
                                "A desk sits in the middle of the room."],},

                },
        },
        "at_entity": { #sturdy oak scratched
            "neutral": ["Scratches run across the wood grains.", "The surface is coarse and rough.",
                        "It's quite sturdy.",
                        "The surface is coarse oak."],
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
                "neutral": ["Garbage and maggots lie in a heap."],
            },
            "leaving": {
                "neutral": ["You turn around."],
            },
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
            "at_entity": [{
                "neutral": ["It's sharp.", "It's been used.", "The blade shines in the light."],
            },{
                "neutral": ["No one notices you holding it."],
            },],
            "leaving": {
                "neutral": ["You put the knife back.", "You place the knife back where it was."],
            },
        },
    },


"knife_01": {
        "default": {
            "at_scene": {
                    "neutral": ["You notice the hilt of a pocket knife sticking out the side."],
            },
            "approaching": {
                "neutral": ["Your hand grips the handle.", "Your fingers curl around the hilt."],
            },
            "at_entity": [{
                "neutral": ["The blade shines in the light."],
            },],
            "leaving": {
                "neutral": ["You put the knife back.", "You place the knife back where it was."],
            },
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
        },
        "loaded": { #loaded with 3 shots
            "at_entity": {
                "neutral": ["It's loaded, with three shots fired.", "Three bullets are loaded.",
                            "Three bullets are missing from an otherwise full chamber."],
            },
        },
    },

    "revolver_02": {  # 3 shots fired IN THE MRUDER!
        "default": {  # unloaded
            "at_scene": {
                "neutral": ["There's a pistol here."]
            },
            "approaching": {
                    "neutral": ["Your fingers curl around the handle.", "The barrel gleams under the light.",
                                "You pick up the gun."],
            },
            "at_entity": [{
                "neutral": ["It has some noticeable weight. The barrel is smooth and polished."],
            },
            ],
            "leaving": {
                "neutral": ["You place the gun back.", "You put it back.", "You set it down with a clunk."],
            },
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
                "neutral": ["It glistens in the light.","It's got some weight to it.",], #should have casing matching desc
            },
            "leaving": {
                "neutral": ["You place the bullet back.", "The bullet rattles as you drop it."],
            },
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
        },
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
        },
        "used": {
            "at_entity": [{
                "neutral": ["You thumb the pub's engraved logo.","It has an engraving of the pub logo."],
            },
                {
                "neutral": ["It's in pristine condition, despite missing a few matches.","Although missing some matches, the cover is practically unblemished."],
            },
            ],
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
                "leather_jacket_02": {
                    "neutral": ["The left pocket has a matchbook."],
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
        },
    },

"apple_01": {
        "default": {
            "at_scene": {
                "default": {"neutral": ["Amongst various items, an apple stands out."],},
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
        },
    },




"coat_hanger_01": {
        "default": {
            "at_scene": {
                "neutral": ["A coat hanger perches in the corner."]
                },
            "approaching": {
                "neutral": [""],
            },
            "at_entity": {
                "neutral": ["It's a coat hanger."]
            },
            "leaving": {
                "neutral": [""],
            },
            "times": {
            },
            "weather": {
            }
        },
},





"flask_01": {
        "default": {
            "at_scene": {"neutral": ["A steel flask lays on it's side."]},
        },
        "1": {
            "at_entity": {
                "bertha_office_01": {
                    "neutral": ["The cap is loose - a spicy, citrus scent comes from the lid."],
                    },
                "morgue_office_01": {
                    "neutral": ["The cap is loose - a spicy, citrus scent comes from the lid."],
                    },
            },
        },
        "2": {
            "at_entity": {
                "bertha_office_01": {
                    "neutral": ["The cap is loose - a sweet, molasses scent comes from the lid."],
                    },
                "morgue_office_01": {
                    "neutral": ["The cap is loose - a smoked, vanilla scent with oak undertones comes from the lid."],
                    },
            },
        },
    },

"gin_01": {
        "default": {
            "at_scene": {
                "neutral":["Near the railing, a dull green bottle of gin perches within arms length."],
            },
            "approaching": {
                "neutral":["You grab the neck"],
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
            "at_entity": {
                "neutral": ["The odor is sharp, spicy, and floral. It reminds you of pine."],
            },
            "leaving": {
            },
            "times": {
            },
            "weather": {
            }
        }
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
                            "The bottle is sticky, with a cloy, honey scent."],
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

"whiskey_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND gin IS MORE CONTRASTING
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
            "approaching": {
            },
            "at_entity": { #OAK, SPICED, VANILLA, SMOKED OAK #maybe gin is more contrasting?
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
"red_wine_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND gin IS MORE CONTRASTING
        "default": {#not opened - CAN OPEN TO SMELL IT? WOULD BE EPIC!
            "at_scene": {
                    "neutral": ["A bottle of red wine stands nearby."],
            },
            "approaching": {
                "neutral": ["You grab it's neck."],
            },
            "at_entity": {
                "neutral": ["It's not opened.","The cork is firmly in place."],
            },
            "leaving": {
                "neutral": ["You leave the wine bottle behind."],
            },
        },
        "opened": {
            "at_entity": {
                "neutral": ["It smells of red wine."],
            },
            "leaving": {
                "neutral": ["You leave the bottle behind, it's aroma lingering."],
            },
        }
    },



"white_wine_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND gin IS MORE CONTRASTING
        "default": {#not opened - CAN OPEN TO SMELL IT? WOULD BE EPIC!
            "at_scene": {
                    "neutral": ["A bottle of white wine stands nearby."],
            },
            "approaching": {
                "neutral": ["You grab it's neck."],
            },
            "at_entity": {
                "neutral": ["It's not opened.","The cap is screwed down tight."],
            },
            "leaving": {
                "neutral": ["You leave the wine bottle behind."],
            },
        },
        "opened": {
            "at_entity": {
                "neutral": ["It smells of white wine."],
            },
            "leaving": {
                "neutral": ["You leave the bottle behind, it's aroma lingering."],
            },
        }
    },


"tomato_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND gin IS MORE CONTRASTING
        "default": {#not opened - CAN OPEN TO SMELL IT? WOULD BE EPIC!
            "at_scene": {
                    "neutral": ["Near you, theres a bowl of tomato soup."],
            },
            "at_entity": {
                "neutral": ["A thin sheen of oil covers the half eaten soup - the color somewhere between orange and red, with a green basil leaf sitting on top."],
            },
        },
    },



"mustard_01": { #OAK, SPICED, VANILLA, SMOKED OAK ; pale gold #MAYBE RUM AND gin IS MORE CONTRASTING
        "default": {#not opened - CAN OPEN TO SMELL IT? WOULD BE EPIC!
            "at_scene": {
                    "neutral": ["Beside that, a half eaten deli sandwich."],
            },
            "at_entity": {
                "neutral": ["The rye split around halfway, spilling out it's contents - mustard, ham, and lettuce."],
            },
        },
    },


"pie_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Thick blueberry pie forms a gelatinous mess on it's plate."],
            },
            "at_entity": {
                "neutral": ["The crust flakes along the cut of the thick slice, blue filling oozing out it's sides."],
            },
        },
    },


"lighter_01": {
        "default": {
            "at_scene": {
                    "neutral": ["A gold lighter shines, sticking out from it's surroundings."],
            },
            "at_entity": {
                "neutral": ["It's gold plated, with a dull, brushed finish."],
            },
        },
    },

"cardigan_scraps_01": { #can now maybe also be something else that is thin laced wool!@!@!@
        "default": {
            "at_scene": {
                    "neutral": ["White fibers are strewn about."],
            },
            "at_entity": {
                "neutral": ["They are from some laced, wool article - it look like they were forcefully torn off."],
            },
        },
    },

"glass_01": {
        "default": {
            "at_scene": {
                    "neutral": ["A wine glass is here."],
            },
            "at_entity": {
                "stage_02": {
                    "neutral": ["LIPSTICK AT THE BRIM."],
                },
                "neutral": ["It's empty.."],
            },
        },
        "white": {

            "at_entity": {
                "stage_02": {
                    "neutral": ["LIPSTICK AT THE BRIM."],
                },
                "neutral": ["It's filled with white wine."],
            },
        },
        "red": {
            "at_entity": {
                "stage_02": {
                                "neutral": ["LIPSTICK AT THE BRIM."],
                            },
                "neutral": ["It's filled with red wine."],
            },
        },
    },
"ticket_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Amidst the clutter, you notice a bus ticket."],
            },
            "at_entity": {
                "neutral": ["It's stamped - the departure date is the morning of the night of the murder."],
            },
        },
    },
"lipstick_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Half opened lipstick is on the floor."],
            },
            "at_entity": {
                "neutral": ["A brass tube holds pink, glossy lipstick."],
            },
        },
    },
"purse_01": {
        "default": {
            "at_scene": {
                    "neutral": ["A light brown purse is here."],
            },
            "at_entity": {
                "neutral": ["It's a purse."],
            },
        },
    },
"bench_01": {
        "default": {
            "at_scene": {
                    "neutral": ["BENCH here."],
            },
            "at_entity": {
                "neutral": ["It's a BENCH ticket."],
            },
        },
    },
"cigs_01": {
        "default": {
            "at_scene": {
                "lounge_01": {
                    "neutral": ["Peeking out the right pocket are some cigarettes."],},
                "neutral": ["Perched around the ashtray are some cigarettes."]
            },
            "at_entity": {
                "neutral": ["The body is made of thin paper surrounding tobacco, the base a white filter. It's a cigarette."],
            },
        },
        "pack": {
            "at_scene": {
                    "neutral": ["Closeby, there's a pack of cigarettes - it looks like a generic brand."],
            },
            "at_entity": {
                "neutral": ["It looks like a common, cheap brand. Each white cigarette butt peeks out the opening."],
            },
        },
    },
"cigs_02": {
        "default": {
            "at_scene": {
                "leather_jacket_02": ["You find some cigarettes in the breast pocket."],
                    "neutral": ["Perched around the ashtray are some cigarettes."],
            },
            "at_entity": {
                "neutral": ["The body is made of thin paper surrounding tobacco, the base a solid silver filter. It's a cigarette."],
            },
        },
        "pack": {
            "at_scene": {
                "leather_jacket_02": ["You find some cigarettes in the breast pocket."],
                    "neutral": ["Closeby, there's a pack of cigarettes - it looks like a nice brand."],
            },
            "at_entity": {
                "neutral": ["The package makes it clear that it's a premium brand. The silver butts of each cigarette peek out the opening."],
            },
        },
    },
"smoke_pipe_01": {
        "default": {
            "at_scene": {
                    "neutral": ["On it's side, a curved, wooden pipe points it's mouthpiece at you."],
            },
            "at_entity": {
                "neutral": ["The grains run along the sides, the bowl quite large, filled with clumping bits of sticky, half burned tobacco."],
            },
        },
    },

"tobacco_01": {
        "default": {
            "at_scene": {
                    "neutral": ["A pouch of tobacco is loosely closed by a sticker."],
            },
            "at_entity": {
                "neutral": ["The pouch is vintage leather. Inside, thin, fresh strips of tobacco create a rich, sweet aroma."],
            },
        },
    },

"fibers_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Her fingernails are jagged and scraped, with something under it."],
            },
            "at_entity": {
                "neutral": ["It looks like general dirt and debris."],
            },
        },
        "hair": {
            "at_entity": {
                "neutral": ["It looks like someone's hair - it's black."],
            },
        },
        "denim": {
            "at_entity": {
                "neutral": ["Theres some dirt - and some blue and white fibers."],
            },
        },
        "leather": {
            "at_entity": {
                "neutral": ["Theres some dirt - and some leather fibers."],
            },
        },
        "suit": {
            "at_entity": {
                "neutral": ["Theres some dirt - and some finely woven fibers."],
            },
        },
    },
"shoe_rack_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Footwear is loosely lined on a nearby shoe rack. "],
            },
            "at_entity": {
                "neutral": ["On top of the rack, you see:"],
            },
        },
    },
"hanger_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Miscellaneous clothing articles are piled atop a hanger."],
            },
            "at_entity": {
                "neutral": ["The items include:"],
            },
        },
    },
"earring_01": {
        "default": {
            "at_scene": {
                "refrigeration_02": {"neutral": ["Her ears are pierced with matching ear rings. "]},
                "neutral": ["Something catches the light on the ground - an ear ring. "],
            },
            "at_entity": {
                "neutral": ["It's a small, copper hoop with a tiny jewel."],
            },
        },
        "single": {
            "at_scene": {
                "refrigeration_02": {"neutral": ["One earlobe is pierced with a hoop - the other torn, without one.. "]},
                "neutral": ["Something catches the light on the ground - an ear ring. "],
            },
            "at_entity": {
                "neutral": ["It's a small, copper hoop with a tiny jewel."],
            },
        },
    },
"denim_jacket_01": {
        "default": {
            "at_scene": {
                    "neutral": ["A faded denim jacket, hung by the neck."],
            },
            "at_entity": {
                "neutral": ["Blue and white fibers fray at the seams.", "Ragged ends of blue and white threads line the sleeves.",
                            "Patches of blue and white fibers unravel along the seams"],
            },
        },
    },
"leather_jacket_01": {
        "default": {
            "at_scene": {
                    "neutral": ["A bomber jacket, rugged and cracked around the shoulders."],
            },
            "at_entity": {
                "neutral": ["It's black leather, with some cracks running through it."],
            },
        },
    },
"leather_jacket_02": {
        "default": {
            "at_scene": {
                    "neutral": ["Hanging from the wall, a rugged leather coat droops down in folds."],
            },
            "at_entity": {
                "neutral": ["Aside from some cracks and tears, the black leather looks well maintained."],
            },
        },
    },
"suit_jacket_02": {
        "default": {
            "at_scene": {
                    "neutral": ["A deep navy blue formal blazer.", "A neatly folded formal jacket, draped on it's side."],
            },
            "at_entity": {
                "neutral": ["Despite some tears across the lining, it's finely woven wool fibers look well maintained.", "It's fibers are finely woven wool, the color is a deep navy."],
            },
        },
    },
"high_heels_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Blood coats her high heels a glossy, crimson finish. "],
            },
            "at_entity": {
                "neutral": ["They connect loosely at the ankle, the brace almost off. A sharp heel juts out, the rest of the sole smooth tapering towards the toes. "],
            },
        },
    },
"sneakers_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Narrow sneakers, it's laces dangling off the sides."],
            },
            "at_entity": {
                "neutral": ["Bits of mud are lodged into the wavy, grooved pattern on the soles."],
            },
        },
    },
"dress_shoes_01": {
        "default": {
            "at_scene": {
                    "neutral": ["Dress shoes, with a dull, glossy sheen.","Dress shoes, the laces neatly tucked into the heel."],
            },
            "at_entity": {
                "neutral": ["The polish contrasts with the dirt lining the shallow heel, the sole narrow and flat."],
            },
        },
    },
"workboots_01": {
        "default": {
            "at_scene": {
                "reception_02": {"neutral": ["Next to the door, a pair of work boots are neatly set on a mat."],},
                "shoe_rack_01": {"neutral": ["Rugged, broad work boots, with a steel toe."],},

            },
            "at_entity": {
                "neutral": ["Caked mud fills the deep, cross hatched grooves that pattern the wide sole."],
            },
        },
    },

"cardigan_01": {
        "default": {
            "at_scene": {
                    "neutral": [
                        "A simple, green dress covers her collarbones to her knees. \n"
                        "Resting overtop, she wears a white cardigan, open at the front."
                                ],
            },
            "at_entity": {
                "neutral": ["The cardigans laced wool creates a textured, warm fabric.\n"
                            "The dress contours her form, wrinkling at the waist."],
            },
        },
        "torn": {
            "at_entity": {
                "neutral": ["From the shoulder to her elbow, large rips stretch and distort the cardigan's laced pattern.\n"
                            "Her dress is warped and fits unevenly - jagged tears run along the seams, exposing her ribs."],
            },
        },
    },



"debbie_01": {
        "default": {
            "at_scene": {
                "open": {"neutral": ["A corpse lays flat in the center of the room."],},
                "closed": {"neutral": ["A white cloth forms subtle, alternating curves.",
                                       "A cloth traces a still form with concave and convex slopes.",
                                       "A white cloth covers a body.",
                                       "The cloth drapes, its edges gently brushing the floor."],},
            },
            "approaching": {
                "neutral": [""],
            },
            "at_entity": {
                "neutral": [""],
            },
            "leaving": {
                "neutral": [""],
            },
            "times": {
            },
            "weather": {
            }
        },
},


"head_01": {
    "default": {
        "at_scene": {"neutral": ["Long, brown hair forms a tangled mess. \n"
                        "Open, grey eyes stare into the void, her skin abnormally pale."], },

        "at_entity": {
            "neutral": ["Brown hair is splayed around her hollow, gaunt face.\n"
                        "Her skin has taken on a waxy pallor; her features and neck locked and tense.\n"
                        "Glassy, fixed eyes have dried out, sinking into their sockets. \n"
                        "Her lips are parted, thin, and chapped.\n"],
        },
    },
},
"torso_01": {
    "default": {
        "at_scene": {"neutral": ["A simple, green dress covers her collarbones to her knees.\n"
                        "Resting overtop, she wears a white cardigan, open at the front."], },
        "at_entity": {
            "neutral": ["Her shoulders down through her back are colored a mottled purple.\n"
                        "Her muscles are rigid and stiff."],
        },
    },
},
"limbs_01": {
    "default": {
        "at_scene": {"neutral": ["Her limbs are locked at awkward angles."], },
        "at_entity": {
            "neutral": ["Her arms and legs are tense and inflexible - her fingers and toes curl, each nail pale and blue."],
        },
    },
},


"morgue_tools_01": {
    "default": {
        "at_scene": {"neutral": ["Various tools and equipment are in an open box against the wall."], },
        "at_entity": {
            "neutral": ["It's an assortment of scalpels, knives, bone saws, forceps, and shears..."],
        },
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
        },
        "cleaned": { #from murder, cooking/bar, mob 'accident', or whateva
            "at_entity": [
                {"neutral": ["They have slight style variations, but are otherwise identical...",
                            "They are all thick blue denim jackets. Some have more wear and tear than others..."]},
                {"neutral": ["One of the jackets is has been forcibly cleaned, it's fibers brittle and color stripped.",
                             "One of the jackets is tattered, with white smears. It's been vigorously cleaned.",
                             "One of the jackets is faded and torn. Blanched patches form stripes.",
                             "One of the jackets is frayed, with some discoloration.\nIt's been bleached."]},
            ],
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
        },
        "cleaned_shoes": { #from murder, cooking/bar, mob 'accident', or whateva
            "at_scene": {
                "bertha_office_closet_01": {
                },
            },
            "at_entity": [
                {"neutral": ["The footwear is a mix of average sized shoes and boots...",
                            "Shoes and boots of varying designs are loosely arranged in a row...",]},
                {"neutral": ["One pair of shoes is noticeably cleaner than the others.",
                             "One pair of shoes has been recently scrubbed, it's seams unraveling."]},
            ],
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


}