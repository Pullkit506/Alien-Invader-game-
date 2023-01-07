from ctypes import pointer
import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # dimensions
        self.width, self.height = 200, 50
        self.button_color = (230, 250, 230)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        # 0,0 - x, y coordinate of topleft point
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # The font.render() method also takes a Boolean value to turn antialiasing on or off (antialias- ing makes the edges of the text smoother).
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        # set the text background to the same color as the button. (If you don’t include a background color, Pygame will try to render the font with a trans- parent background.)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
