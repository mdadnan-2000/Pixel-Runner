import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    """Represents a moving obstacle (fly or snail) that the player must avoid."""
    def __init__(self, pr_game, type):
        """Initialize obstacle with animation frames based on type (fly or snail)."""
        super().__init__()
        self.settings = pr_game.settings

        if type == 'fly':
            fly_frame1= pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = self.settings.fly_y_pos
        else:
            snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = self.settings.ground_y
        
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    
    def _animation(self):
        """Update animation frame for the obstacle."""
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def _destroy(self):
        """Remove obstacle sprite when it moves off-screen to the left."""
        if self.rect.right < 0:
            self.kill()

    def _position(self):
        """Move obstacle to the left across the screen."""
        self.rect.left -= self.settings.speed

    def update(self):
        """Update obstacle animation, position, and check for removal."""
        self._animation()
        self._position()
        self._destroy()