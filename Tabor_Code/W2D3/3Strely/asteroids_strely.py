import pygame
import random
import os

pygame.init() 

WIDTH = 800
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

stars_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/stars.png")

player_surf = pygame.image.load("Tabor_Code/W2D2/striped-grey-kitten.png")
player_surf = pygame.transform.scale_by(player_surf,0.4)
player_rect = player_surf.get_rect()
player_rect.midbottom = (WIDTH/2,HEIGHT)

asteroid_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/asteroid.png")
asteroid_surf = pygame.transform.scale_by(asteroid_surf,0.1)

shot_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/laser.png")
shot_surf = pygame.transform.scale_by(shot_surf,0.2)

# TODO: pridat surface pro strelu

# TODO: spawnovat strelu na hraci, kdyz stiskne klavesu urcenou pro srileni

# TODO: strely jsou jako asteroidy, ale litaji nahoru

# TODO: kolize nyni musime kontrolovat mezi strelou a vsemi asteroidy
# (tzn mezi strelou a celym seznamem asteroidu)

asteroid_rects : list[pygame.Rect] = []
shots : list[pygame.Rect] = []

base_speed  = 5
player_speed = 5
falling_speed = 5
shot_speed = 10

next_spawn_time = 0

def spawn_asteroid():
    nahodna_x = random.randint(0,WIDTH)
    rect = asteroid_surf.get_rect()
    rect.midtop = (nahodna_x,0)
    asteroid_rects.append(rect)

def shoot():
    global player_rect,shots
    rect = shot_surf.get_rect()
    rect.center = player_rect.center
    shots.append(rect)

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

def update_shots():
    global shots, shot_speed, asteroid_rects
    for rect in shots:
        rect.y -= shot_speed
        if rect.bottom < 0:
            shots.remove(rect)
        result = rect.collidelist(asteroid_rects)
        if result != -1:
            asteroid_rects.remove(asteroid_rects[result])
            shots.remove(rect)
        

def update_asteroids():
    global asteroid_rects,falling_speed,player_rect
    for rect in asteroid_rects:
        rect.y += falling_speed
        if rect.y > HEIGHT:
            asteroid_rects.remove(rect)
        if rect.colliderect(player_rect):
            pygame.quit()
            exit()

def draw_everything():
    global screen, stars_surf, player_surf, asteroid_rects, asteroid_surf
    screen.blit(stars_surf,(0,0))
    screen.blit(player_surf,player_rect)
    for asteroid_rect in asteroid_rects:
        screen.blit(asteroid_surf,asteroid_rect)
    for shot_rect in shots:
        screen.blit(shot_surf,shot_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                shoot()
    
    update_player()
    
    update_asteroids()

    update_shots()

    spawn_if_time(pygame.time.get_ticks())
    
    draw_everything()
    
    pygame.display.flip() 
    clock.tick(60)
    