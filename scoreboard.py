import pygame.font


class ScoreBoard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats

        # font settings
        self.text_color = (30, 20, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.width, self.height = 200, 50
        self.button_color = (230, 230, 230)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft

        self.prep_score()

    def prep_score(self):
        score_str = "Score: "
        score_str += str(self.stats.score)
        self.score_img = self.font.render(
            score_str, True, self.text_color, self.button_color)
        self.score_rect = self.score_img.get_rect()

    def draw_score(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.score_img, self.score_rect)
