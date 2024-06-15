from config.settings import EXIT_COMMANDS, ENTER_COMMANDS
from entities.entities.locations.locations import Location
from utilities.general_utils import names_to_ids, match_command_to_option

from config.logging_config import ent_logger

class Cab(Location):
    def __init__(self, id, name, game_state, descriptions, connections, entity_state="default", is_outdoors=False):
        super().__init__(id, name, game_state, descriptions, connections, entity_state, is_outdoors)
        self.cab_connections = ["pub", "alley"]
        self.cab_loc_dic = {
                "pub": "porch_01", #name to entry point
                "porch_01": "porch_01"
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
                ui.announce("cab_driving", result)
                ui.display(self.descriptions.get_description("leaving"))
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
