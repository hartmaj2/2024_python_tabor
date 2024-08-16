import pygame
import random

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Super hra 100% kvalita")

pygame.mixer.music.load("ami_trex/8bit-music-for-game-68698.mp3")
pygame.mixer.music.play(-1)

width, height = 800, 400
window = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((width,height)) 
clock = pygame.time.Clock()
font = pygame.font.Font("ami_trex/Pixeltype.ttf",50)

# background = pygame.image.load("sky.jpg")
#background = pygame.image.load("b0614a2b-ba3d-4210-ad8e-70fcbccf1728_scaled.jpg")
background = pygame.image.load("ami_trex/asteroidgraphics/stars.png")
ground = pygame.transform.grayscale(pygame.image.load("ami_trex/groooooound.png"))


# dino_image = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png")

#Tabor_Code/W2D1/graphics/Sky.png
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

clock = pygame.time.Clock()
fps = 60


dino_image = pygame.image.load("ami_trex/trexgraphics/trex1.png")
dino_image = pygame.transform.scale(dino_image, (50, 50))



ENEMY_SPEED = 10
JUMP = 12
GRAVITY = 0.5
GROUND_HEIGHT = 300

LEVEL_SCORES = [0,100,200,400,1000,2000,3500]

start_time = 0
score = 0
level = 1

border_offset = 10

button_color = "White"

player_standing_x_pos = 100
player_standing_height = 0

player_standing1 = pygame.image.load("ami_trex/trexgraphics/nightdino1.png")
player_standng2 = pygame.image.load("ami_trex/trexgraphics/nightdino2.png")
player_standing_frames = [player_standing1,player_standng2]
player_ducking1 = pygame.image.load("ami_trex/trexgraphics/nightdino3.png")
#player_ducking1 = pygame.transform.scale_by(player_ducking1,)
player_ducking_frame = [player_ducking1]
player_anim_time = 10

player_surf = pygame.image.load("ami_trex/trexgraphics/nightdino1.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (player_standing_x_pos,GROUND_HEIGHT)
player_y_speed = 0

player_ducking = False
player_player_standing_height = player_rect.height

player_next_anim_time = pygame.time.get_ticks() + player_anim_time
player_current_frame = 0

explosion_image = pygame.image.load("ami_trex/asteroidgraphics/explosion.png")
explosion_image = pygame.transform.scale(explosion_image, (50, 50))

is_exploded = False

def draw_explosion():
    if is_exploded:
        window.blit(explosion_image, (dino_icon_rect.x, dino_icon_rect.y))
    else:
        window.blit(dino_image, (dino_icon_rect.x, dino_icon_rect.y))

flying_image_1 = pygame.image.load("ami_trex/trexgraphics/nightbird.png")
flying_image_2 = pygame.image.load("ami_trex/trexgraphics/nightbird2.png")
# flying_image_1 = pygame.transform.scale_by(flying_image_1, 1.2)
# flying_image_2 = pygame.transform.scale_by(flying_image_2, 1.2)
flying_images = [flying_image_1,flying_image_2]

flying_anim_event = pygame.event.custom_type()
flying_frame_index = 0

pygame.time.set_timer(flying_anim_event,100)
flying_surf = flying_images[flying_frame_index]     


score_text_surf = font.render(f"Score: {score}",None,"White")
score_text_rect = score_text_surf.get_rect()
score_text_rect.topleft = (10,10)

level_text_surf = font.render(f"Level: {level}",None,"White")
level_text_rect = level_text_surf.get_rect()
level_text_rect.topright = (width-10,10)

def get_level():
    # print(LEVEL_SCORES)
    # print(score)
    i = 0
    while i < len(LEVEL_SCORES) and LEVEL_SCORES[i] <= score:
        i += 1
    # print(i)
    return i

dino_image = pygame.image.load("ami_trex/trexgraphics/nightdino1.png")
dino_icon_surf = pygame.transform.scale_by(dino_image,2.5)
dino_icon_rect = dino_icon_surf.get_rect()
dino_icon_rect.center = (width/5,height/2)

dino_icon2_surf = pygame.transform.scale_by(dino_image,2.5)
dino_icon2_surf = pygame.transform.flip(dino_icon2_surf,True,False)
dino_icon2_rect = dino_icon2_surf.get_rect()
dino_icon2_rect.center = (width*4/5,height/2)

quit_game_button_surf = font.render("Quit",True,"Red")
quit_game_button_rect = quit_game_button_surf.get_rect()
quit_game_button_rect.midtop = (width/2,height/2+border_offset+10)

start_game_button_surf = font.render("Play",True,"Black")
start_game_button_rect = start_game_button_surf.get_rect()
start_game_button_rect.midbottom = (width/2,height/2-border_offset-10)  

intro_text_surf = font.render("T-Rex game",True,"White")
intro_text_rect = intro_text_surf.get_rect()
intro_text_rect.midtop = (width/2,40)

intro_score_surf = font.render(" ",True,"White")
intro_score_rect = intro_score_surf.get_rect()
intro_score_rect.midtop = (width/2,40)




cactus_image = pygame.image.load("ami_trex/trexgraphics/gray.png")
#cactus_image = pygame.transform.scale_by(cactus_image,0.)

spawn_event = pygame.event.custom_type()

level_base_speed = [9,10,12,14,18]
level_spawn_delay = [1500,1400,1300,1200,1200]
spawn_diff_ratio = 1/3

last_level = level
pygame.time.set_timer(spawn_event,level_spawn_delay[level-1])
    

cactus_rectangles : list[pygame.rect.Rect] = [] 
flying_rectangles : list[pygame.rect.Rect] = []
def draw():
    screen.blit(background,(0,0))
    screen.blit(ground,(0,GROUND_HEIGHT))

highscore = 0 

def load_highscore():
    global highscore
    file = open("ami_trex/asteroidgraphics/highscore.txt","r")
    read = file.readline()
    highscore = int(read)
    file.close()


def write_highscore():
    file = open("ami_trex/asteroidgraphics/highscore.txt", "w")
    file.write(str(highscore))
    file.close()

load_highscore()

def update():
    global score_text_surf, score_text_rect,level_text_rect,level_text_surf,score
    score = (pygame.time.get_ticks() - start_time) // 100
    score_text_surf = font.render(f"Score: {score}",None,"White")
    score_text_rect = score_text_surf.get_rect()
    score_text_rect.topleft = (10,10)

    level = get_level()
    # print(level)
    level_text_surf = font.render(f"Level: {level}",None,"White")
    level_text_rect = level_text_surf.get_rect()
    level_text_rect.topright = (width-10,10)

def spawner_update():
    global last_level,level,spawn_event,level_spawn_delay
    if level > last_level:
        last_level = level
        pygame.time.set_timer(spawn_event,level_spawn_delay[level-1])

def player_update():
    global player_rect, player_y_speed,player_standing_x_pos
    global player_surf
    global player_ducking,player_current_frame
    player_rect.y += player_y_speed
    player_y_speed += GRAVITY
    #print(player_current_frame)
    if player_rect.bottom > GROUND_HEIGHT:
        player_rect.bottom = GROUND_HEIGHT
        player_y_speed = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        if player_rect.bottom >= GROUND_HEIGHT and not player_ducking:
            player_ducking = True
            player_surf = player_ducking_frame[0]
            player_rect = player_surf.get_rect()
            player_rect.midbottom = (player_standing_x_pos+20,GROUND_HEIGHT)
    else:
        if player_rect.bottom >= GROUND_HEIGHT and player_ducking:
            player_ducking = False
            player_surf = player_standing_frames[player_current_frame]
            player_rect = player_surf.get_rect()
            player_rect.midbottom = (player_standing_x_pos,GROUND_HEIGHT) 



game_state = "MENU"

while True:
    for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                write_highscore()
                pygame.quit()
                exit()
            if game_state == "MENU":

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_game_button_rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = "RUNNING"
                        level = 1
                        score = 0
                        cactus_rectangles.clear()
                        flying_rectangles.clear()
                        start_time = pygame.time.get_ticks()
                    if quit_game_button_rect.collidepoint(pygame.mouse.get_pos()):
                        
                        write_highscore()
                        pygame.quit()
                        exit()

            
            elif game_state == "RUNNING":

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        if player_rect.bottom >= GROUND_HEIGHT and not player_ducking:
                            player_y_speed = -JUMP

                elif event.type == spawn_event:
                    percentage = random.randint(0,100)
                    if percentage < 30:
                        rect = flying_surf.get_rect()
                        rect.bottomleft = (width, GROUND_HEIGHT-player_player_standing_height+20)
                        flying_rectangles.append(rect)
                    else:
                        rect = cactus_image.get_rect()
                        rect.bottomleft = (width, GROUND_HEIGHT+10)
                        cactus_rectangles.append(rect)

                elif event.type == flying_anim_event:
                        flying_frame_index = (flying_frame_index + 1) % len(flying_images)
                        flying_surf = flying_images[flying_frame_index]

    if game_state == "MENU":
        
        draw()
        
        background_rect = pygame.Rect(start_game_button_rect.left-border_offset,start_game_button_rect.top-border_offset,start_game_button_rect.width+border_offset*2,start_game_button_rect.height+border_offset*1.2)
        pygame.draw.rect(screen,button_color,background_rect)
        pygame.draw.rect(screen,"Black",background_rect,2)
        screen.blit(start_game_button_surf,start_game_button_rect)

        background_rect = pygame.Rect(quit_game_button_rect.left-border_offset,quit_game_button_rect.top-border_offset,quit_game_button_rect.width+border_offset*2,quit_game_button_rect.height+border_offset*1.2)
        pygame.draw.rect(screen,button_color,background_rect)
        pygame.draw.rect(screen,"Black",background_rect,2)
        screen.blit(quit_game_button_surf,quit_game_button_rect)

        screen.blit(dino_icon_surf,dino_icon_rect)
        screen.blit(dino_icon2_surf,dino_icon2_rect)

        screen.blit(intro_text_surf,intro_text_rect)
        screen.blit(intro_score_surf, intro_score_rect)

        pygame.display.flip() 

    elif game_state == "RUNNING":

        print(highscore)
        if score > highscore:
            highscore = score

            

     
        update()
        spawner_update()
        player_update()

                
        for enemy_rect in cactus_rectangles + flying_rectangles:
            if enemy_rect.colliderect(player_rect):
                game_state = "MENU"
                start_game_button_surf = font.render("Restart",True,"Black")
                start_game_button_rect = start_game_button_surf.get_rect()
                start_game_button_rect.midbottom = (width/2,height/2-border_offset-10)
                intro_text_surf = font.render(f"You died with {score} points.",True,"White")
                intro_text_rect = intro_text_surf.get_rect()
                intro_text_rect.midtop = (width/2,40)
                                
                intro_score_surf = font.render(f"Highscore: {highscore}",True,"White")
                intro_score_rect = intro_score_surf.get_rect()
                intro_score_rect.midtop = (width/2,80)
                
        
        for cactus_rect in cactus_rectangles:
            cactus_rect.x -= level_base_speed[level-1]
            if cactus_rect.right < 0:
                cactus_rectangles.remove(cactus_rect)

       
        for flying_rect in flying_rectangles:
            flying_rect.x -= level_base_speed[level-1]
            if flying_rect.right < 0:
                flying_rectangles.remove(flying_rect)
        
        
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_HEIGHT))

        
        for cactus_rect in cactus_rectangles:
            screen.blit(cactus_image,cactus_rect)

        
        for flying_rect in flying_rectangles:
            screen.blit(flying_surf,flying_rect)

        
        if pygame.time.get_ticks() > player_next_anim_time:
            player_current_frame = (player_current_frame + 1) % len(player_standing_frames)
            player_next_anim_time = pygame.time.get_ticks() + 100
            if not player_ducking:
                player_surf = player_standing_frames[player_current_frame]
            else:
                player_surf = player_ducking_frame[0]
        screen.blit(player_surf,player_rect)

        screen.blit(score_text_surf,score_text_rect)
        screen.blit(level_text_surf,level_text_rect)
        pygame.display.flip() 

        

    # if not is_exploded and dino_icon_rect.x + dino_width > obstacle_x and dino_x < obstacle_x + obstacle_width:
    #     if dino_y + dino_height > obstacle_y:
    #         is_exploded = True
    #         explosion_time = pygame.time.get_ticks()
    clock.tick(60)

