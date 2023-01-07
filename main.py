import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from bullets import Bullet, Missile
from pygame.sprite import Group
from alien import Alien
from random import randint
from game_stat import Game_stat
from button import Button
from scoreboard import ScoreBoard
# This group will be an instance of the class pygame.sprite.Group, which behaves like a list with some extra functionality that’s helpful when building games


class alienInvasion:
    def __init__(self):
        # initialise the game and create game resources
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.length))
        # caption
        pygame.display.set_caption("ALIEN INVASION")
        # icon
        icon = pygame.image.load("images/universe.png")
        pygame.display.set_icon(icon)
        # background
        background = pygame.image.load("images/background.jpg")
        self.bg_img = pygame.transform.scale(
            background, (self.settings.width, self.settings.length))

        # self.bg_color = self.settings.bg_color

        self.SHIP = Ship(self.screen, self.settings)
        # bullets storing
        self.missiles = Group()
        self.bullets = Group()
        self.torpedo = Group()

        # alien
        self.aliens = Group()
        # game_stats
        self.stats = Game_stat(self.settings)
        # button
        self.button = Button(self.settings, self.screen, "Play")

    def run_game(self):
        # creating fleet of aliens
        gf.create_fleet(self.settings, self.screen, self.aliens, self.SHIP)
        sb = ScoreBoard(self.settings, self.screen, self.stats)

        while (True):

            gf.check_events(self.settings, self.screen,
                            self.SHIP, self.bullets, self.missiles, self.stats, self.button, self.torpedo, self.aliens)
            if self.stats.game_active:
                self.SHIP.update_pos()
                gf.update_rid(self.bullets, self.missiles,
                              self.settings, self.aliens, self.SHIP, self.screen, self.torpedo, self.bg_img, self.stats, sb)
                gf.update_aliens(self.settings, self.screen,
                                 self.bullets, self.aliens, self.SHIP, self.stats, self.missiles, self.torpedo, self.button)
                u = randint(1, 500)
                if u < 2:
                    gf.torpedo_create(self.aliens, self.settings,
                                      self.screen, self.torpedo, self.SHIP)
            #  the group automatically calls update() for each sprite in the group.
            gf.update_screen(self.settings, self.screen,
                             self.SHIP, self.bg_img, self.bullets, self.missiles, self.aliens, self.torpedo, self.button, self.stats, sb)


if __name__ == '__main__':
    ai = alienInvasion()
    ai.run_game()
