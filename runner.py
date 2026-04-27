import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.03)

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_walk_index = 0
        self.image = self.player_walk[self.player_walk_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = None
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = None

    def animation(self):
        if self.rect.bottom < 300:
            # In the air
            self.image = self.player_jump
        else:
            # In the ground
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk):
                self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]
    
    def update(self):
        self.player_input()
        if self.gravity != None:
            self.apply_gravity()
        self.animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame1= pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300
        
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    
    def animation(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def destroy(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.animation()
        self.rect.left -= 5
        self.destroy()
    

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacles, False):
        # Collided
        return False
    return True

def display_score():
    current_score = int(pygame.time.get_ticks() / 1000 ) - start_time
    score_surf = text_font.render(f"score: {current_score}", False, "#626262")
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_score


# Initialization
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)

bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.01)
bg_music.play(loops = -1) # Play this shit forever

game_active = False
start_time = 0
current_score = 0

# Background
sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# Obstacles
obstacles = pygame.sprite.Group()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = text_font.render('P i x e l   R u n n e r', False, "#d8d8d8")
game_name_rect = game_name.get_rect(center = (400, 70))

game_msg = text_font.render('press  space  to  run', False, "#d8d8d8")
game_msg_rect = game_msg.get_rect(center = (400, 340))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

while True:
    # Event loop - Check all possible events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == obstacle_timer:
                obstacles.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = int(pygame.time.get_ticks() / 1000)
                game_active = True
                obstacles.empty()
                bg_music.set_volume(0.01)

    if game_active:
        # Build displaying components
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        current_score = display_score()

        # Obstacles
        obstacles.draw(screen)
        obstacles.update()
        
        # Player
        player.draw(screen)
        player.update()

        # Collision
        game_active = collision_sprite()

    else:
        bg_music.set_volume(0)
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        if current_score == 0:
            screen.blit(game_msg, game_msg_rect)
        else:
            score_msg = text_font.render(f'Your score:  {current_score}', False, "#d8d8d8")
            score_msg_rect = score_msg.get_rect(center = (400, 340))
            screen.blit(score_msg, score_msg_rect)

    # Update the display
    pygame.display.update()

    # Controll display updates(per second)
    clock.tick(60)