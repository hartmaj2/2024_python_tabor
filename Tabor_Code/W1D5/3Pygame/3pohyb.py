import pygame

pygame.init() 

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

player = pygame.image.load("W1D5/graphics/Player/jump.png") 
player_x = 0

# TODO: rozpohybuj postavicku

# TODO: Pri pohybu se postavicka na obrazovku vykresli na novou pozici ale nezmizi z te stare
# udelej neco s obrazovkou vzdy, nez vykreslis postavu na nove pozici, aby uz nebyla na te stare

# TODO: Pridej druhou postavu, ktera se bude hybat

# TODO: Ovladej pozici prvni postavy ctenim vstupu od uzivatele pomoci input()

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    screen.blit(player,(player_x,100))
     
    pygame.display.flip() 


# BONUS TODO: Zrus ovladani, ale uprav kod tak, aby kdyz je postava mimo obrazovku se objevila zase na druhe strane
    