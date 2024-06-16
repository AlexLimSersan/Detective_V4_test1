import time
import random
from config.settings import MESSAGE_SLEEP_TIME
import sys
from utilities.general_utils import ids_to_names
from utilities.state_utils import iterate_keys

from config.logging_config import app_logger

from utilities.general_utils import match_command_to_option
class UI:
    def __init__(self):
        self.game_state = None
        self.bar = "_____________________"

    def get_input(self):
        output =  input("> ").lower().strip()

        return output

    def bad_input(self):
        print (f"Command not recognized")
        self.stall()

    def stall(self):
        time.sleep(0.3)
        print("Input any to continue...")
        #sys.stdout.flush()
        self.get_input()

    def beat(self, multiplier = 1):
        time.sleep(0.4*multiplier)
        #print("")


    def display(self, text, pause_time = 0, nested_pause_time=0):
        """
        Display text from a nested list with pauses between each phrase.

        :param text_list: Nested list of phrases to display
        :param pause_time: Pause time between phrases in seconds
        :param nested_pause_time: Pause time between nested lists in seconds
        """
        if not text:
            return
        if isinstance(text, list):
            for item in text:
                #print(".")
                self.display(item)
                time.sleep(nested_pause_time)
        else:
            print(text)
            sys.stdout.flush()  # Ensure the text is displayed immediately
            time.sleep(pause_time)

    def announce(self, verb, subject=None): #could pass last loc and have a if verb x and last loc cab, etc
        if verb == "go":
            choices = ["Moving...", "Approaching...", "Walking to..."]
            new_verb = random.choice(choices)
            #print(f"{new_verb} {subject if subject else ""}...")
            print(f"Moving...")
        elif verb == "insert":
            print(f"announcing: Inserting {subject if subject else ""}...")
        #elif verb == "cab_driving":
            #possible key iterations here
            ...
        else:
            print(f"Announcing: {verb}, {subject}")
        self.beat()
        #could have if subject is cab here

    def confirm(self, command_id, game_state):
        command_name = ids_to_names(command_id, game_state)
        self.display(f"Did you mean '{command_name}'? (y/n): ")
        confirm = self.get_input()
        if confirm in ["y", "ye", "yes"]:
            return True
        return False

    def display_menu(self, game_state, suspects=None, items=None, locations=None, actions=None):
        app_logger.debug(f"UI/DISPLAYMENU() ; \n {suspects} \n {items}\n {locations}\n {actions}")
        print(self.bar)
        #if game_state.player.current_location.id == "cab_01":  # if cab, no return, and maybe display entry points differently later
        #    self.handle_cab_menu(game_state, suspects, items, locations, actions)
        #    return #break


        #pass IDS to menu
        if suspects:
            print(f"Suspects:") #speak withApproach
            for sus in suspects:
                sus_name = ids_to_names(sus, game_state)
                print(f"- {sus_name.capitalize()}")
        if items:
            print(f"Items:") #inspect
            for it in items:
                item_name = ids_to_names(it, game_state)
                print(f"- {item_name.capitalize()}")

        if locations:

            player_last_loc_obj = game_state.player.location_history[-2]  # -1 current, -2 most recent
            print(f"Locations:") #change location? Travel Move to

            for location in locations:
                #for NOT previous locations:
                if location != player_last_loc_obj.id:
                    location_name = ids_to_names(location, game_state)
                    #locations with same name as current loc
                    if location_name == game_state.player.current_location.name: #PUT THIS IN HALLWAY!!
                        print(f"- Continue: down {location_name.capitalize()}")
                    #all locations that are not previous location
                    else:
                        print(f"- {location_name.capitalize()}")

            if player_last_loc_obj.id in locations:
                #if previous location name same as current location name,
                print(f"- Return: to {player_last_loc_obj.name}...")

        if actions:
            player_last_loc_obj = game_state.player.location_history[-2]
            print(f"Actions:")
            for option, description in actions.items():
                description = ids_to_names(description, game_state)
                if option != player_last_loc_obj.id:
                    print(f"- {option.capitalize()}{f": {description}" if description else "..."}")
                elif option == player_last_loc_obj.id:
                    print(f"- Return: to {player_last_loc_obj.name}...")
                else:
                    print(f"what kind of option is {option}")



    def display_menu_type_2(self, options, title="Menu"):
        print(self.bar)
        print(title)
        if isinstance(options, dict):
            for option, description in options.items():
                print(f"- {option.capitalize()}{f": {description}" if description else "..."}")
        elif isinstance(options, list):
            for option in options:
                print(f"- {option.capitalize}")
        elif isinstance(options, str):
            print(f"- {options.capitalize}")
