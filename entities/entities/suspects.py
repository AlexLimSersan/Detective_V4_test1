from entities.entities.base import Mobile_Entity
from entities.descriptions.sus_descriptions import Sus_Descriptions
from entities.components.dialogue import Dialogue

from systems.vibe_system import Vibe_System

from config.settings import SUSPECT_STARTING_MOOD
from config.logging_config import ent_logger
import random

from game.game_state import Game_State

class Suspect(Mobile_Entity):
    #ROUTINE HACK: TIME DESCRIPTIONS FOR ACTIONS! also event?
    def __init__(self, id, name, profile, routine, game_state, descriptions, dialogue, player_options, entity_state="default", is_outdoors=False, current_location=None, dialogue_id = None):
        super().__init__(id, name, game_state, None, entity_state, is_outdoors, current_location, dialogue_id)
        self.profile = profile
        self.routine = routine
        self.mood = Vibe_System(SUSPECT_STARTING_MOOD)
        self.descriptions = Sus_Descriptions(id, name, self.mood, entity_state, game_state, descriptions, current_location, is_outdoors)
        assert isinstance(self.game_state, Game_State)
        self.dialogue = Dialogue(dialogue, player_options, id, name, entity_state, self.mood, game_state, current_location, is_outdoors)

    def loop(self, ui):
        #approach and leave desc already shown
        ui.display(self.descriptions.set_scene())
        self.dialogue.start_loop(ui) #arguably better to pull up some logic to here, like locations
        #bye already dealt with in dialogue

    def update_location(self):
        time_of_day = self.game_state.time_system.current_phase
        current_routine = self.routine.get(self.entity_state, self.routine.get("default"))
        if time_of_day in current_routine:
            loc_id = current_routine[time_of_day]
        else:
            loc_id = current_routine.get("else")
            if not loc_id:
                raise ValueError("SUSPECT LOC ID NOT RECOGNIZED")
        #move through loc manager to sync current location and entity references
        ent_logger.info(f"suspects.py/updatelocation() updating {self.id} to loc {loc_id}")
        self.game_state.location_manager.move_entity(self, loc_id)

class Murderer(Suspect):
    # ROUTINE HACK: TIME DESCRIPTIONS FOR ACTIONS! also event?
    def __init__(self, id, name, profile, routine, game_state, descriptions, dialogue, player_options, entity_state="default", is_outdoors=False, current_location=None):
        super().__init__(id, name, profile, routine, game_state, descriptions, dialogue, player_options, entity_state, is_outdoors, current_location)
        self.profile = self.randomize_profile(profile)

    def randomize_profile(self, profile):
        murderer_profile = {}
        for trait, options in profile.items():
            murderer_profile[trait] = random.choice(options)
        ent_logger.info(f"MURDERER/randomized_profile() = {self.id}\n {murderer_profile}")
        return murderer_profile

    #need murderer mood multiplier

class Debbie(Mobile_Entity):
    ... #could randomize her activites from that night?

