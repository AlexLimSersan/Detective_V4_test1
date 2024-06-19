from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from entities.entities.locations.locations import Location
from utilities.general_utils import names_to_ids
from utilities.command_utils import match_command_to_option, get_command
from utilities.state_utils import iterate_keys
from config.logging_config import ent_logger
import random

class Cab(Location):
    def __init__(self, id, name, game_state, descriptions, connections, entity_state="default", is_outdoors=False):
        super().__init__(id, name, game_state, descriptions, connections, entity_state, is_outdoors)
        self.cab_location_area_names = ["pub", "alley"] #for menu display
        self.cab_loc_dic = {#cab major loc connections to entry point, has entry points and location for command matching
                "pub": "porch_01",
                "porch_01": "porch_01"
            }
        self.buffer_into_view_dic = {
            "porch_01": ["The porch comes into view.."]
        }
        self.buffer_approach_from_cab_dic = {
            "porch_01": ["You step up onto the porch..."]
        }

    def get_actions(self):
        return ["cabbie"]
    def loop(self, ui):
        while True:
            suspects, items, locations, actions = self.get_options()
            #instead of connections, pass the major location names
            ui.display_menu(suspects, items, self.cab_location_area_names, actions=None)
            ui.display(f"Input 'cabbie' for additional options")

            command_id = get_command(ui, self.game_state)
            command_id = self.cab_loc_dic.get(command_id, command_id)
            ent_logger.debug(f"Locations.py/loop: cab changes command_id : {command_id}")

            result = self.process_command(command_id, ui, suspects, items, list(self.cab_loc_dic.keys()), actions)
            result = self.cab_loc_dic.get(result)
            ent_logger.debug(f"LOCATIONS.PY/CAB/LOOP() result = {result}")
            if result:
                if result == "EXIT_GAME":
                    return result
                #regular processing:
                if result != self.game_state.player.location_history[-2].id:
                    self.drive(result, ui)
                #ui.display(self.descriptions.get_description("leaving"))
                #ui.display(self.buffer_approach_from_cab_dic.get(result))  # later, make this a dic!
                return result
    def process_action(self, command_id, ui):
        action_dic = {
            "cabbie": self.handle_cabbie_actions,
            "accuse": self.accuse,
            "leave": self.exit_game
        }
        if command_id in action_dic:
            return action_dic[command_id](ui)

    def accuse(self, ui):
        ui.display(f"ACCUSING #later, have something here about you can hang whoever...")
        choice = self.game_state.player.ask_inv_type(ui, "suspect")
        if choice:
            # handle accusation logic
            ...
    def exit_game(self, ui):
        if ui.confirm(optional_text= "Are you sure you want to leave town? (y/n)"):
            return "EXIT_GAME"

    def handle_cabbie_actions(self, ui):
        ui.display(random.choice(['"What can I do for ya?"']))

        options = {"accuse": "choose suspect...",
                   "leave": "town and drive away... (exit game)",
                   "return": ""}
        ui.display_menu_type_2(options)
        command = ui.get_input()
        command = self.process_command(command, ui, actions=list(options.keys()))
        ui.display(f"Alrighty then.")
        if command:
            return command

    def drive(self, result, ui):
        ui.announce("cab_driving", result)

        driving_dic_1 = {
            "neutral": [f'"You got it boss."', "The engine sputters, and the cab drives off.", "The cab drives..."]}
        driving_dic_2 = {
            "neutral": ["You sit in the cab, watching the city pass by through the window."],
            "good": ["You relax in the cab", "The gentle hum of the engine feels soothing."],
            "bad": ["You brace yourself as the cab hits another pothole, the ride anything but smooth."]
        }

        drive1 = iterate_keys(driving_dic_1, self.game_state.vibe_system.ranked_keys)
        drive2 = iterate_keys(driving_dic_2, self.game_state.vibe_system.ranked_keys)
        ui.display(random.choice(drive1))
        ui.beat()
        ui.display(drive2)
        # could have the buffer area here
        ui.beat()
        ui.beat()
        ui.beat()
        loc_into_view = self.buffer_into_view_dic.get(result)
        ui.display(loc_into_view)
        # you arrive
        ui.display(f"\nInput any to exit cab...")
        ui.get_input()
        ui.beat()
