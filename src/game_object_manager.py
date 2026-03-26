import pygame

from alien import Alien
from ship import Ship


class GameObjectManager:
    """Gerencia os objetos do jogo"""
    def __init__(self, game):
        self.game = game
    
    def _create_alien(self, alien_number: int, row_number: int, alien_width: float, alien_height: float) -> None:
        """Cria um alienigena e o posiciona na linha."""
        alien = Alien(self.game.screen, self.game.settings)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien_height = alien.rect.height
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.game.aliens.add(alien)

    def create_fleet(self):
        alien = Alien(self.game.screen, self.game.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.game.settings.screen_width - (2 * alien_width)
        number_aliens_x = int(available_space_x // (2 * alien_width))
        ship_height = self.game.ship.rect.height
        available_space_y = (
            self.game.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = int(available_space_y // (2 * alien_height))

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number, alien_width, alien_height)

    def create_game_objects(self):
        self.game.ship = Ship(self.game.screen, self.game.settings)
        self.game.bg_color = self.game.settings.bg_color
        self.game.bullets = pygame.sprite.Group()
        self.game.aliens = pygame.sprite.Group()
