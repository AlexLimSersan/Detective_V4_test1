
loc_description_data = {
    "cab_01": {
        "default": {
            "approaching": { #
                "neutral": ["The cab is lazily parked, taking up 3 spots...",  "The cab idles.."],
                "good": ["The cabbie waves as you approach.", "The cab idles.."],
                "bad": ["The cabbie glances your direction.", "The cab is surrounded by cigarettes", "The cab idles.."]
            },
            "at_entity": {#drive
                "neutral": ['The driver adjusts his mirror. "Where to?"', "The cabbie nods his head.",],
                "good": ["You enter the cab.", "You are greeted by a friendly nod from the driver."],
                "bad": ['The cab smells faintly of stale smoke and sweat.', 'The driver adjusts his mirror. "Where to?"' ,'The driver looks indifferent to your presence.']
            },
            "leaving": {
                "neutral": ["You sit in the cab, watching the city pass by through the window."],
                "good": ["You relax in the cab", "The gentle hum of the engine feels soothing."],
                "bad": ["You brace yourself as the cab hits another pothole, the ride anything but smooth."]
            },
            "times": {
                "morning": ["He yawns."],
                "afternoon": ["He rubs his eyes."],
                "evening": ["He lights a cigarette."],
                "night": ["The headlights flicker."]
            },
            "weather": {
                "rain": ["Raindrops pelt the cab, streaking its windows.", "The rain makes a rhythmic drumming sound."],
                "sunny": ["The sun reflects off the cab’s metal, making it shimmer brightly."],
                "grey": ["The sky makes the cab look dull and unremarkable."]
            },
            "tags": ["cab"],
            "connections": {
                "alley_01": {
                    "neutral": ["From the cab, you see the narrow entrance to the alley."],
                    "good": ["The alley looks less intimidating from the comfort of the cab."],
                    "bad": ["The alley appears dark and foreboding from the cab's window."]
                },
                "porch_01": {
                    "neutral": ["The porch is visible, a short walk from the cab."],
                    "good": ["The porch looks welcoming, even from a distance."],
                    "bad": ["The porch looks worn, a stark contrast to the cab."]
                }
            }
        }
    },
"porch_01": {
    "default": {
        "approaching": {
            "neutral": ["The porch comes into view, its wooden planks creaking underfoot."],
            "good": ["The porch looks inviting, with a rocking chair swaying gently in the breeze."],
            "bad": ["The porch appears neglected, the paint peeling and the wood rotting."]
        },
        "at_entity": {
            "neutral": ["You stand on the porch, its surface worn from years of use."],
            "good": ["The porch offers a pleasant place to rest"," the chair creaking as you sit."],
            "bad": ["The porch feels unstable, each step threatening to break the silence with a loud creak."]
        },
        "leaving": {
            "neutral": ["You leave the porch behind, its wooden steps groaning underfoot."],
            "good": ["You step off the porch, feeling refreshed and ready to continue."],
            "bad": ["You hurry off the porch, eager to leave its decay behind."]
        },
        "times": {
            "morning": ["The porch basks in the soft morning light."],
            "afternoon": ["The afternoon sun warms the porch, making the wood hot to the touch."],
            "evening": ["The porch glows softly in the fading light of the evening."],
            "night": ["The porch is cloaked in darkness, the shadows deep and long."]
        },
        "weather": {
            "rain": ["Rain taps against the porch roof, creating a soothing sound."],
            "sunny": ["The porch is bathed in sunlight, casting sharp shadows."],
            "grey": ["The porch looks dreary under the grey sky, its colors muted."]
        },
        "tags": ["urban"],
        "connections": {
            "pub_01": {
                "neutral": ["From the porch, you see the entrance to the pub."],
                "good": ["The pub looks inviting from the porch, a welcome sight."],
                "bad": ["The pub seems unwelcoming from the porch, its exterior worn."]
            },
            "cab_01": {
                "neutral": ["The cab is visible from the porch, parked nearby."],
                "good": ["The cab gleams invitingly from the porch."],
                "bad": ["The cab looks tired and worn from the porch."]
            }
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
        "times": {
            "morning": ["lounge mornig."],
            "afternoon": ["In the afternoon, the pub is quiet, a few patrons nursing their drinks."],
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
            "bar_01": {
                "neutral": ["From the pub, the bar is just a few steps away."],
                "good": ["The bar looks inviting, the bartender already preparing your favorite drink."],
                "bad": ["The bar is crowded and noisy, making it hard to relax."]
            },
            "kitchen_01": {
                "neutral": ["The kitchen door swings open, releasing a wave of delicious aromas."],
                "good": ["The kitchen staff greets you warmly as you approach."],
                "bad": ["The kitchen looks chaotic, the staff struggling to keep up."]
            }
        }
    }
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
        "tags": ["urban", "indoors"],
        "connections": {
            "pub_01": {
                "neutral": ["From the bar, the pub’s entrance is within easy reach."],
                "good": ["The pub's lively atmosphere is palpable from the bar."],
                "bad": ["The pub’s noise spills over into the bar, making it hard to hear."]
            }
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
            "pub_01": {
                "neutral": ["From the kitchen, you hear the lively sounds of the pub."],
                "good": ["The pub's lively atmosphere complements the kitchen's bustle."],
                "bad": ["The pub’s noise adds to the kitchen’s chaotic environment."]
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
            "pub_01": {
                "neutral": ["From the stage, the pub's noise is a distant hum."],
                "good": ["The pub’s lively atmosphere energizes the stage."],
                "bad": ["The pub’s noise distracts from the performance on stage."]
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
        "approaching": {
            "neutral": ["The hallway stretches ahead, dimly lit and lined with closed doors."],
            "good": ["The hallway feels welcoming, with soft lighting and clean walls."],
            "bad": ["The hallway looks dark and foreboding, with flickering lights and peeling paint."]
        },
        "at_entity": {
            "neutral": ["You are in the hallway, the quiet surrounding you."],
            "good": ["The hallway feels like a peaceful respite, with gentle lighting."],
            "bad": ["The hallway feels oppressive, the silence almost deafening."]
        },
        "leaving": {
            "neutral": ["You leave the hallway, the doors closing softly behind you."],
            "good": ["You step out of the hallway, feeling refreshed."],
            "bad": ["You hurry out of the hallway, eager to escape its gloom."]
        },
        "times": {
            "morning": ["The hallway is bathed in soft morning light, quiet and empty."],
            "afternoon": ["The hallway is lightly trafficked, with occasional footsteps echoing."],
            "evening": ["The hallway is busy, with people moving to and fro."],
            "night": ["The hallway is silent and empty, the lights dimmed for the night."]
        },
        "weather": {
            "rain": ["The sound of rain against the windows adds a rhythmic backdrop to the hallway."],
            "sunny": ["Sunlight streams through the hallway windows, casting warm glows."],
            "grey": ["The hallway feels somber under the grey sky, the mood subdued."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "pub_01": {
                "neutral": ["From the hallway, the pub's noise is a distant hum."],
                "good": ["The pub’s lively atmosphere energizes the hallway."],
                "bad": ["The pub’s noise distracts from the hallway's quiet."]
            },
            "stage_02": {
                "neutral": ["The backstage connects directly to the hallway, a frequently used path."],
                "good": ["The hallway provides a quiet escape from the bustling backstage."],
                "bad": ["The hallway feels too quiet compared to the lively backstage."]
            }
        }
    }
},
"hallway_02": {
    "default": {
        "approaching": {
            "neutral": ["The hallway continues, lined with more closed doors and dim lighting."],
            "good": ["The hallway feels calm, with soft lighting and a clean, orderly appearance."],
            "bad": ["The hallway appears darker and more ominous, with flickering lights."]
        },
        "at_entity": {
            "neutral": ["You are in the hallway, the quietness enveloping you."],
            "good": ["The hallway provides a peaceful passage, with a serene ambiance."],
            "bad": ["The hallway feels oppressive, the silence heavy and unsettling."]
        },
        "leaving": {
            "neutral": ["You leave the hallway, moving towards brighter areas."],
            "good": ["You step out of the hallway, feeling lighter and refreshed."],
            "bad": ["You hurry out of the hallway, relieved to escape its gloom."]
        },
        "times": {
            "morning": ["The hallway is calm and quiet in the morning light."],
            "afternoon": ["The hallway has a few people passing through, their footsteps echoing softly."],
            "evening": ["The hallway is busier, with more activity and chatter."],
            "night": ["The hallway is empty and quiet, the lights dimmed for the night."]
        },
        "weather": {
            "rain": ["The sound of rain against the windows adds a soothing backdrop."],
            "sunny": ["Sunlight filters through the hallway windows, creating a warm glow."],
            "grey": ["The hallway feels muted under the grey sky, with a subdued atmosphere."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "hallway_01": {
                "neutral": ["The previous hallway leads seamlessly into this one."],
                "good": ["The transition from the previous hallway feels smooth and welcoming."],
                "bad": ["The previous hallway feels even darker as you continue."]
            },
            "hallway_03": {
                "neutral": ["The hallway extends further, leading to another section."],
                "good": ["The next hallway looks brighter and more inviting."],
                "bad": ["The next hallway appears even more foreboding from here."]
            }
        }
    }
},
"hallway_03": {
    "default": {
        "approaching": {
            "neutral": ["The hallway stretches ahead, its length disappearing into the shadows."],
            "good": ["The hallway is well-lit, with a welcoming ambiance."],
            "bad": ["The hallway looks particularly dark and uninviting, with flickering lights."]
        },
        "at_entity": {
            "neutral": ["You are in the hallway, its length filled with closed doors and silence."],
            "good": ["The hallway feels calm and orderly, with soft lighting."],
            "bad": ["The hallway feels confining, the silence heavy and unsettling."]
        },
        "leaving": {
            "neutral": ["You leave the hallway, stepping towards brighter areas."],
            "good": ["You step out of the hallway, feeling more relaxed."],
            "bad": ["You rush out of the hallway, eager to leave its oppressive silence."]
        },
        "times": {
            "morning": ["The hallway is calm and quiet, bathed in morning light."],
            "afternoon": ["The hallway has light traffic, with soft footsteps echoing."],
            "evening": ["The hallway is busier, with more people moving through."],
            "night": ["The hallway is quiet and empty, with the lights dimmed."]
        },
        "weather": {
            "rain": ["The sound of rain against the windows adds a soothing backdrop."],
            "sunny": ["Sunlight filters through the hallway windows, casting a warm glow."],
            "grey": ["The hallway feels subdued under the grey sky, with a muted atmosphere."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "hallway_02": {
                "neutral": ["The previous hallway leads directly into this one."],
                "good": ["The transition from the previous hallway feels smooth and welcoming."],
                "bad": ["The previous hallway feels even darker as you continue."]
            },
            "bertha_office_door_01": {
                "neutral": ["The office door is visible at the end of the hallway."],
                "good": ["The office door looks sturdy and inviting from here."],
                "bad": ["The office door seems ominous, a potential barrier."]
            },
            "backroom_door_01": {
                "neutral": ["The backroom door is visible, a sturdy barrier."],
                "good": ["The backroom door looks solid and secure."],
                "bad": ["The backroom door seems forbidding, a potential obstacle."]
            }
        }
    }
},
"hallway_04": {
    "default": {
        "approaching": {
            "neutral": ["The hallway stretches ahead, its length disappearing into the shadows."],
            "good": ["The hallway is well-lit, with a welcoming ambiance."],
            "bad": ["The hallway looks particularly dark and uninviting, with flickering lights."]
        },
        "at_entity": {
            "neutral": ["You are in the hallway, its length filled with closed doors and silence."],
            "good": ["The hallway feels calm and orderly, with soft lighting."],
            "bad": ["The hallway feels confining, the silence heavy and unsettling."]
        },
        "leaving": {
            "neutral": ["You leave the hallway, stepping towards brighter areas."],
            "good": ["You step out of the hallway, feeling more relaxed."],
            "bad": ["You rush out of the hallway, eager to leave its oppressive silence."]
        },
        "times": {
            "morning": ["The hallway is calm and quiet, bathed in morning light."],
            "afternoon": ["The hallway has light traffic, with soft footsteps echoing."],
            "evening": ["The hallway is busier, with more people moving through."],
            "night": ["The hallway is quiet and empty, with the lights dimmed."]
        },
        "weather": {
            "rain": ["The sound of rain against the windows adds a soothing backdrop."],
            "sunny": ["Sunlight filters through the hallway windows, casting a warm glow."],
            "grey": ["The hallway feels subdued under the grey sky, with a muted atmosphere."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "hallway_02": {
                "neutral": ["The previous hallway leads directly into this one."],
                "good": ["The transition from the previous hallway feels smooth and welcoming."],
                "bad": ["The previous hallway feels even darker as you continue."]
            },
            "bertha_office_door_01": {
                "neutral": ["The office door is visible at the end of the hallway."],
                "good": ["The office door looks sturdy and inviting from here."],
                "bad": ["The office door seems ominous, a potential barrier."]
            },
            "backroom_door_01": {
                "neutral": ["The backroom door is visible, a sturdy barrier."],
                "good": ["The backroom door looks solid and secure."],
                "bad": ["The backroom door seems forbidding, a potential obstacle."]
            }
        }
    }
},
"bertha_office_01": {
    "default": {
        "approaching": {
            "neutral": ["The office door is just ahead, its surface unmarked and plain."],
            "good": ["The office door looks inviting, promising privacy and quiet."],
            "bad": ["The office door appears imposing, a barrier to whatever lies within."]
        },
        "at_entity": {
            "neutral": ["You are at the office door, its handle within reach."],
            "good": ["The office door opens smoothly, revealing a well-kept space."],
            "bad": ["The office door creaks as it opens, revealing a dimly lit room."]
        },
        "leaving": {
            "neutral": ["You leave the office, the door closing softly behind you."],
            "good": ["You step out of the office, feeling more focused."],
            "bad": ["You exit the office, eager to leave its confining space."]
        },
        "times": {
            "morning": ["The office is bathed in soft morning light, calm and quiet."],
            "afternoon": ["The office is bright and orderly, ready for the day's work."],
            "evening": ["The office is dimly lit, the day's work winding down."],
            "night": ["The office is dark and quiet, the day's work long finished."]
        },
        "weather": {
            "rain": ["The sound of rain outside adds a soothing backdrop to the office's quiet."],
            "sunny": ["Sunlight streams into the office, creating a warm, inviting atmosphere."],
            "grey": ["The office feels somber under the grey sky, the mood subdued."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "bertha_office_door_01": {
                "neutral": ["The office door leads back into the hallway."],
                "good": ["The hallway looks calm and orderly from the office."],
                "bad": ["The hallway appears dark and foreboding from the office."]
            }
        }
    }
},
"backroom_01": {
    "default": {
        "approaching": {
            "neutral": ["The backroom door is ahead, sturdy and unmarked."],
            "good": ["The backroom door looks solid, promising security and privacy."],
            "bad": ["The backroom door appears daunting, a potential obstacle."]
        },
        "at_entity": {
            "neutral": ["You are at the backroom "],
            "good": ["The backroom door opens smoothly, revealing a well-organized space."],
            "bad": ["The backroom door creaks as it opens, revealing a dimly lit room."]
        },
        "leaving": {
            "neutral": ["You leave the backroom, the door closing softly behind you."],
            "good": ["You step out of the backroom, feeling more focused."],
            "bad": ["You exit the backroom, eager to leave its confining space."]
        },
        "times": {
            "morning": ["The backroom is bathed in soft morning light, calm and quiet."],
            "afternoon": ["The backroom is bright and orderly, ready for the day's work."],
            "evening": ["The backroom is dimly lit, the day's work winding down."],
            "night": ["The backroom is dark and quiet, the day's work long finished."]
        },
        "weather": {
            "rain": ["The sound of rain outside adds a soothing backdrop to the backroom's quiet."],
            "sunny": ["Sunlight streams into the backroom, creating a warm, inviting atmosphere."],
            "grey": ["The backroom feels somber under the grey sky, the mood subdued."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "backroom_door_01": {
                "neutral": ["The backroom door leads back into the hallway."],
                "good": ["The hallway looks calm and orderly from the backroom."],
                "bad": ["The hallway appears dark and foreboding from the backroom."]
            }
        }
    }
},
"backroom_door_01": {
    "default": {
        "approaching": {
            "neutral": ["The iron door stands solid and imposing, a barrier to the backroom."],
            "good": ["The iron door looks sturdy and secure, protecting whatever lies beyond."],
            "bad": ["The iron door appears forbidding, a heavy obstacle in your path."]
        },

        "leaving": {
            "neutral": ["You leave the iron door, the backroom hidden once more."],
            "good": ["You step away from the iron door, feeling more secure."],
            "bad": ["You retreat from the iron door, relieved to be away from its oppressive presence."]
        },
        "times": {
            "morning": ["The iron door gleams slightly in the morning light."],
            "afternoon": ["The iron door stands firm, unchanged by the passing day."],
            "evening": ["The iron door casts long shadows in the fading light."],
            "night": ["The iron door blends into the darkness, almost invisible."]
        },
        "weather": {
            "rain": ["Raindrops streak the iron door, their sound absorbed by the heavy metal."],
            "sunny": ["The iron door glints under the bright sun, its surface reflecting the light."],
            "grey": ["The iron door looks dull under the grey sky, its presence somber."]
        },
        "tags": ["urban", "indoors"],
        "connections": {
            "hallway_04": {
                "neutral": ["From the hallway, the iron door looks impenetrable."],
                "good": ["The iron door seems less daunting from the safety of the hallway."],
                "bad": ["The iron door looms menacingly at the end of the hallway."]
            }
        }
    }
},
"bertha_office_door_01": {
    "default": {
        "approaching": ["approaching office door"],
        "connections": {
            "hallway_04": {
                "neutral": ["From the hallway, the office."],
                "good": ["The office door seems less daunting from the safety of the hallway."],
                "bad": ["The office door looms menacingly at the end of the hallway."]
                }
            },
        }
    }
}






