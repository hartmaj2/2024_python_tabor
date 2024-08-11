import pygame
import math
import random

pygame.init() 

WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

player = pygame.image.load("Tabor_Code/W2D1/graphics/Player/jump.png") 
player_x = 250
player_y = 450
speed = 0
rotation = 0

walking = False
next_event = pygame.time.get_ticks() + random.randint(100,2000)

# TODO: rozpohybuj postavicku smerem do prava

# TODO: Pri pohybu se postavicka na obrazovku vykresli na novou pozici ale nezmizi z te stare
# udelej neco s obrazovkou vzdy, nez vykreslis postavu na nove pozici, aby uz nebyla na te stare

# TODO: Pridej druhou postavu, ktera se bude hybat doleva

# TODO: Ovladej pozici prvni postavy ctenim vstupu od uzivatele pomoci input()
# Uzivatel tedy bude moci zadat, na jakou x souradnici bude chtit postavicku teleportovat

def calculate_x_y_movement(how_much,rotation):
    return how_much * math.cos(rotation), how_much * math.sin(rotation)

clock = pygame.time.Clock()    

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    screen.fill("black")

    if pygame.time.get_ticks() > next_event:
        if walking:
            speed = 0
            next_event = pygame.time.get_ticks() + random.randint(1000,3000)
            walking = False
        else:
            speed = 3
            rotation = math.pi / 2 * random.randint(0,3)
            next_event = pygame.time.get_ticks() + random.randint(500,1500)
            walking = True
        print(rotation)

    delta_x,delta_y = calculate_x_y_movement(speed,rotation)
    player_x += delta_x
    player_x = player_x % WIDTH

    player_y += delta_y
    player_y = player_y % HEIGHT
    screen.blit(player,(player_x,player_y))
    
     
    pygame.display.flip() 

    clock.tick(60)


# BONUS TODO: Odeber stupidni ovladani a uprav kod tak, aby kdyz je postava mimo obrazovku se objevila zase na druhe strane

# EXTRA BONUS TODO: Zpusob, aby se postavicky pohybovali jako opila zelva
# (tady se hodi zalozit si promennou pro rotaci a pouzit funkce sinus a cosinus pro spocteni, o kolik se postavicka ma pri dane rotaci posunout po x a po y)
# (!) POZOR: uhel se zadava v radianech, pokud pouzivas math.sin() nebo math.cos()