
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
                "greet_neutral": {
                    "says": ['"What can I do for ya?"', "'Howdy, need anything?'"],
                    "options":  "default_1"
                },
                "greet_bad": {
                    "says": ["Oh, it's you again. What do you want?"],
                    "options": "default_1"
                },
                "redirect_good": {
                    "says": ["So, where were we?", "Well then...", "Need anything?"],
                    "effects": {},
                    "options": "default_1"
                },
                "redirect_bad": {
                    "says": ["Let's get this over with.", "What now?", "Anything else?", "She looks annoyed."],
                    "effects": {},
                    "options": "default_1"
                },
                "bye_good": {
                    "says": ["See ya.", '"Have a good one"'],
                },
                "bye_bad": {
                    "says": ["Finally, you're leaving."],
                }
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                #REACTIONS
                "react_chat_neutral": {
                    "says": ["A beat passes before she responds.", "'Uhhhmm...'", "She shrugs.",
                             "She exhales, pausing for a second.",
                             "'Oh, {topic}? I mean...", "Oh, that?", "I mean...",
                             ],
                },
                "react_grill_neutral": {
                    "says": ['Her eyes furrow.', "She takes a deep breath, calming herself.",
                             "Her eyes flash in annoyance.",
                             "Her shoulders tense..", "She pauses for a moment before answering.",
                             "Could you lay off me?"],
                    "effects": {"mood": -1},
                },
                #
                "again_chat_neutral": { #still responds, but warns player they already asked
                    "says": ['"Again?.."',"I already told you...", "How many times do I have to say it?..",
                             "For the last time,","Alright, I'll repeat myself...","Okay, listen up because I dont want to repeat it again.",
                             "Pay attention so you dont keep pestering me..."],
                    "effects": {"mood": -1},
                },
                "again_grill_neutral": { #still responds, but warns player they already asked
                    "says": ['"Again?.."',"I already told you...", "How many times do I have to say it?..",
                             "For the last time,","Alright, I'll repeat myself...","Okay, listen up because I dont want to repeat it again.",
                             "Pay attention so you dont keep pestering me..."],
                    "effects": {"mood": -1},
                },
                #just talked: if topic is most recent;  respond if count = 1 else no
                "just_talked_chat_neutral": {
                    "says": ['...\n"You literally JUST brought that up..?"',"You really wanna keep talking about {topic}?",
                             "We just talked about this...","Can't we change the subject for a bit?","You really are fixated on {topic}, huh?"],
                    "effects": {"mood": -1},
                },
                "just_talked_grill_neutral": {
                    "says": ['...\n"You JUST brought that up..','We just talked about that, whats the matter with you?"',"You really want to keep grilling me about {topic}?",
                             "Annoy me more with {topic}, why not...","{topic} again? Really?...", "Keep asking about that, why don't you..." ],
                    "effects": {"mood": -1},
                },
                # already_talked: if topic in history, wont respond
                "already_talked_chat_neutral": {
                    "says": ['"Again? Lets chat maybe another time, okay?"',"Dude, we talked about that this {current_phase}, remember?", "{topic} again?.. How about something else?",
                             "Don't you want to talk about something else this {topic}?"],
                    "effects": {"mood": -1},
                },
                "already_talked_grill_neutral": {
                    "says": ['... "Please relax, you already brought that up, remember?"',"You already pressed me about that this {current_phase}!",
                             "Nothing's change since you last questioned me, move on.","What are you hoping changed since you last questioned me?"],
                    "effects": {"mood": -1},
                },
                "already_talked_chat_bad": {
                    "says": ['"Look, you\'re starting to annoy me with your badgering..."',"Honestly, you are really irritating me.. {topic} again?",
                             "You really want to chat about {topic} all {current_phase}, huh?", "Nag me some more, why don't you...", "What do you think's changed since our last conversation?",],
                    "effects": {"mood": -1},
                },
                "already_talked_grill_bad": {
                    "says": ['"You are pissing me off with your repetitive questioning..."',"How many times do you want to interrogate me about {topic}?",
                             "You really are going to ask about {topic} all {current_phase}?", "Grill me more, why don't you..."],
                    "effects": {"mood": -1},
                },
                #unknown
                "unknown_chat_neutral": {
                    "says": ["She shrugs. What do you wanna know about {topic}?", "... Don't know much about that.", "I'm afraid I can't help much with that...",
                             "I mean.. It's {topic}", "What can I say? It's {topic}.", "Afraid I can't help you much with that."],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["Lay off me, would you? I told you I don't know anything.", "Honestly, relax. I dont' know anything.", "Could you lay off me?",
                             "I really don't know much about {topic}."],
                    "effects": {},
                    "options": None
                },
                #START OF ACTUAL TOPICS! LOL

                "kitchen_knife_01_chat_neutral": {
                    "says": ["Yeah, we got plenty of those... We use them.. to cook...", "It's a kitchen knife. Anything specific you want to know?",
                             "I've done my fair share of cooking with those..."],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_grill_neutral": {
                    "says": ["'A kitchen knife - I mean, we need those to cook...'","Wouldnt be much of a food place without that.",
                             "'I guess anyone with kitchen access could grab one?"],
                    "effects": {},
                    "options": None
                },
                "revolver_01_chat_neutral": {
                    "says": ["'Dude, you really opened my desk drawer? Could you not?" ],
                    "effects": {},
                    "options": None
                },
                "revolver_01_grill_neutral": {
                    "says": ["'Look, get out of my face man. It's my personal stuff!'", ],
                    "effects": {},
                    "options": None
                },

                "hair_01_chat_neutral": {
                    "says": ["'I mean... '\n She plays with her nearly identical looking hair. \n 'There's lots of people that could be, right?'", ],
                    "effects": {},
                    "options": None
                },
                "hair_01_grill_neutral": {
                    "says": ["'Look, it's hair man. What do you want me to say?'\n ", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_chat_neutral": {
                    "says": ["Im the bartender here, born and raised - I inherited the pub.", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_grill_neutral": {
                    "says": ["I'm just a girl who works here, ok?", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_chat_neutral": {
                    "says": ["A smirk forms across her lips. \n 'Yeah, I know Gibbs, guy gambles... a lot.","\n Bad money management - anything specific you want to know?'\n ", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_grill_neutral": {
                    "says": ["She looks annoyed.\n 'Gibbs, hes just some bald gambler, now take your questions elsewhere.", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_chat_neutral": {
                    "says": ["'Honestly, haven't seen him here in ages.'","'He weirds me out a little. A long time ago, he used to come here for our red wine, back when it was that fruitier brand.","Man's a hermit, don't see him much, maybe occasionally on late night walks. ", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["Dude, could you relax? He's the guy that deals with our dead people.","He's the mortician, satisfied?", ],
                    "effects": {},
                    "options": None
                },
                "bertha_footwear_01_chat_neutral": {
                    "says": ["'Yeah, I've got everything but dress shoes, if you must know.'"],
                    "effects": {},
                    "options": None
                },
                "bertha_footwear_01_grill_neutral": {
                    "says": ["She rolls her eyes. \n'I have sneakers, and boots. What do you want?'" ],
                    "effects": {},
                    "options": None
                },
                "bertha_clothes_01_chat_neutral": {
                    "says": ["Yes, those are mine.. But could you not go through my stuff?", "Yeahhh... Those are mine. Thanks for snooping around."],
                    "effects": {},
                    "options": None
                },
                "bertha_clothes_01_grill_neutral": {
                    "says": ["'Yes Detective, those are my jackets.'\nShe shakes her denim sleeves. 'Just like this one'" ],
                    "effects": {},
                    "options": None
                },
                "matches_01_chat_neutral": {
                    "says": ['"Those just came in yesterday. You can grab one if you\'d like, but only if you need it please."'],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_neutral": {
                    "says": ["'Detective, those are matches that came in yesterday, everyone is welcome to grab one. New logo, see? She pulls it out to show you. Satisfied?!?" ],
                    "effects": {},
                    "options": None
                },
                "matches_02_chat_neutral": {
                    "says": ['"Ughhh, hate the look of those."'],
                    "effects": {},
                    "options": None
                },
                "cigs_01_chat_neutral": {
                    "says": ["Don't mind if I do actually. She pulls out a smoke.","It's a pretty common brand.",],
                    "effects": {},
                    "options": None
                },
                "cigs_01_grill_neutral": {
                    "says": ["She chuckles. 'Don't sweat me over a cigarette dude. Everyone smokes these here.'",],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_chat_neutral": {
                    "says": ["'It's real fresh stuff. Grows locally, burns really slow.'", "It's super nice actually."],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_grill_neutral": {
                    "says": ["'Dude. Everyone who isn't a loser here smokes this stuff.'",],
                    "effects": {},
                    "options": None
                },
                "tomato_01_chat_neutral": {
                    "says": ["'Delicious, can't imagine someone not liking this.'", "I eat the stuff almost every day."],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["She looks at you.\n \"Really? What do you wan't me to say?\"",],
                    "effects": {},
                    "options": None
                },
                "mustard_01_chat_neutral": {
                    "says": ["Oh yeah mustard... I mean, what about it?", "Eh, I could do without it"],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": ["Hate mustard. Satisfied?",],
                    "effects": {},
                    "options": None
                },
                "grease_01_chat_neutral": {
                    "says": ["Good stuff, love me some greasy food."],
                    "effects": {},
                    "options": None
                },
                "grease_01_grill_neutral": {
                    "says": ["Dude, who doesn't like greasy food?",],
                    "effects": {},
                    "options": None
                },
                "pie_01_chat_neutral": {
                    "says": ["Ah, blueberry pie. Best dish we serve, to be honest."],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_neutral": {
                    "says": ["It's pie. Get a life.",],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_chat_neutral": {
                    "says": ["Super refreshing flavor. Care for one?"],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_grill_neutral": {
                    "says": ["Look, Gibbs likes it too okay!",],
                    "effects": {},
                    "options": None
                },
                "red_wine_01_chat_neutral": {
                    "says": ["Nice, rich, and fruity."],
                    "effects": {},
                    "options": None
                },
                "red_wine_01_grill_neutral": {
                    "says": ["Look, I drink red wine! So what?",],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_chat_neutral": {
                    "says": ["Ughh, I can't stand the smell of that stuff...",],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["Only thing that might help is that most of the guys here like it...",],
                    "effects": {},
                    "options": None
                },
                "rum_01_chat_neutral": {
                    "says": ["That is our specialty, best rum I've tasted honestly.",],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["Could you lay off me? Everyone here drinks rum.",],
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
                            "says": ["He always slightly scared me... Real troubled guy...", "If I were you, I'd stay away from him.","He drinks far too much for his own good."],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            },
        ]
    },
    "gibbs_01": {
        "non_topic": {
            "default": {
                "greet_neutral": {
                    "says": ['"Evening, my good sir."', "'To what do I owe the pleasure of your company?'"],
                    "options":  "default_1"
                },
                "greet_bad": {
                    "says": ["'I did it! I confess! \n...\nJoking, idiot!'"],
                    "options": "default_1"
                },
                "redirect_good": {
                    "says": ["He readjust his fedora, and clears his throat.", "He takes a swig from his flask, whiskey dribbling down his face.", "He wipes his mouth with his sleeve."],
                    "effects": {},
                    "options": "default_1"
                },
                "bye_good": {
                    "says": ["Adios, my amigos! Until we meet again!", '"Farewell, our knight in shining armor!"\nHis voice drips with sarcasm.'],
                },
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                #REACTIONS
                "react_chat_neutral": {
                    "says": ["He cracks his knuckles.", "'Oh yes, {topic}...'", "Ah, {topic} - ",
                             "Well, if I may - ",
                             "'Excellent topic my good sir.'", "{topic}? well you see...", "Uhh.",
                             ],
                },
                "react_grill_neutral": {
                    "says": ['His eyes narrow.', "His face is unreadable.",
                             "Ahh, excellent line of questioning -",
                             "My good sir, I have just the piece of information you need -", "For a fleeting moment, rage sweeps across his face.",
                             "Ah, {topic}, yes yes indeed - "],
                    "effects": {"mood": -1},
                },
                #
                "again_chat_neutral": { #still responds, but warns player they already asked
                    "says": ['"That again?.."',"Have I not told you?", "Why beat a dead horse, you knawsayinn?\nHe makes some bizarre gesture with his arms.",
                             "If you really must know about {topic} - ","He seems confused.","I shall repeat myself...",
                             "Must we discuss this more?"],
                    "effects": {"mood": -1},
                },
                #just talked: if topic is most recent;  respond if count = 1 else no
                "just_talked_chat_neutral": {
                    "says": ['...\n"You just brought that up.. no?"',"We just talked about that!", "Why that again?",
                             "Again?.. why?","It's kind of boring to talk about the same thing so often, no?","Why the obsession with {topic}?"],
                    "effects": {"mood": -1},
                },
                "just_talked_grill_neutral": {
                    "says": ['...\n"Why must you inquire again about {topic}','I have no further information for you, sire.',"Do you think something changed since.. half a second?",
                             "Why must you ask me again about such a thing?","{topic} again? Really?...", "Will you ask about that all {current_phase}?" ],
                    "effects": {"mood": -1},
                },
                # already_talked: if topic in history, wont respond
                "already_talked_chat_neutral": {
                    "says": ['"Perhaps we continue this conversation another time?"',"Have we not discussed that this {current_phase}?",
                             "{topic}? Could you not give it some rest?",
                             "I would rather we discuss another topic..."],
                    "effects": {"mood": -1},
                },
                "already_talked_grill_neutral": {
                    "says": ['... "You already asked me questions about that...?"',"Have we not already discussed that this {current_phase}?",
                             "Nothing's changed, my answer would be the same...","That same line of questioning?"],
                    "effects": {"mood": -1},
                },
                "already_talked_chat_bad": {
                    "says": ['"How about you go bother Bertha."',"Please, you are a very poor conversational partner. It's like a dance you know.. And you need practice, talking about {topic} all {current_phase}...",
                             "I politely decline this subject of conversation due to it being... BORING!", "Quite the bother, aren't you.", "What do you think's changed? Hint - nothing!",],
                    "effects": {"mood": -1},
                },
                "already_talked_grill_bad": {
                    "says": ['Rage flashes in his face, his knuckles whitening before he controls himself.\nDont bother me with that again.',"How many times do you want to interrogate me about {topic}?",
                             "Must you bug me all {current_phase} with your questions?", "Have you thought of... not being a dick?"],
                    "effects": {"mood": -1},
                },
                #unknown
                "unknown_chat_neutral": {
                    "says": ["Tell me more, I care so much.","Cool! What other topic ideas do you have?\nHe looks at you, making a funny face."],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["Oh, yes, {topic}! You are doing great work here, detective.","Groundbreaking idea - case solved with {topic}! He gives you a look before returning to his activities."],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_chat_neutral": {
                    "says": ["'Ah yes, I snuck into the kitchen, took one, and stabbed Debbie repeatedly! Case solved!!!\nHe looks at you sarcastically." ],
                    "effects": {},
                    "options": None
                },
                "revolver_01_chat_neutral": {
                    "says": ["'Whoa, I never knew that was there. Interesting...'", ],
                    "effects": {},
                    "options": None
                },

                "hair_01_chat_neutral": {
                    "says": ["'Oh yes, my favorite.\n He tightens his fedora onto his head. You don't see a shred of hair coming out the sides.'", ],
                    "effects": {},
                    "options": None
                },
                "hair_01_grill_neutral": {
                    "says": ["'Let me save you some trouble. Everyone has hair here!'", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_chat_neutral": {
                    "says": ["A curious girl, known for her amazing ability to pour me a drink.", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_grill_neutral": {
                    "says": ["'Stupid girl, always meddling with the wrong people.'\n He looks around nervously.\n'Dont tell her I said that'", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_chat_neutral": {
                    "says": ["'Ah, the finest man in this town.' \nHe gestures around.\n'The most winningest of the winners in the history of winning!'", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_grill_neutral": {
                    "says": ["He stares at you blankly.\n'Never heard of him.'", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_chat_neutral": {
                    "says": ["'That fool, he bit my style. He tugs on his suit. Cashmere, baby.", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["He looks at you, suddenly serious.\n"
                             "'Detective, I swear I see him out late at night, prowling the cemetery. "
                             "I think he might be...\nHe swallows.\n'EATING PEOPLE!' "
                             "He shivers dramatically, his face sincere.", ],
                    "effects": {},
                    "options": None
                },
                "bertha_footwear_01_chat_neutral": {
                    "says": ["'Dude, isnt that in Berthas personal closet?..\nYou snooping around girls feet?'"],
                    "effects": {},
                    "options": None
                },
                "bertha_footwear_01_grill_neutral": {
                    "says": ["'Truthfully, I dont care if you look at her stuff. "
                             "But I can safely say you will never catch me in those ugly workboots she has.'" ],
                    "effects": {},
                    "options": None
                },
                "bertha_clothes_01_chat_neutral": {
                    "says": ["You really are nosy aren't you?", "Gunna look through her ledger, too?\nHe seems to regret saying that."],
                    "effects": {},
                    "options": None
                },
                "bertha_clothes_01_grill_neutral": {
                    "says": ['"Well done, marvellous deduction! Ask me more about Bertha\'s personal attire."' ],
                    "effects": {},
                    "options": None
                },
                "matches_01_chat_neutral": {
                    "says": ['"Amazing... Very nice..."',"Look at the off black coloring...The subtle thickness of it..","My god, it even has the logo engraved. "],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_neutral": {
                    "says": ["Detective, the rules of the establishment are such that you can only take one of those, and ONLY if you need it.\nHe looks at you, stern." ],
                    "effects": {},
                    "options": None
                },
                "matches_02_chat_neutral": {
                    "says": ['"I may or may not have a few of those. \nHe laughs, suddenly fanning out 5 in some sort of magic trick, before making them vanish."'],
                    "effects": {},
                    "options": None
                },
                "matches_02_grill_neutral": {
                    "says": ['"Those old things? Please good sir, they are a thing of the past, hence why I grabbed so many of those new ones.\nHe suddenly fans out 5 new matchess in some sort of magic trick, before making them vanish."'],
                    "effects": {},
                    "options": None
                },
                "cigs_01_chat_neutral": {
                    "says": ["Suddenly, he starts double fisting cigarettes, creating enormous quantities of smoke.\n'Sorry, couldnt hear you!'",],
                    "effects": {},
                    "options": None
                },
                "cigs_01_grill_neutral": {
                    "says": ["He eats a cigarette, staring you dead in the eye. \n'\"Ever see that done before? New trick I'm working on\"",],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_chat_neutral": {
                    "says": ["'That stuff is for snobs.'\nHe tips his fedora."],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_grill_neutral": {
                    "says": ["'I never, ever, have ONCE, touched that mockery of a tobacco leaf in my life.'",],
                    "effects": {},
                    "options": None
                },
                "tomato_01_chat_neutral": {
                    "says": ["'Ah, lovely.' \nHis eyes suddenly grow distant, reminiscing on something."],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["Sir, you're going to embarass yourself... Everyone eats tomatoes around here.",],
                    "effects": {},
                    "options": None
                },
                "mustard_01_chat_neutral": {
                    "says": ["mmmMMMMMmmm. MUSTARD IS AMAZING!!!! \nHe gets strangely excited."],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": ["Hey now, dont go around angrily asking about stuff like that. You dont want to get hurt now, do you?",],
                    "effects": {},
                    "options": None
                },
                "grease_01_chat_neutral": {
                    "says": ["'No thanks. It makes my tummy grumbly.'"],
                    "effects": {},
                    "options": None
                },
                "grease_01_grill_neutral": {
                    "says": ["'No!' he says forcefully. 'Im serious about my health when it comes to eating.'",],
                    "effects": {},
                    "options": None
                },
                "pie_01_chat_neutral": {
                    "says": ["Wont catch me eating something that sugary, like ever. Thats really bad for you, you know."],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_neutral": {
                    "says": ["He squirms in place. \n'Bertha likes pie!' He blurts.",],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_chat_neutral": {
                    "says": ["omg!?!? GIRLLSS NIGHT!!!\n'I mean.' He looks at you deadpan. 'What am I, some sort of sissy?'"],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_grill_neutral": {
                    "says": ["'A drink only a girl would drink! Am I right?' \nHe looks around, his face seems... sad.",],
                    "effects": {},
                    "options": None
                },
                "red_wine_01_chat_neutral": {
                    "says": ["He retches. DISGUSTING! Bring it up again, I might puke."],
                    "effects": {},
                    "options": None
                },
                "red_wine_01_grill_neutral": {
                    "says": ["I believe, to the best of my knowlege... \n..\n"
                             "Bertha and the Mortician both drink red wine, "
                             "albeit at different times.\n "
                             "You see, the Mortician drinks it along with human blood."
                             "\nHe looks you in the eye.\n I'm serious now, detective. He does. And Bertha.... "
                             "Well she used to drink it with the Mortician, "
                             "way back when the brand here was a thicker, fruitier flavor, "
                             "they used to ferment in smoked oak, I believe.\n "
                             "Regardless, Bertha drinks it by herself, normally when business is slow.\n"
                             "Although, there has been exceptions, like that time I won over $63,000 in one hand.\n"
                             "Care to hear that story?",],
                    "effects": {},
                    "options": "gibbs_red_wine_01_grill_neutral"
                },
                "whiskey_01_chat_neutral": {
                    "says": ["Nice, a man's drink. Now were talking.",],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["Sir, respectfully, change your tone.",],
                    "effects": {},
                    "options": None
                },
                "rum_01_chat_neutral": {
                    "says": ["Ah, the most nicest drink of them all.",],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["Look my good sir. The rum here is excellent. Now buzz off.",],
                    "effects": {},
                    "options": None
                },
                #additional states as needed
            },
        },
        "conditional": [ #witness statements
            {
                "conditions": {"traits":["bertha"]}, #murderer traits here; has to be like this to follow check condition format for items - possible other conditions?
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "bertha_01_chat_neutral": {
                            "says": ["I heard her and Debbie yesterday get into some sort of curfuffle. I dont know the details.", "I think there was yelling from her and Debbie yesterday..."],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            },
        ]
    },
    "mortician_01": {
        "non_topic": {
            "default": {
                "greet_neutral": {
                    "says": ['"Hello..."', "'Yes?'"],
                    "options": "default_1"
                },
                "greet_bad": {
                    "says": ["'And now?..'","Hello, you..."],
                    "options": "default_1"
                },
                "redirect_neutral": {
                    "says": ["He clears his throat."],
                    "effects": {},
                    "options": "default_1"
                },
                "bye_good": {
                    "says": ["Goodbye..."],
                },
                "bye_bad": {
                    "says": ["Finally..."],
                },
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                #REACTIONS
                "react_chat_neutral": {
                    "says": ["He looks at you, blankly.", "'Oh yes... {topic}...'", "Hmmm, {topic}..  ",
                             "Ah yes. ",
                             "His face never changes.", "He takes his time talking.", "His response is monotone and dry.",
                             ],
                },
                "react_grill_neutral": {
                    "says": ['His eyes grow distant.', "His face seems bored.",
                             "'Hmm, let me think...'",
                             "A beat passes before he responds.", "He shrugs his shoulders.",
                             "He clears his throat."],
                    "effects": {"mood": -1},
                },
                #again = WILL TALK, already = WONT talk
                "again_chat_neutral": { #still responds, but warns player they already asked
                    "says": ['"I guess I can repeat myself for you..."',"I just told you - ", "Detective, there isn't more I can say.",
                             "If you want to hear it again - ",],
                    "effects": {"mood": -1},
                },
                #just talked: if topic is most recent;  respond if count = 1 else no
                "just_talked_chat_neutral": {
                    "says": ['Must I repeat myself?',"Quite forgetful, aren't you?",
                             ".. If you want to hear it again,", "{topic}? If you've forgotten - "],
                    "effects": {"mood": -1},
                },
                "just_talked_grill_neutral": {
                    "says": ["I told you, ",
                             "Nothing more I can say about that, Detective.",
                             "I just told you - ","{topic}? I just told you...", "Will you be questioning me about that all {current_phase}?" ],
                    "effects": {"mood": -1},
                },
                # already_talked: if topic in history, wont respond
                "already_talked_chat_neutral": {
                    "says": ['Please detective, you just questioned me about that.','I have no further answers on this topic.',
                            "I would rather not talk about that all {current_phase}...",
                             "{topic}? Could we not move on from that?",
                             "Give that some rest, would you?"],
                    "effects": {"mood": -1},
                },
                "already_talked_grill_neutral": {
                    "says": ['I have no further comments.',"I've told you enough about that already.",
                             "Nothing's changed, Detective.","Dont be so brash, you've already questioned me on that same topic."],
                    "effects": {"mood": -1},
                },
                "already_talked_chat_bad": {
                    "says": ['"I don\'t want to talk about that again."',"Detective, I am not going to talk about {topic} all {current_phase}...",
                             "I decline to discuss that any further, thank you.", "Detective, I'd rather you... left.", ],
                    "effects": {"mood": -1},
                },
                "already_talked_grill_bad": {
                    "says": ['His eyes look blank, but you can tell he is angry.\n"Detective, stop grilling me about that."',
                             "How many questions will suffice for you?",
                             "Is your plan to repetitively bug me all {current_phase}?"],
                    "effects": {"mood": -1},
                },
                #unknown
                "unknown_chat_neutral": {
                    "says": ["I really don't know much...","Afraid I can't help you with that..."],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["Honestly, I really dont know what to say about {topic}..."],
                    "effects": {},
                    "options": None
                },
                "morgue_knife_01_chat_neutral": {
                    "says": ["Ah... Yes, that is indeed a knife.. It is quite common in morgues, you know..." ],
                    "effects": {},
                    "options": None
                },
                "morgue_knife_01_grill_neutral": {
                    "says": ["Look, what would you like me to say?.. It's a knife." ],
                    "effects": {},
                    "options": None
                },
                "morgue_gun_01_chat_neutral": {
                    "says": ["'Well, you will be hard pressed to find a local without some sort of gun...'", ],
                    "effects": {},
                    "options": None
                },

                "hair_01_chat_neutral": {
                    "says": ["'Its quite a common hair type, unfortunately...'\nHe gestures to his black hair.\n'Too common...'", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_chat_neutral": {
                    "says": ["A Bertha, it's been quite some time since I talked to her... Is she doing well?", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_grill_neutral": {
                    "says": ["I mean, I'm not really in a position to say much...", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_chat_neutral": {
                    "says": ["Word is, he has trouble crediting his debtors... \nNot a good reputation to have.", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_grill_neutral": {
                    "says": ["Wish I could help... but I dont have much to say about him...", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_chat_neutral": {
                    "says": ["I've been living here for...\nHe spaces out.\n...\n36 years now...", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["I know being a mortician is quite suspicious.. But it's quite a bit... simpler than being a doctor.", ],
                    "effects": {},
                    "options": None
                },
                "morgue_workboots_01_chat_neutral": {
                    "says": ["'Yes, those are mine... Those are a popular kind, you know...'"],
                    "effects": {},
                    "options": None
                },
                "morgue_workboots_01_grill_neutral": {
                    "says": ["'Every working man or woman would probably have a pair of those.'" ],
                    "effects": {},
                    "options": None
                },
                "morgue_leather_jacket_chat_neutral": {
                    "says": ["'It's quite nice, I must say...'"],
                    "effects": {},
                    "options": None
                },
                "morgue_leather_jacket_grill_neutral": {
                    "says": ['"I mean, what pressing knowledge were you looking to get from this?"' ],
                    "effects": {},
                    "options": None
                },
                "matches_01_chat_neutral": {
                    "says": ['Never seen those before. Are they new?'],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_neutral": {
                    "says": ["I dont know what I'm supposed to say..." ],
                    "effects": {},
                    "options": None
                },
                "matches_02_chat_neutral": {
                    "says": ['"I have a bunch of those around..."'],
                    "effects": {},
                    "options": None
                },
                "matches_02_grill_neutral": {
                    "says": ['Those old matchess are meaningless...'],
                    "effects": {},
                    "options": None
                },
                "cigs_01_chat_neutral": {
                    "says": ["Those are commonplace...",],
                    "effects": {},
                    "options": None
                },
                "cigs_01_grill_neutral": {
                    "says": ["Truth be told, I prefer pipe to those... But I enjoy them on occasion.",],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_chat_neutral": {
                    "says": ["'Very well manufactured - top grade tobacco. If you need some, I've got plenty.'"],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_grill_neutral": {
                    "says": ["'I consider myself quite knowledgeable on this subject - they are tremendous quality tobacco leaves.'",],
                    "effects": {},
                    "options": None
                },
                "tomato_01_chat_neutral": {
                    "says": ["'Not a bad lunch...'"],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["I hate to be rude, but you should lower your voice.",],
                    "effects": {},
                    "options": None
                },
                "mustard_01_chat_neutral": {
                    "says": ["Dijon, with ham and rye. My favorite."],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": ["With all due respect, please stop asking me in that tone. It's mustard.",],
                    "effects": {},
                    "options": None
                },
                "grease_01_chat_neutral": {
                    "says": ["'I try not to have too much, but enjoy it on ocassion.'"],
                    "effects": {},
                    "options": None
                },
                "grease_01_grill_neutral": {
                    "says": ["'Ah, my weakness. Greasy food.'",],
                    "effects": {},
                    "options": None
                },
                "pie_01_chat_neutral": {
                    "says": ["Quite nice with some red wine - highly recommend!"],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_neutral": {
                    "says": ["Sir, we are talking about pie, no?",],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_chat_neutral": {
                    "says": ["No thanks, something about the acidity I don't like - I think it's popular at the Pub.'"],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_grill_neutral": {
                    "says": ["Could you refrain from asking in that tone?",],
                    "effects": {},
                    "options": None
                },
                "red_wine_01_chat_neutral": {
                    "says": ["Delicious, redder the better.","I love the deep, crimson color."],
                    "effects": {},
                    "options": None
                },
                "red_wine_01_grill_neutral": {
                    "says": ["Please Detective, I want to help, but you must change your method.",],
                    "effects": {},
                    "options": "gibbs_red_wine_01_grill_neutral"
                },
                "whiskey_01_chat_neutral": {
                    "says": ["Quite a nice bite to it, I must say.","A whiskey is quite popular with all the men here."],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["Yes, yes, keep bugging me, by all means...",],
                    "effects": {},
                    "options": None
                },
                "rum_01_chat_neutral": {
                    "says": ["A bit too tangy for my taste...",],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["I'm sure its quite popular around here, but I don't care for it.",],
                    "effects": {},
                    "options": None
                },
                #additional states as needed
            },
        },
        "conditional": [ #witness statements
            {
                "conditions": {"traits":["bertha"]}, #murderer traits here; has to be like this to follow check condition format for items - possible other conditions?
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "bertha_01_chat_neutral": {
                            "says": ["Haven't seen her in quite some time... I used to go to her pub, long ago."],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            },
        ]
    },
}