from entities.entities.locations.locations import Location
from utilities.general_utils import ids_to_names, names_to_ids
from config.logging_config import ent_logger

class Hallway(Location):
    def __init__(self, id, name, game_state, descriptions, connections, direction_labels, entity_state="default", is_outdoors=False):
        super().__init__(id, name, game_state, descriptions, connections, entity_state, is_outdoors)
        self.direction_labels = direction_labels # A dict with directions e.g., {"forward": "towards cab", "backward": "towards alley"}


    #def start_loop(self, ui):
    #    ui.display(self.descriptions.get_description("approaching"))
    #    logger.info("Hallway start loop: got approaching, now self.loop()")
    #    matched_command = self.loop(ui)
    #    return matched_command


    def get_navigation_options(self):
        ent_logger.debug(f"HALLWAY/GET_NAV_OPTION() ; orientation = {self.game_state.player.orientation}")
        navigation_options = []
        current_location = self.game_state.player.current_location
        previous_location = self.game_state.player.location_history[-2]
        orientation = self.game_state.player.orientation

        continue_options = []
        return_options = []

        for connection in self.connections:
            connection_name = ids_to_names(connection, self.game_state)
            if connection_name == current_location.name:
                if orientation == "forward":
                    if connection != previous_location.id:
                        continue_options.append(f"continue: {self.direction_labels['forward']}")
                    elif connection == previous_location.id:
                        return_options.append(f"return: {self.direction_labels['backward']}")
                else:  # orientation == "backward"
                    if connection != previous_location.id:
                        continue_options.append(f"continue: {self.direction_labels['backward']}")
                    elif connection == previous_location.id:
                        return_options.append(f"return: {self.direction_labels['forward']}")
            else:
                navigation_options.append(connection)

        # Combine options: continue options first, then navigation options, then return options
        navigation_options = continue_options + navigation_options + return_options

        ent_logger.debug(f"HALLWAYS/GETNAVIGATION_OPTIONS(): Navigation options = {navigation_options}")
        return navigation_options

    def loop(self, ui):

        while True:
            # Get navigation options
            navigation_options = self.get_navigation_options()
            # Get other options (suspects, items, etc.)
            suspects, items, locations, actions = self.get_options()
            # Display menu

            ui.display_menu(self.game_state, suspects, items, navigation_options, actions)

            command = ui.get_input()
            command_id = names_to_ids(command, self.game_state)  # returns a list

            # possibly multiple command_id matches, so handle which one here
            if isinstance(command_id, list):
                command_id = self.handle_command_id_list_logic(command_id, locations)

            result = self.process_command(command_id, ui, suspects, items, locations, actions)
            #result is entity ID
            if result:
                ent_logger.debug("HALLWAY RESULT")
                if isinstance(result, list):
                    result = result[0]

                direction_order = {
                    "pub hallway": ["hallway_01", "hallway_02", "hallway_03", "hallway_04"]
                }
                ent_logger.debug("HALLWAY ENTERING FOR LOOP:")
                for area, ordered_locs in direction_order.items():
                    if result in ordered_locs and self.game_state.player.current_location.id in ordered_locs:
                        ent_logger.debug("HALLWAY IF ")
                        current_value = ordered_locs.index(self.game_state.player.current_location.id)
                        moving_to_value = ordered_locs.index(result)

                        if current_value < moving_to_value:
                            ent_logger.debug(f"ordered locs if - current location {current_value} less than moving location {moving_to_value}, so going forward")
                            self.game_state.player.orientation = "forward"
                        else:
                            ent_logger.debug("ordered locs else")
                            self.game_state.player.orientation = "backward"
                ent_logger.debug(f"HALLWAY FORWARD VALUE")
                return result
            else:
                ui.bad_input()
