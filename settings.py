import pygame


class Settings:
    def __init__(self):
        # screen settings
        self.width = 1200
        self.length = 750
        self.bg_color = (230, 240, 220)
        # ship settings
        self.ship_speed = 1
        self.ship_limit = 3
        # bullet settings
        self.bullet_img = pygame.image.load("images/bullet.png")
        self.bullet_speed = 1.5
        self.Total_bullets = 50
        self.empty_bullet = False
        # missile settings
        self.missile_img = pygame.image.load("images/missile.png")
        self.missile_speed = 2.5
        self.Total_missiles = 3
        self.empty_missiles = False
        # alien
        self.alien_speed = 1
        self.fleet_drop_speed = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # torpedo
        self.speed_t = 1
        self.torpedo_img = pygame.image.load("images/torpedo (1).png")

        self.level_counter = 1
        self.points = 50

    def blitscreen(self, screen, bg_img):

        screen.blit(bg_img, (0, 0))

    def reset_settings(self):
        self.level_counter = 1
        self.Total_missiles = 3
        self.Total_bullets = 50
        self.points = 50
