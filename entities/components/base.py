from abc import ABC, abstractmethod
from game.game_state import Game_State
class Interaction(ABC):
    def __init__(self, id, name, game_state, entity_state = "default", is_outdoors = None, ):
        self.id = id
        self.name = name
        self.game_state = game_state
        self.entity_state = entity_state
        self.is_outdoors = is_outdoors

        assert isinstance(self.game_state, Game_State), f"Expected Game_State, got {type(self.game_state)}"

   # @abstractmethod
    #def get_options(self):
        #get player node, get corresponding options
     #   pass
  #  @abstractmethod
  #  def process_command(self, command, options, ui):
  #      #player node updated to next node from dialogue choice
  #      pass
