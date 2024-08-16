import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

player_surf = pygame.image.load('david_ultra_hardcore/better_rocket_game.png')
player_surf = pygame.transform.scale_by(player_surf, 0.2)
player_rect = player_surf.get_rect()
player_rect.midbottom = (450,900)
player_speed = 0

asteroid_surf = pygame.image.load('david_ultra_hardcore/asteroid.png')
asteroid_surf = pygame.transform.scale_by(asteroid_surf, 0.4)
asteroid_rect = asteroid_surf.get_rect()
asteroid_rect.scale_by(0.75)
asteroid_rect.topleft = (random.randint(0,600),0)

laser_surf = pygame.image.load('david_ultra_hardcore/plamenomet.png')
laser_surf = pygame.transform.scale_by(laser_surf, 1)
laser_rect = laser_surf.get_rect()

hvezda_surf = pygame.image.load('david_ultra_hardcore/hvezda.png')
hvezda_rect = hvezda_surf.get_rect()
hvezda_rect.midbottom = (random.randint(0,800),0)

konec_hry = False
next_spawn_time = 3000
asteroid_speed = 5
skore = 0

font = pygame.font.Font(None,50)

text_surf = font.render('score: ' + str(skore), True, 'white')
text_rect = text_surf.get_rect()

menu1_surf = font.render('vitej v hardcore asteroidove hre', True, 'white')
menu1_rect = menu1_surf.get_rect()
menu1_rect.center = (450,400)

menu2_surf = font.render('pro pokracovani zmackni mezernik', True, 'white')
menu2_rect = menu2_surf.get_rect()
menu2_rect.center = (450,500)

konec1_surf = font.render('umrel si', True, 'white')
konec1_rect = konec1_surf.get_rect()
konec1_rect.center = (450,300)

konec2_surf = font.render('score: ' + str(skore), True, 'white')
konec2_rect = konec2_surf.get_rect()
konec2_rect.center = (450,400)

enemy_surf = pygame.image.load('david_ultra_hardcore/nepritel.png')
enemy_surf = pygame.transform.scale_by(enemy_surf, 2)
enemy_rect = enemy_surf.get_rect()

shot_surf = pygame.image.load('david_ultra_hardcore/laser.png')
shot_surf = pygame.transform.scale_by(shot_surf,1.5)
shot_rect = shot_surf.get_rect()



asteroid_rects = []

game_state = 'menu'

new_highscore = False

sad_trombone_played = False

highscore_music_played = False

def reset_everything():
    global skore, game_state, new_highscore, konec_hry, asteroid_speed, sad_trombone_played, highscore_music_played
    skore = 0
    game_state = 'menu'
    new_highscore = False
    konec_hry = False
    asteroid_rects.clear()
    asteroid_rect.y = 0
    asteroid_speed = 5
    shot_rect.y = enemy_rect.y + 160
    sad_trombone_played = False
    highscore_music_played = False
    
def spawn_laser():
    rect = laser_surf.get_rect()
    rect.midbottom = player_rect.midtop
    screen.blit(laser_surf, rect) 

def spawn_asteroid():
    global rect
    nahodna_x = random.randint(0,600)
    rect = asteroid_surf.get_rect()
    rect.topleft = (nahodna_x, 0)
    asteroid_rects.append(rect)

def asteroid_fall():
    global asteroid_speed
    if asteroid_rect.y >= 900:
        asteroid_rect.x = random.randint(0,600)
        asteroid_rect.y = 0
        asteroid_speed *= 1.025
    else:
        asteroid_rect.y += int(asteroid_speed)

def hvezda_fall():
    if hvezda_rect.y >= 900:
        hvezda_rect.x = random.randint(0,800)
        hvezda_rect.y = 0    
    else:
        hvezda_rect.y += 10

def hvezda_check_collision():
    global skore 
    if hvezda_rect.colliderect(player_rect):
        hvezda_rect.y = 0
        hvezda_rect.x = random.randint(0,800)
        skore += 1

def asteroid_check_collision():
    global new_highscore
    global highscore
    global konec_hry
    if asteroid_rect.colliderect(player_rect):
        file = open('david_ultra_hardcore/highscore.txt','r')
        highscore = file.readline()
        file.close()
        if skore > int(highscore):
            file = open('david_ultra_hardcore/highscore.txt','w')
            highscore = skore
            file.write(str(highscore))
            file.close()
            new_highscore = True
            konec_hry = True
        else:
            konec_hry = True

def asteroids_check_collisions():
    global new_highscore
    global highscore
    global konec_hry
    for rect in asteroid_rects:
        screen.blit(asteroid_surf, rect)
        rect.y += asteroid_speed

        if rect.colliderect(player_rect):
            file = open('david_ultra_hardcore/highscore.txt','r')
            highscore = file.readline()
            file.close()
            if skore > int(highscore):
                file = open('david_ultra_hardcore/highscore.txt','w')
                highscore = skore
                file.write(str(highscore))
                file.close()
                new_highscore = True
                konec_hry = True
            else:
                konec_hry = True
                               

def check_movement():
    global player_rect
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] == True:
        player_speed = -10
    elif keys[pygame.K_d] == True:
        player_speed = 10
    else:
        player_speed = 0

    player_rect.x += player_speed

    if keys[pygame.K_s]:
        spawn_asteroid()

    if keys[pygame.K_SPACE]:
        spawn_laser()

    if player_rect.x < 0:
        player_rect.x = 900
    
    if player_rect.x >= 850:
        player_rect.x = 0


def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def spawn_timed_asteroids():
        global next_spawn_time
        if pygame.time.get_ticks() > next_spawn_time:
            next_spawn_time = pygame.time.get_ticks() + 3000/(asteroid_speed/5)
            spawn_asteroid()

def vytisknout_skore():
    global text_surf
    text_surf = font.render('score: ' + str(skore), True, 'white')

def vyblit():
    global rect
    screen.fill('black')
    screen.blit(player_surf,player_rect)
    screen.blit(asteroid_surf,asteroid_rect)
    screen.blit(text_surf, text_rect)
    # pygame.draw.rect(screen,'red',asteroid_rect)
    for rect in asteroid_rects:
        screen.blit(asteroid_surf,rect)
        # pygame.draw.rect(screen,'red',rect)
    screen.blit(hvezda_surf, hvezda_rect)            
    screen.blit(enemy_surf,enemy_rect)
    screen.blit(shot_surf,shot_rect)

def nakreslit_vsechno():
    pygame.display.flip() 
    clock.tick(60)

def enemy_behavior():
    global konec_hry
    global new_highscore
    global highscore
    enemy_rect.x = player_rect.x - 95
    if shot_rect.y >= 900:
        shot_rect.x = enemy_rect.x  + 82
        shot_rect.y = enemy_rect.y + 160
    else:
        shot_rect.y += asteroid_speed * 3
    if shot_rect.colliderect(player_rect):
        file = open('david_ultra_hardcore/highscore.txt','r')
        highscore = file.readline()
        file.close()
        if skore > int(highscore):
            file = open('david_ultra_hardcore/highscore.txt','w')
            highscore = skore
            file.write(str(highscore))
            file.close()
            new_highscore = True
            konec_hry = True
        else:
            konec_hry = True

def sad_trombone():
    if sad_trombone_played == False:
        pygame.mixer.music.load('david_ultra_hardcore/sad trombone.mp3')
        pygame.mixer.music.play()
        pygame.event.wait(4000)

def play_music():
    pygame.mixer.music.load('david_ultra_hardcore/asteroidsong.mp3')
    pygame.mixer.music.play(-1)

def highscore_music():
    if highscore_music_played == False:
        pygame.mixer.music.load('david_ultra_hardcore/Celebration Sound Effect.mp3')
        pygame.mixer.music.play()
        pygame.event.wait(6000)

while True:
    if konec_hry == False:
        if game_state == 'running':

            check_events()

            asteroid_fall()

            hvezda_fall()

            hvezda_check_collision()

            asteroid_check_collision()

            asteroids_check_collisions()

            check_movement()

            spawn_timed_asteroids()

            vytisknout_skore()

            enemy_behavior()

            vyblit()

        else:
            check_events()
            screen.fill('black')
            screen.blit(menu1_surf,menu1_rect)
            screen.blit(menu2_surf,menu2_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] == True:
                game_state = 'running'
                play_music()

    else:
        check_events()
        screen.fill('black')
        konec2_surf = font.render('score: ' + str(skore), True, 'white')
        screen.blit(konec1_surf,konec1_rect)
        screen.blit(konec2_surf,konec2_rect)
        konec3_surf = font.render('highscore: ' + str(highscore), True, 'white')
        konec3_rect = konec3_surf.get_rect()
        konec3_rect.center = (450,500)
        screen.blit(konec3_surf,konec3_rect)
        keys = pygame.key.get_pressed()
        konec4_surf = font.render('NOVY HIGHSCORE!', True, 'white')
        konec4_rect = konec4_surf.get_rect()
        konec4_rect.center = (450,600)
        konec5_surf = font.render('restart(r) quit(q)', True, 'white')
        konec5_rect = konec5_surf.get_rect()
        konec5_rect.center = (450,700)
        screen.blit(konec5_surf,konec5_rect)
        if new_highscore == True:
            screen.blit(konec4_surf,konec4_rect)
            highscore_music()
            highscore_music_played = True
        else:
            sad_trombone()
            sad_trombone_played = True
        
        if keys[pygame.K_r] == True:
            reset_everything()

        if keys[pygame.K_q] == True:
            pygame.quit()
            exit()

    nakreslit_vsechno()
