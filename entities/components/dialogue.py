from utilities.state_utils import iterate_states, check_nested_weather_or_time_keys
from entities.components.base import Interaction
from game.game_state import Game_State
import random
from config.settings import EXIT_COMMANDS
from utilities.command_utils import match_command_to_option
from config.logging_config import ent_logger


class Dialogue(Interaction): #will move this later, i think in entites/components makes sense
    def __init__(self, dialogue, player_options, id, name, entity_state, mood, game_state, current_location, is_outdoors):
        super().__init__(id, name, game_state, entity_state, is_outdoors)
        self.current_location = current_location
        self.mood = mood
        self.node_history = [] #list of topic ids
        #dialogue types: {state : {topic, {non topic, }}}
        self.dialogue = dialogue #data
        self.current_node = None
        #player options
        self.player_options = player_options #all player options
        self.player_node = None #current node to find player options,
        self.talking = False #for the dialogue loop
        self.topic = "night of the murder"
        #reaction dics using description keying?

        # Ensure game_state is an instance of Game_State
        assert isinstance(self.game_state, Game_State), f"Expected Game_State, got {type(self.game_state)}"

    def start_loop(self, ui):
        self.greet(ui)
        self.talking = True
        self.loop(ui)
        self.bye(ui)

    def greet(self, ui):
        dialogue_dic_to_handle = self.get_dialogue_dic("greet")
        self.handle_dialogue_dic(dialogue_dic_to_handle, ui)

    def bye(self, ui):
        dialogue_dic_to_handle = self.get_dialogue_dic("bye")
        self.handle_dialogue_dic(dialogue_dic_to_handle, ui)

    def loop(self, ui):
        while self.talking:  # loop until no longer talking, can be turned off by event/dialogue effect or player action
            options = self.get_options()
            ent_logger.warning(
                f"DIALOGUE/ loop: {self.id} ; mood: {self.mood.current_value} \n options = {options}\n topic = {self.topic}\n ")
            if not options:
                self.reset_convo(ui)
                continue
            command_executed = False
            while not command_executed:
                ent_logger.debug(f"entering not command executed loop")
                ui.display_menu_type_2(options=options, title=self.name.capitalize())
                command = ui.get_input()
                command_executed = self.process_command(command, options, ui)
            # timesystem.advance time here!?

    def process_command(self, command, options, ui):
        if command in EXIT_COMMANDS:
            self.talking = False
            return True
        elif command in options:
            if command == "change":
                new_topic = self.game_state.player.ask_inv_type(ui, inv_type="topic")
                if isinstance(new_topic, list):
                    new_topic = new_topic[0]
                if not new_topic:
                    self.reset_convo(ui)
                else:
                    self.topic = new_topic

            else:
                self.handle_dialogue_dic(self.get_dialogue_dic(type=self.topic, player_input=command), ui, command)
            return True
        else:
            matched_command, matched = match_command_to_option(command, self.game_state, actions=options)
            if matched:
                if ui.confirm(matched_command):
                    if isinstance(matched_command, list):
                        matched_command = matched_command[0]
                    self.process_command(matched_command, options, ui)
                return True

        ui.bad_input()
        return False

    def handle_dialogue_dic(self, dialogue_dic, ui, command=None):
        ent_logger.debug(f" handle_dialogue_dic: dialogue_dic {dialogue_dic}")
        #handle effects first to reflect reaction
        self.handle_effects(dialogue_dic, command)
        self.handle_says_logic(dialogue_dic, ui)
        # next player node
        # this SHOULD be set to none if there is No options, to reflect that the convo for that topic ends. this will trigger the redirect
        self.player_node = dialogue_dic.get("options")

    def handle_says_logic(self, dialogue_dic, ui):
        # Already keyed by state and mood, so now just optional check weather/time checks if desired.
        says_dic = dialogue_dic.get("says", [...])
        if isinstance(says_dic, dict):
            #i feel like using a list of str numbers is no good lmao...
            #maybe make says a list of dics, the dic is time or weather or text (always) : list of possible responses to print
            #then for the len of list, random from list?
            test_list = []
            for _ in test_list:
                says = check_nested_weather_or_time_keys(says_dic.get(_), self.game_state)
                if says:
                    ui.display(random.choice(says))
                    ui.beat()
        else:  # not a dic becuase ur lazy
            ui.display(random.choice(says_dic))

    def handle_effects(self, dialogue_dic, command=None): #this could even be in event system?
        effects = dialogue_dic.get("effects")
        test_ids = ["apple_01", "whiskey_01", "gibbs_01", "bertha_01", "unknown", "redirect"]
        ent_logger.info(f"self.current node = {self.current_node}")
        for id in test_ids:
            if id in self.current_node:
                ent_logger.info(f"this could work?")
        if "chat" in self.current_node:
            ...
        elif "grill" in self.current_node:
            ...
        if command:
            ent_logger.info(f"command = {command}; possible reaction?!")
        #or could be in base interaction class?
        #effects is a dictionary of effect, value/id ; mood changes, game vibe changes, or IDS for events
        if not effects:
            return
        for effect, data in effects:
            ent_logger.debug(f"handling effects: effect {effect}, data {data}")
            if effect == "mood":
                #if data + or - or 0, can react accordingly right here!
                #could tally up mood modifier + if in murderer_clue_ids and suspect, then just change it later if there is any to be changed
                #then have one unified react, x2 if murderer? ;;
                #can also get reaction based on current location, is outdoors?
                self.mood += data
                #reactions for mood changes!
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
                key: value.format(name=self.name.capitalize(), topic=self.topic)
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

        #CREATE ALL POSSIBLE DIALOGUE NODE KEYS IN ORDER OF PREFERENCE
        #create list of all keys
        dialogue_keys_by_preference = []
        # examples:
        # topic key: apple_chat_good
        # non_topic key: greet_good
        #CREATE NODE KEY LIST
        for _type in type_by_preference: #start with the topic, for example "apple" or "greet"
            for choice in player_choices_by_preference: #then the current choice, like "chat" or "grill"
                for key in mood_keys_by_preference: #then iterate moods.if none, next player choice if no mood found
                    dialogue_keys_by_preference.append(f"{_type}_{f"{choice}_" if player_input else ""}{key}")

        ent_logger.info(f"dialogue_keys_by_preference: {dialogue_keys_by_preference}")
        #GET THE DIALOGUE DIC ACCORDING TO IF THE PLAYER GAVE AN INPUT; THIS TRANSLATES TO TOPIC VS NON TOPIC DIALOGUE
        if player_input:
            ent_logger.debug(f"if player input True: {player_input}")
            dialogue_dic = self.dialogue["topic"]
        else:
            ent_logger.debug(f"if player input False: {player_input}")
            dialogue_dic = self.dialogue["non_topic"]
        # ITERATE THROUGH TO FIND DIALOGUE DIC MATCHED TO NODE
        for dialogue_key in dialogue_keys_by_preference:
            #iterate through event_id, entity_state, and default, to find a matching dialogue.
            #found in preference of the ranked mood keys, then the player choice if player choice
            ent_logger.debug(f"trying dialogue key {dialogue_key}\n iterating states on dialogue_dic {dialogue_dic}")
            response_dic = iterate_states(self.game_state, self.entity_state, dialogue_dic, dialogue_key)
            if response_dic: #respond with first match
                ent_logger.info(f"using dialogue key {dialogue_key}\n response found: {response_dic}")
                self.current_node = dialogue_key
                return response_dic
        raise ValueError("dialogue response did not default to unknown properly")
