import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

background = pygame.image.load("W1D5/graphics/Sky.png")
ground = pygame.image.load("W1D5/graphics/ground.png")


player_surface = pygame.image.load("W1D5/graphics/Player/player_stand.png")
player_rect = player_surface.get_rect()
player_rect.midbottom = (100,300)

snail_surface = pygame.image.load("W1D5/graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect()
snail_rect.bottomleft = (300,300)

# TODO: vyrob rectangle pro snaila a umisti snaila nohama na zemi (nebo ocasem na zemi?)

# TODO: zkontroluj kolizi mezi hracem a snailem pomoci metody colliderect()
# vypis neco jako auvajs, pokud se dotkne hrac

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: exit()
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))
    player_rect.x += 1
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)

    if(player_rect.colliderect(snail_rect)):
        print("auvajs")
        
    
    
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    