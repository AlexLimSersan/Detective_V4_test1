from abc import ABC, abstractmethod

import logging

logger = logging.getLogger('my_game')

class Entity_Manager(ABC):
    def __init__(self, entity_data, description_data, game_state):
        self.entities = {}
        self.entity_data = entity_data
        self.description_data = description_data
        self.game_state = game_state

    @abstractmethod
    def load_entities(self):
        """Abstract method to load entities. Must be implemented by subclasses."""
        pass

    #will also need a spawn entity for mobile ents

    def get_entity(self, entity_id):
        """return entity object by ID"""
        return self.entities.get(entity_id, None)

    def get_entity_name(self, entity_id):
        ent_obj = self.entities.get(entity_id)
        if ent_obj:
            #will need to figure out logic for entities with same name!!!
            #!= current location,
            # or mobile entity in current location
            return ent_obj.name
        return None #must be none else will not move to next ent manager

    def get_entity_id(self, entity_name):
        for ent_id, ent in self.entities.items():
            if ent.name.lower() == entity_name.lower():
                return ent_id
        return None #must be none else will not move to next ent manager

    def get_entity_ids(self, name):
        ids = [entity.id for entity in self.entities.values() if entity.name.lower() == name.lower()]
        logger.debug(f"ENTITY_MANAGER.BASE/get_entity_ids() returning ids {ids}")
        return ids

