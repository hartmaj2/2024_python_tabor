import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

background = pygame.image.load("W1D5/graphics/Sky.png")
ground = pygame.image.load("W1D5/graphics/ground.png")

# TODO: vyrobit tridu, ktera zakomponuje surface a rect do jednoho objektu
class Character:
    def __init__(self,surface : pygame.Surface):
        self.surf = surface
        self.rect = self.surf.get_rect()

player = Character(pygame.image.load("W1D5/graphics/Player/player_stand.png"))
player.rect.midbottom = (100,300)

# TODO: Vyrob pole, do ktereho pak budes ukladat mouchy
flys : list[Character] = [] # type hint pro VSCode
# flys = []

# TODO: Vytiskni vzkaz, pokud je stisknuta mys (pygame.MOUSEBUTTONDOWN)
# HINT: zkontroluj event.type

# TODO: definuj si funkci spawn_fly(pozice), ktera prida mouchu s nastavenou pozici do seznamu flys
def spawn_fly(position):
    fly = Character(pygame.image.load("W1D5/graphics/Fly/Fly1.png"))
    fly.rect.center = position
    flys.append(fly)

# TODO: zavolej tu funkci, kdyz se stiskne mys

# TODO: projed pres seznam a vsechny charaktery v nem vytiskni a pohni s nimi

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                spawn_fly(player.rect.center)
    
    
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))
    
    for fly in flys:
        fly.rect.x += 10
        screen.blit(fly.surf,fly.rect)

    screen.blit(player.surf,player.rect)
    
    pygame.display.flip() 
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    