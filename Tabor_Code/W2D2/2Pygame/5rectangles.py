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


snail_surf = pygame.image.load("Tabor_Code/W2D1/graphics/snail/snail1.png")
snail_rect = snail_surf.get_rect()
snail_rect.bottomright = (300,300)
# TODO: vyrob rectangle pro snaila a umisti snaila nohama na zemi (nebo ocasem na zemi?)
# HINT: nezapomen ho pak vykreslit na obrazovku (textura je surface a pozici zadej rectanglem)

# TODO: zkontroluj kolizi mezi hracem a snailem pomoci metody colliderect()
# vypis neco jako auvajs, pokud se dotkne hrac
snail_speed = -1
player_speed = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] == True:
        player_speed = -1
    elif keys[pygame.K_d] == True:
        player_speed = 1
    else:
        player_speed = 0

    snail_rect.x += snail_speed
    player_rect.x += player_speed

    if snail_rect.colliderect(player_rect) == True:
        snail_surf = pygame.transform.flip(snail_surf,True,False)
        snail_speed = 1

    screen.blit(background,(0,0))

    screen.blit(ground,(0,300))

    screen.blit(snail_surf,snail_rect)

    screen.blit(player_surf,player_rect)
    
    pygame.display.flip() 
    clock.tick(60)
    
    # BONUS TODO: naprogramuj snaila tak, aby se po doteku hrace otocil a jel zase na 
    # druhou stranu (hezke je i pridat, ze kdyz vyjede z obrazovky na jedne strane, tak se objevi na druhe)