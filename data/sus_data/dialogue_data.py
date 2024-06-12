
dialogue_player_options = {
    "default_1": {
        "chat": "with {name} about {topic}",
        "grill": "{name} about {topic}",
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
                }
            },
            #additional states as needed
        },
        "conditional": [ #witness statements
            {
                "conditions": ["gibbs"], #murderer traits here
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "clueid_chat": {
                        "says": ["test: gibbs is murderer, bertha talking"],
                        "effects": {},
                        "options": "default_1"
                    }
                }
            },
            {
                "conditions": ["knife"],
                "dialogue": {
                    "murder_chat": {
                        "says": ["murderer traits has knife"],
                        "effects": {},
                        "options": "default_1"
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
                "conditions": ["bertha"], #murderer traits here
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "clueid_chat": {
                        "says": ["test: bertha is murderer, gibbs talking"],
                        "effects": {},
                        "options": "default_1"
                    }
                }
            },
            {
                "conditions": ["gun"],
                "dialogue": {
                    "murder_chat": {
                        "says": ["murderer traits has gun"],
                        "effects": {},
                        "options": "default_1"
                    }
                }
            }
        ]
    }
}