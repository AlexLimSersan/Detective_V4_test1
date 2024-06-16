from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from entities.entities.locations.locations import Location
from utilities.general_utils import names_to_ids, match_command_to_option
from utilities.state_utils import iterate_keys
from config.logging_config import ent_logger
import random

class Cab(Location):
    def __init__(self, id, name, game_state, descriptions, connections, entity_state="default", is_outdoors=False):
        super().__init__(id, name, game_state, descriptions, connections, entity_state, is_outdoors)
        self.cab_connections = ["pub", "alley"]
        self.cab_loc_dic = {#name to entry point
                "pub": "porch_01",
                "porch_01": "porch_01"
            }
        self.buffer_into_view_dic = {
            "porch_01": ["The porch comes into view.."]
        }
        self.buffer_approach_from_cab_dic = {
            "porch_01": ["You step up onto the porch..."]
        }

    def get_options(self):
        # returns options to display
        #always none
        suspects = [suspect.id for suspect in self.suspects_present.values()]
        items = [item.id for item in self.items_present.values()]

        locations = self.cab_connections
        actions = ["cabbie"]

        return suspects, items, locations, actions

    def loop(self, ui):
        while True:
            # the cab displays the names of the main areas, so pub, alley, etc. it doesnt display the entry point to the main area, like porch, front door, etc.
            suspects, items, locations, actions = self.get_options()
            # list of major area names you want to display
            ui.display_menu(self.game_state, suspects, items, self.cab_connections, actions=None )
            ui.display(f"Input 'cabbie' for additional options")

            command = ui.get_input()
            command_id = names_to_ids(command, self.game_state)
            #returns list, choose first one
            command_id = command_id[0]
            # handle cab locations to entry point:
            # dictionary of main area ids (which will be player command) to entry points (pub vs porch, etc)
            # and entry points to entry points in case player types entry point in, while player current loc is cab:


            result = self.process_command(command_id, ui, suspects, items, locations, actions)
            ent_logger.debug(f"LOCATIONS.PY/CAB/LOOP() result = {result}")
            # COULD DO BUFFER LOCATION, THEN YOU DONT HAVE TO HAVE SPECIAL CAB GETTING INPUTS/
            #and dont need the cab driving announcement.
                #CAB leaving = engine sputters
                #buffer approach = the drive over to the porch
                #at entity = the porch comes into view
                #user input exit cab or choose other area
                #leaving = you leave the cab, and make your way to the pub.
                #then,
                #approaching porch - etc etc

            if result:
                if result == "continue_loop":
                    continue
                elif result == "EXIT_GAME":
                    return result
                #regular processing:
                if result != self.game_state.player.location_history[-2].id:
                    self.drive(result, ui)
                ui.display(self.descriptions.get_description("leaving"))
                ui.display(self.buffer_approach_from_cab_dic.get(result))  # later, make this a dic!
                return result

            else:
                ui.bad_input()
    def process_command(self, command_id, ui, suspects=[], items=[], locations=[], actions=[]):
        ent_logger.info(f"{command_id} {suspects} {items} {locations} {actions}")

        #command changing here so you can recursively call
        #change command id to match entry point
        command_id = self.cab_loc_dic.get(command_id, command_id)
        ent_logger.debug(f"Locations.py/loop: cab changes command_id : {command_id}")
        # if not command id, its ok, will go through the match command to id function
        if command_id in actions:
            if command_id in ["cabbie"]:
                return self.handle_cabbie_actions(command_id, ui)
            else:
                return command_id

        if locations:
            if command_id in EXIT_COMMANDS or command_id in ENTER_COMMANDS:
                return self.handle_command_id_check_enter_or_exit(command_id)
        elif command_id in EXIT_COMMANDS:
            return command_id
        if command_id in suspects + items + list(self.cab_loc_dic.keys()):
            return command_id  # game handles switching handlers
        else:
            matched_command, matched = match_command_to_option(command_id, self.game_state, suspects, items, locations,
                                                               actions)
            if matched:
                if ui.confirm(matched_command, self.game_state):
                    return self.process_command(matched_command, ui, suspects, items, locations, actions)
                else:
                    return "continue_loop"
        return None

    def handle_cabbie_actions(self, command_id, ui):
        while True:
            options = {"accuse": "choose suspect...", "drive": "away and leave town... (exit game)", "return": ""}
            ui.display_menu_type_2(options)
            command = ui.get_input()
            option_keys = list(options.keys())
            command = self.process_command(command, ui, actions=option_keys)
            ent_logger.info(f"cabbie command = {command}")

            if command:
                command = self.handle_additional_options(ui, command)
                return command
            #ui.bad_input()

    def handle_additional_options(self, ui, command):
        if command == "accuse":
            ui.display(f"ACCUSING #later, have something here about you can hang whoever...")
            choice = self.game_state.player.ask_inv_type(ui, "suspect")
            if choice:
                return choice
        elif command == "drive":
            ui.display(f"Are you sure you want to leave town? (y/n)")
            confirm = ui.get_input()
            if confirm in ["y","ye","yes"]:
                return "EXIT_GAME"
            return "continue_loop"
        elif command in EXIT_COMMANDS:
            return "continue_loop"
        else:
            return command

    def drive(self,result,ui):
        ui.announce("cab_driving", result)

        driving_dic_1 = {
            "neutral": [f'"You got it boss."', "The engine sputters, and the cab drives off.", "The cab drives..."]}
        driving_dic_2 = {
            "neutral": ["You sit in the cab, watching the city pass by through the window."],
            "good": ["You relax in the cab", "The gentle hum of the engine feels soothing."],
            "bad": ["You brace yourself as the cab hits another pothole, the ride anything but smooth."]
        }
        drive1 = iterate_keys(self.game_state, driving_dic_1)
        drive2 = iterate_keys(self.game_state, driving_dic_2)
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
