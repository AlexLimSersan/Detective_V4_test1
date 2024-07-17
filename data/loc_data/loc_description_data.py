#for weather or connections, you have
# optional weather or time keys.
# always key weather, time. or just time. but never time, weather!!!
#why not optional time or weather keys for all of them?
loc_description_data = {


"void_01": {
},
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
            "reception_01": {
                "neutral": ["You sit in the cab, watching the city pass by through the window."],
                "good": ["You relax in the cab", "The gentle hum of the engine feels soothing."],
                "bad": ["You brace yourself as the cab hits another pothole, the ride anything but smooth."]
                },
            "EXIT_GAME": {
                "neutral": ["You take one last look at the town...", "The city passes you by through the window..."],
                },
        },
        "driving_arriving": {
            "porch_01": ["The pub comes into view.."],
            "alley_01": ["The alley comes into view..."],
            "reception_01": ["The morgue comes into view..."],
            "EXIT_GAME": ["The cab drives off, leaving it all behind.\n"],
        },
        "approaching": { #approaching current loc, FROM last loc. so can optinally add last locs here, then optional weather, time, etc
            "neutral": ["The cab is lazily parked, taking up 3 spots...",  "The cab idles.."],
            "good": ["The cabbie waves as you approach.", "The cab idles, the engine a low, constant hum."],
            "bad": ["The cabbie glances your direction.", "The cab is surrounded by cigarettes", "The cab idles.."]
        },
        "at_entity": {#inside cab
            "neutral": ['The driver adjusts his mirror. "Where to?"', "The cabbie glances your way as you climb in.", ],
            "good": ["You are acknowledged with a friendly nod.", "The cabbie greets you over the engine purr."],
            "bad": ['The cabbie smells faintly of stale smoke and sweat.', 'The driver adjusts his mirror, you catch a glimpse of his tired eyes. "Where to?"' ,'The driver looks indifferent to your presence.']
        },
        "times": {
            "morning": {"neutral": ["He yawns.", "He stretches in his seat.", "He leans back.", "He grips the steering wheel."],
                        "bad": ["He looks like he hasn't slept.", "His hands reach for another cigarette.", "He rubs his eyes, tired.", "He looks tired.",
                                ]},
            "afternoon": {"neutral": ["He rubs his eyes.", "He stretches in his seat.", "He sinks into his seat.", "He shifts in his seat."],
                        "bad": ["He looks like he hasn't slept.", "His hands reach for another cigarette.", "He rubs his eyes, tired.", "He looks tired."]},
            "evening": {"neutral": ["He scratches his head.", "His eyes wander.", "He shifts in his seat.", "He grips the steering wheel."],
                        "bad": ["He looks like he might fall asleep.", "His hands reach for another cigarette.", "His eyes dart, scanning the horizon.",]},
            "night":{"neutral": ["The headlights beam onto the street.", "He gazes at the night sky.", "He squirms in his seat, restless."],
                        "bad": ["The headlights flicker.", "He looks like he might fall asleep.", "His hands shakily reach for a cigarette.", "His eyes dart across the horizon.",]},
        },
        "weather": { #optionally keyed to time of day - should make sense from INSIDE CAB!
            "storm":["The wind hammers the rain against the cab.", "Lightning arcs across the sky, followed by thunderous, roaring crack.", "The headlights cast the storm with a cone of light."],
            "rain": ["Raindrops pelt the cab, streaking its windows.", "The rain makes a rhythmic drumming sound.", "The headlights cast a pyramid in the rain."],
            "sun": ["The sun reflects off the hood, making you squint.", "The sunlight makes the hood shimmer."],
        },
        "tags": ["cab"],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "porch_01": { #seeing the cab from the porch
                "sun": ["The cab is parked nearby."],
                "rain": ["Through the rain, you can see the idling cab."],
                "storm": ["You can see the cab through the downpour."],
            },
            "alley_01": ["You can see the cabbie waiting across the street."],
            "alley_07": ["You can see the cabbie waiting across the street."],
            "backroom_door_02": ["You can walk to the cab from here..."]
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
            "cab_01": {"neutral": ["You approach the pub, and arrive at the porch."]}
        },
        "at_entity": {
            "neutral": ["Its surface is weathered and worn.", "Wooden planks creak underfoot."],
            "bad": ["The wood groans under your weight.", "Wood is rotting near the foundation."],
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
                    "morning": ["Ahead, the porch basks in the morning sun.","The morning sun bathes the porch in soft light."],
                    "afternoon": [
                        "Ahead, the porch basks in the noon sun.", "The sun casts the porch with sharp shadows."],
                    "evening": [
                        "Ahead, the porch offers a view of the sunset.","Ahead, the porch basks in the evening sun."],
                    "night": [
                        "Ahead, the porch is lit only by soft, dancing candles."]
                },
                "rain": [
                        "You can see the porch ahead, slick from the rain.", ],
                "storm": ["The storm rages on outside, drenching the porch in rain."],
            },
        }
    }
},
"lounge_01": {
    "default": {
        "approaching": [
            {
                "porch_01": {"neutral": ["You push through the pub doors.","You enter the pub."],},
            },
            {
                "neutral": ["The air reeks of smoke.", "You're hit with a wave a smoke."],
                "bad": ["People glance at you briefly.",]
            },
        ],
        "at_entity": {
            "neutral": ["The lounge is a bit run down.", "The lounge has a rustic feel.", "It's a quiet {current_phase}."],
        },
        "leaving": {
            "porch_01": {"neutral": ["You leave the pub.", "The doors swing as you leave the lounge."]}
        },
        "times": {
        },
        "weather": {
        },
        "tags": ["indoors"],
        "connections": {
            "porch_01": { #seeing the lounge from the porch
                "neutral": ["The entrance to the lounge is directly ahead."],
            },
            "bar_01": ["The lounge is back the way you came."],
            "kitchen_01": ["The lounge is back the way you came."],
            "stage_01": { #seeing the lounge from the stage
                "morning": ["You face the lounge."],
                "afternoon": ["You face the lounge."],
                "evening": ["From the lounge, people stare with a puzzle expression."],
                "night": ["People seem to expect you to perform."]
            },
            "hallway_01": { #seeing the lounge from the hallway
                "neutral": ["Ahead, you can see the lounge.","The hallway opens up to the lounge."],
            }
        },
    },
},
"bar_01": {
    "default": {
        "approaching": {
            "morning": ["You take a seat.","The stool rocks as you sit.", "You take a seat. The stool rocks unevenly.",],
            "afternoon": ["You take a seat.","The stool rocks as you sit.", "You take a seat. The stool rocks unevenly.",],
            "evening": ["You maneuver around a few drunks to get a seat.", "You find a seat at the quieter end of the counter."],
            "night": ["You maneuver around a few drunks to get a seat.", "You find a seat at the quieter end of the counter."],
        },
        "at_entity": {
            "neutral": [  #might have to be in approaching
                        "The counter is rough and weathered.",
                        "You notice the coarseness of the counter top.",  ],
        },
        "leaving": {
            "neutral": ["You step away from the bar." ,"You turn back the way you came.", ],
        },
        "times": { #must be of
            "morning": ["Only a few stragglers from the night are here."],
            "afternoon": ["The bar is quiet.",],
            "evening": ["The steady hum of conversation drones on.","Chatter forms a low backdrop."],
            "night": ["The steady hum of conversation drones on.","Chatter forms a low backdrop."]
        },
        "weather": {

        },
        "tags": ["indoors"],
        "connections": {
            "lounge_01": { #seeing the bar from the lounge
                "morning": ["The last few late night drinkers slump at the bar."],
                "afternoon": ["You can see the bar from here."],
                "evening": ["Some amble chatter comes from the bar."],
                "night":["Some amble chatter comes from the bar."],
            },
        }
    }
},
"kitchen_01": {
    "default": {
        "approaching": {
            "neutral": ["The doors swing open.", "The smell of grease hits your nostrils."],
        },
        "at_entity": {
            "good": ["The kitchen is well maintained.","It looks clean here"],
            "bad": ["The kitchen is in disarray.", "The kitchen is a mess."]
        },
        "leaving": {
            "neutral": ["You leave the kitchen", "You push through the kitchen doors and leave.", "You leave the way you came."],
        },
        "times": {
            "morning": ["Looks like they are just starting to prep for the day."],
            "afternoon": ["A few cooks and clattering pots surround you."],
            "evening": ["It's a quiet night.", "It's not busy at all."],
            "night": ["No one's here."]
        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "lounge_01": { #seeing the kitchen from the lounge
        "neutral": ["Swinging doors in the corner lead to the kitchen."],
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
                "neutral": ["Opposite the bar, a small, raised platform marks the stage."],
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
                "neutral" : ["The hallway entrance can be seen from here.", "The entrance to the hallway is in the far corner of the room."],
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
            "neutral": ["The hallway stretches on.", "It's silent and empty."],

        },
        "leaving": {
        },
        "times": {
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
                "neutral": ["The pub's lounge is at the end of the hall.","The hallway leads back to the lounge."]
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
                "neutral": ["The hall leads back to the pub.", "The hallway stretches on, all the way to the pub."],
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
            "neutral": [],
        },
        "at_entity": { #should just have a bunch of at scene description stuff here. relevant clues! desk, boxes, flask, etc
            "neutral": ["It's a small, quaint space.", "It's well kept."],
            "bad": ["The mess is slightly off putting.","The office is quite messy."]
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
"backroom_door_02": {
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
            "backroom_01": {
                "open": ["A backdoor leads out to the street."],
                "closed": ["A backdoor leads out to the street."],
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
                    "rain": ["Water trickles down an eavestrough.", "An eavestrough drains a thin stream of water.","A nearby gutter dribbles out the rain."],
                    "storm": ["Water jets out an eavestrough.", "An eavestrough gushes water.","A nearby gutter lets our a heavy flow of rain."]
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
            "storm": ["The alcove shields you from the storm."],
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
            "alley_03_1": {"neutral": ["The alleyway widens.", "The passage opens up to a small court."], },

        },
        "at_entity": {
            "neutral": [],
        },
        "leaving": {
        },
        "times": {},
        "tags": ["urban"],
        "connections": {
            "alley_03_1": {
                "neutral": [""],
            },
            "crime_scene_02": {
            }
        }
    }
},

"crime_scene_02": { #widens to crime scene
    "default": {
        "approaching": {
        },
        "at_entity": {
        },
        "leaving": {
        },
        "times": {},
        "weather": {
                    },
        "tags": ["urban"],
        "connections": {
            "crime_scene_01": {
                "neutral": [""],
            },
            "alley_04": {
                "neutral": ["The alley narrows again ahead."],
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

"dead_end_01": { #archway
    "default": {
        "approaching": {
            "neutral": ["You pass under.","You duck under the arch."]
        },
        "at_entity": {
            "neutral": [""],
        },
        "leaving": {
            "neutral": [""],
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
"dead_end_02": {
    "default": {
        "approaching": {
            "neutral": ["The area is littered with trash and debris."],
        },
        "at_entity": {
            "neutral": ["It's a dead end."],
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
            "fire_escape_01": { #at base of ladde,r not actually on the laddeer...
                "sun":{"neutral": ["The concrete scrapes against your shoes."],},
                "rain":{"neutral": ["You stand in a puddle."],},
                "storm":{"neutral": ["You stand in a puddle."],},
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
            "sun": {
                "night": ["The rungs feel cold under your hands."],
                "neutral": ["The rungs feel hot under your hands.",],
                "bad": ["Hot rust digs into your hands."]
            ,},
            "rain": {
                "neutral": ["The rungs feel cold under your hands."],
                "bad": ["Wet rust digs into your hands."]
                        ,},
            "storm": {
                "neutral": ["The rungs feel cold under your hands."],
                "bad": ["Wet rust digs into your hands."]
                        ,},


        },
        "leaving": {
            "fire_escape_01": {"neutral": ["You drop down to the alley."]}
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "fire_escape_01": {
                "neutral": ["The ladder hangs above you."],
            },
            "fire_escape_03": {
                "neutral": ["The ladder leads back down to the alley."],
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
            "sun": {
                "night": ["The rungs feel cold under your hands."],
                "neutral": ["The rungs feel hot under your hands.",],
                "bad": ["Hot rust digs into your hands."]
            ,},
            "rain": {
                "neutral": ["The rungs feel cold under your hands."],
                "bad": ["Wet rust digs into your hands."]
                        ,},
            "storm": {
                "neutral": ["The rungs feel cold under your hands."],
                "bad": ["Wet rust digs into your hands."]
                        ,},


        },
        "leaving": {
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "fire_escape_02": {
                "neutral": ["The ladder leads all the way to the roof."],
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
        {"neutral": ["Multiple paths from here lead to different areas of the city... "]},
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
            "neutral": ["From here, the alley continues towards the residential area. "],
        },
        "leaving": {
            "neutral": ["You turn back."],
        },
        "times": {},
        "weather": {},
        "tags": ["urban"],
        "connections": {
            "alley_06": {
                "neutral": ["The alley leads all the way to the residential area."],
            }
        }
    }
},



###############MORGUE######################
"reception_01": { #door
    "default": {
        "approaching": {
            "neutral": ["The old door is rusting at the hinges."]
        },
        "at_entity": {
            "neutral": [],
        },
        "leaving": {
            "neutral": [""],
        },
        "times": {
            "evening": ["A lantern flickers ominously."],
            "night": ["A lantern flickers ominously."],
        },
        "weather": {
            "sun": ["The sun brings out each peeling flake of paint.","The handle glints in the sun.", "Each curling flake of paint has a matching shadow."],
            "rain": ["It's coated slick from the rain.","Water beads down door, pooling at odd places.","Water drips from the handle at regular intervals."],
            "storm": ["Thunder rumbles in the distance.","A thunderclap echoes.","Lightning flashes.","Rain slams against the door.","The wind howls, rain slamming into the door.","The wind brings a shower of rain onto the door."],

        },
        "tags": [""],
        "connections": {
            "cab_01": {
                "neutral": ["Through the window, you can see the morgue."],
            },
            "reception_02": {
                "neutral": ["The exit is ahead."],
            },
        }
    }
},
"reception_02": {
            "default": {
                "approaching": {
                    "neutral": ["The air is cold here."],
                },
                "at_entity": {
                    "neutral": ["Each step sends an echo across the room.","A steady, droning hum comes from the hall."],
                },
                "leaving": {
                    "neutral": [""],
                },
                "times": {},
                "weather": {},
                "tags": ["indoors"],
                "connections": {
                    "reception_01": {
                        "neutral": ["Through the opening, you can see the laminated floors of the reception."],
                    },
                    "hallway_morgue_01": {
                        "neutral": ["The hallway opens up towards the reception."],
                    }
                }
            },


},
"morgue_office_01": { #utility room
            "default": {
                "approaching": {
                    "neutral": ["You walk into the office."]
                },
                "at_entity": {
                    "neutral": ["It's a small, run down office, each surface sterile and clean."],
                },
                "leaving": {
                    "neutral": [""],
                },
                "times": {},
                "weather": {},
                "tags": ["indoors"],
                "connections": {
                    "reception_02": {
                        "neutral": ["The ceiling lowers at the entrance to the office."],
                    }
                }
            }
},
"refrigeration_01": {
            "default": {
                "approaching": {
                    "neutral": ["You walk up to the metal door."]
                },
                "at_entity": {
                    "neutral": [""],
                },
                "leaving": {
                    "neutral": [""],
                },
                "times": {},
                "weather": {},
                "tags": [""],
                "connections": {
                    "hallway_morgue_02": {
                        "neutral": ["A heavy metal door faces you at the end of the hall."],
                    },
                    "refrigeration_02": {
                        "neutral": ["The door leads back to the hallway."],
                    }
                }
            },
},



"hallway_morgue_01": {
            "default": {
                "approaching": {
                    "neutral": ["You walk to hallway."]
                },
                "at_entity": {
                    "neutral": [""],
                },
                "leaving": {
                    "neutral": [""],
                },
                "times": {},
                "weather": {},
                "tags": ["indoors"],
                "connections": {
                    "reception_02": {
                        "neutral": ["Across the office, a hallway leads deeper in to the morgue."],
                    },
                    "hallway_morgue_02": {
                        "neutral": ["The hallway leads back to reception."],
                    }
                }
            },
},

"hallway_morgue_02": {
            "default": {
                "approaching": {
                    "neutral": ["Footsteps echo across the walls."]
                },
                "at_entity": {
                    "neutral": [""],
                },
                "leaving": {
                    "neutral": [""],
                },
                "times": {},
                "weather": {},
                "tags": [""],
                "connections": {
                    "refrigeration_01": {
                        "neutral": [""],
                    },
                    "hallway_morgue_01": {
                        "neutral": ["The hallway leads to a metal door."],
                    }
                }
            },
},



"refrigeration_02": {
            "default": {
                "approaching": {
                    "neutral": ["The temperature plummets as soon as you enter."]
                },
                "at_entity": {
                    "neutral": ["Each exhale emits a fleeting puff of condensed breath."],
                },
                "leaving": {
                    "neutral": [""],
                },
                "times": {},
                "weather": {},
                "tags": [""],
                "connections": {
                    "refrigeration_01": {
                        "neutral": ["Cold air rushes through the gap."],
                    },
                }
            },
},



}







