import pygame
import math

pygame.init()

screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

player_surf = pygame.surface.Surface((50,50))
player_surf.fill("Red")
player_rect = player_surf.get_rect() 
player_rect.center = (150,150)

# TODO: naimplementuj hloupou gravitaci: kazdy moment hraci pridej k jeho y pozici (tim bude jakoby padat)

# TODO: naimplementuj skok tim, ze hrace teleportujes o neco vys
# HINT: budeme chtit registrovat event aby se teleportoval jen jednou

# TODO: naimplementuj kolizi se zemi tim, ze prestanes hrace posouvat dolu, pokud uz je moc nizko (na zemi)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    screen.fill("Black")
    screen.blit(player_surf,player_rect)
    pygame.display.flip()
    clock.tick(60)


    # BONUS TODO: naimplementuj, aby hrac nemohl vyjet do boku mimo obrazovku
