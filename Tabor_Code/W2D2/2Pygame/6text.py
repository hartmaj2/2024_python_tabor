import pygame
import random

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

# TODO: vytvor si objekt pro defaultni font velikosti 50
# HINT: pygame.font.Font(None,velikost)
font = pygame.font.Font(None,50)

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")


player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (400,300)

# TODO: Vyrob novy surface, ktery bude drzet text: "Score: 0"
# Pro ten surface take vyrob rect a umisti ho na hezke misto
# HINT: pouzij funkci render(text,True,barva) na fontu, ktery sis vytvoril/a

# TODO: Vykresli text na obrazovku

# TODO: Vytvor si promennou na pocitani skore (score bude pozdeji pocet kliknuti na hrace)

# TODO: Zvysuj hraci skore vzdy, kdyz klikne mysi na obrazovku
# HINT: nastane event s event.type == pygame.MOUSEBUTTONDOWN

# TODO: Vzdy prepisuj surface se skore na novy pomoci font.render(novy_text,True,barva)
# Ten text bude napr. "Score: 14" pokud ma hrac score 14

# BONUS TODO: Zvysuj skore pouze, pokud kliknes na hracuv rectangle
# HINT: pouzij player_rect.collidepoint()
# HINT: souradnice mysi ziskas pomoci pygame.mouse.get_pos()

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ...

    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    screen.blit(player_surf,player_rect)

    pygame.display.flip() 
    clock.tick(60)

# BONUS TODO: nakresli caru z leveho horniho rohu do praveho dolniho pomoci pygame.draw.neco kde neco si vyhledej v dokumentaci
# dokumentace: https://www.pygame.org/docs/

# BONUS TODO: kresli caru vzdy mezi misi a pozici posledniho kliknuti
# HINT: nejprve zkus kreslit z jednoho rohu k misi ( pygame.mouse.get_pos() )
# HINT: vyrob si promennou na ulozeni posledni pozice kliknuti