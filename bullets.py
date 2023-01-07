import pygame
from pygame.sprite import Sprite
from time import sleep


class Bullet(Sprite):
    # class to manage bullet
    def __init__(self, screen, ai_settings, ship):
        """Create a bullet object at the ship's current position."""
        #  we call super() to inherit properly from Sprite.
        super().__init__()
        # When you use sprites, you can group related ele- ments in your game and act on all the grouped elements at once.

        self.screen = screen
        self.settings = ai_settings

        self.Total = self.settings.Total_bullets
        image = self.settings.bullet_img
        self.img = pygame.transform.scale(image, (25, 25))
        self.rect = self.img.get_rect()

        self.rect.y = ship.rect.top - 8
        self.rect.x = ship.rect.centerx - 12
        self.y = float(self.rect.y)

        self.speed = self.settings.bullet_speed

    def update(self):
        # Update the rect position.
        self.rect.y = self.rect.y - self.speed

    def draw_bullets(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.img, self.rect)


class Missile(Sprite):
    def __init__(self, screen, ai_settings, ship):
        """Create a bullet object at the ship's current position."""
        #  we call super() to inherit properly from Sprite.
        super().__init__()
        self.screen = screen
        self.settings = ai_settings

        # missile
        self.m_speed = self.settings.missile_speed
        self.Total = self.settings.Total_missiles

        misile_img = self.settings.missile_img
        self.missile_img = pygame.transform.scale(misile_img, (60, 60))

        self.rect = self.missile_img.get_rect()
        self.rect.x = ship.rect.centerx - 28
        self.rect.y = ship.rect.bottom - 100
        self.y = float(self.rect.y)

    def update(self):
        self.rect.y = self.rect.y - self.m_speed + 0.5

    def draw_missiles(self):
        self.screen.blit(self.missile_img, self.rect)


class Torpedo(Sprite):
    def __init__(self, screen, ai_settings, aliens):
        """Create a bullet object at the ship's current position."""
        #  we call super() to inherit properly from Sprite.
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        self.alien = aliens
        self.speed = self.settings.speed_t

        img = self.settings.torpedo_img
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.alien.rect.centerx - 28
        self.rect.y = self.alien.rect.bottom

    def update(self):
        self.rect.y = self.rect.y + self.speed

    def draw_torpedo(self):
        self.screen.blit(self.image, self.rect)
