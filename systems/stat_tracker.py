from config.logging_config import app_logger


class Stat_Tracker:
    def __init__(self):
        self.game_state = None
        self.murderer = None #INITIALIZED from suspect manager when suspects are spawned
        self.murder_clues_tracker = {} #condition: [{item_id: spawn_locs}]
        self.murder_cleanup_tracker = {} #item: starting_state
        self.witness_statements = {} #condition: [{ suspect, dialogue id}]
        # NEW tests:
        self.unreliable_witness_statements = {}
        self.unreliable_witness_conditions = {}
        self.true_statements = {}
        self.true_statements_conditions = {}
        self.murderer_clues = {}

    def track_murderer(self, item_id, murder_condition, query_type, state_or_spawn_id):

        if query_type == "spawn":

            for condition in murder_condition:
                if condition not in self.murder_clues_tracker:
                    self.murder_clues_tracker[condition] = []
                #just for clarity:
                spawn_locs = state_or_spawn_id
                self.murder_clues_tracker[condition].append({item_id: spawn_locs})
                # for example, knife condition = knife_wounds_01
                app_logger.info(f"STAT_TRACKER/ track_murderer() | SPAWN \n{condition} - {item_id}: {spawn_locs}")
        if query_type == "state":
            if item_id not in self.murder_cleanup_tracker:
                self.murder_cleanup_tracker[item_id] = []
            # just for clarity:
            starting_state = state_or_spawn_id
            self.murder_cleanup_tracker[item_id].append(starting_state)
            # for example, knife starting state was clean because the murderer cleaned it.
            app_logger.info(f"STAT_TRACKER/ track_murderer() | STATE \n{item_id}: {starting_state} ")

        if query_type == "dialogue":
            suspect_id = item_id
            #maybe pass dilaogue dic? or just says!
            state_dialogue_dic = state_or_spawn_id
            for condition in murder_condition:
                # would be suspect id?
                if condition not in self.witness_statements:
                    self.witness_statements[condition] = []
                for state, dialogue_dic in state_dialogue_dic.items():
                    self.witness_statements[condition].append({suspect_id: dialogue_dic}) #condition list of dic
                app_logger.info(f"STAT_TRACKER/ track_murderer() | DIALOGUE \n{condition}: {suspect_id}, {state_dialogue_dic} ")
                    #appending whole dialogue dic - but losing state it gets appended?
                        #assuming all default for now?
                # for example, knife - bertha says she saw gibbs eyeing the kitchen often .
    def track_dialogue(self, sus_id, condition, dialogue_dic, track_type):
        if track_type == "80":
            for x, y in dialogue_dic["default"].items(): #fuckit
                if sus_id in self.true_statements:
                    for key, value in self.true_statements.items():
                        if key == sus_id:
                            value.append(y["says"])
                            for _key, _value in self.true_statements_conditions.items():
                                if _key == sus_id:
                                    _value.append(condition)
                else:
                    self.true_statements[sus_id] = y["says"]
                    self.true_statements_conditions[sus_id] = [condition]
        if track_type == "20":
            for x, y in dialogue_dic["default"].items(): #fuckit
                if sus_id in self.unreliable_witness_conditions:
                    for key, value in self.unreliable_witness_statements.items():
                        if key == sus_id:
                            value.append(y["says"])
                            for _key, _value in self.unreliable_witness_conditions.items():
                                if _key == sus_id:
                                    _value.append(condition)
                else:
                    self.unreliable_witness_statements[sus_id] = y["says"]
                    self.unreliable_witness_conditions[sus_id] = [condition]

    def dump_profile(self, ui):
        ui.display(f"MURDERER PROFILE:")
        for trait_category, trait in self.murderer.profile.items():
            ui.display(f"{trait_category}: {trait}")

    def dump_spawned_clues(self, ui):
        ui.display(f"\nMURDERER LEFT THE FOLLOWING CLUES")
        # condition: {item_id: spawn_locs}

        for condition, item_loc_pair in self.murder_clues_tracker.items():
            ui.display(f"{condition}:")
            for dic_pair in item_loc_pair:
                for item, loc in dic_pair.items():
                    ui.display(f"- {item}: {loc}")

    def dump_altered_states(self,ui):
        ui.display(f"\nMURDERER ALTERED STARTING STATE:")
        for item_id, starting_state in self.murder_cleanup_tracker.items():
            item_ent = self.game_state.item_manager.get_entity(item_id)
            if item_ent.spawned:
                ui.display(f"- {item_id}: {starting_state}")


    def dump_witness_statements(self,ui):
        ui.display(f"\nWITNESS STATEMENTS:")
        for condition, list_of_sus_dialogue_dic_pair in self.witness_statements.items():
            ui.display(f"Murder condition {condition}:")
            for sus_dialogue_dic_pair in list_of_sus_dialogue_dic_pair:
                for sus_id, dialogue_dic in sus_dialogue_dic_pair.items():
                    for node, dialogue_data in dialogue_dic.items():
                        ui.display(f"- {sus_id}, {node}: {dialogue_data["says"]}")

    def dump_true_statements(self, ui):
        ui.display(f"\nSUSPECTS SAY: 80 - CONDITIONS MET")
        for x, y in self.true_statements.items():
            ui.display(f"Suspect {x} claims {self.true_statements_conditions[x]}:")
            for _ in y:
                ui.display(f"- {_}")
    def dump_false_statements(self, ui):
        ui.display(f"\nSUSPECTS SAY: 20 - UNRELIABLE:")
        for x, y in self.unreliable_witness_statements.items():
            ui.display(f"Suspect {x} claims {self.unreliable_witness_conditions[x]}:")
            for _ in y:
                ui.display(f"- {_}")
    def dump(self, ui):
        #if ui.confirm(text = f"Dump data? (y/n)"):
        self.dump_profile(ui)
        self.dump_spawned_clues(ui)
        self.dump_altered_states(ui)

        self.dump_true_statements(ui)
        self.dump_false_statements(ui)
        #can have a "you found" thing later, and also more additional stats as desired

class StoryGenerator:
    def __init__(self, story_templates, game_state):
        self.story_templates = story_templates
        self.game_state = game_state #might as well

    def generate_story(self, murderer_id):
        profile = self.game_state.suspect_manager.murderer.profile
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
