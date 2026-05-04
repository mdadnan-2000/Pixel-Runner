import pygame

class Background:
    """Handles rendering of sky and ground textures for the game environment."""
    def __init__(self, pr_game):
        """Initialize background with screen and settings from the game instance."""
        self.screen = pr_game.screen
        self.settings = pr_game.settings

        self.sky_surf = pygame.image.load('graphics/sky.png').convert()
        self.ground_surf = pygame.image.load('graphics/ground.png').convert()
    
    def draw(self):
        """Draw the sky and ground surfaces to the screen."""
        self.screen.blit(self.sky_surf, (0, 0))
        self.screen.blit(self.ground_surf, (0, self.settings.ground_y))