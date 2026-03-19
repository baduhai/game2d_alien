import pygame

from settings import Settings
from input_handler import InputHandler
from game_object_manager import GameObjectManager
from game_renderer import GameRenderer
from game_updater import GameUpdater


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.renderer = GameRenderer(self)
        self.input_handler = InputHandler(self)
        self.object_manager = GameObjectManager(self)
        self.game_updater = GameUpdater(self)
        
        self.renderer.init_window()
        self.object_manager.create_game_objects()
        
    def run_game(self):
        self.object_manager.create_fleet()

        while True:
            self.input_handler.handle_keys()
            self.game_updater.update_game()
            self.renderer.update_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
