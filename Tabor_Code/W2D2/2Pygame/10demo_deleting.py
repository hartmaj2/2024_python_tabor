# DEMO WHY YOU SHOULD DELETE CHARACTERS THAT ARE OUT OF SCREEN
# (1) we create 250 000 (1/4 million) flys at the edge of the screen
# (2) you can see the number of flys on the screen
# (3) press space to delete all except 100 last flys in the list

import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")

player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,300)

number_of_flys_text_surf = font.render(f"Flys amount: 0",True,"black")
number_of_flys_text_rect = number_of_flys_text_surf.get_rect()
number_of_flys_text_rect.midtop = (WIDTH/2,20)

fly_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Fly/Fly1.png")
fly_surf = pygame.transform.flip(fly_surf,True,False)
# TODO: Vyrob prazdne pole, do ktereho pak budes ukladat mouchy
# HINT: staci ukladat jejich rectangles, obrazek muzes pouzit pro vsechny stejny
flys = []


# TODO: Vytiskni vzkaz, pokud je stisknuta mys (pygame.MOUSEBUTTONDOWN)
# HINT: zkontroluj event.type

# TODO: definuj si funkci spawn_fly(pozice), ktera prida mouchu se zadanou pozici do seznamu flys

def spawn_fly(position):
    fly_rect = fly_surf.get_rect()
    fly_rect.bottomleft = position
    flys.append(fly_rect)

# TODO: zavolej tu funkci, kdyz se stiskne mys

# TODO: zadefinuj si funkci update_all_flys(seznam), ktera pohne vsemi mouchami
# (!) POZOR: nezapomen mouchy ze seznamu mazat, pokud vyleti z obrazovky (hru to zatim nijak neovlivni, ale je to dobry navyk)

def update_all_flys(screen : pygame.Surface, flys : list[pygame.Rect]):
    for fly_rect in flys:
        fly_rect.x += 10

        screen.blit(fly_surf,fly_rect)

def clear_lost_flys():
    global flys
    flys = flys[-100:]

for i in range(250_000):
    spawn_fly((WIDTH,0))

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(pygame.mouse.get_pos()):
                spawn_fly(player_rect.center)

    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    number_of_flys_text_surf = font.render(f"Flys amount: {len(flys)}",True,"black")
    number_of_flys_text_rect = number_of_flys_text_surf.get_rect()
    number_of_flys_text_rect.midtop = (WIDTH/2,20)
    screen.blit(number_of_flys_text_surf,number_of_flys_text_rect)
    
    update_all_flys(screen,flys)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 10
    if keys[pygame.K_s]:
        player_rect.y += 10
    if keys[pygame.K_SPACE]:
        clear_lost_flys()
    
    spawn_fly(player_rect.center)

    screen.blit(player_surf,player_rect)
    
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    