import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    "загальний клас, для керування ресурсами та поведінкою"

    def __init__(self):
        "ініціалізувати гру, створити ресурси"
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # задаємо фон
        self.bg_color = (230, 230, 230)

    def run_game(self):
        "Розпочати цикл гри"
        while True:
            # Слідкувати за подіями миші та клави
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Заново перемалювати екран
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # показ останнього намальованого екрану
            pygame.display.flip()

if __name__ == '__main__':
    # створити екземпляр гри та запустити
    ai = AlienInvasion()
    ai.run_game()