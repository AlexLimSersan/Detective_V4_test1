
dialogue_player_options = {
    "default_1": {
        "chat": "about {topic}",
        "grill": "about {topic}",
        "change": "topic...",
        "return": "leave conversation..."
    }
}

sus_dialogue_data = {
    "bertha_01": {
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
                },
                "whiskey_01_chat_neutral": {
                    "says": ["ugh I hate whiskey.",],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["only thing that might be helpful is that I served a bunch at the bar last night. I think I poured some for Phil, Gibbs, and the Butcher..",],
                    "effects": {},
                    "options": None
                },
                #additional states as needed
            },
        },
    "conditional": [ #witness statements
            {
                "conditions": {"traits":["gibbs"]}, #murderer traits here; has to be like this to follow check condition format for items - possible other conditions?
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "gibbs_01_chat_neutral": {
                            "says": ["test: gibbs is murderer, bertha talking"],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            },
            {
                "conditions": {"traits":["bertha"]},
                "dialogue": {
                    "default": {
                        "bertha_01_chat_neutral": {
                            "says": ["murderer traits has bertha"],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            }
        ]
    },
    "gibbs_01": {
        "non_topic": {
            "default": {
                "greet_good": {
                    "says": ["Hey there, detective! Feeling lucky today?"],
                    "options":  "default_1"
                },
                "greet_bad": {
                    "says": ["Oh, it's you. What do you want?"],
                    "options": "default_1"
                },
                "redirect_good": {
                    "says": ["So, what were we talking about?"],
                    "effects": {},
                    "options": "default_1"
                },
                "redirect_bad": {
                    "says": ["Can we get this over with?"],
                    "effects": {"mood": -1},
                    "options": "default_1"
                },
                "bye_good": {
                    "says": ["Goodbye, detective. Try your luck next time!"],
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
                    "says": ["I don't really know about that.", "Maybe ask someone else?"],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["I'm telling you, I know nothing.", "You're wasting your time."],
                    "effects": {},
                    "options": None
                }
            },
            #additional states as needed
        },
        "conditional": [ #witness statements
            {
                "conditions": {"traits":["bertha"]}, #murderer traits here
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "bertha_01_chat_neutral": {
                            "says": ["test: bertha is murderer, gibbs talking"],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            },
            {
                "conditions": {"traits":["gibbs"]},
                "dialogue": {
                    "default": {
                        "gibbs_01_chat_neutral": {
                            "says": ["murderer traits has gibbs"],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            }
        ]
    }
}