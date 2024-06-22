from entity_managers.base import Entity_Manager
from entities.entities.suspects import Suspect, Murderer
from config.logging_config import ent_logger

import random
from entities.components.dialogue import Dialogue
class Suspect_Manager(Entity_Manager):
    def __init__(self, entity_data, description_data, dialogue_data, player_options, game_state):
        super().__init__(entity_data, description_data, game_state)
        self.dialogue_data = dialogue_data
        self.processed_dialogue_data = None
        self.player_options = player_options
        self.murderer = None

    def load_entities(self):
        suspect_ids = list(self.entity_data.keys())
        murderer_id = random.choice(suspect_ids)  # Randomly select a murderer ID
        for suspect_id, suspect_data in self.entity_data.items():
            if suspect_id == murderer_id:
                self.murderer = Murderer(
                    id=suspect_id,
                    game_state=self.game_state,
                    descriptions=self.description_data[suspect_id],
                    dialogue=None,
                    player_options=self.player_options,
                    **suspect_data
                )
                self.entities[suspect_id] = self.murderer
                ent_logger.info(f"loading MURDERER:{suspect_id}, {suspect_data}")
                self.game_state.stat_tracker.murderer = self.murderer
            else:
                self.entities[suspect_id] = Suspect(
                    id=suspect_id,
                    game_state=self.game_state,
                    descriptions=self.description_data[suspect_id],
                    dialogue=None,
                    player_options=self.player_options,
                    **suspect_data
                )
                ent_logger.info(f"loading suspect: {suspect_id}, {suspect_data}")

        self.processed_dialogue_data = self.preprocess_all_suspect_dialogues()
        import json
        #print(json.dumps(self.processed_dialogue_data, indent=4))
        for suspect_id, suspect in self.entities.items():
            suspect.dialogue = Dialogue(
                dialogue=self.processed_dialogue_data[suspect_id],
                player_options=self.player_options,
                id=suspect_id,
                name=suspect.name,
                entity_state=suspect.entity_state,
                mood=suspect.mood,
                game_state=self.game_state,
                current_location=suspect.current_location,
                is_outdoors=suspect.is_outdoors
            )

    def update_entity_locations(self):
        for entity in self.entities.values():
            entity.update_location()

    def spawn_suspects(self):
        time_of_day = self.game_state.time_system.current_phase

        for id, obj in self.entities.items():
            current_routine = obj.routine.get(obj.entity_state, obj.routine.get("default"))
            if time_of_day in current_routine:
                loc_id = current_routine[time_of_day]
            else:
                loc_id = current_routine.get("else")
                if not loc_id:
                    raise ValueError("SUSPECT LOC ID NOT RECOGNIZED")
            ent_logger.info(f"SUS_MANAGER.PY/SPAWNING {id} {loc_id}")
            self.game_state.location_manager.spawn_entities(obj, loc_id)


    def preprocess_all_suspect_dialogues(self):
        merged_dialogue_data = {}
        for suspect_id, dialogue_data in self.dialogue_data.items():
            merged_dialogue = self.preprocess_dialogue(dialogue_data, suspect_id)
            merged_dialogue_data[suspect_id] = merged_dialogue
        return merged_dialogue_data

    def preprocess_dialogue(self, dialogue_template, sus_id):
        merged_dialogue = dialogue_template.copy()
        for conditional_dialogues in dialogue_template.get("conditional", []):
            if self.game_state.item_manager.check_conditions(conditions_dic = conditional_dialogues["conditions"], item_id = sus_id,
                                                             query_type = "dialogue", spawn_or_state_id = conditional_dialogues["dialogue"]):
                self.merge_dialogue(merged_dialogue["topic"], conditional_dialogues["dialogue"])
        return merged_dialogue



    def merge_dialogue(self, base_dialogue, additional_dialogue):
        for dialogue_id, dialogue_dic in additional_dialogue.items():
            if dialogue_id in base_dialogue:
                if isinstance(base_dialogue[dialogue_id], dict) and isinstance(dialogue_dic, dict):
                    self.merge_dialogue(base_dialogue[dialogue_id], dialogue_dic)
                else:
                    base_dialogue[dialogue_id] = dialogue_dic
            else:
                base_dialogue[dialogue_id] = dialogue_dic
