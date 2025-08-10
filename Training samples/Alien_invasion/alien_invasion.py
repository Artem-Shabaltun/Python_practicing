import sys
import pygame

class AlienInvasion:
    "загальний клас, для керування ресурсами та поведінкою"

    def __init__(self):
        "ініціалізувати гру, створити ресурси"
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        "Розпочати цикл гри"
        while True:
            # Слідкувати за подіями миші та клави
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # показ останнього намальованого екрану
            pygame.display.flip()

if __name__ == '__main__':
    # створити екземпляр гри та запустити
    ai = AlienInvasion()
    ai.run_game()