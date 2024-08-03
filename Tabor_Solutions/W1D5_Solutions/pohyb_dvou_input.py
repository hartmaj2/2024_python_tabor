import pygame

pygame.init() # Tohle je dulezite, provede to nejakou magii, ktera vse pripravi

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Vytvorime okno tzv. DISPLAY SURFACE, zkusime spustit 
# Nyni vyrobime herni smycku, aby se okno vubec ukazalo tak (asi) potrebujeme prochazet
# vsechny eventy, muzeme vyzkouset, co se vypise

player = pygame.image.load("W1D5/graphics/Player/jump.png") 
character = pygame.Surface((100,100))
character.fill('Red')
player_x = 0
char_x = 0

# TODO: Pridej druhou postavu, ktera se bude hybat

# TODO: Ovladej pozici prvni postavy ctenim vstupu od uzivatele pomoci input()

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: exit()
    char_x += 2
    player_x = int(input())
    screen.blit(character,(char_x,300))
    screen.blit(player,(player_x,100))
     
    pygame.display.flip() 
    