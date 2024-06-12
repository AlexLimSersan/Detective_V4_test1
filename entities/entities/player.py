
from utilities.general_utils import match_command_to_option
from config.settings import PLAYER_STARTING_LOCATION, MOVE_TIME
from config.logging_config import ent_logger

from utilities.general_utils import names_to_ids, ids_to_names


class Player():
    def __init__(self, game_state):
        self.clues_found = [] #tracker for end game analysis
        self.location_history = [] #loc history ; objects of locs, including current loc just for flexibility?
        self._current_location = None#loc object
        self.inventory = [] #list of objects
        self.convo_topics = ["night of the murder"] #handles convo topic logic; night of the murder = default
        self.game_state = game_state
        self.orientation = "forward"

    @property
    def current_location(self):
        return self._current_location
    @current_location.setter
    def current_location(self, loc_object):
        ent_logger.debug(f"PLAYER/CURRENT LOCATION = {loc_object.id}")
        self._current_location = loc_object
        self.location_history.append(loc_object)
        ent_logger.debug(f"PLAYER/location history = {self.location_history[-2].id}")

    def move(self, matched_command, ui):
        # location manager always is used to change entity location - syncs between location and item.

        ui.announce("moving_player", matched_command)
        #you leave the cab, and approach entry location
        ui.display(self.current_location.descriptions.get_description("leaving"))
        #ui.beat()

        loc_object = self.game_state.location_manager.get_entity(matched_command)
        self.current_location = loc_object
        # ELAPSE TIME
        self.game_state.time_system.elapse_time(MOVE_TIME, ui)  # event checker here?
        ui.display(self.current_location.descriptions.get_description("approaching"))

    def initialize(self):
        # Initialize Player (with starting loc)
        starting_loc_object = self.game_state.location_manager.get_entity(PLAYER_STARTING_LOCATION)
        self.location_history = [starting_loc_object]
        self.current_location = starting_loc_object
    def add_known_topic(self, ent_id):
        #logic for dictionary of clues to topics to reuse dialogue
        #just for now:
        self.convo_topics.append(ent_id)
        self.clues_found.append(ent_id)

    def ask_inv_type(self, type, ui):
        inv_by_type = []
        for item in self.inventory: #can just list all inventory? use apple as whimsical?
            if item.type == type:
                inv_by_type.append(item)
        #DISPLAY
        ui.display(f"Choose {type}:")
        for item in inv_by_type:

            ui.display(f"- {item.name}")

        command = ui.get_input()
        command_id = names_to_ids(command, self.game_state)
        for item in inv_by_type:
            if item.id == command_id:
                return command_id
        matched_command, matched = match_command_to_option(command, self.game_state, items=inv_by_type)
        if matched and ui.confirm(matched_command, self.game_state):
            return matched_command
        ui.display(f"You can't find {command_id}")

    def get_convo_topic(self, ui):
        topics = []
        ui.display(f"Change topic:")
        for topic in topics:
            ids_to_names(topic, self.game_state)
            ui.display(f"- {topic}")
        command = ui.get_input()
        command_id = names_to_ids(command, self.game_state)
        for topic in topics:
            if topic == command_id:
                return command_id
        matched_command, matched = match_command_to_option(command, self.game_state, items=inv_by_type)
        if matched and ui.confirm(matched_command, self.game_state):
            return matched_command


        matched_command, matched = match_command_to_option(command, self.game_state, items=inv_by_type)
        if matched and ui.confirm(matched_command, self.game_state):
            return matched_command
        ui.display(f"You can't find {command_id}")








