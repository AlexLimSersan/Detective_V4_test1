#for weather or connections, you have
# optional weather or time keys.
# always key weather, time. or just time. but never time, weather!!!
loc_description_data = {
"cab_01": {
    "default": {
        "approaching": { #
            "neutral": ["The cab is lazily parked, taking up 3 spots...",  "The cab idles.."],
            "good": ["The cabbie waves as you approach.", "The cab idles.."],
            "bad": ["The cabbie glances your direction.", "The cab is surrounded by cigarettes", "The cab idles.."]
        },
        "at_entity": {#driver
            "neutral": ['The driver adjusts his mirror. "Where to?"', "The cabbie nods his head.", "You enter the cab."],
            "good": ["You are greeted by a friendly nod from the driver.", "You enter the cab."],
            "bad": ['The cab smells faintly of stale smoke and sweat.', 'The driver adjusts his mirror. "Where to?"' ,'The driver looks indifferent to your presence.']
        },
        "times": {
            "morning": ["He yawns."],
            "afternoon": ["He rubs his eyes."],
            "evening": ["He lights a cigarette."],
            "night": ["The headlights flicker."]
        },
        "weather": { #optionally keyed to time of day
            "rain": ["Raindrops pelt the cab, streaking its windows.", "The rain makes a rhythmic drumming sound."],
            "sunny": ["The sun reflects off the cab’s metal, making it shimmer brightly."],
            "grey": ["The sky makes the cab look dull and unremarkable."]
        },
        "tags": ["cab"],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "porch_01": { #seeing the cab from the porch
                "sunny": {
                    "morning": ["The cab is parked nearby, its polished surface reflecting the morning sun."],
                    "afternoon": ["The cab stands out in the bright afternoon sun, casting a sharp shadow."],
                    "evening": ["The cab is bathed in the soft hues of the evening, its metal surface taking on a warm glow."],
                    "night": ["The cab is a dark silhouette, its form barely visible under the streetlight."]
                },
                "rain": {
                    "morning": ["The cab is slick with rain, water running in rivulets down its sides."],
                    "afternoon": ["The cab appears slightly blurred through the rain, its form softened by the downpour."],
                    "evening": ["The cab reflects the dim evening light, its surface shimmering with rainwater."],
                    "night": ["The cab is a dark, wet silhouette, barely visible through the rain."]
                },
                "grey": {
                    "morning": ["The cab is muted under the grey morning sky, blending into the subdued surroundings."],
                    "afternoon": ["The cab sits quietly in the grey afternoon, its details softened by the overcast light."],
                    "evening": ["The cab is a dark shape against the greying evening, its form indistinct."],
                    "night": ["The cab is barely visible in the dim, grey light of night, a shadow among shadows."]
                }
            },
            "alley_01": { #seeing the cab from the alley
                "sunny": {
                    "morning": ["The cab is parked at the end of the alley, its polished surface glinting in the morning sun."],
                    "afternoon": ["The cab casts a sharp shadow against the alley walls, standing out in the bright afternoon sun."],
                    "evening": ["The cab is bathed in the warm evening light, its metal surface glowing softly."],
                    "night": ["The cab is a dark silhouette at the end of the alley, its form barely visible under the streetlight."]
                },
                "rain": {
                    "morning": ["The cab is slick with rain, water running in rivulets down its sides as it sits at the end of the alley."],
                    "afternoon": ["The cab appears slightly blurred through the rain, its form softened by the downpour."],
                    "evening": ["The cab reflects the dim evening light, its surface shimmering with rainwater."],
                    "night": ["The cab is a dark, wet silhouette at the end of the alley, barely visible through the rain."]
                },
                "grey": {
                    "morning": ["The cab is muted under the grey morning sky, blending into the subdued surroundings at the end of the alley."],
                    "afternoon": ["The cab sits quietly in the grey afternoon, its details softened by the overcast light."],
                    "evening": ["The cab is a dark shape against the greying evening sky, its form indistinct."],
                    "night": ["The cab is barely visible in the dim, grey light of night, a shadow among shadows at the end of the alley."]
                }
            },
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
            "sunny": {
                "morning": ["The porch basks in the soft morning light."],
                "afternoon": ["The afternoon sun warms the porch, making the wood hot to the touch."],
                "evening": ["The porch glows softly in the fading light of the evening."],
                "night": ["The porch is cloaked in darkness, the shadows deep and long."]
            },
            "rain": {
                "morning": ["Raindrops tap gently on the porch roof as the morning light filters through the clouds."],
                "afternoon": ["The porch is slick and shiny from the rain, with puddles forming in the corners."],
                "evening": ["The porch glistens in the dim light as rain continues to fall, creating a soothing rhythm."],
                "night": ["The porch is shrouded in darkness, with the sound of rain pattering softly against the wood."]
            },
            "grey": {
                "morning": ["The porch is wrapped in a soft, grey light, the sky overcast and dull."],
                "afternoon": ["The afternoon brings a steady grey, the porch cool and shaded."],
                "evening": ["The porch is enveloped in a muted grey, the light fading gently as evening falls."],
                "night": ["The porch is dimly lit, with shadows blending into the grey of the night sky."]
            }
        },

        "tags": ["urban"],
        "connections": {#optional weather or time keys.
                # always key weather, time. or just time. but never time, weather!!!
            "lounge_01": {  # seeing the porch from the lounge
                "sunny": {
                    "morning": ["The porch basks in the soft morning light, visible through the lounge windows."],
                    "afternoon": [
                        "The porch is bright and inviting, the afternoon sun making the wood hot to the touch."],
                    "evening": [
                        "The porch glows softly in the fading light of the evening, a peaceful sight from the lounge."],
                    "night": [
                        "The porch is cloaked in darkness, the shadows deep and long, only faintly visible from the lounge."]
                },
                "rain": {
                    "morning": [
                        "Raindrops tap gently on the porch roof, the morning light filtering through the clouds, visible from the lounge."],
                    "afternoon": [
                        "The porch is slick and shiny from the rain, with puddles forming in the corners, a calming view from the lounge."],
                    "evening": [
                        "The porch glistens in the dim light as rain continues to fall, creating a soothing rhythm seen from the lounge."],
                    "night": [
                        "The porch is shrouded in darkness, with the sound of rain pattering softly against the wood, barely visible from the lounge."]
                },
                "grey": {
                    "morning": [
                        "The porch is wrapped in a soft, grey light, the sky overcast and dull, creating a serene view from the lounge."],
                    "afternoon": [
                        "The afternoon brings a steady grey, the porch cool and shaded, a calm scene from the lounge."],
                    "evening": [
                        "The porch is enveloped in a muted grey, the light fading gently as evening falls, a quiet sight from the lounge."],
                    "night": [
                        "The porch is dimly lit, with shadows blending into the grey of the night sky, barely discernible from the lounge."]
                }
            },
        }
    }
},
"lounge_01": {
    "default": {
        "approaching": {
            "neutral": ["The lounge reeks of smoke."],
            "good": ["The pub's lively atmosphere draws you in, promises of good times inside."],
            "bad": ["The pub looks rough around the edges, its patrons eyeing you warily."]
        },
        "at_entity": {
            "neutral": ["You stand at the entrance of the pub, the door slightly ajar."],
            "good": ["The warm glow from inside the pub spills out, inviting you in."],
            "bad": ["The pub’s interior is dim and smoky, the air thick with the scent of stale beer."]
        },
        "leaving": {
            "neutral": ["You leave the pub, the noise fading behind you."],
            "good": ["You step out of the pub, feeling refreshed and invigorated."],
            "bad": ["You exit the pub, the night's cold air biting at your skin."]
        },
        "times": { #lounge is quiet, picks up in the evening/night
            "morning": ["It's a quiet morning."],
            "afternoon": ["In the afternoon, the lounge is quiet, a few patrons nursing their drinks."],
            "evening": ["The pub comes alive in the evening, filled with laughter and music."],
            "night": ["At night, the pub is bustling, the sound of revelry spilling into the street."]
        },
        "weather": {
            "rain": ["Raindrops patter against the pub's windows, creating a cozy ambiance inside."],
            "sunny": ["The pub's sign gleams under the bright sun, a beacon for thirsty travelers."],
            "grey": ["The pub looks dreary under the grey sky, but inside, it’s a different story."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "porch_01": { #seeing the lounge from the porch
                "sunny": {
                    "morning": ["The lounge windows glimmer in the soft morning light, inviting with a warm glow from the porch."],
                    "afternoon": ["The lounge is filled with bright light, its windows almost too bright to look at directly from the porch."],
                    "evening": ["The lounge lights start to flicker on, creating a cozy, inviting atmosphere as seen from the porch."],
                    "night": ["The lounge is a beacon of light, the windows glowing warmly against the night, visible from the porch."]
                },
                "rain": {
                    "morning": ["The lounge windows are streaked with rain, the light inside soft and welcoming as seen from the porch."],
                    "afternoon": ["The lounge windows glisten with raindrops, the interior light diffused through the wet glass, visible from the porch."],
                    "evening": ["The lounge lights shine through the rain, casting a warm glow onto the wet street, visible from the porch."],
                    "night": ["The lounge is a warm, glowing refuge, its light cutting through the rainy night, visible from the porch."]
                },
                "grey": {
                    "morning": ["The lounge windows reflect the dull grey light, the interior dim and quiet as seen from the porch."],
                    "afternoon": ["The lounge is calm and quiet, the grey light filtering softly through the windows, visible from the porch."],
                    "evening": ["The lounge windows begin to glow, a warm light emerging from the grey backdrop, visible from the porch."],
                    "night": ["The lounge is a soft glow in the grey night, the light spilling out onto the street, visible from the porch."]
                }
            },
            "bar_01": { #seeing the lounge from the bar
                "morning": ["The lounge is serene, a place of quiet before the day begins."],
                "afternoon": ["The lounge is lively with chatter, contrasting the bar's calm."],
                "evening": ["The lounge is cozy and inviting, a warm glow seen from the bar."],
                "night": ["The lounge is vibrant and energetic, visible from the bustling bar."]
            },
            "kitchen_01": { #seeing the lounge from the kitchen
                "morning": ["The lounge is calm, soft hues touching its furnishings."],
                "afternoon": ["The lounge is vibrant, filled with people and energy."],
                "evening": ["The lounge glows warmly, a comforting sight from the kitchen."],
                "night": ["The lounge buzzes with energy, the kitchen a backstage view."]
            },
            "stage_01": { #seeing the lounge from the stage
                "morning": ["The lounge is quiet, filled with anticipation from the stage."],
                "afternoon": ["The lounge hums with activity, lively and bustling."],
                "evening": ["The lounge is warm and inviting, seen from the stage."],
                "night": ["The lounge is vibrant, the stage offering a unique view."]
            },
            "hallway_01": { #seeing the lounge from the hallway
                "morning": ["The lounge is a peaceful retreat, calm and quiet."],
                "afternoon": ["The lounge is lively, a world away from the quiet hallway."],
                "evening": ["The lounge is warm and active, inviting from the hallway."],
                "night": ["The lounge is energetic, the hallway a silent observer."]
            }
        },
    },
},
"bar_01": {
    "default": {
        "approaching": {
            "neutral": ["The bar comes into view, a bustling hive of activity."],
            "good": ["The bar looks lively, with patrons chatting animatedly."],
            "bad": ["The bar appears crowded and noisy, with a few rough-looking patrons."]
        },
        "at_entity": {
            "neutral": ["You stand at the bar, the bartender giving you a nod of acknowledgment."],
            "good": ["The bartender smiles as you approach, ready to take your order."],
            "bad": ["The bar is packed, and getting the bartender's attention seems challenging."]
        },
        "leaving": {
            "neutral": ["You step away from the bar, the noise fading slightly."],
            "good": ["You leave the bar, feeling satisfied and content."],
            "bad": ["You move away from the bar, eager to escape the commotion."]
        },
        "times": {
            "morning": ["The bar is quiet, only a few early risers present."],
            "afternoon": ["The bar is moderately busy, a steady hum of conversation in the air."],
            "evening": ["The bar is lively, filled with people unwinding after a long day."],
            "night": ["The bar is at its peak, the noise and energy almost palpable."]
        },
        "weather": {
            "rain": ["The sound of rain outside mixes with the chatter inside the bar."],
            "sunny": ["Sunlight streams through the windows, casting warm glows on the patrons."],
            "grey": ["The bar feels cozier under the grey sky, a refuge from the dreary weather."]
        },
        "tags": ["indoors"],
        "connections": {
            "lounge_01": { #seeing the bar from the lounge
                "morning": ["The bar is quiet, the morning light casting soft shadows."],
                "afternoon": ["The bar is bustling, a lively scene from the lounge."],
                "evening": ["The bar glows warmly, filled with patrons and chatter."],
                "night": ["The bar is vibrant, a hub of activity seen from the lounge."]
            },
        }
    }
},
"kitchen_01": {
    "default": {
        "approaching": {
            "neutral": ["The kitchen door swings open, releasing a wave of delicious aromas."],
            "good": ["The scent of freshly cooked meals wafts from the kitchen, enticing you inside."],
            "bad": ["The kitchen door is ajar, but the chaotic sounds from within make you hesitant."]
        },
        "at_entity": {
            "neutral": ["You are in the kitchen, surrounded by bustling cooks and clattering pots."],
            "good": ["The kitchen is a well-oiled machine, with chefs expertly preparing dishes."],
            "bad": ["The kitchen is in disarray, with staff struggling to keep up with orders."]
        },
        "leaving": {
            "neutral": ["You leave the kitchen, the sounds and smells fading behind you."],
            "good": ["You exit the kitchen, satisfied by the efficiency and delicious aromas."],
            "bad": ["You step out of the kitchen, glad to leave the chaos behind."]
        },
        "times": {
            "morning": ["The kitchen is preparing breakfast, with the smell of bacon and eggs in the air."],
            "afternoon": ["The kitchen is busy with lunch orders, a flurry of activity."],
            "evening": ["The kitchen is at its peak, with dinner service in full swing."],
            "night": ["The kitchen is winding down, with only a few late-night orders being prepared."]
        },
        "weather": {
            "rain": ["The sound of rain outside contrasts with the warmth and activity inside the kitchen."],
            "sunny": ["Sunlight streams through the kitchen windows, highlighting the busy chefs."],
            "grey": ["The kitchen feels like a cozy refuge from the grey sky outside."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "lounge_01": { #seeing the kitchen from the lounge
        "morning": ["The kitchen is calm, a peaceful start to the day."],
        "afternoon": ["The kitchen is busy, filled with movement and energy."],
        "evening": ["The kitchen glows warmly, a comforting sight."],
        "night": ["The kitchen is active, a backstage view of the evening's events."]
            }
        }
    }
},
"stage_01": {
    "default": {
        "approaching": {
            "neutral": ["The stage is set, the curtains drawn back to reveal a simple setup."],
            "good": ["The stage looks inviting, ready for the evening's performance."],
            "bad": ["The stage appears neglected, with dusty props and a worn backdrop."]
        },
        "at_entity": {
            "neutral": ["You stand on the stage, the lights casting long shadows."],
            "good": ["The stage feels alive, the audience's anticipation palpable."],
            "bad": ["The stage feels empty, the silence almost oppressive."]
        },
        "leaving": {
            "neutral": ["You step off the stage, the lights dimming behind you."],
            "good": ["You leave the stage, the applause echoing in your ears."],
            "bad": ["You exit the stage, feeling a sense of relief."]
        },
        "times": {
            "morning": ["The stage is quiet, the morning light filtering through the curtains."],
            "afternoon": ["The stage is being prepared for the evening, a flurry of activity."],
            "evening": ["The stage is in full swing, the performance captivating the audience."],
            "night": ["The stage is dark and empty, the show long over."]
        },
        "weather": {
            "rain": ["The sound of rain outside adds a rhythmic backdrop to the stage."],
            "sunny": ["The stage is brightly lit, matching the sunny day outside."],
            "grey": ["The stage feels somber under the grey sky, the mood reflected in the audience."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "lounge_01": { #seeing the stage from the lounge
                "morning": ["The stage is quiet, anticipation hanging in the air."],
                "afternoon": ["The stage is lively, preparations underway."],
                "evening": ["The stage glows invitingly, ready for the night's performance."],
                "night": ["The stage is vibrant, the focus of the lounge's energy."]
            }
        }
    }
},
"stage_02": {
    "default": {
        "approaching": {
            "neutral": ["The backstage area is dimly lit, filled with props and equipment."],
            "good": ["The backstage buzzes with anticipation, ready for the upcoming performance."],
            "bad": ["The backstage feels cramped and cluttered, a stark contrast to the stage."]
        },
        "at_entity": {
            "neutral": ["You are backstage, the faint sound of the audience filtering through."],
            "good": ["The backstage is a hive of activity, with performers preparing eagerly."],
            "bad": ["The backstage feels chaotic, with people rushing and tempers flaring."]
        },
        "leaving": {
            "neutral": ["You leave the backstage, the noise and activity fading away."],
            "good": ["You step out of the backstage, feeling a sense of accomplishment."],
            "bad": ["You exit the backstage, glad to escape the chaos."]
        },
        "times": {
            "morning": ["The backstage is quiet, with only a few staff preparing for the day."],
            "afternoon": ["The backstage is busy, with preparations for the evening's show in full swing."],
            "evening": ["The backstage is a whirlwind of activity, with performers getting ready."],
            "night": ["The backstage is empty, the show long over and the lights dimmed."]
        },
        "weather": {
            "rain": ["The sound of rain against the roof adds a calming backdrop to the backstage hustle."],
            "sunny": ["Sunlight filters in through small windows, casting warm glows on the scene."],
            "grey": ["The backstage feels subdued under the grey sky, the mood reflected in the performers."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "stage_01": {
                "neutral": ["From backstage, the stage is just a step away."],
                "good": ["The stage looks inviting from backstage, ready for the performance."],
                "bad": ["The stage seems a distant goal, the backstage chaos overwhelming."]
            },
            "hallway_01": {
                "neutral": ["The hallway connects to the backstage, a route often used by staff."],
                "good": ["The hallway feels like a quiet escape from the backstage buzz."],
                "bad": ["The hallway looks unwelcoming, a stark contrast to the busy backstage."]
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
                "neutral" : ["Theres a hallway closeby.", " A hallway entrance can be seen from here."],
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
            "neutral": ["The hallway stretches on, "],
        },
        "leaving": {
        },
        "times": {
            "morning": [" silent and empty."],
            "afternoon": ["with occasional footsteps echoing."],
            "evening": ["with people moving to and fro.", "dimly lit."],
            "night": ["late nighters stumbling about."]
        },
        "weather": {

        },
        "tags": [],
        "connections": {
            "hallway_01": {
                "neutral": ["You can make out doors at the end of the hall."],
                "bad": ["Doors face you at the end of the hall."]
            },
            "hallway_03": {
                "neutral": ["The pub's lounge is close ahead."]
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
                "neutral": ["You are coming close to the end of the hallway."],
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
                "neutral": ["You are near the end of the hallway."],
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
                "open": ["Beside that, you can see a wooden door, partly open."],
                "closed": ["Beside that, you can see a wooden door, firmly closed."],
                },
            }
        }
    }

}






