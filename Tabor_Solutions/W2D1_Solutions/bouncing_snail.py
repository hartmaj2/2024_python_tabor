import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")


player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,300)

# TODO: vyrob rectangle pro snaila a umisti snaila nohama na zemi (nebo ocasem na zemi?)
# HINT: nezapomen ho pak vykreslit na obrazovku (textura je surface a pozici zadej rectanglem)
snail_surf = pygame.image.load("Tabor_Code/W2D1/graphics/snail/snail1.png")
snail_rect = snail_surf.get_rect()
snail_rect.midbottom = (500,300)

snail_speed = -5

# TODO: zkontroluj kolizi mezi hracem a snailem pomoci metody colliderect()
# vypis neco jako auvajs, pokud se dotkne hrac

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    snail_rect.x += snail_speed

    if snail_rect.colliderect(player_rect):
        snail_surf = pygame.transform.flip(snail_surf,True,False)
        snail_speed *= -1
    
    snail_rect.centerx %= WIDTH

    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    screen.blit(player_surf,player_rect)
    screen.blit(snail_surf,snail_rect)
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    
    # BONUS TODO: naprogramuj snaila tak, aby se po doteku hrace otocil a jel zase na 
    # druhou stranu (hezke je i pridat, ze kdyz vyjede z obrazovky na jedne strane, tak se objevi na druhe)