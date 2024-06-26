#for weather or connections, you have
# optional weather or time keys.
# always key weather, time. or just time. but never time, weather!!!
#why not optional time or weather keys for all of them?
loc_description_data = {
    #FOR APPROACH/LEAVING, TRY CONNECTIONS?

"cab_01": {
    "default": {
        "driving_start": {
            "neutral": [f'"You got it boss."', "The engine sputters, and the cab drives off.", "The cab drives..."]},
        "driving_during": {
            "porch_01": {
                "neutral": ["You sit in the cab, watching the city pass by through the window."],
                "good": ["You relax in the cab", "The gentle hum of the engine feels soothing."],
                "bad": ["You brace yourself as the cab hits another pothole, the ride anything but smooth."]
                },
            "alley_01": {
                "neutral": ["You sit in the cab, watching the city pass by through the window."],
                "good": ["You relax in the cab", "The gentle hum of the engine feels soothing."],
                "bad": ["You brace yourself as the cab hits another pothole, the ride anything but smooth."]
                },
        },
        "driving_arriving": {
            "porch_01": ["The porch comes into view.."],
            "alley_01": ["The alley comes into view..."]
        },
        "approaching": { #approaching current loc, FROM last loc. so can optinally add last locs here, then optional weather, time, etc
            "neutral": ["The cab is lazily parked, taking up 3 spots...",  "The cab idles.."],
            "good": ["The cabbie waves as you approach.", "The cab idles, the engine a low, constant hum."],
            "bad": ["The cabbie glances your direction.", "The cab is surrounded by cigarettes", "The cab idles.."]
        },
        "at_entity": {#inside cab
            "neutral": ['The driver adjusts his mirror. "Where to?"', "The cabbie nods his head as you climb in.", ],
            "good": ["You are greeted by a friendly nod from the driver.", "The cabbie greets you over the engine purr."],
            "bad": ['The cabbie smells faintly of stale smoke and sweat.', 'The driver adjusts his mirror. "Where to?"' ,'The driver looks indifferent to your presence.']
        },
        "times": {
            "morning": {"neutral": ["He yawns.", "He stretches in his seat.", "He leans off to the side."],
                        "bad": ["He looks like he hasn't slept.", "His hands reach for another cigarette.", "He rubs his eyes, tired.", "He looks tired."]},
            "afternoon": {"neutral": ["He rubs his eyes.", "He stretches in his seat.", "He leans off to the side.", "He shifts in his seat."],
                        "bad": ["He looks like he hasn't slept.", "His hands reach for another cigarette.", "He rubs his eyes, tired.", "He looks tired."]},
            "evening": {"neutral": ["He scratches his head.", "His eyes wander.", "He leans off to the side.", "He shifts in his seat."],
                        "bad": ["He looks like he might fall asleep.", "His hands reach for another cigarette.", "His eyes dart, scanning the horizon.",]},
            "night":{"neutral": ["The headlights beam onto the street.", "He stares at the night sky.", "He shifts in his seat, restless."],
                        "bad": ["The headlights flicker.", "He looks like he might fall asleep.", "His hands tremble as he reaches for a cigarette.", "His eyes scan the horizon.",]},
        },
        "weather": { #optionally keyed to time of day - should make sense from INSIDE CAB!
            "rain": ["Raindrops pelt the cab, streaking its windows.", "The rain makes a rhythmic drumming sound.", "The headlights cast a pyramid in the rain."],
            "sun": ["The sun reflects off the cab’s metal, making you squint.", "The sunlight makes the cab shimmer."],
            "grey": ["The grey sky paints the cab dull."]
        },
        "tags": ["cab"],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "porch_01": { #seeing the cab from the porch
                "sun": ["The cab is parked nearby."],
                "rain": ["The cab is parked nearby.", "You can see the cab through the downpour."],
                "grey": ["The cab is parked nearby."],
            },
            "alley_01": ["The cab is parked nearby.", "You can see the cabbie waiting across the street."]
            },
        "leaving": { #leaving from this loc TO player current loc, so key by current loc, then weather or time,,,
            "neutral": ["You exit the cab, closing the door behind you.", "Your feet hit the ground, and you climb out the car.",
                        "The pavement scrapes against your shoes.","You clamber out the cab.", "Your back aches."],
        },

    },
},
"porch_01": {
    "default": {
        "approaching": {
            "cab_01": {"neutral": ["You approach the pub."]}
        },
        "at_entity": {
            "neutral": ["You stand on the porch, its surface weathered and worn.", "Wooden planks creak underfoot.", "The porch is weathered and worn."],
            "bad": ["The wood groans under your weight."],
            "good": ["The porch is a cozy spot."],
        },
        "leaving": {
        },
        "times": {
            #if keying time to weather, really dont need this!
        },
        "weather": {

        },

        "tags": [],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "lounge_01": {  # seeing the porch from the lounge
                "sun": {
                    "morning": ["Ahead, the porch basks in the morning sun."],
                    "afternoon": [
                        "Ahead, the porch basks in the sun."],
                    "evening": [
                        "Ahead, the porch basks in the evening sun."],
                    "night": [
                        "Ahead, the porch is lit only by the soft, flickering lights."]
                },
                "rain": [
                        "Ahead, the porch is slick from the rain.", ],
                "grey": ["Ahead, you can see the porch."],
            },
        }
    }
},
"lounge_01": {
    "default": {
        "approaching": [
            {
            "porch_01": {
                "neutral": ["You push through the pub doors.","You enter the pub."],
                },
            },
            {
                "neutral": ["The air reeks of smoke.", "You're hit with a wave a smoke."],
                "bad": ["People glance at you briefly."]
                },
        ],
        "at_entity": {
            "neutral": ["The lounge is a bit run down.", "The lounge has a rustic feel.", "", ""],
        },
        "leaving": {
            "porch_01": {"neutral": ["You leave the pub.", "The doors swing as you leave the lounge."]}
        },
        "times": { #lounge is quiet, picks up in the evening/night
            "morning": ["It's a quiet morning.", "A few staff members are cleaning up from last night."],
            "afternoon": ["People laze around."],
            "evening": ["It's busy.", "Drunk chatter forms a noisy backdrop."],
            "night": ["It's starting to get rowdy.", "It's packed in here.", "People bump into you as they amble about."]
        },
        "weather": { #replaces weather decorator
            "rain": ["Raindrops slam against the windows."],
            "sun": ["Sun filters through the blinds.", "The sun casts it all in dramatic lighting."],
            "grey": ["It's dim in here."]
        },
        "tags": ["indoors"],
        "connections": {
            "porch_01": { #seeing the lounge from the porch
                "morning": ["The entrance to the lounge is directly ahead."],
                "afternoon": ["The entrance to the lounge is directly ahead."],
                "evening": ["You can hear commotion from the lounge.", "Ahead, the lounge seems busy."],
                "night": ["You can hear commotion from the lounge.", "Ahead, the lounge seems busy."],
            },
            "bar_01": ["The lounge is back the way you came."],
            "kitchen_01": ["The lounge is back the way you came."],
            "stage_01": { #seeing the lounge from the stage
                "morning": ["The stage faces the lounge."],
                "afternoon": ["The stage faces the lounge."],
                "evening": ["From the lounge, people stare with a puzzle expression."],
                "night": ["People seem to expect you to perform."]
            },
            "hallway_01": { #seeing the lounge from the hallway
                "morning": ["Ahead, you can see the lounge."],
                "afternoon": ["Ahead, you can see the lounge."],
                "evening": ["Ahead, you can see the lounge.", "People squeeze by you to get to the lounge."],
                "night": ["Ahead, you can see the lounge.", "People squeeze by you to get to the lounge."],
            }
        },
    },
},
"bar_01": {
    "default": {
        "approaching": {
            "morning":  ["You push past the swinging doors, and enter the bar."],
            "afternoon":  ["You push past the swinging doors, and enter the bar."],
            "evening":  ["You push past the swinging doors, and enter the bar.", "You find a seat at the quieter end of the counter.", "You maneuver around a few drunks to get a seat.",],
            "night":  ["You push past the swinging doors, and enter the bar.", "The patrons seem briefly annoyed at your presence, before returning to their activities.",
                       "You find a seat at the quieter end of the counter.", "You maneuver around a few drunks to get a seat."],

        },
        "at_entity": {
            "neutral": [  #might have to be in approaching
                        "The counter is rough and weathered.",
                        "You notice the coarseness of the counter top.", "You take a seat. The stool rocks unevenly.", ],
        },
        "leaving": {
            "neutral": ["You step away from the bar." ,"You turn back the way you came.", "You push past the swinging doors as you leave."],
        },
        "times": { #must be of
            "morning": ["Only a few stragglers from the night are here."],
            "afternoon": ["The steady hum of conversation drones on."],
            "evening": ["The bar is lively.","A mix of chatter and laughter form the backdrop."],
            "night": ["The bar is at its peak, the noise and energy almost palpable."]
        },
        "weather": {

        },
        "tags": ["indoors"],
        "connections": {
            "lounge_01": { #seeing the bar from the lounge
                "morning": ["You can see the bar from here.", "You can see the last few late night drinkers at the bar."],
                "afternoon": ["You can see the bar from here."],
                "evening": ["You can see the bar from here.", "The bar seems busy."],
                "night": ["You can see the bar from here.", "The bar seems busy."],
            },
        }
    }
},
"kitchen_01": {
    "default": {
        "approaching": {
            "neutral": ["The kitchen doors swing open.", "The smell of grease hits your nostrils."],
        },
        "at_entity": {
            "good": ["The kitchen is well maintained."],
            "bad": ["The kitchen is in disarray.", "The kitchen is a mess."]
        },
        "leaving": {
            "neutral": ["You leave the kitchen", "You push through the kitchen doors and leave.", "You leave the way you came."],
        },
        "times": {
            "morning": ["Cooks are prepping for the day.", "Cooks are busy prepping."],
            "afternoon": ["Bustling cooks and clattering pots surround you."],
            "evening": ["Dinner service is in full swing.", "You are surrounded by bustling cooks and clattering pots."],
            "night": ["It's winding down", "Only a few late-night orders are being prepared."]
        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "lounge_01": { #seeing the kitchen from the lounge
        "morning": ["The kitchen doors are in the corner."],
        "afternoon": ["The kitchen doors are in the corner."],
        "evening": ["Cooks come in and out the kitchen doors.", "The kitchen doors are in the corner."],
        "night": ["The kitchen doors are in the corner."],
            }
        }
    }
},
"stage_01": {
    "default": { #EMPTY STAGE!
        "approaching": {
            "lounge_01": ["You climb up onto the stage."],
            "stage_02": ["You walk up to the stage."]
        },
        "at_entity": {
            "neutral": ["You stand on the stage."],
        },
        "leaving": {
            "lounge_01": ["You step off the stage."],
            "stage_02": ["You walk towards the back."]
        },
        "times": {

        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "lounge_01": { #seeing the stage from the lounge
                "morning": ["The stage is empty."],
                "afternoon": ["The stage is empty."],
                "evening": ["The stage is empty."],
                "night": ["The stage is empty."],
            },
            "stage_02": { #seeing the stage from the backstage
                "morning": ["The stage is empty."],
                "afternoon": ["The stage is empty."],
                "evening": ["The stage is empty."],
                "night": ["The stage is empty."],
            },
        }
    }
},
"stage_02": {
    "default": {#no stage activity
        "approaching": {
            "stage_01": [""],
            "hallway_01": ["You hunch as the ceiling lowers."],
        },
        "at_entity": {
            "neutral": ["You are backstage.","Miscellaneous props and equipment surrounds you."],
            "bad": ["The backstage feels cramped and cluttered.", "It feels cramped.", "It's messy."]
        },
        "leaving": {
        },
        "times": {

        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "stage_01": { #seeing backstage from stage
                "neutral": ["You can see the backstage from here.",],
            },
            "hallway_01": {
                "neutral": ["The hallway connects to the backstage.", ],
            }
        }
    }
},
"hallway_01": {
    "default": {

        "at_entity": {
            "neutral": ["You are in the hallway."],
        },
        "leaving": {
        },
        "times": {

        },

        "connections": {
            "lounge_01": { #seeing the hallway from the lounge
                "neutral" : ["Theres a hallway closeby.", "The hallway entrance can be seen from here.", "The entrance to the hallway is in the far corner of the room."],
            },
            "stage_02": {  #seeing the hallway from the backstage
                "neutral": ["The backstage connects directly to the hallway."],
            }
        }
    }
},
"hallway_02": {
    "default": {
        "approaching": {

        },
        "at_entity": {

        },
        "leaving": {
        },
        "times": {
            "morning": ["The hallway stretches on.", "The hallway stretches on, silent and empty." ],
            "afternoon": ["The hallway stretches on.","The hallway stretches on, with occasional footsteps echoing."],
            "evening": ["The hallway stretches on.","The hallway stretches on, with people moving to and fro.", "The hallway stretches on, dimly lit."],
            "night": ["The hallway stretches on.","The hallway stretches on, late nighters stumbling about."]
        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "hallway_01": {
                "neutral": ["You can make out doors at the end of the hall.", "Doors face you at the end of the hall."],
                "bad": []
            },
            "hallway_03": {
                "neutral": ["The pub's lounge is at the end of the hall."]
            }
        }
    }
},
"hallway_03": {
    "default": {
        "approaching": {
        },
        "at_entity": {

        },
        "leaving": {

        },
        "times": {

        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "hallway_02": {
                "neutral": ["Doors face you at the end of the hall.", "You can see doors at the end of the hall."],
            },
            "hallway_04": {
                "neutral": ["Ahead is the path to the pub.", "The hallway stretches on, all the way to the pub."],
            }
        }
    }
},
"hallway_04": { #dim, leave the claustrophobia cramped stuff for alley and maybe butcher..
    "default": {
        "approaching": {
            "hallway_03": {"neutral": ["You come to the end of the hallway."],},
            "bertha_office_door_01": {"neutral": ["You enter the hallway."],},
            "backroom_door_01": {"neutral": ["You enter the hallway."],}
        },
        "at_entity": {
            "neutral": ["Wood groans underfoot.", "", ""],
        },
        "leaving": {

        },
        "times": {

        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "hallway_03": { #see 04 from 03
                "neutral": ["You near the end of the hallway.", "You are coming close to the end of the hallway."],
            },
            "bertha_office_door_01": {

                #door connections are keyed by open/closed, then optionally weather, times, etc like before.
                #but, this is for seeing hallway_04 from the door, so this is not a door connection desc.

                "neutral": ["The door leads to the hallway."],
            },
            "backroom_door_01": {
                "neutral": ["The door leads to the hallway."],
            }
        }
    }
},
"bertha_office_01": {
    "default": {
        "approaching": {
            "neutral": ["You enter through the door."],
        },
        "at_entity": { #should just have a bunch of at scene description stuff here. relevant clues! desk, boxes, flask, etc
            "neutral": ["You are in the office."]
        },
        "leaving": {
            "neutral": ["You turn back the way you came..."]
        },
        "times": {

        },
        "weather": {

    },
        "tags": ["indoors"],
        "connections": {
            "bertha_office_door_01": {
                "neutral": ["Through the gap, you can see Bertha's office."]
            }
        }
    }
},
"backroom_01": {
    "default": {
        "approaching": {
            "neutral": ["You walk through the door and enter the backroom."],
        },
        "at_entity": {
            "neutral": ["You are at the backroom "],
        },
        "leaving": {
            "neutral": ["You leave the way you came..."],
        },
        "times": {
            "morning": ["Only the most hardcore late night gamblers are still up.", "Most of the tables are empty.", "It's quiet, with the occasional groans from lost bets."],
            "afternoon": ["Most of the tables are empty.", "The clinking of chips punctuates the silence.", "It's quiet, with the occasional groans from lost bets." ],
            "evening": ["Cards ruffle and shuffle.", "A mix of chatter and laughter create a backdrop of the night."],
            "night": ["It's a rambunctious kind of night.","Cards ruffle and shuffle.", "A mix of chatter and laughter create a backdrop of the night."]
        },
        "weather": {
        },
        "tags": ["indoors"],
        "connections": {
            "backroom_door_01": {
                "neutral": ["Through the gap, you can see the backroom."]
                }
            }
        }
    },
"backroom_door_01": {
    "default": {
        "approaching": {
        },

        "leaving": {
        },
        "times": {

        },
        "weather": {

        },
        "bump": {"neutral" : ["A loud ring echoes as your head slams into the door."]},
        "at_entity": [

        ],
        "connections": {
            "hallway_04": {
                "open": ["The iron door is ajar."],
                "closed": ["An iron door faces you."],
            },
            "backroom_01": {
                "open": ["YOU CAN SEE THE IRON DOOR FORM HERE?1"],
                "closed": ["YOU CAN SEE THE IRON DOOR FORM HERE?1."],
                }
            }
        }
    },
"bertha_office_door_01": {
    "default": {
        "approaching": [""],
        "connections": {
            "hallway_04": {
                "open": ["A wooden door is here, partly open."],
                "closed": ["You can see a wooden door, firmly closed."],
                },
            }
        }
    },

# ALLEY DESCRIPTIONS

"alley_01": { #standing at alley entrance
    "default": {
        "approaching": {
            "cab_01" : {"neutral": ["You cross the sidewalk...", "Walking up to the alleyway...",]},
            "alley_02": {"neutral": ["You exit the alleyway, and return to the street."]}
        },
        "at_entity": [

        ],
        "leaving": {
            "cab_01": {"neutral": ["You leave the alley behind..."]},
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "cab_01": {
                "neutral": ["The alleyway can be seen from here."],
            },
            "alley_02": {
                "neutral": ["The alley opens up to the street."]
            }
        }
    }
},

"alley_02": { #start of actually in alley
    "default": {
        "approaching": {
            "alley_01": {"neutral": ["The alley narrows.","The walls close in."]},
        },
        "at_entity": [
            {"neutral": ["Buildings loom overhead.", "The passage stretches on."],
             "bad": ["It's quite narrow.", "It feels claustrophobic.", "It's cramped."]},
            {
                "bad": ["It smells of garbage and decay.", "The walls are covered in graffiti.", "It's eerily quiet."],
                "good": ["It's surprisingly calm.", "It's surprisingly quiet."],
            }
        ],

        "leaving": {
        },
        "times": {},
        "weather": {"sun": ["You hear the sound of dripping water.", "The air is damp and musty."],
                    "rain": ["Water gushes down an eavestrough.", "An eavestrough gushes water.","A nearby gutter drains the rain."]
                    },
        "tags": ["urban"],
        "connections": {
            "alley_01": {
                "neutral": ["The entrance lies before you.", "The alleyway lies before you."],
            },
            "alcove_01": {
                "neutral": ["An alcove connects to the alley."],
            },
            "alley_03": {
                "neutral": ["The alley continues onwards to the street."],
            }
        }
    }
},

"alcove_01": { #maybe have some object with the ashes nested?
    "default": {
        "approaching": {"neutral": ["You step into a small alcove."]},
        "at_entity": {
            "neutral": [""],
        },
        "leaving": {
            "neutral": ["You step back into the alley."],
        },
        "times": {},
        "weather": { #prevents regular weather
            "rain": ["The alcove shields you from the rain."],
            "sun": ["It's noticeably darker here.", "It provides quite a bit of shade."],
        },
        "tags": ["urban"],
        "connections": {
            "alley_02": {
                "neutral": ["An alcove branches off the main path.", "An alcove is beside you."],
            }
        }
    }
},
"alley_03": {
    "default": {
        "approaching": {
            "neutral" :["The alley bends slightly.", "Buildings tower above you."]
        },
        "at_entity": {
            "neutral": [],

        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_02": {
                "neutral": ["The alley continues, dark and narrow."],
            },
            "alley_03_1": {
                "neutral": ["From here, the path leads all the way back to the cab."],
            }
        }
    }
},
"alley_03_1": {
    "default": {
        "approaching": {
            "neutral" :[]
        },
        "at_entity": {
            "neutral": [],

        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_02": {
                "neutral": [""],
            },
            "alley_03_1": {
                "neutral": ["From here, the path leads all the way back to the cab."],
            }
        }
    }
},

"crime_scene_01": { #widens to crime scene
    "default": {
        "approaching": {
            "neutral": ["The alleyway widens.", "The passage opens up to a small court."],
        },
        "at_entity": {
            "neutral": ["You arrive at the crime scene."],
        },
        "leaving": {
        },
        "times": {},
        "weather": {"sun": [],
                    "rain": []
                    },
        "tags": ["urban"],
        "connections": {
            "alley_03_1": {
                "neutral": [""],
            },
            "alley_04": {
                "neutral": ["The crime scene is ahead."],
            }
        }
    }
},

"alley_04": { #narrows again - muddy ground, footprint
    "default": {
        "approaching": {"neutral": ["The ground is uneven.", "You walk across uneven footing."]
        },
        "at_entity": {
            "neutral": ["The ground squelches under your feet.", "The mud sticks to your shoes."],
            #you notice muddy footprints, imprints, they are messed up but clear enough to make out shoe vs boot?

            #MUD STICKS HINT FOR THE CLEAN SHOES
        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "crime_scene_01": {
                "neutral": ["The alley stretches on..."],
            },
            "dead_end_01": {
                "neutral": ["The dead end connects to the alley."],
            },
            "alley_05": {
                "neutral": ["The alley stretches on..."],
            }
        }
    }
},

"dead_end_01": {
    "default": {
        "approaching": {
        },
        "at_entity": {
            "neutral": ["You are at a dead end.", "The area is littered with trash and debris.", "It's a dead end."],
        },
        "leaving": {
            "neutral": ["You turn back."],
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_04": {
                "neutral": [""],
            }
        }
    }
},

"alley_05": { #TURN AND FALL
    "default": {
        "approaching": {
            "neutral": ["You follow the sharp turn. ", "The alley turns sharply.", "You follow the bend."],
        },

        "at_entity": {
            "neutral": ["Here, the alley is tight and confined.", "The walls press inwards.", "The alley is narrow, but manageable."],
            "bad": ["The alley feels oppressive and claustrophobic.", "The walls press inwards.", "Here, the alley is tight and confined."],
        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_04": {
                "neutral": ["Ahead, the alley branches.", "The alley branches."],
            },
            "alley_06": {
                "neutral": ["The alley continues further."],
            }
        }
    }
},

"alley_06": { #get up from fall, come to 3 way branch
    "default": {
        "approaching": {
        },
        "at_entity": {
        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_05": {
                "neutral": ["The alley leads onwards."],
            },
            "alley_07": {
                "neutral": ["The alley leads onwards."],
            },
            "fire_escape_01": {
                "neutral": ["The fire escape descends into the alleyway.", "The ground is beneath you."],
            }
        }
    }
},

"fire_escape_01": { #AT BASE OF LADDER.
    # event (maybe no event needed), janked metal rail, scrap type AND fire escape here
    "default": {
        "approaching": {
            "neutral": [],
        },
        "at_entity": {
            "neutral": ["You stand at the base of the fire escape.", "The ladder hangs just within reach."],
        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_06": {
                "neutral": ["A fire escape is nearby."],
            },
            "fire_escape_02": {
                "neutral": ["The fire escape leads down to the alley."],
            }
        }
    }
},
"fire_escape_02": { #ON LADDER #hair
    "default": {
        "approaching": {
            "neutral": ["The ladder shakes as you climb", "The metal creaks."],
            "bad": ["The rungs groan under your weight.", "It rattles as you climb."]
        },
        "at_entity": {
            "neutral": ["The rungs feel cold under your hands."],
            "bad": ["The rust digs into your hands."],
        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban", "outdoors"],
        "connections": {
            "fire_escape_01": {
                "neutral": ["The ground is beneath you."],
            },
            "fire_escape_03": {
                "neutral": ["The ladder leads all the way to the roof."],
            }
        }
    }
},

"fire_escape_03": { #ON LADDER #hair
    "default": {
        "approaching": {
            "neutral": ["The ladder shakes as you climb", "The metal creaks."],
            "bad": ["The rungs groan under your weight.", "It rattles as you climb."]
        },
        "at_entity": {
            "neutral": ["The rungs feel cold under your hands."],
            "bad": ["The rust digs into your hands."],
        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban", "outdoors"],
        "connections": {
            "fire_escape_02": {
                "neutral": ["The ladder extends below."],
            },
            "roof_top_01": {
                "neutral": ["The ladder leads to the rooftop.", "Above, you can see the rooftop."],
            }
        }
    }
},
"roof_top_01": {
    "default": {
        "approaching": {
            "neutral": ["You climb up onto the rooftop.", ],
        },
        "at_entity": [{
            "neutral": ["The city stretches out before you.","Your gaze stretches out onto the city.", "You look down at the city."],

        },
        {"bad": ["A lurch of vertigo hits you.", "It makes you slightly nauseous.", "You feel a pang of fear as you imagine falling."],
            "good": ["The rooftop offers a stunning view.", "The view from here is breathtaking."],},
        {"neutral": ["Multiple paths from here lead to different areas of the city... \n *turn back* "]},
        ],
        "leaving": {
            "neutral": ["You climb back down."],
        },
        "times": {},
        #GREAT PLACE FOR WEATHER!!!!
        "weather": {"sun": ["The roof has special weather text"],
                    "rain": ["The roof has special weather text"]
                    },
        "tags": ["urban"],
        "connections": {
            "fire_escape_01": {
                "neutral": ["The fire escape leads back down to the alley."],
            }
        }
    }
},

"alley_07": {
    "default": {
        "approaching": {
        },
        "at_entity": {
            "neutral": ["From here, the alley continues towards the residential area. \n *turn back*"],
        },
        "leaving": {
            "neutral": ["You turn back."],
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_06": {
                "neutral": ["The alley leads back the way you came."],
            }
        }
    }
},


}







