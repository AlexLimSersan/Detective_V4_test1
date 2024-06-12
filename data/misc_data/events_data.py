events_data = {
    "band_playing": {
        "conditions": { #conditions for event, can have vibe, suspect mood, time, weather, player loc, etc
            "time": ["evening", "night"], #any of these times it happens!
        },
        "descriptions": {
            #dic of locs(can hear)/time/description; default loc and time, then weighted!
        }
    },
    "backroom_intro": {
        "conditions": {
            "location": "backroom_door", #current location
        },
    },
    # Add more events as needed
}