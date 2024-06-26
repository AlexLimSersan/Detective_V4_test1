

class Game_State:
    def __init__(self):
        #managers
        self.suspect_manager = None
        self.location_manager = None
        self.item_manager = None
        #systems
        self.stat_tracker = None
        self.vibe_system = None
        self.weather_system = None
        self.time_system = None
        self.event_system = None
        #player
        self.player = None
        #handler
        self.current_handler = None

    def initialize(self, stat_tracker, suspect_manager, location_manager, item_manager,
                   vibe_system, weather_system, time_system, event_system, player):
        self.stat_tracker = stat_tracker
        self.suspect_manager = suspect_manager
        self.location_manager = location_manager
        self.item_manager = item_manager
        self.vibe_system = vibe_system
        self.weather_system = weather_system
        self.time_system = time_system
        self.event_system = event_system
        self.player = player

        # Ensure all components have updated references to game_state
        self.update_references()
        self.spawn_entities()


    def spawn_entities(self):
        self.item_manager.spawn_items()
        self.suspect_manager.spawn_suspects()


    def update_references(self):
        # Update game_state references in systems and managers
        if self.stat_tracker:
            self.stat_tracker.game_state = self
        if self.weather_system:
            self.weather_system.game_state = self
        if self.time_system:
            self.time_system.game_state = self
        if self.event_system:
            self.event_system.game_state = self
        if self.location_manager:
            self.location_manager.game_state = self
        if self.suspect_manager:
            self.suspect_manager.game_state = self
        if self.item_manager:
            self.item_manager.game_state = self
        assert isinstance(self.item_manager.game_state, Game_State)
        self.location_manager.load_entities()
        self.suspect_manager.load_entities()
        self.item_manager.load_entities()

        if self.player:
            self.player.initialize()