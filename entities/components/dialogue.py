from utilities.state_utils import iterate_states
from entities.components.base import Interaction
from game.game_state import Game_State
import random
from config.settings import EXIT_COMMANDS
from utilities.general_utils import match_command_to_option
from config.logging_config import ent_logger


class Dialogue(Interaction): #will move this later, i think in entites/components makes sense
    def __init__(self, dialogue, player_options, id, name, entity_state, mood, game_state, current_location, is_outdoors):
        super().__init__(id, name, game_state, entity_state, is_outdoors)
        self.current_location = current_location
        self.mood = mood
        #dialogue types: {state : {topic, {non topic, }}}
        self.dialogue = dialogue #data
        #player options
        self.player_options = player_options #all player options
        self.player_node = None #current node to find player options,
        self.talking = False #for the dialogue loop
        self.topic = "night of the murder"

        # Ensure game_state is an instance of Game_State
        assert isinstance(self.game_state, Game_State), f"Expected Game_State, got {type(self.game_state)}"

    def start_loop(self, ui):
        #greet
        self.handle_dialogue_dic(self.get_dialogue_dic("greet"), ui)
        self.talking = True
        ent_logger.info(f"{self.id} ; mood: {self.mood}")
        self.loop(ui)
        self.handle_dialogue_dic(self.get_dialogue_dic("bye"), ui)

    def handle_dialogue_dic(self, dialogue_dic, ui):
        ent_logger.debug(f" handle_dialogue_dic: dialogue_dic {dialogue_dic}")
        #handle effects first to reflect reaction
        effects_to_handle = dialogue_dic.get("effects")
        self.handle_effects(effects_to_handle)
        #suspect responds
        suspect_says = dialogue_dic.get("says", [...])
        ui.display(random.choice(suspect_says))
        #next player node
        # this SHOULD be set to none if there is No options, to reflect that the convo for that topic ends. this will trigger the redirect
        self.player_node = dialogue_dic.get("options")


    def handle_effects(self, effects): #this could even be in event system?
        #or could be in base interaction class?
        #effects is a dictionary of effect, value/id ; mood changes, game vibe changes, or IDS for events
        if not effects:
            return
        for effect, data in effects:
            ent_logger.debug(f"handling effects: effect {effect}, data {data}")
            if effect == "mood":
                self.mood += data
            elif effect == "vibe":
                self.game_state.vibe_system += data
            elif effect == "new_event": #later, will make this more robust
                #could be like bertha watching or something? can have conditions to trigger
                self.game_state.event_system.add_event(data)
            else:
                raise ValueError("effect not recognized")
        self.game_state.event_system.check_events()

    def get_options(self):
        if self.player_node:
            options = self.player_options.get(self.player_node, {})
            formatted_options = {
                key: value.format(name=self.name, topic=self.topic)
                for key, value in options.items()
            }
            return formatted_options
        else:
            return False

    def reset_convo(self, ui):
        ui.stall() #to reflect that convo is being redirected

        self.handle_dialogue_dic(self.get_dialogue_dic("redirect"), ui) #suspect says "so anyways..." or equivalent
        #redirect resets player node since it has options
        ent_logger.debug(f"resetting convo")


    def get_dialogue_dic(self, type, player_input=None):
        ent_logger.debug(f" get_dialogue_dic; type (ie hello, apple): {type} ;\n player_input {player_input}")
        #type = greet, bye, or clue ; player input = chat, grill, etc
        #player input none means that its a non topic dialogue
        type_by_preference = [type, "unknown"]
        player_choices_by_preference = list(dict.fromkeys([player_input, "chat", "grill"])) #remove duplicates
        mood_keys_by_preference = self.mood.ranked_keys

        #create list of all keys
        dialogue_keys_by_preference = []
        # examples:
        # topic key: apple_chat_good
        # non_topic key: greet_good
        for _type in type_by_preference: #start with the topic, for example "apple" or "greet"
            for choice in player_choices_by_preference: #then the current choice, like "chat" or "grill"
                for key in mood_keys_by_preference: #then iterate moods.if none, next player choice if no mood found
                    dialogue_keys_by_preference.append(f"{_type}_{f"{choice}_" if player_input else ""}{key}")

        ent_logger.info(f"dialogue_keys_by_preference: {dialogue_keys_by_preference}")
        if player_input:
            ent_logger.debug(f"if player input True: {player_input}")
            dialogue_dic = self.dialogue["topic"]
        else:
            ent_logger.debug(f"if player input False: {player_input}")
            dialogue_dic = self.dialogue["non_topic"]

        for dialogue_key in dialogue_keys_by_preference:
            #iterate through event_id, entity_state, and default, to find a matching dialogue.
            #found in preference of the ranked mood keys, then the player choice if player choice
            ent_logger.debug(f"trying dialogue key {dialogue_key}\n iterating states on dialogue_dic {dialogue_dic}")
            response = iterate_states(self.game_state, self.entity_state, dialogue_dic, dialogue_key)
            if response: #respond with first match
                ent_logger.info(f"using dialogue key {dialogue_key}\n response found: {response}")
                return response
        raise ValueError("dialogue response did not default to unknown properly")


    def loop(self, ui):
        while self.talking: #loop until no longer talking, can be turned off by event/dialogue effect or player action
            options = self.get_options()
            ent_logger.debug(f"dialogue loop starting; \n options = {options}\n topic = {self.topic}\n ")
            if not options:
                self.reset_convo(ui)
                continue
            command_executed = False
            while not command_executed:
                ent_logger.debug(f"entering not command executed loop")
                ui.display_menu(self.game_state, actions = options)
                command = ui.get_input()
                command_executed = self.process_command(command, options, ui)
            #timesystem.advance time here!


    def process_command(self, command, options, ui):
        if command in EXIT_COMMANDS:
            # if return,, leave, etc, self.talking = false
            self.talking = False
            return True
        elif command in options:
            #if command in change here
            self.handle_dialogue_dic(self.get_dialogue_dic(type=self.topic, player_input=command), ui)
            return True
        else:
            matched_command, matched = match_command_to_option(command, self.game_state, actions = options)
            if matched and ui.confirm(matched_command, self.game_state):
                if isinstance(matched_command, list):
                    matched_command = matched_command[0]
                if matched_command in EXIT_COMMANDS:
                    # if return,, leave, etc, self.talking = false
                    self.talking = False
                    return True
                elif matched_command in options:
                    self.handle_dialogue_dic(self.get_dialogue_dic(type=self.topic, player_input=command), ui)
                    return True
        """
        JUST NEED a change topic?
        """
        ui.bad_input()
        return False

