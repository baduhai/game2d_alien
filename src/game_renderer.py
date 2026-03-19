import pygame


class GameRenderer:
    """Gerencia a rederização da janela do jogo"""
    def __init__(self, game):
        self.game = game
    
    def init_window(self):
        self.game.screen = pygame.display.set_mode(
            (self.game.settings.screen_width, self.game.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def update_screen(self):
        self.game.screen.fill(self.game.bg_color)
        self.game.ship.blitme()
        self.game.aliens.draw(self.game.screen)

        for bullet in self.game.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()
