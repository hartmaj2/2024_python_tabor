import pygame
import random
import os

pygame.init() 

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

stars_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/stars.png")

player_surf = pygame.image.load("Tabor_Code/W2D2/striped-grey-kitten.png")
player_surf = pygame.transform.scale_by(player_surf,0.4)
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,HEIGHT)

asteroid_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/asteroid.png")
asteroid_surf = pygame.transform.scale_by(asteroid_surf,0.1)

asteroid_rects : list[pygame.Rect] = []

player_speed = 5
falling_speed = 5

next_spawn_time = 0

def spawn_asteroid():
    nahodna_x = random.randint(0,WIDTH)
    rect = asteroid_surf.get_rect()
    rect.midtop = (nahodna_x,0)
    asteroid_rects.append(rect)

def remove_out_asteroids():
    for rect in asteroid_rects:
        if rect.y > HEIGHT:
            asteroid_rects.remove(rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_speed = -5
    elif keys[pygame.K_d]:
        player_speed = 5
    else:
        player_speed = 0
    
    if pygame.time.get_ticks() > next_spawn_time:
        prodleva = random.randint(100,1000)
        next_spawn_time = pygame.time.get_ticks() + prodleva
        spawn_asteroid()

    player_rect.x += player_speed
    
    screen.fill("black")
    screen.blit(stars_surf,(0,0))
    screen.blit(player_surf,player_rect)

    for rect in asteroid_rects:

        if rect.colliderect(player_rect):
            pygame.time.delay(1000)
            pygame.quit()
            exit()

        rect.y += falling_speed
        screen.blit(asteroid_surf,rect)

    pygame.display.flip() 
    clock.tick(60)
    