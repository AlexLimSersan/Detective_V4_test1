from entities.entities.locations.locations import Location
from utilities.general_utils import ids_to_names, names_to_ids
from utilities.command_utils import get_command
from config.logging_config import ent_logger

class Hallway(Location):
    def __init__(self, id, name, game_state, descriptions, connections, direction_labels, entity_state="default", is_outdoors=False):
        super().__init__(id, name, game_state, descriptions, connections, entity_state, is_outdoors)
        self.direction_labels = direction_labels # A dict with directions e.g., {"forward": "towards cab", "backward": "towards alley"}
        self.direction_order = {
                    #add more ordered hallway types here. key is not used in code, so just name as desired.
            #last position lounge and cab reset the orientation
                    "pub hallway": ["hallway_01", "hallway_02", "hallway_03", "hallway_04", "lounge_01"],
                    "alleyway": ["alley_01", "alley_02", "alley_03", "alley_03_1","crime_scene_01", "crime_scene_02","alley_04",
                                 "dead_end_01","dead_end_02", "alley_05", "alley_06","fire_escape_01", "alley_07", "alley_08"],
                    "alley_ladder": ["alley_06","fire_escape_01", "fire_escape_02", "fire_escape_03","roof_top_01"],
                "morgue": ["hallway_morgue_01", "hallway_morgue_02"]
                }

    def get_directional_locations(self):
        ent_logger.debug(f"HALLWAY/get_directional_options() ; orientation = {self.game_state.player.orientation}")
        directional_options = []
        current_location = self.game_state.player.current_location
        previous_location = self.game_state.player.location_history[-2]
        orientation = self.game_state.player.orientation

        if orientation == "forward":
            cont_title = self.direction_labels.get("continue_title", "continue:")
            ret_title = self.direction_labels.get("return_title", "return:")
        else:
            cont_title = self.direction_labels.get("continue_title_backward", self.direction_labels.get("continue_title", "continue:"))
            ret_title = self.direction_labels.get("return_title_backward", self.direction_labels.get("return_title", "return:"))

        continue_options = []
        return_options = []
        #GET CONTINUE/RETURN OPTIONS
        if len(self.get_connections()) == 2:
            for connection in self.connections:
                if orientation == "forward":
                    if connection != previous_location.id:
                        continue_options.append(f"{cont_title} {self.direction_labels['forward']}")
                    elif connection == previous_location.id:
                        return_options.append(f"{ret_title} {self.direction_labels['backward']}")
                else:  # orientation == "backward"
                    if connection != previous_location.id:
                        continue_options.append(f"{cont_title} {self.direction_labels['backward']}")
                    elif connection == previous_location.id:
                        return_options.append(f"{ret_title} {self.direction_labels['forward']}")
        else:
            connection_names = []
            for connection in self.connections:
                connection_name = ids_to_names(connection, self.game_state)
                connection_names.append(connection)

            #if all connections have unique names
            #if len(self.connections) == len(set(connection_names)):
            #    for connection in self.connections:
            #        directional_options.append(connection)
            #else:
            for connection in self.connections:
                connection_name = ids_to_names(connection, self.game_state)
                connection_names.append(connection)
                if connection_name == current_location.name:
                    if orientation == "forward":
                        if connection != previous_location.id:
                            continue_options.append(f"{cont_title} {self.direction_labels['forward']}")
                        elif connection == previous_location.id:
                            return_options.append(f"{ret_title} {self.direction_labels['backward']}")
                    else:  # orientation == "backward"
                        if connection != previous_location.id:
                            continue_options.append(f"{cont_title} {self.direction_labels['backward']}")
                        elif connection == previous_location.id:
                            return_options.append(f"{ret_title} {self.direction_labels['forward']}")
                else:
                    directional_options.append(connection)
        #END OF CONT/RETURN OPTIONS

        #ORDER THE COMBINED OPTIONS
        directional_options = continue_options + directional_options + return_options
        ent_logger.debug(f"HALLWAYS/GETNAVIGATION_OPTIONS(): Navigation options = {directional_options}")
        return directional_options




    def loop(self, ui):
        while True:
            #lmao just fix here like if alcove, forward?
            suspects, items, locations, actions = self.get_options()
            #locations displayed as actions in hallways
            ui.display_menu(suspects, items, self.get_directional_locations(), actions)
            command_id = get_command(ui, self.game_state)
            result = self.process_command(command_id, ui, suspects, items, locations, actions)
            if result:
                self.update_orientation(result)
                return result
            elif command_id in self.whimsical_handlers:
                self.whimsical_handlers[command_id](ui)

    def update_orientation(self, result):
        for area, ordered_locs in self.direction_order.items():
            if result in ordered_locs and self.game_state.player.current_location.id in ordered_locs:

                current_value = ordered_locs.index(self.game_state.player.current_location.id)
                moving_to_value = ordered_locs.index(result)
                ent_logger.warning(f"HALLWAY update orientation \n {self.game_state.player.current_location.id}:{current_value} \n {result}:{moving_to_value}")
                if current_value < moving_to_value:
                    ent_logger.debug(
                        f"ordered locs if - current location {current_value} less than moving location {moving_to_value}, so going forward")
                    self.game_state.player.orientation = "forward"
                else:
                    ent_logger.debug("ordered locs else")
                    self.game_state.player.orientation = "backward"
            else:
                ent_logger.debug(f"Leaving hallway or bug lol")