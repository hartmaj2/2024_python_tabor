import pygame
import random
pygame.init()
WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()

muj_font=pygame.font.Font("vasek_asteroids/Pixeltype.ttf",50)

text_surf=muj_font.render("level 1:",True,"white")
text_rect=text_surf.get_rect()
text_rect.topleft=(0,0)
asteroid_speed=6
next_shot_time=0
next_spawn_time=500
spiderman_speed = 13
pavucina_speed=10
enemy_spawn_time=0
level=1
high_score = 0
score = 0
kill_sound=pygame.mixer.Sound("vasek_asteroids/roblox.mp3")
kill_sound.set_volume(1.0)
game_sound=pygame.mixer.Sound("vasek_asteroids/drama.wav")
game_sound.set_volume(1.0)

shot_sound=pygame.mixer.Sound("vasek_asteroids/shot.wav")
enemy_speed=3
enemy_shot_speed=2
enemy_shot_surf=pygame.image.load("vasek_asteroids/strela enemy.png")
enemy_shot_surf=pygame.transform.scale_by(enemy_shot_surf,0.1)
enemy_shot_rect=enemy_shot_surf.get_rect()
enemy_surf=pygame.image.load("vasek_asteroids/enemy.png")
enemy_surf=pygame.transform.scale_by(enemy_surf,0.2)
high_score_surf=muj_font.render("High score:",True,"white")
high_score_rect=high_score_surf.get_rect()
stars_surf = pygame.image.load("vasek_asteroids/stars.png")
stars_surf=pygame.transform.scale_by(stars_surf,6.0)
pavucina_surf = pygame.image.load("vasek_asteroids/pavucina.png")
spiderman_surf = pygame.image.load("vasek_asteroids/spider cat.png")
spiderman_surf=pygame.transform.scale_by(spiderman_surf,0.8)
asteroid_surf = pygame.image.load("vasek_asteroids/asteroid.png")
asteroid_surf=pygame.transform.scale_by(asteroid_surf,0.1)
pavucina_surf=pygame.transform.scale_by(pavucina_surf,0.1)
spiderman_rect = spiderman_surf.get_rect()
spiderman_rect.midbottom = (100,900)
asteroid_rects:list[pygame.Rect]=[]
pavucina_rects:list[pygame.Rect]=[]
enemy_shots:list[pygame.Rect]=[]

enemy_rects:list[pygame.Rect]=[]
enemy_shot_times=[]

def update_enemies():
     for i in range(len(enemy_rects)):
        enemy_rects[i].x += enemy_speed
        if enemy_rects[i].x >= WIDTH:
            enemy_rects[i].x = 20
        if pygame.time.get_ticks() > enemy_shot_times[i]:
            rect = enemy_shot_surf.get_rect()
            rect.center = enemy_rects[i].center
            enemy_shots.append(rect)
            enemy_shot_times[i] = pygame.time.get_ticks() + random.randint(1000,3000)


def load_highscore():
    global high_score
    file=open("vasek_asteroids/highscore.txt","r")
    high_score=int(file.readline())
    file.close()
def write_highscore():
    file=open("vasek_asteroids/highscore.txt","w")
    file.write(str(high_score))
    file.close()
def check_highscore():
    global score,high_score
    if score>high_score:
        high_score=score
     
def update_score():    
    global score,score_rect,score_surf,high_score_surf,high_score_rect
    score=int (pygame.time.get_ticks()/1000)
      

    score_surf=muj_font.render("skore:"+str( int(score) ),True,"white")
    score_rect=score_surf.get_rect()
    score_rect.topright=(600,0)
    score=int (pygame.time.get_ticks()/1000)
       

    high_score_surf=muj_font.render("H igh score:"+str( int(high_score) ),True,"white")
    high_score_rect=high_score_surf.get_rect()
    high_score_rect.topright=(600,50)
def levely():
    global score,asteroid_speed,text_surf,text_rect,level,enemy_shot_speed,asteroid_speed,prodleva
    if score>0 and score<11:
        level=1 
        text_surf=muj_font.render("level 1:",True,"white")
        text_rect=text_surf.get_rect()
        text_rect.topleft=(0,0)

    if score>10 and score<26:
        level=2
        text_surf=muj_font.render("level 2:",True,"white")
        text_rect=text_surf.get_rect()
        text_rect.topleft=(0,0)
        asteroid_speed=10
        enemy_shot_speed=10
        prodleva=random.randint(5000,10000)
    if score>25 and score< 40:      
        text_surf=muj_font.render("level 3:",True,"white")
        text_rect=text_surf.get_rect()
        text_rect.topleft=(0,0)
        asteroid_speed=12
        enemy_shot_speed=10
        
        prodleva=random.randint(4000,6000)
    if score>40 and score< 51:      
        text_surf=muj_font.render("level 4:",True,"white")
        text_rect=text_surf.get_rect()
        text_rect.topleft=(0,0)
        asteroid_speed=17
        enemy_shot_speed=12
        prodleva=random.randint(2000,4000)
    if score>50 and score< 60:      
        text_surf=muj_font.render("level 4:",True,"white")
        text_rect=text_surf.get_rect()
        text_rect.topleft=(0,0)
        asteroid_speed=25
        enemy_shot_speed=15
        prodleva=random.randint(2000,4000)
        if score>60 and score< 100:      
            text_surf=muj_font.render("level 5:",True,"white")
            text_rect=text_surf.get_rect()
            text_rect.topleft=(0,0)
            asteroid_speed=27
            enemy_shot_speed=17
            prodleva=random.randint(1000,3000)
            

def spawn_enemy():
    
    enemy_rect=enemy_surf.get_rect()
    enemy_rect.midtop=(random.randint(0,900),0)
    enemy_rects.append(enemy_rect)
    enemy_shot_times.append(0)
   
    
def vyhral_jsi():     
    if score == 100:
        pygame.quit()
        exit()
        

def blitovani():
    
    screen.blit(stars_surf,(0,0))
    screen.blit(spiderman_surf,spiderman_rect)
    screen.blit(text_surf,text_rect)
    screen.blit(score_surf,score_rect)
    screen.blit(high_score_surf,high_score_rect)

    for kebab in asteroid_rects:
          screen.blit(asteroid_surf,kebab)
    for shoot in pavucina_rects:
          screen.blit(pavucina_surf,shoot)
    for kebab in enemy_rects:
         screen.blit(enemy_surf,kebab)
    for kebab in enemy_shots:
        screen.blit(enemy_shot_surf,kebab)



def spawn_enemy_if_time():
    global enemy_spawn_time
    if pygame.time.get_ticks()> enemy_spawn_time:
            prodleva=random.randint(5000,10000)
            enemy_spawn_time=pygame.time.get_ticks()+prodleva
            spawn_enemy()      



def spawn_if_time():
    global spiderman_rect
    global spiderman_speed
    global next_spawn_time
    
    if pygame.time.get_ticks()> next_spawn_time:
            prodleva=random.randint(500,1500)
            next_spawn_time=pygame.time.get_ticks()+prodleva
            spawn_asteroids()


def spawn_asteroids():
    global asteroid_surf,WIDTH
    nahodna_x=random.randint(0,WIDTH)
    rect=asteroid_surf.get_rect()
    rect.midtop=(nahodna_x,0)  
    asteroid_rects.append(rect)


def remove_out_asteroids():
      global spiderman_rect,asteroid_speed


def update_asteroids():
   global asteroid_speed
   for kebab in asteroid_rects:
        kebab.y += asteroid_speed 

def update_enemy_shots():
    for enemy_shot_rect in enemy_shots:
        enemy_shot_rect.y += enemy_shot_speed

def spawn_pavucin():
    global pavucina_surf,spiderman_rect,pavucina_rects   
    rect=pavucina_surf.get_rect()
    rect.center= spiderman_rect.center
    pavucina_rects.append(rect)


def update_pavucin():
      for kebab in pavucina_rects:
        kebab.y-=pavucina_speed
        if kebab.bottom< 0:
              pavucina_rects.remove(kebab )
        for asteroid_rect in asteroid_rects:
              if kebab.colliderect(asteroid_rect):
                    print ("znic asteroid")
                    asteroid_rects.remove(asteroid_rect)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_highscore() 
            pygame.quit()
            exit()


def kolize():
    global spiderman_surf,enemy_rect,pavucina_surf
    for rect in asteroid_rects:
        if rect.colliderect(spiderman_rect):
           write_highscore()
           kill_sound.play()
           pygame.time.delay(500) 
           kill_sound.play()
           pygame.time.delay(500) 
           kill_sound.play()
           pygame.time.delay(2000) 
           print ("zemrel jsi")
           exit()
    for rect in enemy_shots:
        if  rect.colliderect(spiderman_rect):
            write_highscore()
            kill_sound.play()
            pygame.time.delay(500) 
            kill_sound.play()
            pygame.time.delay(500) 
            kill_sound.play()
            
            pygame.time.delay(2000)  
            print ("zemrel jsi")
            exit()
    for kebab in pavucina_rects:
        for enemy_rect in enemy_rects:
            if kebab.colliderect(enemy_rect):
                print ("znicil jsi enemy")
                enemy_rects.remove(enemy_rect)


def mackani_klaves():
    global spiderman_speed
    
    pygame.key.get_pressed()
    
    if keys[pygame.K_a] == True:
        spiderman_speed= - 5
    elif keys[pygame.K_d] == True:
        spiderman_speed = 5
    else:
        spiderman_speed = 0
    spiderman_rect.x += spiderman_speed
    if spiderman_rect.right < 0:
        spiderman_rect.left = WIDTH
    if spiderman_rect.left > WIDTH:
        spiderman_rect.right = 0

load_highscore()
game_sound.play(loops=-1) 
while True:
    
    print("highscore:",high_score)
    print("score:",score)
    check_events()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and pygame.time.get_ticks() > next_shot_time:
        shot_sound.play()
        next_shot_time = pygame.time.get_ticks()+2000
        spawn_pavucin()
    # if keys[pygame.K_s] == True:
    #      spawn_enemy()
    # print (next_shot_time)
    #print(pygame.time.get_ticks())
    #print (len (asteroid_rects))
    keys = pygame.key.get_pressed()
    
    update_score()
    levely()
    
   
    check_highscore()
    mackani_klaves()
    update_enemy_shots()
    update_pavucin() 
        #remove_out_asteroids()
    spawn_if_time()


    if level==2: 
        spawn_enemy_if_time()
    update_enemies()
    update_asteroids()

    kolize()


    blitovani()
    vyhral_jsi()

    pygame.display.flip() 
    clock.tick(60)
    


