import pygame

pygame.init()

screen = pygame.display.set_mode((900,600)) 

surface = pygame.Surface((200,100)) # 1. VYTVORIME SURFACE

# TODO: Zmen barvu surface na nejakou jinou

# TODO zmen kod aby vykreslil surface do leveho dolniho rohu

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(surface,(100,100)) # 2. REKNEME OBRAZOVCE, KAM A KOHO MA NAKRESLIT
    pygame.display.flip() # 3. REKNEME PYGAME, AT OBNOVI OBRAZOVKU
    