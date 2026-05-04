import pygame

class Settings:
    """Stores all game configuration settings and constants."""
    def __init__(self):
        """Initialize all game settings including screen size, fonts, audio, and gameplay parameters."""
        # Screen 
        self.screen_height = 400
        self.screen_width = 800
        self.ground_y = 300

        # Font 
        self.text_font = pygame.font.Font('font/Pixeltype.ttf', 50)

        # Background music
        self.bg_music = pygame.mixer.Sound('audio/music.wav')
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.bg_music_volumne = 0.1
        self.jump_sound_volumne = 0.3

        # Player
        self.velocity = -20
        self.gravity = 1

        # Obstacle
        self.fly_y_pos = 210
        self.speed = 5
        self.creation_rate = 1200 # add 1 obstacle per 1200 ms

        # Inro page
        self.ip_bg_color = (94, 129, 162)
        self.ip_font_color = "#d8d8d8"
        

