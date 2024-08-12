# DEMO WHY YOU SHOULD DELETE CHARACTERS THAT ARE OUT OF SCREEN
# (1) we create 250 000 (1/4 million) flys at the edge of the screen
# (2) you can see the number of flys on the screen
# (3) press space to delete all except 100 last flys in the list

import pygame
import random

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")

player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,300)

number_of_flys_text_surf = font.render(f"Flys amount: 0",True,"black")
number_of_flys_text_rect = number_of_flys_text_surf.get_rect()
number_of_flys_text_rect.midtop = (WIDTH/2,20)

fly_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Fly/Fly1.png")
fly_surf = pygame.transform.flip(fly_surf,True,False)
flys = []

asteroid_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/asteroid.png")
asteroid_surf = pygame.transform.scale_by(asteroid_surf,0.1)
asteroids = []

def spawn_object(position, texture : pygame.Surface, creature_list : list):
    rect = texture.get_rect()
    rect.center = position
    creature_list.append(rect)


def update_all_asteroids(screen : pygame.Surface, asteroids : list[pygame.Rect], flys : list[pygame.Rect]):
    for asteroid_rect in asteroids:
        asteroid_rect.x -= 5
        collision_index = asteroid_rect.collidelist(flys)
        if collision_index >= 0:
            asteroids.remove(asteroid_rect)
            flys.remove(flys[collision_index])
        if asteroid_rect.colliderect(player_rect):
            input("You lost...")
            pygame.quit()
            exit()
        if asteroid_rect.right < 0:
            asteroids.remove(asteroid_rect)
        screen.blit(asteroid_surf,asteroid_rect)

def update_all_flys(screen : pygame.Surface, flys : list[pygame.Rect]):
    for fly_rect in flys:
        fly_rect.x += 10
        if fly_rect.left > WIDTH:
            flys.remove(fly_rect)
        screen.blit(fly_surf,fly_rect)

spawn_event = pygame.event.custom_type()
spawn_interval = 1000
pygame.time.set_timer(spawn_event,spawn_interval)

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                spawn_object(player_rect.center,fly_surf,flys)
        if event.type == spawn_event:
            spawn_object((WIDTH,random.randint(0,HEIGHT)),asteroid_surf,asteroids)

    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    number_of_flys_text_surf = font.render(f"Flys amount: {len(flys)}",True,"black")
    number_of_flys_text_rect = number_of_flys_text_surf.get_rect()
    number_of_flys_text_rect.midtop = (WIDTH/2,20)
    screen.blit(number_of_flys_text_surf,number_of_flys_text_rect)
    
    update_all_flys(screen,flys)
    update_all_asteroids(screen,asteroids,flys)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 10
    if keys[pygame.K_s]:
        player_rect.y += 10

    screen.blit(player_surf,player_rect)
    screen.blits
    
    pygame.display.update() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    