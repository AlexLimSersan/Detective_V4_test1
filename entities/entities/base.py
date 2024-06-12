from abc import ABC, abstractmethod
import random
from entities.descriptions.base import Descriptions, Mobile_Descriptions
from config.logging_config import ent_logger


class Entity(ABC):
    """base entity for locations, suspects, and items"""
    def __init__(self, id, name, game_state, descriptions, entity_state = "default", is_outdoors = False):
        self.id = id
        self.name = name
        self.game_state = game_state
        self.descriptions = Descriptions(self.id, self.name, entity_state, self.game_state, descriptions, is_outdoors)
        self._entity_state = entity_state
        self.is_outdoors = is_outdoors

    @property
    def entity_state(self):
        return self._entity_state

    @entity_state.setter
    def entity_state(self, new_state):
        self.descriptions.entity_state = new_state  # Sync with descriptions
        self._entity_state = new_state

        assert self._entity_state == self.descriptions.entity_state

    def start_loop(self, ui):
        ui.display(self.descriptions.get_description("approaching"))
        self.loop(ui) #dialogue or interactions
        ui.display(self.descriptions.get_description("leaving"))

    @abstractmethod
    def loop(self, ui):
        #something like:
        #get at ent desc, get options, process command
        pass


class Mobile_Entity(Entity):
    """base class for items and suspects, that can move and will update description location correspondingly"""
    #routine hack: event->move mobile entity wherever, then event descriptions-> can be tailored for that location. default is default routine
    def __init__(self, id, name, game_state, descriptions, entity_state = "default", is_outdoors = False, current_location = None):
        super().__init__(id, name, game_state, None, entity_state, is_outdoors)
        self.descriptions = Mobile_Descriptions(self.id, self.name, self.entity_state, self.game_state, descriptions, current_location, is_outdoors)
        self._current_location = current_location #reference to lcoation object

    @property
    def current_location(self):
        return self._current_location
    @current_location.setter
    def current_location(self, new_loc_object):
        """Setter should never be called directly - use move_to method in loc manager to ensure syncing with locations."""
        if self._current_location != new_loc_object:
            # update current loc and same for descriptions
            self._current_location = new_loc_object
            self.descriptions.current_location = new_loc_object
            # update is_outdoors and same for descriptions
            self.is_outdoors = new_loc_object.is_outdoors
            self.descriptions.is_outdoors = new_loc_object.is_outdoors

            # Verify synchronization
            assert self.current_location == self.descriptions.current_location, \
                "ERROR: Can't sync entity's current location and description's current location"
            assert self.is_outdoors == self.descriptions.is_outdoors, \
                "ERROR: Can't sync entity's is_outdoors and description's is_outdoors"
        else:
            ent_logger.warning(f"Mobile Entity/move location - new location {new_loc_object.id} is already current location {self.current_location.id} ")

    @abstractmethod
    def update_location(self):
        pass


