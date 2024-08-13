import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")


player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,300)

# TODO: vyrob rectangle pro snaila a umisti snaila nohama na zemi (nebo ocasem na zemi?)
# HINT: nezapomen ho pak vykreslit na obrazovku (textura je surface a pozici zadej rectanglem)

# TODO: naprogramuj snaila, aby se plazil smerem ke hraci

# TODO: zkontroluj kolizi mezi hracem a snailem pomoci metody colliderect()
# vypis neco jako auvajs, pokud se dotkne hrac


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    screen.blit(background,(0,0))

    screen.blit(ground,(0,300))

    screen.blit(player_surf,player_rect)
    
    pygame.display.flip() 
    clock.tick(60)
    
    # BONUS TODO: naprogramuj snaila tak, aby se po doteku hrace otocil a jel zase na 
    # druhou stranu (hezke je i pridat, ze kdyz vyjede z obrazovky na jedne strane, tak se objevi na druhe)