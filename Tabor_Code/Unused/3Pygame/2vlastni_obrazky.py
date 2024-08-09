import pygame

pygame.init() 

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

player = pygame.image.load("W1D5/graphics/Player/jump.png") 

# TODO: naimportuj druhy obrazek a hod ho nekam na plochu

# TODO: co se stane kdyz je das oba na stejne misto?

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(player,(100,100))
     
    pygame.display.flip() 
    