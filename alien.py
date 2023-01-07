from numpy import true_divide
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = ai_settings

        # to call draw function there should be 2 attributes
        # 1 - image
        # 2- rect

        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height + 40

        # storing alien exact position

        self.x = float(self.rect.x)

    def update(self):
        self.rect.x = self.rect.x + self.settings.alien_speed*self.settings.fleet_direction

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

        return False

    def draw_aliens(self):
        self.screen.blit(self.image, self.rect)
