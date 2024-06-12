


#for witness dialogue, can group like:
#LOADING DIALOGUE BASED ON MURDER PROFILE! SO DIALOGUE CONDITIONS? LIKE CLUE_CHAT: CONDITION: SMOKE TYPE, ACCESS TO, PHIL MURDERER, ETC


location_data_template = {
    "loc_01": {
        "name": "Cab",
        "connections": ["alley_01", "pub_01", "butcher_01", "docks_01", "morgue_01"],
        "is_outdoors": True,
    },
    "loc_02": {
        "name": "Pub",
        "connections": [],
        "is_outdoors": False
    }
}

sus_template = {
    "bertha_01": {
        "name": "bertha",
        "profile": {

        },
        "routine": { #routine management here
            "default": { #can have different states
                "morning": "porche",
                "else": "bar" #ids!
            }
        }
    }
}

murderer_profile_all_possibilities = {
            "murderer": ["bertha", "gibbs", "phil","bob","maxwell"],
            "weapon_type": ["knife", "gun"],
            "fight_type": ["strong", "weak"],
            "outfit_type": ["leather", "denim"],
            "smoke_type": ["cigs", "tobacco", "none"],
            #maybe at bar just for dialogue and story
            "match_type": ["new_matches", "old_matches", "none"],
            "drink_type": ["whiskey", "rum", "none"],
            "hair_type": ["hair", "bald"],
            "shoe_type": ["shoes", "boots"],
        }



loc_description_data = {
    #id
    "loc_01": {
        #state
        "default": {
            #type of description
            "approaching": {
                "neutral": ["", []], #descriptions chooses a random iterable from the outer list. you can have nested lists for phrasing purposes, as it changes print speed.
#can also have optional good or bad descriptions,
                },
            "at_entity": {
                "neutral": [""],
                },
            "leaving": {
                "neutral": [""],
                },
            "times": { #for any routine type descriptions
                "morning": {
                    "neutral": [""],
                },
                "afternoon": {
                    "neutral": [""],
                },
                "evening": {
                    "neutral": [""],
                },
                "night": {
                    "neutral": [""],
                },
            },
            "weather": { #optional weather descriptions for rain, sunny, or grey.
                "rain": {
                    "neutral": [""],
                },
                "sunny": {
                    "neutral": [""],
                },
                "grey": {
                    "neutral": [""],
                },
            },
            "tags": [], #CHOOSE FROM: waterfront, urban, indoors (for if you can detect the weather from the indoors)
            "connections": {
                #connection descriptions work like this:
                #the actual connection location object returns a description (below) for the id that is requesting the description.
                #example: player in bar, gets connection description from hallway. hallway returns connection description for the bar.
                #ALLOWS STATE DESCRIPTIONS DEPENDENT ON THE ACTUAL CONNECTION YOU ARE GETTING THE DESC, NOT YOUR CURRENT LOCATION!
                "connection_id_1": {
                    "neutral": [""],
                },
                "connection_id_2": {
                    "neutral": [""],
                }
            }
        },
        #more states/events as needed here
    },
    #new entities starts here
}

#mobile just add at_scene
loc_description_template = {
    "entity_id": {
        "default": {
            "approaching": {

            },
            "at_entity": {

            },
            "leaving": {

            },
            "times": {
                "morning": ["The sun is rising."],
                "afternoon": ["The sun is high in the sky."],
                "evening": ["The sun is setting."],
                "night": ["The stars are out."]
            },
            "weather": {
                "rain": ["It's raining heavily."],
                "sunny": ["The sun is shining brightly."]
            },
            "tags": {},
            "connections": {
                "connection_id_1": {
                    "neutral": ["There is a path leading to the north."],
                    "good": ["A well-trodden path leads to the north."],
                    "bad": ["A narrow, overgrown path leads to the north."]
                },
                "connection_id_2": {
                    "neutral": ["A door to the east."],
                    "good": ["An inviting door to the east."],
                    "bad": ["A creaky door to the east."]
                }
            }
        },
        #more states/events as needed here
    },
    #new entities starts here
}


mobile_description_template = {
    #id
    "loc_01": {
        #state
        "default": {
            #type of description
            "approaching": {
                "neutral": ["", []], #descriptions chooses a random iterable from the outer list. you can have nested lists for phrasing purposes, as it changes print speed.
#can also have optional good or bad descriptions,
                },
            "at_entity": {
                "neutral": [""],
                },
            "leaving": {
                "neutral": [""],
                },
            "times": { #for any routine type descriptions
                "morning": {
                    "neutral": [""],
                },
                "afternoon": {
                    "neutral": [""],
                },
                "evening": {
                    "neutral": [""],
                },
                "night": {
                    "neutral": [""],
                },
            },
            "weather": { #optional weather descriptions for rain, sunny, or grey.
                "rain": {
                    "neutral": [""],
                },
                "sunny": {
                    "neutral": [""],
                },
                "grey": {
                    "neutral": [""],
                },
            },
            "tags": [], #CHOOSE FROM: waterfront, urban, indoors (for if you can detect the weather from the indoors)
            "connections": {
                #connection descriptions work like this:
                #the actual connection location object returns a description (below) for the id that is requesting the description.
                #example: player in bar, gets connection description from hallway. hallway returns connection description for the bar.
                #ALLOWS STATE DESCRIPTIONS DEPENDENT ON THE ACTUAL CONNECTION YOU ARE GETTING THE DESC, NOT YOUR CURRENT LOCATION!
                "connection_id_1": {
                    "neutral": [""],
                },
                "connection_id_2": {
                    "neutral": [""],
                }
            }
        },
        #more states/events as needed here
    },
    #new entities starts here
}


dialogue_template = {
    "suspect_id": {
        "non_topic": {
            "default": {
                "greet_good": {
                    "says": ["Hello, detective! What a pleasant surprise."],
                    "options":  "default_1"
                },
                "greet_bad": {
                    "says": ["Oh, it's you again. What do you want?"],
                    "options": "default_1"
                },
                "redirect_good": {
                    "says": ["So, where were we?"],
                    "effects": {},
                    "options": "default_1"
                },
                "redirect_bad": {
                    "says": ["Let's get this over with."],
                    "effects": {"mood": -1},
                    "options": "default_1"
                },
                "bye_good": {
                    "says": ["Goodbye, detective. Take care."],
                },
                "bye_bad": {
                    "says": ["Finally, you're leaving."],
                }
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                "unknown_chat_neutral": {
                    "says": ["I don't know much about that.", "Can you ask something else?"],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["I really don't know anything.", "You're barking up the wrong tree."],
                    "effects": {},
                    "options": None
                }
            },
            #additional states as needed
        },
        "conditional": [
            {
                "conditions": {"smoke_type": "cigarette", "access_to": "bar"},
                "dialogue": {
                    "clue_chat": {
                        "says": ["I saw someone smoking a cigarette near the bar."],
                        "effects": {},
                        "options": "default_1"
                    }
                }
            },
            {
                "conditions": {"suspect": "Phil", "murderer": True},
                "dialogue": {
                    "murder_chat": {
                        "says": ["I saw Phil acting suspiciously that night."],
                        "effects": {},
                        "options": "default_1"
                    }
                }
            }
        ]
    }
}
