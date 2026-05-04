import pygame

class GameStat:
    """Tracks and displays the current game score and statistics."""
    def __init__(self, pr_game):
        """Initialize game stats with screen reference and starting score."""
        self.screen = pr_game.screen
        self.settings = pr_game.settings

        self.start_time = 0
        self.current_score = 0
    
    def reset_score(self):
        """Reset score timer and current score at the start of a new game."""
        self.start_time = int(pygame.time.get_ticks() / 1000)
        self.current_score = 0
    
    def display_score(self):
        """Calculate and render the current score on screen."""
        self.current_score = int(pygame.time.get_ticks() / 1000 ) - self.start_time
        score_surf = self.settings.text_font.render(f"score: {self.current_score}", False, "#626262")
        score_rect = score_surf.get_rect(center = (400, 50))
        self.screen.blit(score_surf, score_rect)