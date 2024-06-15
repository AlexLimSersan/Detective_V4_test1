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
        self.cab_loc_dic = {
                "pub": "porch_01", #name to entry point
                "porch_01": "porch_01"
            }
        self.cab_buffer_dic = {
            "porch_01": ["The porch comes into view.."]
        }


    def loop(self, ui):
        while True:
            # the cab displays the names of the main areas, so pub, alley, etc. it doesnt display the entry point to the main area, like porch, front door, etc.
            suspects, items, locations, actions = self.get_options()
            # list of major area names you want to display
            ui.display_menu(self.game_state, suspects, items, self.cab_connections, actions)

            command = ui.get_input()
            command_id = names_to_ids(command, self.game_state)
            #returns list, choose first one
            command_id = command_id[0]
            # handle cab locations to entry point:
            # dictionary of main area ids (which will be player command) to entry points (pub vs porch, etc)
            # and entry points to entry points in case player types entry point in, while player current loc is cab:

            #change command id to match entry point
            command_id = self.cab_loc_dic.get(command_id, command_id)
            ent_logger.debug(f"Locations.py/loop: cab changes command_id : {command_id}")
            #if not command id, its ok, will go through the match command to id function
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
                if result != self.game_state.player.location_history[-2].id:
                    self.drive(result, ui)
                ui.display(self.descriptions.get_description("leaving"))
                ui.display(f"\nYou step up onto the porch...")  # later, make this a dic!
                return result
            else:
                ui.bad_input()
    def process_command(self, command_id, ui, suspects, items, locations, actions):
        if command_id in suspects + items + locations + actions:
            return command_id  # game handles switching handlers
        elif command_id in EXIT_COMMANDS or command_id in ENTER_COMMANDS:
            return self.handle_command_id_check_enter_or_exit(command_id)
        else:
            matched_command, matched = match_command_to_option(command_id, self.game_state, suspects, items, self.cab_connections,
                                                               actions)
            if matched and ui.confirm(matched_command, self.game_state):
                if matched_command in EXIT_COMMANDS or matched_command in ENTER_COMMANDS:
                    return self.handle_command_id_check_enter_or_exit(matched_command)
                return self.cab_loc_dic.get(matched_command)
        return None

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
        loc_into_view = self.cab_buffer_dic.get(result)
        ui.display(loc_into_view)
        # you arrive
        ui.display(f"\nInput any to exit cab...")
        ui.get_input()
        ui.beat()
