from game.game_manager import Game_Manager

def main():
    game_manager = Game_Manager()
    game_manager.initialize()
    game_manager.run()

if __name__ == "__main__":
    main()