import pygame
import math

pygame.init()

screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

player_surf = pygame.surface.Surface((50,50))
player_surf.fill("Red")
player_rect = player_surf.get_rect() 
player_rect.center = (150,150)

# TODO: Naimplementuj chytrou gravitaci: budeme potrebovat promennou pro hracovu rychlost letu
# pojmenuj ji treba speed_y

# TODO: skok naimplementujeme tak, ze nastavime hracovu speed_y na nejakou pevnou hodnotu (treba 5) vzdy, kdyz stiskneme sipku nahoru

# TODO: gravitace v kazdem tiknuti cyklu ukousne pevne danou hodnotu z jeho speed_y

# TODO: ted uz staci jen vzdy menit y pozici hrace o speed_y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    screen.fill("Black")
    screen.blit(player_surf,player_rect)
    pygame.display.flip()
    clock.tick(60)


    # BONUS TODO: naimplementuj, aby hrac nemohl skakat ve vzduchu
