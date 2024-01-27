import pygame
from bullet import Bullet
from explosion import Explosion


class Ship:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.game = game

        self.bullets = pygame.sprite.Group()

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.game)
            self.bullets.add(new_bullet)
            self.game.stats.bullets_fired += 1

    def update_bullets(self):
        self.bullets.update()
        for b in self.bullets.copy():
            if b.rect.bottom <= 0:
                self.bullets.remove(b)

        collision = pygame.sprite.groupcollide(
            self.bullets, self.game.aliens, True, True
        )

        if collision:
            for aliens in collision.values():
                for alien in aliens:
                    explosion = Explosion(self.game)
                    explosion.set_explosion_center_and_object(
                        alien.rect.center, "alien"
                    )
                    self.game.explosions.add(explosion)
                    self.game.stats.score += 1
                    # self.game.create_alien_fleet()

    def blit(self):
        self.screen.blit(self.image, self.rect)  # blit(source, dest)

    def update(self):
        if pygame.sprite.spritecollideany(self, self.game.aliens):
            print("CRASH!")

        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
