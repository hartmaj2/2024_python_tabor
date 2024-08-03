import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

# TODO: vytvor si objekt pro defaultni font velikosti 50
font = pygame.font.Font(None,50)

background = pygame.image.load("W1D5/graphics/Sky.png")
ground = pygame.image.load("W1D5/graphics/ground.png")


class Character:
    def __init__(self,surface : pygame.Surface):
        self.surf = surface
        self.rect = self.surf.get_rect()


player = Character(pygame.image.load("W1D5/graphics/Player/player_stand.png"))
player.rect.midbottom = (100,300)

# TODO: Vyrob novy character objekt, kteremu predas surface vyrobeny pomoci font.render(text,True,barva)
score_text = Character(...)
score_text.rect.midtop = ...

# TODO: Vytvor si promennou na pocitani skore (score bude pocet kliknuti na hrace)
score = 0

flys : list[Character] = [] 

def spawn_fly(position):
    fly = Character(pygame.image.load("W1D5/graphics/Fly/Fly1.png"))
    fly.rect.center = position
    flys.append(fly)


# TODO: Prepis surface promenne score_text pomoci font.render(novy_text,True,barva)

# TODO: nakresli caru z leveho horniho rohu do praveho dolniho pomoci pygame.draw.neco kde neco si vyhledej v dokumentaci

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            last_mouse_pos = pygame.mouse.get_pos()
            if player.rect.collidepoint(last_mouse_pos):
                spawn_fly(player.rect.center)
                
    
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    for fly in flys:
        fly.rect.x += 10
        screen.blit(fly.surf,fly.rect)

    screen.blit(player.surf,player.rect)
    
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    
# BONUS TODO: kresli caru vzdy mezi misi a pozici posledniho kliknuti
# HINT: nejprve zkus kreslit z jednoho rohu k misi ( pygame.mouse.get_pos() )
# HINT: vyrob si promennou na ulozeni posledni pozice kliknuti