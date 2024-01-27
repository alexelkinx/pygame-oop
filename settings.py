from dataclasses import dataclass


@dataclass
class Settings:
    screen_width = 800
    screen_height = 600
    caption = "Space Invaders"
    bg_color = (230, 230, 230)

    ship_speed = 0.5

    bullet_width = 3
    bullet_height = 15
    bullet_color = (255, 255, 255)
    bullet_speed = 0.5
    bullets_allowed = 3

    alien_speed = 0.2
