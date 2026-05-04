import pygame

class Player(pygame.sprite.Sprite):
    """Represents the player character with walking and jumping animations."""
    def __init__(self, pr_game):
        """Initialize player with walk and jump animations, starting position on ground."""
        super().__init__()
        self.settings = pr_game.settings
        self.y_val = None
        self.settings.jump_sound.set_volume(self.settings.jump_sound_volumne)

        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_walk_index = 0
        self.image = self.player_walk[self.player_walk_index]
        self.rect = self.image.get_rect(midbottom = (80, self.settings.ground_y)) 
    
    def _jump_chk(self):
        """Check for space key press and initiate jump if player is on ground."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.settings.ground_y:
            self.y_val = self.settings.velocity
            self.settings.jump_sound.play()
    
    def _apply_gravity(self):
        """Apply gravity to player and update vertical position, landing on ground when appropriate."""
        self.y_val += self.settings.gravity
        self.rect.y += self.y_val
        if self.rect.bottom >= self.settings.ground_y:
            self.rect.bottom = self.settings.ground_y
            self.y_val = None

    def _animation(self):
        """Update player image based on whether jumping or walking on ground."""
        if self.rect.bottom < self.settings.ground_y:
            # In the air
            self.image = self.player_jump
        else:
            # In the ground
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk):
                self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]
    
    def update(self):
        """Update player state including jump input, gravity, and animation."""
        self._jump_chk()
        if self.y_val != None:
            self._apply_gravity()
        self._animation()