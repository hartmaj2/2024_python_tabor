import pygame

pygame.init() 

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

player = pygame.image.load("Tabor_Code/W2D1/graphics/Player/jump.png") 
player = pygame.transform.rotate(player,180)
player = pygame.transform.flip(player,True,False)

# TODO: naimportuj druhy obrazek a hod ho nekam na plochu

# TODO: co se stane kdyz je das oba na stejne misto?

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    screen.blit(player,(100,100))
     
    pygame.display.flip() 


# BONUS TODO: otoc obrazek hrace hlavou dolu  
# HINT: novy_surface = pygame.transform.rotate(stary_surface,pocet_stupnu_otoceni)

# EXTRA BONUS TODO: zkus najit prikaz v pygame.transform ktery ti umozni, aby i po otoceni hlavou dolu player koukal doprava