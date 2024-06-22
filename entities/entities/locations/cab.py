from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from entities.entities.locations.locations import Location
from utilities.general_utils import names_to_ids
from utilities.command_utils import match_command_to_option, get_command
from utilities.state_utils import iterate_vibe_keys, iterate_states

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

    def get_actions(self):
        return ["cabbie"]

    def start_loop(self, ui):
        # buffer towards cab?!?!?
        ui.beat(2)
        return super().start_loop(ui)
    def loop(self, ui):

        while True:
            suspects, items, locations, actions = self.get_options()
            #instead of connections, pass the major location names
            ui.display_menu(suspects, items, self.cab_location_area_names, actions=None)
            ui.display(f"Input 'cabbie' for additional options")

            command_id = get_command(ui, self.game_state)
            command_id = self.cab_loc_dic.get(command_id, command_id)
            ent_logger.info(f"Locations.py/loop: cab changes command_id : {command_id}")

            result = self.process_command(command_id, ui, suspects, items, list(self.cab_loc_dic.keys()), actions)
            result = self.cab_loc_dic.get(result, result)
            if result:
                if result == "EXIT_GAME":
                    return result
                #regular processing:
                if result != self.game_state.player.location_history[-2].id:
                    self.drive(result, ui)
                ent_logger.info(f"returning result = {result}")
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
        if ui.confirm(text= "Are you sure you want to leave town? (y/n)"):
            return "EXIT_GAME"

    def handle_cabbie_actions(self, ui):
        ui.display(random.choice(['"What can I do for ya?"']))
        options = {"accuse": "choose suspect...",
                   "leave": "town and drive away... (exit game)",
                   "return": ""}
        ui.display_menu_type_2(options, title="Cabbie")
        command = ui.get_input()
        command = self.process_command(command, ui, actions=list(options.keys()))
        ui.display(f"Alrighty then.")
        return command


    def drive(self, result, ui):
        ui.announce("cab_driving", result)
        # want to drive before moving player
        driving_descriptions_to_get = ["driving_start", "driving_during", "driving_arriving"]
        for description_type in driving_descriptions_to_get:
            ui.display(self.descriptions.get_description(description_type, result))
            if description_type == "driving_during":
                ui.beat(3)
            else:
                ui.beat()
        ui.stall(text = f"\nInput any to exit cab...")
