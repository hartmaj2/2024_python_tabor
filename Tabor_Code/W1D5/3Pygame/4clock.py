import pygame

pygame.init() 

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

player = pygame.image.load("W1D5/graphics/Player/jump.png")
player_x = 0


while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    screen.fill("Black")
    player_x += 5
    if player_x > WIDTH:
        player_x = 0 - player.get_width()
    screen.blit(player,(player_x,100))
    
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    