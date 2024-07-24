
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
                    "says": ['"What can I do for ya?"', "'Howdy, need anything?'", "'Hey, what's up?'","'Hey, whats going on?'",
                             "'What can I do for you, Detective?'"],
                    "options":  "default_1"
                },
                "greet_bad": {
                    "says": ["'Oh, it's you again...'","'What do you want?'","'Great, now what..?'", "'Detective.. What now?'"],
                    "options": "default_1"
                },
                "redirect_good": {
                    "says": ["'So, where were we?'", "'Well then...'", "'Need anything?'","'Anything else?'","'So, what next?'"],
                    "effects": {},
                    "options": "default_1"
                },
                "redirect_bad": {
                    "says": ["'Let's get this over with.'", "'What now?..'", "'Is this going to be much longer..?'",
                             "She looks annoyed.", "'Will you be talking to me much longer?'"],
                    "effects": {},
                    "options": "default_1"
                },
                "bye_good": {
                    "says": ["'See ya.'", "'Have a good one!'","'Good luck!'","'Take care!'","'Until next time!'"],
                },
                "bye_bad": {
                    "says": ["'Finally...'","'About time...'", "'Bye!' she says, relieved.","She breathes a sigh of relief as you leave."],
                }
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                #REACTIONS
                "react_chat_neutral": {
                    "says": ["A beat passes before she responds.", "'Uhhhmm...'", "She shrugs.",
                             "She exhales, pausing for a second.", "'Right,'", "'Well...'"
                             "'Oh, {topic}? I mean...", "'Oh, that?'", "'I mean...'", "She scratches her head.",
                             "'{topic}?.. '", "'{topic}, huh?'"
                             ],
                },
                "react_grill_neutral": {
                    "says": ['Her eyes furrow.', "She takes a deep breath, calming herself.", "She crosses her arms.",
                             "Her eyes flash in annoyance.", "'Let me think...'", "'Hmmm...'", "'Okay, okay..'",
                             "Her shoulders tense..", "She pauses for a moment before answering.", "'Look dude...'",
                             "Could you lay off me?", "'Uhmmm...'", "'Uhhh - {topic}?'"],
                    "effects": {"mood": -1},
                },
                #again = exact same node, will respond
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
                    "says": ["'She shrugs. What do you wanna know about {topic}?'", "'... Not too sure what to say about that.'", "'I'm afraid I can't help much with that...'",
                             "'I mean.. It's {topic}...'", "'What can I say? It's {topic}.'", "'You really wanna chat about that? I got nothing, man.'"],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["'Lay off me, would you? What am I supposed to say about {topic}?'", "'Honestly, relax. I dont' know anything about {topic}.'", "'Could you lay off me? It's {topic}...'",
                             "'I really don't know much about {topic}... What were you expecting?'", "'Afraid I can't help you much with that.'"],
                    "effects": {},
                    "options": None
                },
                #
                #
                #
                #START OF ACTUAL TOPICS! LOL
                "night of the murder_chat_neutral": {
                    "says": ["'Debbie came here late afternoon, sang a little... Then left.'"],
                    "effects": {},
                    "options": None
                },
                "night of the murder_grill_neutral": {
                    "says": ["'Wish I could help more. She arrived late afternoon, hung around, and Gibbs walked her 'round the corner.'"],
                    "effects": {},
                    "options": None
                },
                "murder_matchbook_01_chat_neutral": {
                    "says": ["'In the alley, huh?..' \n'Afraid everyone uses matches around here - except maybe Debbie.'"],
                    "effects": {},
                    "options": None
                },
                "murder_matchbook_01_grill_bad": {
                    "says": ["'Hate to say it, but everyone in this town carries matches, Detective.'", ],
                    "effects": {},
                    "options": None
                },
                "murder_ash_01_chat_neutral": {
                    "says": ["'You're really reaching - I think literally everyone smokes 'round here...'","'Who doesnt smoke? Can you tell what kind they are?'"],
                    "effects": {},
                    "options": None
                },
                "murder_ash_01_grill_neutral": {
                    "says": ["'I couldn't of left any ashes there, because I was here at the bar all night!'","'They are probably left from Debbie herself!'"],
                    "effects": {},
                    "options": None
                },

                "murder_roach_01_chat_neutral": {
                    "says": ["'I guess you could try comparing it to roaches in the ashtrays...'"],
                    "effects": {},
                    "options": None
                },
                "murder_roach_01_grill_neutral": {
                    "says": ["'Did you catch what kind? If it's generic, good luck... "
                             "But if it's premium, I think Gibbs and the Mortician smoke those.'"],
                    "effects": {},
                    "options": None
                },

                "roach_01_chat_neutral": {
                    "says": ["'Please, try to ash those in the ashtrays... I hate when people just throw it around.'"],
                    "effects": {},
                    "options": None
                },
                "roach_01_grill_neutral": {
                    "says": ["'What am I supposed to say here?.. Anyone who smokes cigarettes leaves a roach somewhere.'"],
                    "effects": {},
                    "options": None
                },
                "blood_01_chat_neutral": {
                    "says": ["'Ughhh...'\nShe shivers.\n'Horrible to think who might've done that...'"],
                    "effects": {},
                    "options": None
                },
                "blood_01_grill_neutral": {
                    "says": ["'Wish I could help you more. Maybe you could analyze the splatter or something?..'"],
                    "effects": {},
                    "options": None
                },
                "tooth_01_chat_neutral": {
                    "says": ["'Holy smokes..'\nThrough closed lips, she runs her tongue around her teeth.\n'Brutal man...'"],
                    "effects": {},
                    "options": None
                },
                "tooth_01_grill_neutral": {
                    "says": ["'Her tooth was knocked out?..\nShe must have gotten hit by something or someone pretty dang strong...'"],
                    "effects": {},
                    "options": None
                },
                "bruising_01_chat_neutral": {
                    "says": ["'Well, I guess some bruises are not really unexpected...'","What'd they look like? Are they bad?"],
                    "effects": {},
                    "options": None
                },
                "bruising_01_grill_neutral": {
                    "says": ["'Look dude - not really sure what I'm supposed to tell you here...'"],
                    "effects": {},
                    "options": None
                },
                "wounds_01_chat_neutral": {
                    "says": ["'Tragic... Hope it was quick is all.'","Can you tell what caused them?.. "],
                    "effects": {},
                    "options": None
                },
                "wounds_01_grill_neutral": {
                    "says": ["'How am I supposed to know anything about this?'"],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_chat_neutral": {
                    "says": ["'I guess you found the weapon! Any other leads?'"],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_grill_neutral": {
                    "says": ["'Look, to be honest - everyone has access to a knife around here...'"],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_chat_neutral": {
                    "says": ["'Probably a good indicator a gun was used... but whose?'"],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_grill_neutral": {
                    "says": ["'I dont know anything about that, I'm sorry!'"],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_chat_neutral": {
                    "says": ["Must of been taken from the alley, there is all sorts of abandoned scrap there.."],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_grill_neutral": {
                    "says": ["'Must be someone strong to bludgeon someone to death - does that help?'"],
                    "effects": {},
                    "options": None
                },
                "scent_01_chat_neutral": {
                    "says": ["Hate to break it to you - there are all sorts of scents in that place.."],
                    "effects": {},
                    "options": None
                },
                "scent_01_grill_neutral": {
                    "says": ["'How am I supposed to know any details about that?'"],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_chat_neutral": {
                    "says": ["'Cigarettes eh? I mean, I smoke those, but who doesn't?.."],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_grill_neutral": {
                    "says": ["'If you find the brand, that might help - aside from that, can't help you.'"],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_chat_neutral": {
                    "says": ["'In the alley, huh? Interesting.. 'Fraid I can't help much with that...'."],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_grill_neutral": {
                    "says": ["'Sorry dude - I got nothing.'"],
                    "effects": {},
                    "options": None
                },
                "scrap_leather_01_chat_neutral": {
                    "says": ["She nervously wipes her hands on her leather pants...\n'Lot's of people have leather 'round here...'"],
                    "effects": {},
                    "options": None
                },
                "scrap_leather_01_grill_neutral": {
                    "says": ["'Look, hate to break it to you - everyone could have access to leather!'","'How do you know it's not just Debbie's?!'"],
                    "effects": {},
                    "options": None
                },
                "scrap_denim_01_chat_neutral": {
                    "says": ["'Lot's of people have denim - okay?'\nShe readjusts her denim jacket, and swallows."],
                    "effects": {},
                    "options": None
                },
                "scrap_denim_01_grill_neutral": {
                    "says": ["'Everyone could have denim, probably even Debbie! Right?'"],
                    "effects": {},
                    "options": None
                },
                "scrap_suit_01_chat_neutral": {
                    "says": ["'I never wear anything formal like that - talk to someone else...'"],
                    "effects": {},
                    "options": None
                },
                "scrap_suit_01_grill_neutral": {
                    "says": ["'Well, Debbie wore a silk dress if I recall.. Gibbs always wears dress shirts and suits... That's all I got'"],
                    "effects": {},
                    "options": None
                },
                "scrap_suit_01_grill_bad": {
                    "says": ["'I don't wear things like that, capiche?'"],
                    "effects": {},
                    "options": None
                },
                "hair_01_chat_neutral": {
                    "says": ["'I mean... '\nShe plays with her identical looking hair. \n'There's lots of people that could be, right?'", ],
                    "effects": {},
                    "options": None
                },
                "hair_01_grill_neutral": {
                    "says": ["'I'd recommend talking to more people.\n "
                             "You're going to find lots of suspects with matching hair, especially if it was torn unevenly like that.' ", ],
                    "effects": {},
                    "options": None
                },
                "hair_01_grill_bad": {
                    "says": ["'Look, it's hair man. What do you want me to say?'", ],
                    "effects": {},
                    "options": None
                },
                "fridge_01_chat_neutral": {
                    "says": ["'That's got all our food in it, you can take some, just... not too much okay?'"],
                    "effects": {},
                    "options": None
                },
                "fridge_01_grill_neutral": {
                    "says": ["'How is the fridge supposed to help your case?'", ],
                    "effects": {},
                    "options": None
                },
                "bertha_office_drawer_01_chat_neutral": {
                    "says": ["'Yeah, that's where I do the paperwork... Been using that thing for years now.'"],
                    "effects": {},
                    "options": None
                },
                "bertha_office_drawer_01_grill_neutral": {
                    "says": ["'Dude, it's my desk okay? Would you lay off me?'", ],
                    "effects": {},
                    "options": None
                },
                "debbie_01_chat_neutral": {
                    "says": ["'So sad what happened. I actually knew her growing up, long time ago.'\nShe looks off into the distance.\n'How things have changed...'"],
                    "effects": {},
                    "options": None
                },
                "debbie_01_grill_neutral": {
                    "says": ["'We were old friends way back, grew up at a nearby town. She almost felt like my younger sister.\n"
                             "We drifted apart slowly - I moved here... for work. And she went on to do her music thing.'", ],
                    "effects": {},
                    "options": None
                },
                "debbie_01_grill_bad": {
                    "says": ["'Dude, piss off would you.'", ],
                    "effects": {},
                    "options": None
                },
                "ashtray_01_chat_neutral": {
                    "says": ["'Yeah, we got those scattered around.'","'Try to use those eh? Don't just throw your roaches on the ground.'",
                             "'I try to clean em' every now and then, but they can get pretty gnarly.'"],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_chat_neutral": {
                    "says": ["'We got plenty of those. Feel free to grab one if you need to cook, just put it back, and CLEAN IT!'",
                             ],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_chat_bad": {
                    "says": [
                             "'... We use them.. to cook...'","'Wouldn't be much of a food place without those.'",
                             "'It's a kitchen knife... Anything specific you want to know?'",
                             ],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_grill_neutral": {
                    "says": ["'It's a kitchen knife - I mean, we need those to cook..."
                             "I guess anyone around here could grab one?"],
                    "effects": {},
                    "options": None
                },
                "revolver_01_chat_neutral": {
                    "says": ["'Dude, you really opened my desk drawer? That's my personal stuff, and yes, I have a gun...'" ],
                    "effects": {"mood":-1},
                    "options": None
                },
                "revolver_01_grill_neutral": {
                    "says": ["'Could you not go through my personal stuff? "
                             "Yes I've got a gun, but that's very common around here...'", ],
                    "effects": {"mood":-1},
                    "options": None
                },
                "bullets_01_chat_neutral": {
                    "says": [
                        "'How about, you, like, not go through my personal belongings? "
                        "Yes, I've got bullets, for my gun, it's common around here, okay?'"],
                    "effects": {"mood": -1},
                    "options": None
                },
                "bullets_01_grill_neutral": {
                    "says": [
                        "'Those are bullets, for my gun - now get out of my face dude, and stop going through my personal stuff."],
                    "effects": {"mood": -1},
                    "options": None
                },
                "office_trash_01_chat_neutral": {
                    "says": [
                        "'Just a trashcan dude, not much more to say...'"],
                    "effects": {"mood": -1},
                    "options": None
                },
                "office_trash_01_grill_neutral": {
                    "says": [
                        "'Sorry, I'm afraid I really don't have anything relevant to say... Like, it's a trashcan."],
                    "effects": {"mood": -1},
                    "options": None
                },

                "bertha_01_chat_neutral": {
                    "says": ["Im the bartender, and owner here - work at the pub all day, everyday.", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_grill_neutral": {
                    "says": ["I'm just a girl who works here, ok?", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_chat_neutral": {
                    "says": ["'Guy is the worst gambler I've ever heard of... Actually, he was chatting up Debbie yesterday.'",
                             "'He can be exceedingly annoying, not going to lie... I saw him yesterday, hanging around Debbie. He can be a creep.'"
                             ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_grill_neutral": {
                    "says": ["'I saw him and Debbie yesterday, he tried to walk her home, following her...'", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_chat_neutral": {
                    "says": ["'Honestly, haven't seen him here in ages. He doesn't go out much.'", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["'I really don't know him well, he hasn't been here in ages - he sticks to himself.'", ],
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
                    "says": ["'Love those - they just came in yesterday. You can grab one from the bar if you'd like, but only if you need it please.'"],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_neutral": {
                    "says": ["'Those are the new style, they just came in yesterday actually. I keep a bowl of them on the bar..."
                             "Not sure how that helps your investigation, but there you are.'" ],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_bad": {
                    "says": ["'Detective, those are matches that came in yesterday. New logo, see?'\n"
                             "She pulls one out, jabbing her finger at it.\n'Satisfied?!?'" ],
                    "effects": {},
                    "options": None
                },
                "matches_02_chat_neutral": {
                    "says": ["'Ugh, hate those old ones. I threw mine out as soon as the new ones came in yesterday.'",],
                    "effects": {},
                    "options": None
                },
                "matches_02_grill_neutral": {
                    "says": ["'Those are the old style. We have a bowl at the bar in case anyone needs to smoke - just replaced it with the new matchbooks. \nHope that helps.'",],
                    "effects": {},
                    "options": None
                },
                "flask_01_chat_neutral": {
                    "says": ["'Easy to carry, can fill it with your preferred drink - what's not to like?'",
                            "'Pretty common around here, it's an easy way to carry your drink around.'"
                             ],
                    "effects": {},
                    "options": None
                },
                "flask_01_grill_neutral": {
                    "says": ["'I really can't think of what might help - I have a flask, I know Gibb's has a flask too... \n"
                             "I mean, around here, everyone's got one Detective.'",],
                    "effects": {},
                    "options": None
                },
                "gin_01_chat_good": {
                    "says": [
                             "'Funny story - maybe about 4 months ago, I went shot for shot with Gibbs drinking gin. \n"
                             "Guy puked so much that night, he can't even look at the stuff without gagging.' She lets out a wheezing laugh.\n"
                             "I was actually just drinking water the whole time - although I do love the stuff.'" ],
                    "effects": {},
                    "options": None
                },
                "gin_01_chat_neutral": {
                    "says": ["'Mmm, love gin - something about the sharp, pine taste is delicious. Care for some?'",
                             ],
                    "effects": {},
                    "options": None
                },
                "gin_01_grill_neutral": {
                    "says": ["'Look, not sure how I can help. I know Gibbs hates gin, that's something.'", ],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_chat_neutral": {
                    "says": ["'Ughh, I can't stand the smell... \n"
                             "One day, like years ago, I drank so much whiskey I couldn't stop puking all night. Ever since then, I haven't touched it.'", ],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["'Only thing that might help is that most of the guys here like it...'", ],
                    "effects": {},
                    "options": None
                },
                "rum_01_chat_neutral": {
                    "says": ["'Great stuff - rich, sweet flavor, aged in oak. Love it.'", ],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["'Everyone 'round here drinks rum.", ],
                    "effects": {},
                    "options": None
                },
                "tomato_01_chat_neutral": {
                    "says": ["'Delicious, can't imagine what kind of weirdo wouldn't like this.'",],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["'It's a pretty popular dish.. We keep a pot in the kitchen.'", ],
                    "effects": {},
                    "options": None
                },
                "mustard_01_chat_neutral": {
                    "says": ["'Eh, I could do without it - not a big fan of mustard. But that's not a very popular opinion.'"],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": ["'Hate that sandwich... I think I saw Gibbs eat one yesterday? Not too sure though.'", ],
                    "effects": {},
                    "options": None
                },
                "pie_01_chat_neutral": {
                    "says": ["'Oh man, when that's fresh, it's delicious. Care for a bite?'"],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_neutral": {
                    "says": ["'I had some yesterday night - actually, I served Debbie some too.'", ],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_bad": {
                    "says": ["It's pie. Get a life.", ],
                    "effects": {},
                    "options": None
                },
                "lighter_01_chat_neutral": {
                    "says": ["'I never liked lighters - have to get fuel, can't lose it... Matches are easy - less maintenance.'", ],
                    "effects": {},
                    "options": None
                },
                "lighter_01_grill_neutral": {
                    "says": ["'I know Debbie had a gold lighter - most people around here don't actually use lighters, they use the matchbooks by the bar..'", ],
                    "effects": {},
                    "options": None
                },

                "lipstick_01_chat_neutral": {
                    "says": [
                        "'I prefer less obvious lipstick... Debbie uses runny, glossy stuff.'", ],
                    "effects": {},
                    "options": None
                },
                "lipstick_01_grill_neutral": {
                    "says": [
                        "'That's gotta be Debbie's - I'd never use a brand that thick and glossy.'", ],
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
                "cigs_02_chat_neutral": {
                    "says": ["'Those are kind of over priced in my opinion. If I'm going for experience, why not just smoke pipe?'",],
                    "effects": {},
                    "options": None
                },
                "cigs_02_grill_neutral": {
                    "says": ["'I don't smoke those, I'm fairly certain the gamblers do though.'",],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_chat_neutral": {
                    "says": ["'It's real fresh stuff, I love it. Grows locally, burns real slow.'"],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_grill_neutral": {
                    "says": ["'Everyone who isn't a loser here smokes this stuff.'",],
                    "effects": {},
                    "options": None
                },
                "smoke_pipe_01_chat_neutral": {
                    "says": ["'That's my preferred way to smoke tobacco - cigarettes are okay too.'"],
                    "effects": {},
                    "options": None
                },
                "smoke_pipe_01_grill_neutral": {
                    "says": ["'Not sure how to help you - my pipe should be on my desk, I doubt anyone would move it.'",],
                    "effects": {},
                    "options": None
                },
                "earring_01_chat_neutral": {
                    "says": ["'I don't like wearing any, just more things to keep track of.'"],
                    "effects": {},
                    "options": None
                },
                "earring_01_grill_neutral": {
                    "says": ["'Only person I recall with ear rings is Debbie herself - she wore small hoops.'",],
                    "effects": {},
                    "options": None
                },
                "denim_jacket_01_chat_neutral": {
                    "says": ["'I've got a couple denim jackets around here - like this one.'\nShe gestures to her jacket."],
                    "effects": {},
                    "options": None
                },
                "denim_jacket_01_grill_neutral": {
                    "says": ["'That one on in the lounge is mine - I might have one in my office too. And of course, the one I'm wearing.'", ],
                    "effects": {},
                    "options": None
                },
                "leather_jacket_01_chat_neutral": {
                    "says": ["'Love leather.' She gestures to her leather pants.\n'Comfortable and durable, whether pants or a jacket.'"],
                    "effects": {},
                    "options": None
                },
                "leather_jacket_01_grill_neutral": {
                    "says": ["'I've got one of mine around here - can't remember if it's in the lounge or my office.'", ],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_chat_neutral": {
                    "says": ["'Too formal for my taste, I'd never wear a suit here.'"],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_grill_neutral": {
                    "says": ["'Pretty sure that one in the lounge is Gibbs - he also might have a spare somewhere.'", ],
                    "effects": {},
                    "options": None
                },

                "high_heels_01_chat_neutral": {
                    "says": ["'Hate high heel, like, how are you supposed to walk normally in those?!'"],
                    "effects": {},
                    "options": None
                },
                "high_heels_01_grill_neutral": {
                    "says": ["'Honestly, I think the only gal around here who wears that is... Debbie'", ],
                    "effects": {},
                    "options": None
                },
                "sneakers_01_chat_neutral": {
                    "says": ["'Who doesn't own a pair of sneakers?'"],
                    "effects": {},
                    "options": None
                },
                "sneakers_01_grill_neutral": {
                    "says": ["'Dude, it's sneakers - I'm wearing them right now!'\nShe taps her foot on the floor, bringing attention to her shoes. They're sneakers.", ],
                    "effects": {},
                    "options": None
                },
                "dress_shoes_01_chat_neutral": {
                    "says": ["'Why someone would wear that around here, I've got no idea. So not my style.'"],
                    "effects": {},
                    "options": None
                },
                "dress_shoes_01_grill_neutral": {
                    "says": ["'Not sure whose pair those are at the front, but plenty of the guys like em.'", ],
                    "effects": {},
                    "options": None
                },
                "workboots_01_chat_neutral": {
                    "says": ["'Those are so practical, I always keep a pair around just in case.'"],
                    "effects": {},
                    "options": None
                },
                "workboots_01_grill_neutral": {
                    "says": ["'Doubt I've got much to tell you here. The pair at the fronts mine.'", ],
                    "effects": {},
                    "options": None
                },


                "grease_01_chat_neutral": {
                    "says": ["Good stuff, love me some greasy food."],
                    "effects": {},
                    "options": None
                },
                "grease_01_grill_neutral": {
                    "says": ["Dude, who doesn't like greasy food?", ],
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

                #additional states as needed
            },
        },
        "conditional": [ #GOTTA GO OVER THIS MORE, MAKE IT WAY BETTER, MOST DIALOGUE SHOULD BE CONDITIONAL DIALOGUE!
            {
                "conditions": {"traits":["gibbs"]}, #murderer traits here; has to be like this to follow check condition format for items - possible other conditions?
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "gibbs_01_chat_neutral": {
                            "says": ["'Annoying guy. He seemed... Really angry last night. Weirdly so...'",
                                     "'When he was hanging around Debbie - I saw something in his eyes.. I'm not sure what. But something was off.'",
                                     ],
                            "effects": {},
                            "options": "default_1"
                        },
                        "gibbs_01_grill_neutral": {
                            "says": ["'I saw him, glaring at Debbie after they talked - I wonder what happened. I saw them leave the pub together.'",
                                     "'When he was hanging around Debbie - I saw something in his eyes.. Something bad. Something was off.'",
                                     ],
                            "effects": {},
                            "options": "default_1"
                        },
                    }
                }
            },{
                "conditions": {"traits":["gibbs","knife"]},
                "dialogue": {
                    "default": {
                "kitchen_knife_01_chat_neutral": {
                    "says": ["People often use those to make a sandwich or something - like Gibbs last night."],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_grill_neutral": {
                    "says": ["'Swear to god, I thought one was missing late last night, after Gibbs and Debbie left... It was back later.'",
                             "'I actually saw Gibbs sneak into the kitchen right before walking Debbie home - might've grabbed a knife? Or a sandwich...'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","whiskey"]},
                "dialogue": {
                    "default": {
                "whiskey_01_chat_neutral": {
                    "says": ["Personally, I can't stand the stuff, but Gibbs was drinking that like crazy that night.",
                             ],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["'I served Gibbs some whiskey that night - I'm pretty sure he poured some into his flask.'",
                             "'Gibbs was drinking really heavy before the murder. Like, REALLY heavy. And I'm pretty sure it was whiskey.. "
                            ],
                    "effects": {},
                    "options": None
                },
                "flask_01_grill_neutral": {
                    "says": [ "'At the bar, I'm almost certain I saw Gibbs pour the whiskey I served him into his flask...'",],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","rum"]},
                "dialogue": {
                    "default": {
                "rum_01_chat_neutral": {
                    "says": ["Big rum fan myself. Actually, last night, Gibbs was drinking that like crazy...",
                             ],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["'I'm pretty sure Gibbs poured the rum I served him into his flask.'",
                             "'Before the murder, Gibbs drank so much rum - it wasn't normal. He seemed mad."
                            ],
                    "effects": {},
                    "options": None
                },
                "flask_01_grill_neutral": {
                    "says": [ "'I saw Gibbs pour the rum I served him into his flask. I'm almost certain...'",],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","tomato"]},
                "dialogue": {
                    "default": {
                "tomato_01_chat_neutral": {
                    "says": ["That's a great dish here - served some to Gibb's last night.. If I recall correctly.",
                             ],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["'I think Gibbs ate that last night - he was so drunk, he spilled a bunch all over his clothing.'",
                             "'Gibbs ate a bunch of that while talking to Debbie. Pretty sure I saw him spill it all over himself."
                            ],
                    "effects": {},
                    "options": None
                },
                "fridge_01_grill_neutral": {
                    "says": [ "'Gibbs kept raiding the fridge, getting some tomato soup - it was kind of weird. He seemed paranoid.'",],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","mustard"]},
                "dialogue": {
                    "default": {
                "mustard_01_chat_neutral": {
                    "says": ["Can't stand how much mustard are in those - Gibbs on the other hand, I've never seen a guy put more mustard on a sandwich then him.",
                             ],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": ["'Gibbs made a HUGE sandwich last night - I remember because he made a mess, mustard got everywhere.'",
                             "'The amount of sandwiches Gibbs eats, and the amount of mustard he puts on - if you want info on a sandwich, he's your guy.'"
                            ],
                    "effects": {},
                    "options": None
                },
                "fridge_01_grill_neutral": {
                    "says": [ "'Gibbs was always hanging around that, looking for sandwich stuff.. More than usual - it seemed weird.'",],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","suit"]},
                "dialogue": {
                    "default": {
                "suit_jacket_02_chat_neutral": {
                    "says": ["'Eh, not my style - Gibbs wears suits all the time, it's probably his.'"],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_grill_neutral": {
                    "says": ["'You know, Gibbs brought a different suit in this morning - it looks similar, but I swear it's different.'",
                             "'I don't think I've ever seen Gibbs wear the suit he's wearing now - wonder why...'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","suit"]},
                "dialogue": {
                    "default": {
                "scrap_suit_01_chat_neutral": {
                    "says": ["'Strange - lots of people wear suits, but from the sound of it, that could be from Gibbs.'"],
                    "effects": {},
                    "options": None
                },
                "scrap_suit_01_grill_neutral": {
                    "says": ["'You know, I was thinking that Gibbs was wearing a new suit today.. Maybe he tore it? Or it's covered in blood.'",
                             "'I don't think Gibbs has worn the suit today before - maybe he has. But I could see him tearing it like that, then changing his outfit..'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","denim"]},
                "dialogue": {
                    "default": {
                "scrap_denim_01_chat_neutral": {
                    "says": ["'Denim is pretty common around here - I mean, I wear a denim jacket - Gibbs always wears denim jeans.'"],
                    "effects": {},
                    "options": None
                },
                "scrap_denim_01_grill_neutral": {
                    "says": ["'I think Gibbs is wearing new denim pants today - I swear it's different from his regular pair of jeans. Same style though.'",
                             "'I don't think that I've ever seen Gibbs with denim pants as clean and new as he's wearing right now... Wonder if he cleaned it recently.'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","new"]},
                "dialogue": {
                    "default": {
                "matches_01_grill_neutral": {
                    "says": ["'Gibbs always thinks he is so sneaky, taking as many as he can, stuffing his pockets full with them... Like, they just arrived last night, save some for people who need it!'",
                             "'Those new matches are great, just came in last night - I need to make sure Gibbs doesn't steal the whole stack, as usual...'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["gibbs","old"]},
                "dialogue": {
                    "default": {
                "matches_02_grill_neutral": {
                    "says": ["'Those are the old kind, I hate them - Gibbs used to stockpile them, thinking no one knew.. Fucking guy.'",
                             "'I saw Gibbs use one yesterday, even though he said he didn't have any and needed the new ones - asshole.'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{ #more night of murder
                "conditions": {"traits":["gun"]},
                "dialogue": {
                    "default": {
                "night of the murder_chat_neutral": {
                    "says": ["'I could've sworn I heard a gunshot late that night - after Debbie left.'","'After Debbie left, I think I heard a gunshot...'",
                             ],
                    "effects": {},
                    "options": None
                },
                "night of the murder_grill_neutral": {
                    "says": ["'I was on the porch, just about to go to bed when I heard a gunshot - might've been the murder...'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{ #more night of murder
                "conditions": {"traits":["gibbs"]},
                "dialogue": {
                    "default": {
                "debbie_01_grill_neutral": {
                    "says": ["'Gibbs was trying to put the moves on Debbie - she seemed... really uncomfortable.'",
                             "'After Debbie left, Gibbs kept trying to walk her home... He seemed drunk, and aggressive.'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },
            #BERTHA AS MURDERER
                {
                "conditions": {"traits":["bertha"]},
                "dialogue": {
                    "default": {
                "night of the murder_chat_neutral": {
                    "says": ["'Afraid there isn't much I can say...' She swallows, clearing her throat.\n'It was just a regular night.'",
                             "'I mean, I was at the bar all night, working.'\nShe speaks quickly.\n'I didn't see much.'"
                             ],
                    "effects": {},
                    "options": None
                },
                "night of the murder_grill_neutral": {
                    "says": ["'Look, I got nothing for you - it was like any other day!.'","'I was here at the bar all night, honestly! I didn't see much, I would tell you if I did...'"
                             "'If I knew something, I'd tell you for sure.' She bites her lip."
                             ],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },
            {
                "conditions": {"traits":["bertha"]},
                "dialogue": {
                    "default": {
                "debbie_01_grill_neutral": {
                    "says": ["Her voice wavers as she speaks.\n'Can't believe what happened - like, who could do something like that to her?'"
                             ],
                    "effects": {},
                    "options": None
                },
                "bruising_01_grill_neutral": {
                    "says": ["'Was it bad? I hope it didn't hurt.. So sad what happened..'\nShe looks slightly sick."
                             ],
                    "effects": {},
                    "options": None
                },
                "wounds_01_grill_neutral": {
                    "says": ["'I swear I don't know anything! I'd tell you if I did - promise!'\nHer tapping foot betrays her otherwise calm demeanor.",
                             "She rubs the back of her neck, seemingly nervous.\n'Gotta be really evil to do something like that..'"
                             ],
                    "effects": {},
                    "options": None
                },
                "blood_01_grill_neutral": {
                    "says": ["'That's awful... Just awful...'\nHer eyes dart around the room, her face pale...",
                             "'To think someone could do that to her - what a monster!..'\nFear flashes across her face."
                             ],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["bertha"]},
                "dialogue": {
                    "default": {
                "murder_matchbook_01_grill_neutral": {
                    "says": ["'Can't imagine who left that there.'\nShe clears her throat.\n'Can't be me, I like my matches too much..'",
                                "'I bet you Gibbs left the matchbook there!'", "'I bet the Mortician left it there!'"
                             ],
                    "effects": {},
                    "options": None
                },
                "murder_roach_01_grill_neutral": {
                    "says": ["'That doesn't mean anything, like, it could be from anyone...'"
                             ],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_grill_neutral": {
                    "says": ["'Anyone could've dropped that, right?....'"
                             ],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_grill_neutral": {
                    "says": ["'Anyone could've dropped that, right?....'"
                             ],
                    "effects": {},
                    "options": None
                },
                "scent_01_grill_neutral": {
                    "says": ["'I wouldn't read too much into that, it's just some smell, no?..'\nShe swallows."
                             ],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["bertha","knife"]},
                "dialogue": {
                    "default": {
                "kitchen_knife_01_grill_neutral": {
                    "says": ["'That's just a kitchen knife, for cooking, we need those to cook. No one would take one...'\nShe speaks slightly rushed.",
                             ],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_grill_neutral": {
                    "says": ["'Well that's great news!' She bites her nails.\n'But anyone could use a knife around here...'"
                             ],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },
            {
                "conditions": {"traits":["bertha","gun"]},
                "dialogue": {
                    "default": {
                "revolver_01_grill_neutral": {
                    "says": ["'I haven't touched that thing in ages, it's just their for safety!'\nHer hands fidget with her coat buttons."
                             ],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_grill_neutral": {
                    "says": ["She forces a smile, her lips trembling.\n'Well, that helps you out!'","She stammers, her throat dry.\n'There are some shady people around here who could have guns...'",
                             ],
                    "effects": {},
                    "options": None
                },
                "bullets_01_grill_neutral": {
                    "says": ["'Those are so old, I haven't touched them since I got them years ago!..'\nShe runs her hand across the nape of her neck. "
                             ],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },{
                "conditions": {"traits":["bertha","blunt"]},
                "dialogue": {
                    "default": {
                "tooth_01_grill_neutral": {
                    "says": ["Her face pales. \n'Crazy to think what happened that night... Wish I could help more..'"
                             ],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_grill_neutral": {
                    "says": ["She speaks, her voice forced and dry. \n'The murderer must have grabbed it in the alley, or brought it from their house or something..'",
                             ],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },


            {
                "conditions": {"traits":["mortician"]},
                "dialogue": {
                    "default": {
                "mortician_01_chat_neutral": {
                    "says": ["'He is such a weird guy - he hasn't been here in ages, thank god. Really creeped me out - morbid fucking dude.'",
                             ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["'Rumor is, he experiments on the bodies at the morgue... But you didn't hear that from me, okay?'",
                             "'As a bartender, I hear all sorts of things...'\nShe looks around.\n'I heard he experiments on the bodies. Probably just rumors - but don't tell anyone I told you that.'"],
                    "effects": {},
                    "options": None
                },
                        }
                    }
                },
        ]
    },
    "gibbs_01": {
        "non_topic": {
            "default": {
                "greet_neutral": {
                    "says": [ "'You gunna keep looking at me with that ugly mug?'\nHis lips pull into a thin smirk.",
                             "'Oh hey, guess who it is...'","'Speak of the devil - it's you.'","'Oh, look who the cat dragged in..'"],
                    "options":  "default_1"
                },
                "redirect_good": {
                    "says": ["'What now?'", "'So you still wanna bug me about something?'", "'What else you wanna talk about?'",
                             "'Lets keep it moving, huh?'", "'And, now what?'","'But wait, theres more!'"
                             ],
                    "effects": {},
                    "options": "default_1"
                },
                "bye_neutral": {
                    "says": ["'Adios Detective.'","'I did it! I confess! \n...\nJoking, idiot!'", "'Sayonara, pal.'",
                             "'Farewell, our knight in shining armor!'\nHis voice drips with sarcasm."],
                },
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                #REACTIONS
                "react_chat_neutral": {
                    "says": ["He cracks his knuckles.", "'{topic}, huh?..'", "'Ah, {topic} - '",
                             "'Right - '", "'Hmmm...'", "'I mean, '", "'Well...'", "'You see, '", "'Thing is - '",
                             "'Excellent topic choice.'", "'{topic}? Well...'", "'Uhh.'",
                             ],
                },
                "react_grill_neutral": {
                    "says": ["'Hmmm...'", 'His eyes narrow.', "He gives you a look.", "'Uhhhhhhhh...'", "'I'll try to help...' \nHe thinks for a moment.",
                             "'{topic}, right - '", "He shrugs, half focused.", "'Give me a second - '\nMultiple seconds pass.\n", "'Well, if I may - '",
                             "'Let me think...'", "'Hold on, let me think a minute...'", "'Okay, relax - '", "'Oh, yes, {topic}!'",
                             "'{topic}, yes yes - ","'Right, {topic}'"],
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
                    "says": ["'Lets talk more about that, I care so much.'", "'Who gives a fuck about {topic}?'",
                             "'You expect me to say something interesting?'", "'Who cares about {topic}?'",
                             "'What other cool conversation ideas do you have?'\nHe looks at you, making a funny face."],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["'You're doin' great work here, Detective...'\nHe says it sarcastically, focusing on the game.",
                             "'Did you expect me to actually have something important to say about that?'",
                             "'How about you grill me some more about that, that's a real smart idea!'", "'Am I supposed to take you seriously? It's {topic}'",
                             "'Groundbreaking idea - case solved with {topic}!' He gives you a look before returning to his activities."],
                    "effects": {},
                    "options": None
                },
                #
                #
                #

                # START OF ACTUAL TOPICS! LOL
                "night of the murder_chat_neutral": {
                    "says": ["'Debbie arrived late afternoon... She does a little singing, talks people up, then bounces.. All seriousness, not sure I have anything useful to say.'"],
                    "effects": {},
                    "options": None
                },
                "night of the murder_grill_neutral": {
                    "says": ["'Bertha and her actually argued a bit, not sure about what. Then she left... I walked her just past the corner, but she didn't want me around...'",
                        ],
                    "effects": {},
                    "options": None
                },
                "murder_matchbook_01_chat_neutral": {
                    "says": ["'Can't help much with that boss. Try asking elsewhere, okay?'"],
                    "effects": {},
                    "options": None
                },
                "murder_matchbook_01_grill_neutral": {
                    "says": ["'Truth is Detective, that really doesn't seem useful. Everyone grabs matchbooks from the bar in this town.'",
                        ],
                    "effects": {},
                    "options": None
                },
                "murder_ash_01_chat_neutral": {
                    "says": ["'We talkin' 'bout ashes?' He seems genuinely confused.\n'Good luck with the case.'"],
                    "effects": {},
                    "options": None
                },
                "murder_ash_01_grill_neutral": {
                    "says": ["'Ashes? You really grilling me about ashes? You think I know how to differentiate between ashes based on a description?'",
                        ],
                    "effects": {},
                    "options": None
                },
                "murder_roach_01_chat_neutral": {
                    "says": ["'Roaches are like... uhh. They're like, real common to see on the ground.'"],
                    "effects": {},
                    "options": None
                },
                "murder_roach_01_grill_neutral": {
                    "says": ["'Eyo, relax - if you know the color, maybe you can find the brand. Otherwise, I got nothing.'",
                        ],
                    "effects": {},
                    "options": None
                },
                "roach_01_chat_neutral": {
                    "says": ["'You ain't a conversationalist are you? A roach?..'"],
                    "effects": {},
                    "options": None
                },
                "roach_01_grill_neutral": {
                    "says": ["He gestures to the ashtray in front of him.\n'That help?'",
                        ],
                    "effects": {},
                    "options": None
                },
                "blood_01_chat_neutral": {
                    "says": ["'Someone was out for blood huh? Damn.'"],
                    "effects": {},
                    "options": None
                },
                "blood_01_grill_neutral": {
                    "says": ["'You think I know something about the blood?'\nHe shakes his head.\n'Wrong guy, man.'",
                        ],
                    "effects": {},
                    "options": None
                },
                "tooth_01_chat_neutral": {
                    "says": ["'Dang, hate to think someone ruined that pretty smile.'\nHe winces, regretting his words.\n'I mean, hate to think someone killed her...'"],
                    "effects": {},
                    "options": None
                },
                "tooth_01_grill_neutral": {
                    "says": ["'What do you expect me to say? Her tooth got knocked out... Guess she was hit hard in the mouth. Right?'",
                        ],
                    "effects": {},
                    "options": None
                },
                "bruising_01_chat_neutral": {
                    "says": ["'Try talking to the Mortician if you want info on that kind of stuff.'"],
                    "effects": {},
                    "options": None
                },
                "bruising_01_grill_neutral": {
                    "says": ["'You think that I beat her or something? For what? Beating me at cards?'\nHe shifts uncomfortably in his seat.",
                             "'Well, I can tell you she didn't have a bruise when I saw her last night. Not that I saw that much of her... "
                             "I mean, her forearms and head didn't have bruises - maybe she had them somewhere else. Or I don't know, probably not. All I'm saying is, I ain't see no bruises.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "wounds_01_chat_neutral": {
                    "says": ["'Crazy - gotta be a real sicko to do something like that. Or have some personal reason...'\nHe shrugs."],
                    "effects": {},
                    "options": None
                },
                "wounds_01_grill_neutral": {
                    "says": ["'How the hell am I supposed to know anything about her wounds? Try asking the Mortician - that's like, his thing.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_chat_neutral": {
                    "says": ["'Well, guess you found the murder weapon, huh?'"],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_grill_neutral": {
                    "says": ["'Detective, everyone uses a knife 'round here. Hate to break it to you.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_chat_neutral": {
                    "says": ["'Not too sure how to help. Try snooping around, looking for a gun.'"],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_grill_neutral": {
                    "says": ["'I don't have a gun, promise you that. Wish I did though.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_chat_neutral": {
                    "says": ["'Guess anyone could of just grabbed it, and swung for the fences, huh?'"],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_grill_neutral": {
                    "says": ["'I got nothing for that, Detective - anyone with arms could grab it and swing that thing around, no?'"
                        ],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_chat_neutral": {
                    "says": ["'They gotta be someones... Check what brand they are.'"],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_grill_neutral": {
                    "says": ["'Try to see who smokes those cigarettes. It could be anyone.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_chat_neutral": {
                    "says": ["'That's gotta be from someone who smokes pipe - obvious I know, but it's something.'"],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_grill_neutral": {
                    "says": ["'I don't smoke pipe tobacco, never touched loose leaf. I only smoke pre-made cigarettes.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "scrap_leather_01_chat_neutral": {
                    "says": ["'Well, I guess someone there was wearing leather... If its not Debbie's, it's gotta be the murderer.'"],
                    "effects": {},
                    "options": None
                },
                "scrap_leather_01_grill_neutral": {
                    "says": ["'Not sure whose that could be. But I don't wear leather, ever - hate that material. Bertha likes it - try asking her.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "scrap_denim_01_chat_neutral": {
                    "says": ["'Well, if you found denim there, I guess it's either Debbie's or the murderers... Don't recall Debbie wearing denim...'"],
                    "effects": {},
                    "options": None
                },
                "scrap_denim_01_grill_neutral": {
                    "says": ["'Now, lets not jump to any conclusions...'\nHe wipes his hands on his denim jeans, nervous."
                        ],
                    "effects": {},
                    "options": None
                },
                "scrap_suit_01_chat_neutral": {
                    "says": ["'Suit's are pretty common around here - sorry bud.'"],
                    "effects": {},
                    "options": None
                },
                "scrap_suit_01_grill_neutral": {
                    "says": ["'Look, I know it's not a good look...'\nHe pulls his suit tighter across his torso.\n'No way that's from me - try asking Bertha.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "hair_01_chat_neutral": {
                    "says": ["'My favorite.\n He tightens his fedora onto his head. You don't see a shred of hair coming out the sides.'", ],
                    "effects": {},
                    "options": None
                },
                "hair_01_grill_neutral": {
                    "says": ["'Everyone has hair here!!!'", ],
                    "effects": {},
                    "options": None
                },
                "fridge_01_chat_neutral": {
                    "says": ["'Bertha keeps the food there, it's a pretty easy going, public kind of fridge, you know?.'", ],
                    "effects": {},
                    "options": None
                },
                "fridge_01_grill_neutral": {
                    "says": ["'It's Bertha's fridge, you should be asking her about it.'", ],
                    "effects": {},
                    "options": None
                },
                "debbie_01_chat_neutral": {
                    "says": ["'I only met her last night. Pretty gal. Tried to walk her home, but she turned down my offer. Oh well...'", ],
                    "effects": {},
                    "options": None
                },
                "debbie_01_grill_neutral": {
                    "says": ["'That damned dead damsel... Real shame. I saw her and Bertha argue last night - couldn't hear the details.'", ],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_chat_neutral": {
                    "says": ["'Just a knife to cut up food. Like a sandwich.'" ],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_grill_neutral": {
                    "says": ["'Anyone around here can take one of those to use - it's just for food.'" ],
                    "effects": {},
                    "options": None
                },
                "revolver_01_chat_neutral": {
                    "says": ["'Whoa, I never knew that was there. Interesting...'", ],
                    "effects": {},
                    "options": None
                },
                "revolver_01_grill_neutral": {
                    "says": ["'Honestly - first I'm hearing about a revolver here. I know some of the gang here's got guns, but it's pretty rare...'\nHe looks around the room, a bit nervous.", ],
                    "effects": {},
                    "options": None
                },
                "bullets_01_chat_neutral": {
                    "says": ["'I guess bullets plus a gun.. You do the math.'", ],
                    "effects": {},
                    "options": None
                },
                "bullets_01_grill_neutral": {
                    "says": ["'Yeah, those aren't mine - I'm sure you can tell based on where you found it.'", ],
                    "effects": {},
                    "options": None
                },
                "revolver_02_chat_neutral": {
                    "says": ["'That's from the Mortician, you say? Haven't seen him in ages...'", ],
                    "effects": {},
                    "options": None
                },
                "revolver_02_grill_neutral": {
                    "says": ["'Never seen that before, and truth be told, I haven't seen the Mortician in ages anyways.", ],
                    "effects": {},
                    "options": None
                },

                "matches_01_chat_neutral": {
                    "says": ["'Amazing... Very nice...'",
                             "'Look at the off black coloring...The subtle thickness of it..'",
                             "'My god, it even has the logo engraved.'"],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_neutral": {
                    "says": [
                        "'Those are new eh, and you can only take one of those, and ONLY if you need it.'\nHe looks at you, stern."],
                    "effects": {},
                    "options": None
                },
                "matches_02_chat_neutral": {
                    "says": [
                        "'I may or may not have a few of those.' \nHe laughs, suddenly fanning out 5 in some sort of magic trick, before making them vanish."],
                    "effects": {},
                    "options": None
                },
                "matches_02_grill_neutral": {
                    "says": [
                        "'Those old things? They are a thing of the past, hence why I grabbed so many of those new ones.'"
                        "'\nWithout warning, he conjures a black and brown matchbook in each hand, as if pulling it out of thin air."
                        "\nHe gives you a knowing look.'"],
                    "effects": {},
                    "options": None
                },
                "flask_01_chat_neutral": {
                    "says": [
                        "'Can't be out in public without one of those!'\nHe adjusts his suit, revealing his flask holstered to his side like a gun."],
                    "effects": {},
                    "options": None
                },
                "flask_01_grill_neutral": {
                    "says": [
                        "'Everyone has a flask, Detective. Honest. I'd be shocked if you found someone who didn't. Except Debbie - I remember she didn't have one, and I was shocked.'"],
                    "effects": {},
                    "options": None
                },
                "gin_01_chat_neutral": {
                    "says": ["'Ewwwwwww - please, never mention that around me again.'\nHe shivers.",
                             "'I swear, I hate that stuff so much. Who wants to drink a pine tree?..'"],
                    "effects": {},
                    "options": None
                },
                "gin_01_grill_neutral": {
                    "says": ["'That's not a drink if you ask me. Bertha likes it though, because shes a fucking weirdo.'",],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_chat_neutral": {
                    "says": ["'Nice, a man's drink. Now were talking.'",],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["'Relax - I love the stuff. I can't imagine a guy around here not liking it, in all seriousness.'",],
                    "effects": {},
                    "options": None
                },
                "rum_01_chat_neutral": {
                    "says": ["'Rum is great. Smooth, sweet, rich... Gotta love it.'",],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["'If it helps, I know Bertha like it too.'",],
                    "effects": {},
                    "options": None
                },
                "tomato_01_chat_neutral": {
                    "says": ["'That's served everyday - you can grab some from the fridge if you'd like.'"],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["'You really grilling me over tomato soup? What are you expecting me to say? Everyone likes it...'", ],
                    "effects": {},
                    "options": None
                },
                "mustard_01_chat_neutral": {
                    "says": ["'mmmMMMMMmmm. MUSTARD IS AMAZING!!!!'\nHe gets strangely excited."],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": [
                        "'That sandwich is crazy good - dijon, ham, lettuce... did I mention dijon? Delicious... \nNot sure how that helps you, but there you are.'", ],
                    "effects": {},
                    "options": None
                },
                "pie_01_chat_neutral": {
                    "says": [
                        "'No thanks. It makes my tummy grumbly.'"],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_neutral": {
                    "says": ["He squirms in place. \n'Bertha likes pie!' He blurts.", ],
                    "effects": {},
                    "options": None
                },

                "lighter_01_chat_neutral": {
                    "says": [ "'If I didn't have an infinite supply of matchbooks, I might consider using a lighter.'"
                        ],
                    "effects": {},
                    "options": None
                },
                "lighter_01_grill_neutral": {
                    "says": ["'That's Debbie's - I don't think I've seen anyone around here use a lighter, except her...'", ],
                    "effects": {},
                    "options": None
                },
                "cardigan_01_chat_neutral": {
                    "says": [ "'She dresses pretty low key, I gotta say.'"],
                    "effects": {},
                    "options": None
                },
                "cardigan_01_grill_neutral": {
                    "says": ["'Not sure how to help - she wore a cardigan for the cold, and a green dress underneath.'", ],
                    "effects": {},
                    "options": None
                },
                "cardigan_scraps_01_chat_neutral": {
                    "says": [ "'Wish I could help, but I haven't seen anything like that.'"],
                    "effects": {},
                    "options": None
                },
                "cardigan_scraps_01_grill_neutral": {
                    "says": ["'Detective, what am I supposed to say? I put those there? I don't know what those are, but clearly from the crime somehow..'", ],
                    "effects": {},
                    "options": None
                },
                "glass_01_chat_neutral": {
                    "says": [ "'Eh, I prefer to just use my flask.'"],
                    "effects": {},
                    "options": None
                },
                "glass_01_grill_neutral": {
                    "says": ["'Debbie drank from one of those last night - I remember because she got her lipstick on it. It should still be around, either here, or maybe backstage.'", ],
                    "effects": {},
                    "options": None
                },
                "lipstick_01_chat_neutral": {
                    "says": [ "'Oh, can you bring me some? I just ran out.'\nHe laughs to himself."],
                    "effects": {},
                    "options": None
                },
                "lipstick_01_grill_neutral": {
                    "says": ["'I remember Debbie kept a tube with her. Probably hers.'", ],
                    "effects": {},
                    "options": None
                },
                "cigs_01_chat_neutral": {
                    "says": [
                        "Suddenly, he starts double fisting cigarettes, creating enormous quantities of smoke.\n'Sorry, couldnt hear you!'", ],
                    "effects": {},
                    "options": None
                },
                "cigs_01_grill_neutral": {
                    "says": [
                        "He eats a cigarette, staring you dead in the eye. Through a mouthful, he starts talking. \n'Ever see that done before? New trick I'm working on'", ],
                    "effects": {},
                    "options": None
                },
                "cigs_02_chat_neutral": {
                    "says": [
                        "Without warning, he starts smoking as fast as possible, cigarettes in each hand. The amount of smoke he creates is preposterous."
                        "\n'Not a bad trick eh? What do you think!'", ],
                    "effects": {},
                    "options": None
                },
                "cigs_02_grill_neutral": {
                    "says": [
                        "'What's that, behind your ear?'\n He reaches behind your ear, pulling out a premium cigarette with a silver filter. \n'Thought I lost this, thanks!' he says as he lights it.", ],
                    "effects": {},
                    "options": None
                },
                "smoke_pipe_01_chat_neutral": {
                    "says": [
                        "'Not my thing - I prefer pre-made cigarettes. Kind of a pain to have to clean it and all that...'", ],
                    "effects": {},
                    "options": None
                },
                "smoke_pipe_01_grill_neutral": {
                    "says": [
                        "'I know Bertha uses one of those. But I hate em.'", ],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_chat_neutral": {
                    "says": ["'That stuff is for snobs.'\nHe tips his fedora."],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_grill_neutral": {
                    "says": ["'I never, ever, have ONCE, touched that mockery of a tobacco leaf in my life.'", ],
                    "effects": {},
                    "options": None
                },
                "earring_01_chat_neutral": {
                    "says": ["'Debbie wore ear rings that night - small, copper hoops, right?'"],
                    "effects": {},
                    "options": None
                },
                "earring_01_grill_neutral": {
                    "says": ["'If it helps, Bertha makes a point to never wear em. As do I.'", ],
                    "effects": {},
                    "options": None
                },
                "denim_jacket_01_chat_neutral": {
                    "says": ["'Not sure whose that is. I think denim jackets are so tacky, don't you? It only belongs on pants.'"],
                    "effects": {},
                    "options": None
                },
                "denim_jacket_01_grill_neutral": {
                    "says": ["'Definitely not mine, but I know Bertha loves her denim jackets.'", ],
                    "effects": {},
                    "options": None
                },
                "leather_jacket_01_chat_neutral": {
                    "says": ["'Leather isn't really my style. I'm more of a.. business casual kinda guy.'"],
                    "effects": {},
                    "options": None
                },
                "leather_jacket_01_grill_neutral": {
                    "says": ["'I know Bertha loves her leather jackets, she probably is wearing one now. If not, I bet she's wearing a denim jacket.'", ],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_chat_neutral": {
                    "says": ["'Love the look of that thing - matches my suit perfectly, same material and everything.'"],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_grill_neutral": {
                    "says": ["'That one by the entrance, in the lounge - that's mine.\nHe tugs on his suit. 'Cashmere, baby.'", ],
                    "effects": {},
                    "options": None
                },
                "high_heels_01_chat_neutral": {
                    "says": ["'Oh, those are mine.'\nHe chuckles, then coughs as he inhales spit."],
                    "effects": {},
                    "options": None
                },
                "high_heels_01_grill_neutral": {
                    "says": ["'It's gotta be Debbies right? She wore those last night. Not too high a high heel, but a high heel none the less.'", ],
                    "effects": {},
                    "options": None
                },
                "sneakers_01_chat_neutral": {
                    "says": ["'Everyone here's gotta pair of those, no?..'"],
                    "effects": {},
                    "options": None
                },
                "sneakers_01_grill_neutral": {
                    "says": ["'Bertha's got sneakers, as do I. I mean, they are just shoes after all...'", ],
                    "effects": {},
                    "options": None
                },
                "dress_shoes_01_chat_neutral": {
                    "says": ["'Can't have a fancy suit without a matching pair of fancy shoes...'\nHe tips his fedora."],
                    "effects": {},
                    "options": None
                },
                "dress_shoes_01_grill_neutral": {
                    "says": ["'I'd imagine anyone wearing formal wear also has dress shoes somewhere around. I keep both a pair of dress shoes and sneakers at the front.'", ],
                    "effects": {},
                    "options": None
                },
                "workboots_01_chat_neutral": {
                    "says": ["'Aren't those just the ugliest things you've ever seen?'"],
                    "effects": {},
                    "options": None
                },
                "workboots_01_grill_neutral": {
                    "says": ["'I would never wear those - what am I, pouring asphalt?'", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_chat_neutral": {
                    "says": ["'I've only been in town a few days myself, and let me tell you, that gal can.. pour a mean drink.'", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_grill_neutral": {
                    "says": ["'She seems to hang around a rough bunch. And from the sounds of it, she's been living here ages.'", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_chat_neutral": {
                    "says": ["'Ah, the finest man in this town.'","He gestures around.\n'The most winningest of winners in the history of winning!'", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_grill_neutral": {
                    "says": ["'He stares at you blankly.\n'Never heard of him.'", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_chat_neutral": {
                    "says": ["'I haven't seen him in ages, but I distinctly remember the day after I bought my suit, he bought something similar. Can you believe it?" ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["He looks at you, suddenly serious.\n"
                             "'Detective, I swear I see him out late at night, prowling the cemetery. "
                             "I think he might be...\nHe swallows.\n'EATING PEOPLE!' "
                             "He shivers dramatically.", ],
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
                "grease_01_chat_neutral": {
                    "says": ["'No thanks. It makes my tummy grumbly.'"],
                    "effects": {},
                    "options": None
                },
                "grease_01_grill_neutral": {
                    "says": ["'No!' he says forcefully. 'Im serious about my health when it comes to eating.'", ],
                    "effects": {},
                    "options": None
                },
                "white_wine_01_chat_neutral": {
                    "says": [
                        "omg!?!? GIRLLSS NIGHT!!!\n'I mean.' He looks at you deadpan. 'What am I, some sort of sissy?'"],
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
                #additional states as needed
            },
        },
        "conditional": [ #witness statements
            {
                "conditions": {"traits":["bertha"]}, #murderer traits here; has to be like this to follow check condition format for items - possible other conditions?
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "bertha_01_chat_neutral": {
                            "says": ["'I heard her and Debbie argue yesterday - it actually seemed a bit intense. I dont know the details.'",
                                     "'Bertha is cool, but she hangs with a rough crowd. Keep an eye on her.'"],
                            "effects": {},
                            "options": "default_1"
                        },
                        "bertha_01_grill_neutral": {
                            "says": ["'After Debbie sang, she and Bertha got into a fight - nothing crazy, but Bertha actually seemed really mad. Not sure why...'",
                                     "'I swear I saw Bertha angrier last night than any other night - not saying she did it, but look into it.'"

                                     ],
                            "effects": {},
                            "options": "default_1"
                        }
                    }
                }
            },{
                "conditions": {"traits":["gibbs","knife"]}, #murderer traits here; has to be like this to follow check condition format for items - possible other conditions?
                "dialogue": { #will add all these nodes to dialogue if all conditions in murderer profile
                    "default": {
                        "kitchen_knife_01_chat_neutral": {
                            "says": ["'You got me. I snuck into the kitchen, took one, and stabbed Debbie repeatedly! Case solved!!!'\nHe looks at you sarcastically." ],
                            "effects": {},
                            "options": None
                        },
                        "kitchen_knife_01_grill_neutral": {
                            "says": ["'I don't like using them, because... like...'\nHe swallows.\n'I might cut myself!'." ],
                            "effects": {},
                            "options": None
                        },
                        "murder_knife_01_grill_neutral": {
                            "says": ["Sweat beads on his forehead.\n'Well, everyone in this town has access to a knife - but it's a start.'" ],
                            "effects": {},
                            "options": None
                        },
                    }
                }
            },
        ]
    },
    "mortician_01": {
        "non_topic": {
            "default": {
                "greet_neutral": {
                    "says": ["'Hello...'", "'Yes?'","'Can I help you?'","'I'm busy, let's make it quick...'",
                             "'How are you this {current_phase}?'", "'Detective, a pleasure...'"
                             ],
                    "options": "default_1"
                },
                "redirect_neutral": {
                    "says": ["He clears his throat.","'And now?..'","'Can we speed things along?'","'What next, Detective...'",
                             "'Is there more?..'","'What else?..'"
                             ],
                    "effects": {},
                    "options": "default_1"
                },
                "bye_neutral": {
                    "says": ["'Goodbye...''","'Farewell...'","'See you, Detective...'", "'Enjoy your day, Detective...'"],
                },
            },
            #additional states as needed
        },
        "topic": {
            "default": {
                #REACTIONS
                "react_chat_neutral": {
                    "says": ["He looks at you, blankly.", "'Oh yes... {topic}...'", "'Hmmm, {topic}..'",
                             "'Ah yes...'", "'{topic}?.. '", "'Yes, yes, {topic}...'",
                             "His face never changes.", "He takes his time talking.", "His response is monotone and dry.",
                             ],
                },
                "react_grill_neutral": {
                    "says": ['His eyes grow distant.', "'{topic}? Let me think...'", "'Indeed, yes, {topic}...'",
                             "'Hmm, let me think...'", "'{topic}? Hmm..'","'Just a moment, please...'\nA beat passes.",
                             "A beat passes before he responds.", "He shrugs his shoulders.", "'Well, '",
                             "He clears his throat before answering."],
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
                    "says": ["'I really don't know much about that...'","'Afraid I'm not much of a conversationalist...'", "'What is there to say?.. '",
                             "'Not too sure what to say... Perhaps we chat about something else?'","'I don't have anything interesting to say about that...'"],
                    "effects": {},
                    "options": None
                },
                "unknown_grill_neutral": {
                    "says": ["'I really dont know what to say about {topic}...'","'Afraid I can't help you with that...'",
                             "'I wish I could help you with {topic}, but I can't...'","Honestly, I don't know what to say...",
                             "'Is there anything specific you wanted to know? I'm sorry, I can't help you with that...'"
                             ],
                    "effects": {},
                    "options": None
                },
                "night of the murder_chat_neutral": {
                    "says": ["'I'm always here in the office, working... Although I do enjoy my late night walks...'" ],
                    "effects": {},
                    "options": None
                },
                "night of the murder_grill_neutral": {
                    "says": ["'I keep to myself, and only leave this place on my late night walks... I don't have much else to tell you...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_matchbook_01_chat_neutral": {
                    "says": ["'That's a start... '" ],
                    "effects": {},
                    "options": None
                },
                "murder_matchbook_01_grill_neutral": {
                    "says": ["'Is there something particular about a matchbook you'd like to know?.. I use matches, much like the rest of town here...'" ],
                    "effects": {},
                    "options": None
                },
                "blood_01_chat_neutral": {
                    "says": ["'Must have been... Quite a sight..'" ],
                    "effects": {},
                    "options": None
                },
                "blood_01_grill_neutral": {
                    "says": ["'She lost roughly 3-4 liters by my estimation, although of course, more measurements are needed...'" ],
                    "effects": {},
                    "options": None
                },
                "tooth_01_chat_neutral": {
                    "says": ["'Yes, I noticed that she was missing her left incisor...'" ],
                    "effects": {},
                    "options": None
                },
                "tooth_01_grill_neutral": {
                    "says": ["'I'd imagine the strike to the front of her face was responsible for dislodging that tooth...'" ],
                    "effects": {},
                    "options": None
                },
                "bruising_01_chat_neutral": {
                    "says": ["'Yes, yes. I saw it too... Anything specific?'" ],
                    "effects": {},
                    "options": None
                },
                "bruising_01_grill_neutral": {
                    "says": ["'I believe those were inflicted prior to her death - although I would need to collect more information...'" ],
                    "effects": {},
                    "options": None
                },
                "wounds_01_chat_neutral": {
                    "says": ["'Quite gruesome... I haven't had a murder victim here in quite some time actually - it was refreshing to investigate...'" ],
                    "effects": {},
                    "options": None
                },
                "wounds_01_grill_neutral": {
                    "says": ["'I imagine that those were the cause of death... As I'm sure you could surmise...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_chat_neutral": {
                    "says": ["'Well, your description seems to match the wounds...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_knife_01_grill_neutral": {
                    "says": ["'Unfortunately, I don't have more information to yield regarding the bloody knife...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_chat_neutral": {
                    "says": ["'Yes, indeed... That would be expected given the wounds...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_gun_01_grill_neutral": {
                    "says": ["'I think it was expected that bullet wounds would have corresponding evidence at the scene of the crime...'" ],
                    "effects": {},
                    "options": None
                },
                "pipe_01_chat_neutral": {
                    "says": ["'Down in the alley, you say?..\nHe forms a wrinkled smirk. 'Only thing I could use that for is a walking stick...' '" ],
                    "effects": {},
                    "options": None
                },
                "pipe_01_grill_neutral": {
                    "says": ["'Not much I could tell you about a metal pipe... Too weak to work with that stuff nowadays...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_chat_neutral": {
                    "says": ["'Well, someone with a strong arm must have used that...'\nHe groans as he tests his shoulder.\n'Sometimes, I miss my youth...'" ],
                    "effects": {},
                    "options": None
                },
                "murder_pipe_01_grill_neutral": {
                    "says": ["'That matches the blunt trauma...'\nHe chuckles, his laugh coarse and dry.\n'Such a barbaric way to kill someone.'" ],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_chat_neutral": {
                    "says": ["'That must have spilled out during the commotion...'" ],
                    "effects": {},
                    "options": None
                },
                "spilled_cigs_01_grill_neutral": {
                    "says": ["'I would examine the location and type of cigarettes.. Why and when was it spilled, and who might carry such an item on their person...'" ],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_chat_neutral": {
                    "says": ["'Likely spilled out during the commotion...'" ],
                    "effects": {},
                    "options": None
                },
                "spilled_tobacc_01_grill_neutral": {
                    "says": ["'Well, we know there were two people at the scene of the crime. Did it spill before or after the murder? Then, who might have carried such an item...'" ],
                    "effects": {},
                    "options": None
                },
                "hair_01_chat_neutral": {
                    "says": ["'Its quite a common hair type, unfortunately...'\nHe gestures to his black hair.\n'Too common...'", ],
                    "effects": {},
                    "options": None
                },
                "hair_01_grill_neutral": {
                    "says": ["'I'm lucky enough to keep my youthful hair into my old age, but now it comes back to haunt me...'\n"
                             "He lets out a dry laugh, shaking medium black hair out of his eyes." ],
                    "effects": {},
                    "options": None
                },
                "debbie_01_chat_neutral": {
                    "says": ["'Truth be told, I haven't actually heard of her until she was transported here...'"
                             "\nHis head jerks towards the back. 'She's ready for your investigation, just down the hall...'", ],
                    "effects": {},
                    "options": None
                },
                "debbie_01_grill_neutral": {
                    "says": ["'Take a look yourself, I have her ready in refrigeration, just down the hall...'" ],
                    "effects": {},
                    "options": None
                },
                "morgue_tools_01_chat_neutral": {
                    "says": ["'Those are essential tools in any morgue...'", ],
                    "effects": {},
                    "options": None
                },
                "morgue_tools_01_grill_neutral": {
                    "says": ["'You can take a look yourself... It's a generic set of autopsy equipment...'" ],
                    "effects": {},
                    "options": None
                },
                "ashtray_01_chat_neutral": {
                    "says": ["'If you smoke here, please use that... Frankly, I'm not used to visitors, I'm making an exception for you...'", ],
                    "effects": {},
                    "options": None
                },
                "ashtray_01_grill_neutral": {
                    "says": ["'Well, Detective... It's just an ashtray...'" ],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_chat_neutral": {
                    "says": ["'A kitchen knife is a basic utensil...'", ],
                    "effects": {},
                    "options": None
                },
                "kitchen_knife_01_grill_neutral": {
                    "says": ["'I have nothing useful to say, aside from the obvious: a kitchen knife is a must have in... a kitchen.'" ],
                    "effects": {},
                    "options": None
                },
                "revolver_02_chat_neutral": {
                    "says": ["'That is indeed mine...'", ],
                    "effects": {},
                    "options": None
                },
                "revolver_02_grill_neutral": {
                    "says": ["'I tend to keep it on my person when I go out... A man my age needs something like that around here...'" ],
                    "effects": {},
                    "options": None
                },
                "bullets_01_chat_neutral": {
                    "says": ["'You need bullets for a gun...'", ],
                    "effects": {},
                    "options": None
                },
                "bullets_01_grill_neutral": {
                    "says": ["'One is useless without the other... Were you looking for something specific?..'" ],
                    "effects": {},
                    "options": None
                },
                "porch_table_01_chat_neutral": {
                    "says": ["'In front of the pub, on the porch?'\nA wry smile works it's way across his face.\n'Ah, I remember I used loiter there, a long time ago...'", ],
                    "effects": {},
                    "options": None
                },
                "porch_table_01_grill_neutral": {
                    "says": ["'You know, I actually helped build that when I was... Maybe 14 years old.. Funny you bring it up, all these years later...'" ],
                    "effects": {},
                    "options": None
                },
                "matches_01_chat_neutral": {
                    "says": ["'Never seen those before. Are they new?'"],
                    "effects": {},
                    "options": None
                },
                "matches_01_grill_neutral": {
                    "says": ["'Truthfully, I've never seen those before... I only use the brown ones...'" ],
                    "effects": {},
                    "options": None
                },
                "matches_02_chat_neutral": {
                    "says": ["'Yes, I have plenty of those - you can take one if you'd like...'"],
                    "effects": {},
                    "options": None
                },
                "matches_02_grill_neutral": {
                    "says": ["'Those are the matches I use - just as many others use... They are quite common around here...'"],
                    "effects": {},
                    "options": None
                },
                "flask_01_chat_neutral": {
                    "says": ["'I keep it close by, in case my throat feels parched...'"],
                    "effects": {},
                    "options": None
                },
                "flask_01_grill_neutral": {
                    "says": ["'You will be hard pressed to find someone who doesn't have a flask in this town...'"],
                    "effects": {},
                    "options": None
                },
                "gin_01_chat_neutral": {
                    "says": ["'A wonderful drink, sharp and refreshing... I have a bottle somewhere around here...'"],
                    "effects": {},
                    "options": None
                },
                "gin_01_grill_neutral": {
                    "says": ["'Did you want some? I buy it from Fisherman Phil, like everyone else...'"],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_chat_neutral": {
                    "says": ["'Very nice, delicious drink.. Quite a nice bite to it..'"],
                    "effects": {},
                    "options": None
                },
                "whiskey_01_grill_neutral": {
                    "says": ["'Most the men around town enjoy the whiskey... If that helps..'"],
                    "effects": {},
                    "options": None
                },
                "rum_01_chat_neutral": {
                    "says": ["'A bit too sweet and tangy for my taste...'",],
                    "effects": {},
                    "options": None
                },
                "rum_01_grill_neutral": {
                    "says": ["'I'm sure its quite popular, but I don't care for it...'",],
                    "effects": {},
                    "options": None
                },
                "tomato_01_chat_neutral": {
                    "says": ["'I don't really like tomatoes...'"],
                    "effects": {},
                    "options": None
                },
                "tomato_01_grill_neutral": {
                    "says": ["'If I recall, that was the daily dish at the pub.. That might of changed. I never liked it.'",],
                    "effects": {},
                    "options": None
                },
                "mustard_01_chat_neutral": {
                    "says": ["'Dijon, with ham and rye. My favorite.'"],
                    "effects": {},
                    "options": None
                },
                "mustard_01_grill_neutral": {
                    "says": ["'I'm afraid I have nothing useful to tell you about mustard... Is it relevant to your investigation?..'",],
                    "effects": {},
                    "options": None
                },
                "pie_01_chat_neutral": {
                    "says": ["'Very nice, tart flavor - the blueberries are quite fresh this time around.' "],
                    "effects": {},
                    "options": None
                },
                "pie_01_grill_neutral": {
                    "says": ["'Was there a specific piece of information you were expecting about pie?.. I like it - I'm afraid that's all I know...'",],
                    "effects": {},
                    "options": None
                },
                "lighter_01_chat_neutral": {
                    "says": ["'I'm a dog stuck in his old ways - I don't think I'll ever not use my matchbooks...' "],
                    "effects": {},
                    "options": None
                },
                "lighter_01_grill_neutral": {
                    "says": ["'I'm sure someone in town uses a lighter - but personally, I like matches...'",],
                    "effects": {},
                    "options": None
                },
                "cardigan_01_chat_neutral": {
                    "says": ["'Not sure what I can say about her clothes..'"],
                    "effects": {},
                    "options": None
                },
                "cardigan_01_grill_neutral": {
                    "says": ["'Detective, just inspect it yourself. I don't have any more info to give you about that.'",],
                    "effects": {},
                    "options": None
                },
                "cardigan_scraps_01_chat_neutral": {
                    "says": ["'Hmmm... I wonder if it's from Debbie's cardigan?'"],
                    "effects": {},
                    "options": None
                },
                "cardigan_scraps_01_grill_neutral": {
                    "says": ["'It sounds like fine shreds of wool, no? They likely tore from Debbie's cardigan during a scramble...'",],
                    "effects": {},
                    "options": None
                },
                "cigs_01_chat_neutral": {
                    "says": ["'Those are commonplace... But I hate them.'",],
                    "effects": {},
                    "options": None
                },
                "cigs_01_grill_neutral": {
                    "says": ["'I never smoke those, they are way too dry... Either premium cigarettes, or pipe for me...'",],
                    "effects": {},
                    "options": None
                },
                "cigs_02_chat_neutral": {
                    "says": ["'Great brand, terrific...'",],
                    "effects": {},
                    "options": None
                },
                "cigs_02_grill_neutral": {
                    "says": ["'Excellent quality, I much prefer them to the generic brand, which I find much too harsh...'",],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_chat_neutral": {
                    "says": ["'Those leaves are always quite fresh, I find...'","'Great, thick leaves which burn real slow.. It can be annoying to clean though.'",],
                    "effects": {},
                    "options": None
                },
                "tobacco_01_grill_neutral": {
                    "says": ["'Not sure how I can help your investigation on this topic - but I like smoking pipe using that.. If I recall, I actually introduced Bertha to it as well...'"],
                    "effects": {},
                    "options": None
                },

                "fibers_01_chat_neutral": {
                    "says": ["'It isn't uncommon to find something under a victims nails, if not just regular dirt and debris...'", ],
                    "effects": {},
                    "options": None
                },
                "fibers_01_grill_neutral": {
                    "says": [
                        "'If she clawed at her attacker, there may be some useful clues under those...'"],
                    "effects": {},
                    "options": None
                },
                "denim_jacket_01_chat_neutral": {
                    "says": ["'I hate denim, it's just... Not my aesthetic.'", ],
                    "effects": {},
                    "options": None
                },
                "denim_jacket_01_grill_neutral": {
                    "says": [
                        "'I don't think I've ever worn denim. I remember Bertha was quite fond of her denim jacket though...'"],
                    "effects": {},
                    "options": None
                },
                "leather_jacket_02_chat_neutral": {
                    "says": ["'Quite a nice jacket, I must say. Don't you agree?'", ],
                    "effects": {},
                    "options": None
                },
                "leather_jacket_02_grill_neutral": {
                    "says": [
                        "'That's mine - out there in the front? I think it goes well with my suit..'"],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_chat_neutral": {
                    "says": ["'I don't think I've seen that exact pair, but it sounds similar to mine...'", ],
                    "effects": {},
                    "options": None
                },
                "suit_jacket_02_grill_neutral": {
                    "says": [
                        "'Well, a suit is quite common to wear. From the sound of it, it may as well be the same one I'm wearing...'"],
                    "effects": {},
                    "options": None
                },
                "sneakers_01_chat_neutral": {
                    "says": ["'Those don't really go with my outfit... Neither classy, or useful...'", ],
                    "effects": {},
                    "options": None
                },
                "sneakers_01_grill_neutral": {
                    "says": [
                        "'I don't own a pair of sneakers.'\nHe wiggles his feet. 'I prefer dress shoes...'"],
                    "effects": {},
                    "options": None
                },
                "workboots_01_chat_neutral": {
                    "says": ["'Those next to the door are mine.. They are pretty useful to own...'", ],
                    "effects": {},
                    "options": None
                },
                "workboots_01_grill_neutral": {
                    "says": [
                        "'While they don't really go with my suit, I find they are very practical - I wear them on my walks sometimes, if I don't feel like dirtying my dress shoes...'"],
                    "effects": {},
                    "options": None
                },
                "bertha_01_chat_neutral": {
                    "says": ["'A Bertha, it's been quite some time since I talked to her... Is she doing well?'", ],
                    "effects": {},
                    "options": None
                },
                "bertha_01_grill_neutral": {
                    "says": ["'I haven't seen her in.. probably a few months is all. But it feels like longer.'", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_chat_neutral": {
                    "says": ["'He's the new gambler in town, yes?... I've heard bits and pieces, but never met him..'", ],
                    "effects": {},
                    "options": None
                },
                "gibbs_01_grill_neutral": {
                    "says": ["'Word is, he has trouble crediting his debtors... \nNot a good reputation to have.'", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_chat_neutral": {
                    "says": ["'I'm just the old town mortician... too old now, with a bad back and shoulder...'\nHe shrugs gingerly, testing his shoulder.", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_neutral": {
                    "says": ["'Well, I've lived here near all my life, from a youthful young boy, to an old, frail man...' \nHe adjusts his posture, grimacing as he moves his back.", ],
                    "effects": {},
                    "options": None
                },
                "mortician_01_grill_bad": {
                    "says": ["'I'm afraid I'm not that interesting... I just take care of the dead people here...'", ],
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