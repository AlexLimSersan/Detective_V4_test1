from game.game_state import Game_State
from game.game import Game

from ui.ui import UI

#loc data
from data.loc_data.loc_data import loc_ent_data
from data.loc_data.loc_description_data import loc_description_data

#sus data
from data.sus_data.sus_data import sus_ent_data
from data.sus_data.sus_description_data import sus_description_data
from data.sus_data.dialogue_data import sus_dialogue_data
from data.sus_data.dialogue_data import dialogue_player_options

#item data
from data.item_data.item_data import item_ent_data
from data.item_data.item_description_data import item_description_data

#player
from entities.entities.player import Player

#managers
from entity_managers.location_manager import Location_Manager
from entity_managers.suspect_manager import Suspect_Manager
from entity_managers.item_manager import Item_Manager

#systems
from systems.stat_tracker import Stat_Tracker
from systems.event_system import Event_System
from systems.ambiance_system import Ambiance_System
from systems.weather_system import Weather_System
from systems.time_system import Time_System
from data.misc_data.weather_data import weather_data
from data.misc_data.events_data import events_data

#settings
from config.settings import PLAYER_STARTING_LOCATION

class Game_Manager:
    def __init__(self):
        self.game_state = None
        self.game = None
        self.ui = None
        #have a difficulty for item/clue hints (someone big must have swung the pipe)

    def initialize(self):

        # Initialize UI
        self.ui = UI()

        # Temporarily initialize game_state with None or minimal required components
        self.game_state = Game_State()


        # Initialize Systems
        vibe_system = Ambiance_System()
        weather_system = Weather_System(weather_data=weather_data, game_state=self.game_state)
        time_system = Time_System(game_state=self.game_state)
        event_system = Event_System(game_state=self.game_state, events_data=events_data)

        #story system for end game, later! story system can also act as tracker



        # Initialize Managers
        #locs first
        location_manager = Location_Manager(
            entity_data=loc_ent_data,
            description_data=loc_description_data,
            game_state=self.game_state
        )

        suspect_manager = Suspect_Manager(
            entity_data=sus_ent_data,
            description_data=sus_description_data,
            dialogue_data=sus_dialogue_data,#for now, later will do the preprocessing stuff below
            player_options=dialogue_player_options,
            game_state=self.game_state
        )

        #need to pass murderer profile to item manager. so just load ents, and then spawn after randomizer (fully initialized)
        item_manager = Item_Manager(
            entity_data= item_ent_data,
            description_data= item_description_data,
            game_state = self.game_state
        )

        player = Player(self.game_state)

        stat_tracker = Stat_Tracker()

        # Initialize Game State with all required components
        self.game_state.initialize(
            stat_tracker=stat_tracker,
            suspect_manager=suspect_manager,#for now
            location_manager=location_manager,
            item_manager=item_manager,
            vibe_system=vibe_system,
            weather_system=weather_system,
            time_system=time_system,
            event_system=event_system,
            player=player
        )

        self.ui.game_state = self.game_state
        # Initialize Game with Game_State and UI
        self.game = Game(self.game_state, self.ui)





    def run(self):
        self.game.run()
        self.game_state.stat_tracker.dump(self.ui)
