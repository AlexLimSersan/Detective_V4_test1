#for weather or connections, you have
# optional weather or time keys.
# always key weather, time. or just time. but never time, weather!!!
#why not optional time or weather keys for all of them?
loc_description_data = {
    #FOR APPROACH/LEAVING, TRY CONNECTIONS?
"cab_01": {
    "default": {
        "approaching": { #
            "neutral": ["The cab is lazily parked, taking up 3 spots...",  "The cab idles.."],
            "good": ["The cabbie waves as you approach.", "The cab idles, the engine a low, constant hum."],
            "bad": ["The cabbie glances your direction.", "The cab is surrounded by cigarettes", "The cab idles.."]
        },
        "at_entity": {#driver
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
        "weather": { #optionally keyed to time of day
            "rain": ["Raindrops pelt the cab, streaking its windows.", "The rain makes a rhythmic drumming sound.", "The headlights cast a pyramid in the rain."],
            "sunny": ["The sun reflects off the cab’s metal, making you squint.", "The sunlight makes the cab shimmer."],
            "grey": ["The grey sky paints the cab dull."]
        },
        "tags": ["cab"],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "porch_01": { #seeing the cab from the porch
                "sunny": ["The cab is parked nearby."],
                "rain": ["The cab is parked nearby.", "In the distance, you can see the cab through the rain."],
                "grey": ["The cab is parked nearby."],
            },
            "alley_01": ["The cab is parked nearby."],
            },
        "leaving": {
            "neutral": ["You exit the cab, closing the door behind you."],
        },

    },
},
"porch_01": {
    "default": {
        "approaching": {
            "neutral": ["Wooden planks creak underfoot.",],
        },
        "at_entity": {
            "neutral": ["You stand on the porch, its surface weathered and worn."],
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

        "tags": ["urban"],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "lounge_01": {  # seeing the porch from the lounge
                "sunny": {
                    "morning": ["Ahead, the porch basks in the morning sun."],
                    "afternoon": [
                        "Ahead, the porch basks in the sun."],
                    "evening": [
                        "Ahead, the porch basks in the evening sun."],
                    "night": [
                        "Ahead, the porch is lit only by the soft, flickering lights."]
                },
                "rain": [
                        "Ahead, porch is slick from the rain.", ],
                "grey": ["Ahead, you can see the porch."],
            },
        }
    }
},
"lounge_01": {
    "default": {
        "approaching": {
            "neutral": ["The air reeks of smoke.", "You're hit with a wave a smoke as you enter."],
            "bad": ["People glance at you briefly as you enter."]
        },
        "at_entity": {
            "neutral": ["The lounge is a bit run down.", "The lounge has a rustic feel.", "", ""],
        },
        "leaving": {

        },
        "times": { #lounge is quiet, picks up in the evening/night
            "morning": ["It's a quiet morning.", "A few staff members are cleaning up from last night."],
            "afternoon": ["People laze around."],
            "evening": ["It's busy.", "Drunk chatter forms a noisy backdrop."],
            "night": ["It's starting to get rowdy.", "It's packed in here.", "People bump into you as they amble about."]
        },
        "weather": {
            "rain": ["Raindrops slam against the windows."],
            "sunny": ["Sun filters through the blinds.", "The sun casts it all in dramatic lighting."],
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
            "rain": ["The rain mixes with the chatter.", "The window panes shake with the howling wind."],
            "sunny": ["Sunlight streams through the windows, casting warm glows on the patrons."],
            "grey": ["The wind blows against the window, rattling it."]
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

        },
        "at_entity": {
            "neutral": ["You stand on the stage."],
        },
        "leaving": {
            "neutral": ["You step off the stage."],
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
            "neutral": ["You hunch to get through the passage.", ""],
        },
        "at_entity": {
            "neutral": ["You are backstage, next to miscellaneous props and equipment."],
            "bad": ["The backstage feels cramped and cluttered."]
        },
        "leaving": {
            "neutral": ["You hunch to get through the passage.", ""],
        },
        "times": {

        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "stage_01": { #seeing backstage from stage
                "neutral": ["You can see the backstage from here."],
            },
            "hallway_01": {
                "neutral": ["The hallway connects to the backstage."],
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
            "neutral": [" "],
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
"hallway_04": {
    "default": {
        "approaching": {
            "neutral": ["You come to the end of the hallway."],

        },
        "at_entity": {
            "neutral": ["Wood groans underfoot.", "It's a tight area.", "It feels cramped."],
            "bad": ["The walls feel slightly claustrophobic.", "It feels cramped."]
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
        "tags": [""],
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
        "approaching": ["approaching office door"],
        "connections": {
            "hallway_04": {
                "open": ["A wooden door is here, partly open."],
                "closed": ["You can see a wooden door, firmly closed."],
                },
            }
        }
    }

}






