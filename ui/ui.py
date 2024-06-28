import time
import random
from config.settings import MESSAGE_SLEEP_TIME
import sys
from utilities.general_utils import ids_to_names
from utilities.state_utils import iterate_vibe_keys

from config.logging_config import app_logger

from utilities.command_utils import match_command_to_option


class UI:
    def __init__(self):
        self.game_state = None
        self.bar = "_____________________"

    def get_input(self):
        output =  input("> ").lower().strip()
        return output

    def bad_input(self, text = None, beat_multiplier = 1):
        print (f"Command not recognized")
        self.stall(text, beat_multiplier)

    def stall(self, text = None, beat_multiplier = 1):
        self.beat(beat_multiplier)
        self.display(text or "Input any to continue...")
        #sys.stdout.flush()
        self.get_input()

    def beat(self, multiplier = 1):
        time.sleep(0.4*multiplier)

    def display(self, text, pause_time = 0, nested_pause_time=0):
        #something for if not ending with .??
        if not text:
            return
        if isinstance(text, list):
            for nested_str in text:
                self.display(nested_str)
                time.sleep(nested_pause_time)
        elif isinstance(text, dict):
            for key, value in text:
                self.display(f"{key}{f": {value}" if value else ""}")
        else:
            print(text)
        sys.stdout.flush()  # Ensure the text is displayed immediately
        time.sleep(pause_time)

    def announce(self, verb, subject=None):
        #refactor - could be good for all commands that work, like "chatting... or grilling... or opening..."
        # then you could also get less reliant on "its open"
        if verb == "go":
            choices = ["Moving...", "Approaching...", "Walking to..."]
            new_verb = random.choice(choices)
            #print(f"{new_verb} {subject if subject else ""}...")
            print(f"Moving...")
        elif verb == "insert":
            print(f"announcing: Inserting {subject if subject else ""}...")
        else:
            print(f"Announcing: {verb}, {subject}")
        self.beat()

    def confirm(self, command_id=None, text = None):
        command_name = None

        if command_id:
            command_name = ids_to_names(command_id, self.game_state)
        self.display(text or f"Did you mean '{command_name}'? (y/n):")
        confirm = self.get_input()
        if confirm in ["y", "ye", "yes"]:
            return True
        elif confirm in ["n", "no", "nope"]:
            return False
        else:
            self.bad_input()
            return False

    def display_menu(self, suspects=None, items=None, locations=None, actions=None):
        app_logger.debug(f"UI/DISPLAYMENU() ; \n {suspects} \n {items}\n {locations}\n {actions}")
        print(self.bar)
        #pass IDS to menu
        if suspects:
            print(f"Suspects:") #speak withApproach
            for sus in suspects:
                sus_name = ids_to_names(sus, self.game_state)
                print(f"- {sus_name.capitalize()}")
        if items:
            print(f"Items:") #inspect
            for it in items:
                item_name = ids_to_names(it, self.game_state)
                print(f"- {item_name.capitalize()}")
        if locations:
            player_last_loc_obj = self.game_state.player.location_history[-2]  # -1 current, -2 most recent
            print(f"Locations:") #change location? Travel Move to
            for location in locations:
                #for NOT previous locations:
                if location != player_last_loc_obj.id:
                    location_name = ids_to_names(location, self.game_state)
                    #locations with same name as current loc
                    if location_name == self.game_state.player.current_location.name: #PUT THIS IN HALLWAY!!
                        print(f"- Continue: down {location_name.capitalize()}")
                    #all locations that are not previous location
                    else:
                        print(f"- {location_name.capitalize()}")
            if player_last_loc_obj.id in locations:
                #if previous location name same as current location name,
                print(f"- Return: to {player_last_loc_obj.name}...")
        if actions:
            player_last_loc_obj = self.game_state.player.location_history[-2]
            print(f"Actions:")
            if isinstance(actions, dict):
                for option, description in actions.items():
                    description = ids_to_names(description, self.game_state)
                    if option != player_last_loc_obj.id:
                        print(f"- {option.capitalize()}{f": {description}" if description else "..."}")
                    elif option == player_last_loc_obj.id:
                        print(f"- Return: to {player_last_loc_obj.name}...")
                    else:
                        print(f"what kind of option is {option}!@!@!@")
            else:
                for action in actions:
                    print(f"- {action.capitalize()}")

    def display_menu_type_2(self, options, title="Menu", options_2 = None, title_2=None):
        print(self.bar)
        print(title.capitalize())
        #for text in options ids to names self.game_state
        if options:
            self.handle_option_printing_logic(options)
        else:
            self.display("-")
        if options_2:
            self.handle_option_printing_logic(options_2, title_2)

    def handle_option_printing_logic(self, options, title_2=None):
        if title_2:
            print(title_2.capitalize())
        if isinstance(options, dict):
            for option, description in options.items():

                if description == "_None":
                    print(
                        f"- {ids_to_names(option, self.game_state).capitalize()}")
                else:
                    description = ' '.join(self.handle_topic_display_logic(word) for word in description.split())
                    print(f"- {ids_to_names(option, self.game_state).capitalize()}{f": {ids_to_names(description, self.game_state)}" if description else "..."}")
        elif isinstance(options, list):
            for option in options:
                print(f"- {ids_to_names(option, self.game_state).capitalize()}")
        elif isinstance(options, str):
            print(f"- {options.capitalize}")
        else:
            raise ValueError(f"what are you printing man")

    def handle_topic_display_logic(self, word):
        topic_obj = self.game_state.item_manager.get_entity(word) or self.game_state.suspect_manager.get_entity(word)
        formatted_topic = None
        from entities.entities.suspects import Suspect
        if isinstance(topic_obj, Suspect):
            formatted_topic = topic_obj.name.capitalize()
        return formatted_topic or word