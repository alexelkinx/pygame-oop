import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    def __init__(self, game):
        super().__init__()
        self.anim = {}
        self.anim["alien"] = []
        # self.anim['ship'] = []
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.frame_rate = 50
        self.game = game

        for i in range(9):
            file_name = f"regularExplosion0{i}.png"
            image = pygame.image.load("images/" + file_name).convert_alpha()
            scaled_image = pygame.transform.scale(image, (60, 58))
            self.anim["alien"].append(scaled_image)

    def set_explosion_center_and_object(self, center, object):
        self.object = object
        self.image = self.anim[self.object][0]
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim[self.object]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.anim[self.object][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
