from tkinter import TOP
from turtle import right
import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        # initialise the ship and set its starting position
        self.screen = screen
        self.setting = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        # centerx , bottom are keyword in pygame
        # matching the bottom of image to bottom of window and center of x axis of image to that of window so that we can place a ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        # To store the ship’s position accurately, we define a new attribute self.center, which can hold decimal values
        # self.center = float(self.rect.centerx)

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        # self.rect.right returns the x-coordinate value of the right edge of the ship’s rect
        if self.right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx = self.rect.centerx + self.setting.ship_speed

        if self.left and self.rect.left >= self.screen_rect.left:
            self.rect.centerx = self.rect.centerx - self.setting.ship_speed

        if self.down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.centery = self.rect.centery + self.setting.ship_speed

        if self.up and self.rect.top >= self.screen_rect.top:
            self.rect.centery = self.rect.centery - self.setting.ship_speed

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
