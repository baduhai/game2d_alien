import sys 
import pygame

class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    
    def run_game(self):
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()

    
if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
