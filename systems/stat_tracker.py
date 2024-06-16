from config.logging_config import app_logger


class Stat_Tracker:
    def __init__(self):
        self.game_state = None
        self.murderer = None #INITIALIZED from suspect manager when suspects are spawned
        self.murder_clues_tracker = {} #condition: [{item_id: spawn_locs}]
        self.murder_cleanup_tracker = {} #item: starting_state

    def track_murderer(self, item_id, murder_condition, query_type, state_or_spawn_id):

        if query_type == "spawn":
            app_logger.info(f"{query_type}: {item_id}: {murder_condition}: {state_or_spawn_id}")
            for condition in murder_condition:
                if condition not in self.murder_clues_tracker:
                    self.murder_clues_tracker[condition] = []
                #just for clarity:
                spawn_locs = state_or_spawn_id
                self.murder_clues_tracker[condition].append({item_id: spawn_locs})
                # for example, knife condition = knife_wounds_01
        if query_type == "state":
            if item_id not in self.murder_cleanup_tracker:
                self.murder_cleanup_tracker[item_id] = []
            # just for clarity:
            starting_state = state_or_spawn_id
            self.murder_cleanup_tracker[item_id].append(starting_state)
            # for example, knife starting state was clean because the murderer cleaned it.

    def dump(self, ui):
        ui.display(f"Dump data? (y/n)")
        command = ui.get_input()
        if command in ["y", "ye", "yes"]:
            print(f"MURDERER PROFILE:")
            for trait_category, trait in self.murderer.profile.items():
                print(f"{trait_category}: {trait}")

            print(f"MURDERER LEFT THE FOLLOWING CLUES")
            # condition: {item_id: spawn_locs}

            for condition, item_loc_pair in self.murder_clues_tracker.items():
                print(f"- {condition}:")
                for dic_pair in item_loc_pair:
                    for item, loc in dic_pair.items():
                        print(f"{item}: {loc}")

            print(f"MURDERER ALTERED STARTING STATE:")
            for item_id, starting_state in self.murder_cleanup_tracker.items():
                print(f"- {item_id}: {starting_state}")

        #can have a "you found" thing later, and also more additional stats as desired

class StoryGenerator:
    def __init__(self, story_templates, game_state):
        self.story_templates = story_templates
        self.game_state = game_state #might as well

    def generate_story(self, murderer_id, profile):
        story_texts = self.story_templates[murderer_id]
        #for

suspect_story_templates = {
    "id": {
        #text = print every time. else, if key in murderer_trait_id, then print value
        "intro": {
            "text": "debbies back"
        },
        "relation": {
            "text": "bertha is old friends with deb"
        },
        "spent_the_day": {
            "at_bar": "bertha works the bar at night"
        },
        "access_to_matches": {
            "at_bar"
        },
        "next_day": {
            "clean": "The next day, she cleans the weapon, shoes, etc."
        }
    },
    # Add more suspects with their own templates
}
