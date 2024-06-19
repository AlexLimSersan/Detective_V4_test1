from utilities.command_utils import match_command_to_option
from config.settings import PLAYER_STARTING_LOCATION, MOVE_TIME
from config.logging_config import ent_logger

from utilities.general_utils import names_to_ids, ids_to_names

from entities.entities.suspects import Suspect
class Player():
    def __init__(self, game_state):
        #self.clues_found = [] #tracker for end game analysis - can just cross check anything found vs
        self.location_history = [] #loc history ; objects of locs, including current loc just for flexibility?
        self._current_location = None#loc object
        self.known_clues = [] #list of objects; CANT PICK ANYTHING UP YET!
        self.game_state = game_state
        self.orientation = "forward"
        #for convo topics, just use inventory
        #self.convo_topics = ["night of the murder"] #handles convo topic logic; night of the murder = default


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
        # change current location to matched command object
        loc_object = self.game_state.location_manager.get_entity(matched_command)
        self.current_location = loc_object

        #leaving from last location, can check against current loc for leaving to
        ui.display(self.location_history[-2].descriptions.get_description("leaving"))
        #get approaching description from current location; can check against last loc for directional (approaching from)
        ui.display(self.current_location.descriptions.get_description("approaching"))
        ui.beat()
        # ELAPSE TIME
        self.game_state.time_system.elapse_time(MOVE_TIME, ui)  # event checker here?

    def initialize(self):
        # Initialize Player (with starting loc)
        starting_loc_object = self.game_state.location_manager.get_entity(PLAYER_STARTING_LOCATION)
        self.location_history = [starting_loc_object]
        self.current_location = starting_loc_object
    def add_known_topic(self, ent_obj):
        #logic for dictionary of clues to topics to reuse dialogue
        #just for now:
        #self.convo_topics.append(ent_id)
        #self.clues_found.append(ent_id)
        if ent_obj not in self.known_clues:
            self.known_clues.append(ent_obj)

    def ask_inv_type(self, ui, inv_type): #get topics like this?!?
        inv_by_type = []
        ids_by_type = []

        if inv_type == "topic":
            inv_by_type.append("night of the murder")
            ids_by_type.append("night of the murder")
            for obj in self.known_clues: #should append any for topic
                inv_by_type.append(obj.name)
                ids_by_type.append(obj.id)
        elif inv_type == "suspect":
            for obj in self.known_clues:
                if isinstance(obj, Suspect):
                    inv_by_type.append(obj.name)
                    ids_by_type.append(obj.id)
        else:
            for obj in self.known_clues:  # should append any for topic
                try:
                    if obj.item_type == inv_type:
                        inv_by_type.append(obj.name)
                        ids_by_type.append(obj.id)
                except:
                    ent_logger.warning(f"PLAYER/get inv type: no item_type for {obj.id}")

        #DISPLAY
        ui.display(f"Choose {inv_type}:")
        ent_logger.debug(f"inv_by_type = {inv_by_type}")
        for name in inv_by_type:

            ui.display(f"- {name.capitalize()}")

        command = ui.get_input()
        command_id = names_to_ids(command, self.game_state)
        ent_logger.info(f"command id: {command_id}")
        for id in ids_by_type:
            if id in command_id:
                return command_id

        matched_command, matched = match_command_to_option(command, self.game_state, items=inv_by_type)
        if matched and ui.confirm(matched_command, self.game_state):
            matched_id = names_to_ids(matched_command, self.game_state)
            return matched_id
        ui.display(f"No {command_id} {inv_type}")










