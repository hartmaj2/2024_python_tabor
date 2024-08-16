import pygame
import random
import os

pygame.init() 

WIDTH = 800
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)

game_music = pygame.mixer.Sound("Tabor_Code/W2D1/sounds/music.ogg")
game_music.set_volume(0.1)
explosion_sound = pygame.mixer.Sound("Tabor_Code/W2D1/sounds/explosion.wav")
shot_sound = pygame.mixer.Sound("Tabor_Code/W2D1/sounds/shot.wav")

text_surf = font.render("Ahoj svete",True,"white")
text_rect = text_surf.get_rect()
text_rect.topright = (WIDTH-20,20)

stars_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/stars.png")

player_surf = pygame.image.load("Tabor_Code/W2D2/striped-grey-kitten.png")
player_surf = pygame.transform.scale_by(player_surf,0.4)
player_rect = player_surf.get_rect()
player_rect.midbottom = (WIDTH/2,HEIGHT)

explosion_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/explosion.png")
explosion_surf = pygame.transform.scale_by(explosion_surf,0.1)


asteroid_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/asteroid.png")
asteroid_surf = pygame.transform.scale_by(asteroid_surf,0.1)
asteroid_hitbox_scale = 0.65 

laser_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/laser.png")
laser_surf = pygame.transform.scale_by(laser_surf,0.3)

asteroid_rects : list[pygame.Rect] = []
lasers_rects : list[pygame.Rect] = []

base_speed  = 5
player_speed = 5
falling_speed = 5
shot_speed = 10

next_spawn_time = 0
next_shot_time = 0

# for explosion we need to add code, that will wait after the player has died until the game_end_time time

# we also add boolean indicator to show, whether the player is dead or not so we can decide to not
# update score if the player is dead already

# for animation, we need a variable to hold time, when the animation frame should change to the next frame
# it is also nice to calculate this time using explosion_duration / explosion_frames

# to be extra nice, we can add variable current frame to see, if we are halfway through the animation
# if we are, we can start scaling the explosion down again

current_frame = 0
explosion_duration = 500
explosion_frames = 20
next_explosion_frame = 0
game_end_time = 60_000_000
player_dead = False

def update_score():
    global text_rect, text_surf
    time_seconds = int(pygame.time.get_ticks() / 1000)
    print(time_seconds)
    text_surf = font.render("Skore: " + str(time_seconds),True,"white")
    text_rect = text_surf.get_rect()
    text_rect.topright = (WIDTH-20,20)

def spawn_asteroid():
    nahodna_x = random.randint(0,WIDTH)
    rect = asteroid_surf.get_rect()
    rect.scale_by_ip(asteroid_hitbox_scale)
    rect.midtop = (nahodna_x,0)
    asteroid_rects.append(rect)

def spawn_laser():
    rect = laser_surf.get_rect()
    rect.center = player_rect.center
    lasers_rects.append(rect)

def remove_out_asteroids():
    for rect in asteroid_rects:
        if rect.y > HEIGHT:
            asteroid_rects.remove(rect)

def get_new_speed(keys):
    new_speed = 0
    if keys[pygame.K_a]:
        new_speed -= base_speed
    if keys[pygame.K_d]:
        new_speed += base_speed
    return new_speed

def spawn_if_time(time_now):
    global next_spawn_time
    if time_now > next_spawn_time:
        prodleva = random.randint(100,1000)
        next_spawn_time = time_now + prodleva
        spawn_asteroid()

def update_player():
    global player_speed, player_rect
    keys = pygame.key.get_pressed()
    player_speed = get_new_speed(keys)
    player_rect.x += player_speed

def update_asteroids():
    global asteroid_rects,falling_speed,player_rect,player_dead,game_end_time,player_surf
    for rect in asteroid_rects:
        rect.y += falling_speed
        if rect.y > HEIGHT:
            asteroid_rects.remove(rect)
        if rect.colliderect(player_rect) and not player_dead:
            explosion_sound.play()
            player_dead = True
            game_end_time = pygame.time.get_ticks() + explosion_duration
            old_center = player_rect.center
            player_surf = explosion_surf
            player_rect = player_surf.get_rect(center = old_center)
            asteroid_rects.remove(rect)

def update_lasers():
    for laser_rect in lasers_rects:
        laser_rect.y -= shot_speed
        if laser_rect.bottom < 0:
            lasers_rects.remove(laser_rect)
        for asteroid_rect in asteroid_rects:
            if laser_rect.colliderect(asteroid_rect):
                asteroid_rects.remove(asteroid_rect)
        
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

def get_blit_pos_for_scaled(orig_rect : pygame.Rect ,scale : float):
    move_amount = (orig_rect.width / scale) * (1 - scale) / 2
    print(move_amount)
    return pygame.Rect(orig_rect.left-move_amount,orig_rect.top-move_amount,orig_rect.width/scale,orig_rect.height/scale)
    
def draw_everything():
    global screen, stars_surf, player_surf, asteroid_rects, asteroid_surf
    screen.blit(stars_surf,(0,0))
    screen.blit(player_surf,player_rect)
    for rect in asteroid_rects:
        screen.blit(asteroid_surf,get_blit_pos_for_scaled(rect,asteroid_hitbox_scale))

    for kebab in lasers_rects:
        screen.blit(laser_surf,kebab) 
    screen.blit(text_surf,text_rect)

def check_key_presses():
    global next_shot_time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and pygame.time.get_ticks() > next_shot_time:
        next_shot_time = pygame.time.get_ticks() + 500
        shot_sound.play()
        spawn_laser()

def check_explosion_over():
    if pygame.time.get_ticks() > game_end_time:
        pygame.quit()
        exit()

def animate_explosion():
    global current_frame,player_surf,player_rect,next_explosion_frame
    if pygame.time.get_ticks() > next_explosion_frame:
        current_frame += 1
        old_center = player_rect.center
        scale = 0.8
        if current_frame < explosion_frames // 2:
            scale = 1.2
        player_surf = pygame.transform.scale_by(player_surf,scale)
        player_rect = player_surf.get_rect(center=old_center)
        next_explosion_frame = pygame.time.get_ticks() + explosion_duration / explosion_frames

game_music.play(loops=-1)

while True:

    check_events()

    if not player_dead:

        check_key_presses()

        update_score()

        update_player()
        
        update_asteroids()

        update_lasers()

        spawn_if_time(pygame.time.get_ticks())
        
        draw_everything()
    
    if player_dead:

        update_asteroids()

        check_explosion_over()

        animate_explosion()

        draw_everything()
    
    pygame.display.flip() 
    clock.tick(60)
    