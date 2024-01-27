import pygame


class Text:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.text_color = (255, 255, 255)
        # self.font = pygame.font.Font('font_name.ttf, 30')
        self.font = pygame.font.SysFont(None, 30)
        self.x = x
        self.y = y

    def blit(self, caption, value):
        text_string = caption + " " + str(value)
        text = self.font.render(text_string, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.topleft = (self.x, self.y)
        self.screen.blit(text, text_rect)
