class Game_stat:
    def __init__(self, ai_settings):
        self.settings = ai_settings
        self.reset_stat()
        self.game_active = False
        self.score = 0
        # we’ll need to reset some statistics each time the player starts
        # a new game. To do this, we’ll initialize most of the statistics in the method reset_stats() instead of directly in __init__(). We’ll call this method from __init__() so the statistics are set properly when the GameStats instance is first createdu, but we’ll also be able to call reset_stats() any time the player starts a new game.

    def reset_stat(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
