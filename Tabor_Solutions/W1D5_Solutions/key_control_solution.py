import pygame
import math

pygame.init()

screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

player_surf = pygame.surface.Surface((50,50))
player_surf.fill("Red")
player_rect = player_surf.get_rect() 
player_rect.center = (150,150)

player_speed = 10

# TODO: pohybuj hracem pomoci sipek (vytvor keys = pygame.key.get_pressed())
# tim ziskas seznam, ve kterem je True / False pro pozici odpovidajici klavesy
# pozice muzes ziskat pomoci pygame.K_UP atd.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    movement = [0,0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        movement[1] -= 1
    if keys[pygame.K_DOWN]:
        movement[1] += 1
    if keys[pygame.K_LEFT]:
        movement[0] -= 1
    if keys[pygame.K_RIGHT]:
        movement[0] += 1

    if abs(movement[0]) + abs(movement[1]) > 1:
        movement[0] /= 1.41
        movement[1] /= 1.41

    player_rect.x += movement[0] * player_speed
    player_rect.y += movement[1] * player_speed

    screen.fill("Black")
    screen.blit(player_surf,player_rect)
    pygame.display.flip()
    clock.tick(60)


    # BONUS TODO: kdyz se pohybujes diagonalne (sikmo) tak je postavicka pomalejsi/rychlejsi? proc?
    # zkus se zamyslet v cem je problem a treba ho i opravit (zase je pytagoras kamarad)