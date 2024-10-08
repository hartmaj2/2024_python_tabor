import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME

# TODO: vytvor si objekt pro defaultni font velikosti 50
font = pygame.font.Font(None,50)

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")

player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,300)

score_text_surf = font.render("Score: 0",True,"Black")
score_text_rect = score_text_surf.get_rect()
score_text_rect.topright = (WIDTH-10,10)

highscore_text_surf = font.render("Highscore: 0",True,"black")
highscore_text_rect = highscore_text_surf.get_rect()
highscore_text_rect.topleft = (10,10)

fly_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Fly/Fly1.png")

# TODO: Napiseme si funkce pro nacteni highscore a zapsani highscore do souboru
# Funkce pojmenujeme treba nacti_highscore() a uloz_highscore()

def update_score_text(score):
    global score_text_surf, score_text_rect
    score_text_surf = font.render("Score: " + str(score),True,"Black")  
    score_text_rect = score_text_surf.get_rect()
    score_text_rect.topright = (WIDTH-10,10)
    

def update_highscore_text(highscore):
    global highscore_text_surf, highscore_text_rect
    highscore_text_surf = font.render("Highscore: " + str(highscore),True,"black")
    highscore_text_rect = highscore_text_surf.get_rect()
    highscore_text_rect.topleft = (10,10)
    

# TODO: Uloz do promenne vysledek z funkce nacti_highscore()
# vyzkousej, ze kdyz do souboru napises nejake skore, tak se opravdu nacte 
score = 0
highscore = 0

# TODO: Zatim v souboru prepis highscore na 0
# Naprogramuj kod tak, aby kdyz score je vetsi nez highscore, tak do highscore budeme psat hodnotu aktualniho score
# Vyzkousej, ze se ti meni opravdu i highscore


flys : list[pygame.Rect] = [] 
fly_speed = 10

def spawn_fly(position):
    fly_rect = fly_surf.get_rect()
    fly_rect.center = position
    flys.append(fly_rect)

def draw_everything():
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))
    screen.blit(score_text_surf,score_text_rect)
    screen.blit(highscore_text_surf,highscore_text_rect)
    for fly_rect in flys:
        screen.blit(fly_surf,fly_rect)
    screen.blit(player_surf,player_rect)

def update_flys():
    global flys, fly_speed
    for fly_rect in flys:
        fly_rect.x += fly_speed
        if fly_rect.left > WIDTH:
            flys.remove(fly_rect)

def react_to_mousedown():
    global player_rect, score
    last_mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(last_mouse_pos):
        spawn_fly(player_rect.center)
        score += 1

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            react_to_mousedown()
    
    update_score_text(score)
    update_highscore_text(highscore)
    update_flys()

    draw_everything()

    pygame.display.flip() 
    clock.tick(60)
    
# BONUS TODO: kresli caru vzdy mezi misi a pozici posledniho kliknuti
# HINT: nejprve zkus kreslit z jednoho rohu k misi ( pygame.mouse.get_pos() )
# HINT: vyrob si promennou na ulozeni posledni pozice kliknuti