from entity_managers.base import Entity_Manager

from entities.entities.base import Mobile_Entity

from entities.entities.locations.locations import Location
from entities.entities.locations.cab import Cab
from entities.entities.locations.hallways import Hallway
from entities.entities.locations.doors import Door, Drawer
from config.logging_config import ent_logger

class Location_Manager(Entity_Manager):
    def __init__(self, entity_data, description_data, game_state):
        super().__init__(entity_data, description_data, game_state)

    def load_entities(self):
        for loc_id, loc_data in self.entity_data["locations"].items():
            if loc_id == "cab_01":
                self.entities[loc_id] = Cab(id=loc_id, game_state=self.game_state,
                                                 descriptions=self.description_data[loc_id], **loc_data)
            else:
                self.entities[loc_id] = Location(id=loc_id, game_state=self.game_state,
                                             descriptions = self.description_data[loc_id], **loc_data)
            ent_logger.info(f"loading location {loc_id}, {loc_data}")
        for door_id, door_data in self.entity_data["doors"].items():
            ent_logger.debug(f"loading door {door_id} with {door_data}")
            self.entities[door_id] = Door(id=door_id, game_state=self.game_state,
                                          descriptions=self.description_data[door_id], **door_data)
        for loc_id, loc_data in self.entity_data["halls"].items():
            ent_logger.debug(f"loading halls {loc_id} with {loc_data}")
            self.entities[loc_id] = Hallway(id=loc_id, game_state=self.game_state,
                                                 descriptions=self.description_data[loc_id], **loc_data)


    def get_location_of_entity(self, entity_id):
        """finds loc where entity is at"""
        for location_object in self.entities.values():
            if entity_id in location_object.suspects_present or entity_id in location_object.items_present:
                return location_object
        raise ValueError("Location_Manager: entity location not found")
        # return None

    def move_entity(self, entity, new_location_id):
        """always only move entities through here to ensure sync.
        MOVING ENTITY MUST BE OBJECT
        raises value errors for no old_id removing, etc
        """
        if not isinstance(entity, Mobile_Entity):
            raise ValueError("Entity must be a Mobile_Entity object")

        new_location = self.get_entity(new_location_id)
        old_location = self.get_location_of_entity(entity.id)
        if not new_location:
            raise ValueError(f"Location {new_location_id} not found")
        if not old_location:
            raise ValueError(f"Old Location {old_location.id} not found")
        # update locations
        old_location.remove_entity(entity)
        new_location.add_entity(entity)
        # update mobile entity
        entity.current_location = new_location
        # ensure sync
        assert entity.current_location == self.get_location_of_entity(entity.id)


    def spawn_entities(self, mobile_entity, spawn_loc_ids):
        if not isinstance(spawn_loc_ids, list):
            spawn_loc_ids = [spawn_loc_ids]
        for id in spawn_loc_ids: #IF OBJ.INDRAWER = TRUE, THEN ADD TO HIDDEN ENTITIES?
            loc_obj = self.get_entity(id) or self.game_state.item_manager.get_entity(id) #loc or item accept it
            if not loc_obj:
                raise ValueError(f"incorrect initialization order for ent {mobile_entity.id}, loc id {spawn_loc_ids}\n id = {id}\nloc_obk = {loc_obj}")
            loc_obj.add_entity(mobile_entity)
            ent_logger.info(f"spawning {mobile_entity.id} in {loc_obj.id}")


