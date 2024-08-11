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

def update_fly_text():
    text_surf = font.render(f"Flys amount: {len(flys)}",True,"black")
    text_rect = text_surf.get_rect()
    text_rect.midtop = (WIDTH/2,20)
    return text_surf, text_rect

fly_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Fly/Fly1.png")
fly_surf = pygame.transform.flip(fly_surf,True,False)

flys = []

# TODO: definuj si funkci spawn_fly(pozice), ktera prida mouchu se zadanou pozici do seznamu flys

# TODO: zavolej tu funkci, kdyz se stiskne klavesa space
# HINT: pouzij event s event.type == pygame.KEYDOWN

# TODO: zadefinuj si funkci update_all_flys(seznam), ktera pohne vsemi mouchami
# (!) POZOR: nezapomen mouchy ze seznamu mazat, pokud vyleti z obrazovky (hru to zatim nijak neovlivni, ale je to dobry navyk)

def update_all_flys(screen : pygame.Surface, flys : list[pygame.Rect]):
    ...

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    number_of_flys_text_surf, number_of_flys_text_rect = update_fly_text()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 10
    if keys[pygame.K_s]:
        player_rect.y += 10

    screen.blit(player_surf,player_rect)

    screen.blit(number_of_flys_text_surf,number_of_flys_text_rect)
    
    pygame.display.flip() 
    clock.tick(60)
    