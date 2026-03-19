import sys
import pygame


class InputHandler:
    """Gerencia as entradas de tecla no jogo"""
    def __init__(self, game):
        self.game = game
    
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.game.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.game.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    if len(self.game.bullets) < self.game.settings.bullet_allowed:
                        from bullet import Bullet
                        new_bullet = Bullet(
                            self.game.screen, self.game.settings, self.game.ship
                        )
                        self.game.bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.game.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.game.ship.moving_left = False
