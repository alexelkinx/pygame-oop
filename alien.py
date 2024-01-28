import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()  # call parent constructor (Sprite)
        self.settings = game.settings  #
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)
        self.direction = 1
        self.game = game

    def create_alien_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_of_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            self.game.aliens.add(alien)

    def change_fleet_direction(self):
        for alien in self.game.aliens:
            alien.rect.y += alien.rect.width
            alien.direction = -alien.direction

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def check_fleet_edges(self):
        for alien in self.game.aliens:
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def update(self):
        # self.check_fleet_edges()
        if self.direction == 1 and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.alien_speed
        elif self.direction == -1 and self.rect.left > 0:
            self.x -= self.settings.alien_speed
        # else:
        #     self.direction = -self.direction
        #     self.rect.y += self.rect.height
        self.rect.x = self.x
