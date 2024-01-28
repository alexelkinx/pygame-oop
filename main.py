import pygame
from settings import Settings
from events import Events
from ship import Ship
from alien import Alien
from UI import Text
from stats import Stats


class SpaceInvaders:
    def __init__(
        self,
    ):  # __init__() method takes the new object as its first argument, self. It is also called a constructor.
        pygame.init()  # initializing pygame
        self.settings = Settings()  # create object/instance settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )  # creating screen
        pygame.display.set_caption(self.settings.caption)  # name of a pygame window
        self.bg_image = pygame.image.load("images/starfield.png").convert_alpha()

        self.ship = Ship(self)
        self.alien = Alien(self)
        self.events = Events()
        self.stats = Stats()

        self.aliens = pygame.sprite.Group()  # create object of class Group
        self.alien.create_alien_fleet()

        self.explosions = pygame.sprite.Group()

        self.txt_bullets_fired = Text(self.screen, 10, 10)
        self.txt_score = Text(self.screen, 700, 10)

    def run(self):
        while True:
            self.events.check_keys(self.ship)
            self.screen.blit(self.bg_image, self.screen.get_rect())

            self.txt_bullets_fired.blit("BULLETS FIRED", self.stats.bullets_fired)
            self.txt_score.blit("SCORE", self.stats.score)

            self.ship.blit()
            self.ship.update()
            self.ship.update_bullets()

            self.aliens.draw(self.screen)
            self.alien.check_fleet_edges()
            self.aliens.update()

            self.explosions.update()
            self.explosions.draw(self.screen)

            for b in self.ship.bullets:
                b.draw_bullet()

            pygame.display.flip()


if __name__ == "__main__":
    game = SpaceInvaders()  # create object/instance game
    game.run()
