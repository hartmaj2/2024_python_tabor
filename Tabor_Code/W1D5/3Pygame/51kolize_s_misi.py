import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

background = pygame.image.load("W1D5/graphics/Sky.png")
ground = pygame.image.load("W1D5/graphics/ground.png")

# TODO: vyrobit tridu Character, ktera zakomponuje surface a rect do jednoho objektu

player = Character(pygame.image.load("W1D5/graphics/Player/player_stand.png"))
player.rect.midbottom = (100,300)

# TODO: Vyrob pole, do ktereho pak budes ukladat mouchy

# TODO: Vytiskni vzkaz, pokud je stisknuta mys (pygame.MOUSEBUTTONDOWN)
# HINT: zkontroluj event.type

# TODO: definuj si funkci spawn_fly(pozice), ktera prida mouchu s nastavenou pozici do seznamu flys

# TODO: zavolej tu funkci, kdyz se stiskne mys na hraci (funkce collidepoint() )

# TODO: projed pres seznam a vsechny charaktery v nem vytiskni a pohni s nimi

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    screen.blit(player.surf,player.rect) 
    
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)

# BONUS TODO: deletuj mouchy z listu, pokud vyleti mimo obrazovku