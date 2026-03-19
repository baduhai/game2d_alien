import sys
import pygame


class GameUpdater:
    """Gerencia a atualização dos objetos do jogo"""
    def __init__(self, game):
        self.game = game
    
    def update_game(self):
        self.game.ship.update()
        self.game.bullets.update()
        
        for bullet in self.game.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.game.bullets.remove(bullet)

        pygame.sprite.groupcollide(
            self.game.bullets, self.game.aliens, True, True
        )

        for alien in self.game.aliens.sprites():
            if alien.check_edges():
                for alien in self.game.aliens.sprites():
                    alien.rect.y += self.game.settings.fleet_drop_speed
                self.game.settings.fleet_direction *= -1
                break

        self.game.bullets.update()
        self.game.aliens.update()

        if pygame.sprite.spritecollideany(self.game.ship, self.game.aliens):
            print("A nave foi atingida!")
            sys.exit()
