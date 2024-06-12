
loc_description_template = {
    "entity_id": {
        "default": {
            "approaching": {
"neutral": [], "good": [], "bad": [],
            },
            "at_entity": {
"neutral": [], "good": [], "bad": [],
            },
            "leaving": {
"neutral": [], "good": [], "bad": [],
            },
            "times": {
                "morning": [""],
                "afternoon": [""],
                "evening": [""],
                "night": [""],
            },
            "weather": {
                "rain": [""],
                "sunny": [""],
                "grey": [""],
            },
            "tags": {}, #choose from: "urban", "rural", "indoors" (this is passed to the weather system to add weather description types)
            "connections": {
                # these descriptions are given to the keyed id, when the player is at that keyed id. so the perspective is from that keyed id, looking at this id.
                "connection_id_1": {
                    "neutral": [""],
                    "good": [""],
                    "bad": [""],
                },
                "connection_id_2": {
                    "neutral": [""],
                    "good": [""],
                    "bad": [""],
                }
        },
        #IGNORE FOR NOW PLEASE: more states/events as needed here
    },
    #new entities starts here
}
}