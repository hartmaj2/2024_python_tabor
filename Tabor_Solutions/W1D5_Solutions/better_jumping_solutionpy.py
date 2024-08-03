import pygame
import math

pygame.init()

screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

player_surf = pygame.surface.Surface((50,50))
player_surf.fill("Red")
player_rect = player_surf.get_rect() 
player_rect.center = (150,150)

player_speed = [0,0]
player_x_speed = 5

gravity = 0.4
# TODO: Naimplementuj hloubou gravitaci: kazdy moment hraci uber trochu z jeho pozice, 

# TODO: naimplementuj skok tim, ze hrace teleportujes o neco vys

# TODO: naimplementuj kolizi se zemi tim, ze prestanes hrace posouvat dolu, pokud uz je moc nizko (na zemi)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player_speed[1] = -10
                

    keys = pygame.key.get_pressed()

    movement = 0
    if keys[pygame.K_LEFT]:
        movement -= 1
    if keys[pygame.K_RIGHT]:
        movement += 1

    player_speed[1] += gravity
    player_speed[0] = movement * player_x_speed
    
    player_rect.x += player_speed[0]
    player_rect.y += player_speed[1]


    screen.fill("Black")
    screen.blit(player_surf,player_rect)
    pygame.display.flip()
    clock.tick(60)


    # BONUS TODO: naimplementuj, aby hrac nemohl vyjet do boku mimo obrazovku
