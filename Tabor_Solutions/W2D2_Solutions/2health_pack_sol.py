import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

background = pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png")
ground = pygame.image.load("Tabor_Code/W2D1/graphics/ground.png")


player_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (100,300)


snail_surf = pygame.image.load("Tabor_Code/W2D1/graphics/snail/snail1.png")
snail_rect = snail_surf.get_rect()
snail_rect.bottomright = (300,300)

# Do naseho programu s playerem a snailem pridame padajici health pack

# TODO: Vyrob surface a s nim i jeho rectangle pro health pack a zatim
# ho vytiskni nekam na obrazovku. (obrazek pro health pack je ve slozce W2D2)
health_pack_surf = pygame.image.load("Tabor_Code/W2D2/health_pack.png")
health_pack_rect = health_pack_surf.get_rect()
health_pack_rect.center = (WIDTH/2,HEIGHT/2)


# TODO: Naprogramuj health pack, aby se pri stisknuti klavesy "h" objevil na vrchu obrazovky
# Pokud hrac nedrzi klavesu "h" tak bude pomalu padat (porad stejnou rychlosti)

# TODO: Umozni hraci, aby mohl health pack sebrat
# Kdyz hrac health pack sebere, health pack zmizi a vypise se "Player health increased."
# HINT: detekuj kolizi mezi hracem a health packem 

# TODO: Naprogramuj health pack tak, aby sve padani zastavil na zemi
# HINT: pokud je jeho y souradnice moc velka, tak aby nepada

snail_speed = -1
player_speed = 5
falling_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] == True:
        player_speed = -5
    elif keys[pygame.K_d] == True:
        player_speed = 5
    else:
        player_speed = 0
    
    if keys[pygame.K_w]:
        print("jump")
        if player_rect.bottom >= 300:
            player_rect.y -= 150

    if keys[pygame.K_h]:
        health_pack_rect.midtop = (WIDTH/2,0)
    
    if health_pack_rect.bottom < 300:
        health_pack_rect.y += falling_speed
    
    if player_rect.bottom < 300:
        player_rect.y += falling_speed

    snail_rect.x += snail_speed
    player_rect.x += player_speed

    if snail_rect.colliderect(player_rect) == True:
        snail_surf = pygame.transform.flip(snail_surf,True,False)
        snail_speed = snail_speed * -1

    if health_pack_rect.colliderect(player_rect) == True:
        health_pack_rect.x = -50
        print("Player health increased!")

    screen.blit(background,(0,0))

    screen.blit(ground,(0,300))

    screen.blit(health_pack_surf,health_pack_rect)

    screen.blit(snail_surf,snail_rect)

    screen.blit(player_surf,player_rect)
    
    pygame.display.flip() 
    clock.tick(60)
    
    # BONUS TODO: naprogramuj snaila tak, aby se po doteku hrace otocil a jel zase na 
    # druhou stranu (hezke je i pridat, ze kdyz vyjede z obrazovky na jedne strane, tak se objevi na druhe)