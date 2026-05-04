import pygame
from sys import exit
from random import choice
from settings import Settings
from background import Background
from intro_page import IntroPage
from player import Player
from obstacle import Obstacle
from game_stat import GameStat

class PixelRunner:
    """Main game class that manages game initialization, events, updates, and rendering."""
    def __init__(self):
        """Initialize the game with Pygame, settings, graphics, and sprite groups."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Pixel Runner")

        self.settings.bg_music.set_volume(0)
        self.settings.bg_music.play(loops = -1)

        self.score_stat = GameStat(self)

        self.bg = Background(self)
        self.into_page = IntroPage(self)

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self))

        self.obstacles = pygame.sprite.Group()
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, self.settings.creation_rate)

        self.game_active = False
    
    def run_game(self):
        """Main game loop that runs until the game is quit."""
        while True:
            self._check_events()

            if self.game_active:
                self.player.update()
                self.obstacles.update()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Handle user input and game events (quit, start game, create obstacles)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active:
                if event.type == self.obstacle_timer:
                        self._create_obstacle()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self._start_new_game()

    def _create_obstacle(self):
        """Spawn a random obstacle (fly or snail) on the screen."""
        obstacle = Obstacle(self, choice(['fly', 'snail', 'snail', 'snail']))
        self.obstacles.add(obstacle)
    
    def _start_new_game(self):
        """Initialize a new game session and reset all game state."""
        self.score_stat.reset_score()
        self.game_active = True
        self.obstacles.empty()
        self.settings.bg_music.set_volume(self.settings.bg_music_volumne)
    
    def _collision_chk(self):
        """Check if player collided with any obstacle; return False if collision detected."""
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacles, False):
            # Collided
            return False
        return True

    def _update_screen(self):
        """Render game graphics and update display based on game state."""
        if self.game_active:
            self.bg.draw()
            self.player.draw(self.screen)
            self.obstacles.draw(self.screen)
            self.score_stat.display_score()

            self.game_active = self._collision_chk()
        else:
            self.settings.bg_music.set_volume(0)
            msg = f"Your score: {self.score_stat.current_score}" if self.score_stat.current_score > 0 else None
            self.into_page.draw(msg)
        
        pygame.display.flip()

if __name__ == "__main__":
    PixelRunner().run_game()