import pygame
import math

pygame.init()

screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

player_surf = pygame.surface.Surface((50,50))
player_surf.fill("Red")
player_rect = player_surf.get_rect() 
player_rect.center = (150,150)

# TODO: pohybuj hracem pomoci sipek (vytvoris promennou keys = pygame.key.get_pressed())
# tim ziskas seznam, ve kterem je True / False pro pozici odpovidajici klavesy
# odpovidajici pozice klaves v seznamu muzes ziskat pomoci pygame.K_UP atd.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    for i in range(40,90):
        if keys[i]:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print("...")

    screen.fill("Black")
    screen.blit(player_surf,player_rect)
    pygame.display.flip()
    clock.tick(60)


    # BONUS TODO: kdyz se pohybujes diagonalne (sikmo) tak je postavicka pomalejsi/rychlejsi? proc?
    # zkus se zamyslet v cem je problem a treba ho i opravit (zase je pytagoras kamarad)