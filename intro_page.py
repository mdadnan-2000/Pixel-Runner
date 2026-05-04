import pygame

class IntroPage:
    """Displays the introduction/menu screen before gameplay starts."""
    def __init__(self, pr_game):
        """Initialize intro page with game title, player stand image, and instructions."""
        self.screen = pr_game.screen
        self.settings = pr_game.settings

        self.player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center = (400, 200))

        self.game_name = self.settings.text_font.render('P i x e l   R u n n e r', False, self.settings.ip_font_color)
        self.game_name_rect = self.game_name.get_rect(center = (400, 70))

        self.game_msg = self.settings.text_font.render('press  space  to  run', False, self.settings.ip_font_color)
        self.game_msg_rect = self.game_msg.get_rect(center = (400, 340))

    def draw(self, msg = None):
        """Draw intro page with title, player image, and optional message."""
        self.screen.fill(self.settings.ip_bg_color)
        self.screen.blit(self.player_stand, self.player_stand_rect)
        self.screen.blit(self.game_name, self.game_name_rect)
        if not msg:
            self.screen.blit(self.game_msg, self.game_msg_rect)
        else:
            msg_img = self.settings.text_font.render(f"{msg}", False, self.settings.ip_font_color)
            msg_img_rect = msg_img.get_rect(center = (400, 340))
            self.screen.blit(msg_img, msg_img_rect)
