import pygame
import random

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() 
font = pygame.font.Font("Tabor_Code/W2D1/font/Pixeltype.ttf",50)

background = pygame.transform.grayscale(pygame.image.load("Tabor_Code/W2D1/graphics/Sky.png"))
ground = pygame.transform.grayscale(pygame.image.load("Tabor_Code/W2D1/graphics/ground.png"))

ENEMY_BASE_SPEED = 10
JUMP_POWER = 12
GRAVITY = 0.5
GROUND_HEIGHT = 300

LEVEL_SCORES = [0,50,100,200,400]

start_time = 0
score = 0
level = 1



border_offset = 10

button_color = "Grey"


# player 
player_standing_x_pos = 100
player_standing_height = 0

player_standing_frame_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex3.png")
player_standing_frame_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex4.png")
player_standing_frames = [player_standing_frame_1,player_standing_frame_2]
player_ducking_frame_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex_duck1.png")
player_ducking_frame_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex_duck2.png")
player_ducking_frames = [player_ducking_frame_1,player_ducking_frame_2]
player_anim_time = 100

player_surf = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png")
player_rect = player_surf.get_rect()
player_rect.midbottom = (player_standing_x_pos,GROUND_HEIGHT)
player_y_speed = 0

player_ducking = False
player_player_standing_height = player_rect.height


player_next_anim_time = pygame.time.get_ticks()  + player_anim_time
player_current_frame = 0

# flying enemy
flying_image_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/flying1.png")
flying_image_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/flying2.png")
flying_images = [flying_image_1,flying_image_2]

flying_anim_event = pygame.event.custom_type()
flying_frame_index = 0

pygame.time.set_timer(flying_anim_event,100)
flying_surf = flying_images[flying_frame_index]     
    

score_text_surf = font.render(f"Score: {score}",None,"Black")
score_text_rect = score_text_surf.get_rect()
score_text_rect.topleft = (10,10)

level_text_surf = font.render(f"Level: {level}",None,"Black")
level_text_rect = level_text_surf.get_rect()
level_text_rect.topright = (WIDTH-10,10)
        

dino_image = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png")
dino_icon_surf = pygame.transform.scale_by(dino_image,1.5)
dino_icon_rect = dino_icon_surf.get_rect()
dino_icon_rect.center = (WIDTH/5,HEIGHT/2)

dino_icon2_surf = pygame.transform.scale_by(dino_image,1.5)
dino_icon2_surf = pygame.transform.flip(dino_icon2_surf,True,False)
dino_icon2_rect = dino_icon2_surf.get_rect()
dino_icon2_rect.center = (WIDTH*4/5,HEIGHT/2)

quit_game_button_surf = font.render("Quit",True,"Black")
quit_game_button_rect = quit_game_button_surf.get_rect()
quit_game_button_rect.midtop = (WIDTH/2,HEIGHT/2+border_offset+10)


start_game_button_surf = font.render("Start Game",True,"Black")
start_game_button_rect = start_game_button_surf.get_rect()
start_game_button_rect.midbottom = (WIDTH/2,HEIGHT/2-border_offset-10)  

intro_text_surf = font.render("Retro-Rex",True,"Black")
intro_text_rect = intro_text_surf.get_rect()
intro_text_rect.midtop = (WIDTH/2,40)

 
cactus_image = pygame.image.load("Tabor_Code/W2D1/trexgraphics/cactus1.png")

spawn_event = pygame.event.custom_type()

level_base_speed = [9,10,12,14,18]
level_spawn_delay = [1500,1400,1300,1200,1200]
spawn_diff_ratio = 1/3

last_level = level
pygame.time.set_timer(spawn_event,level_spawn_delay[level-1])
    

cactus_rectangles : list[pygame.rect.Rect] = [] 
flying_rectangles : list[pygame.rect.Rect] = []

game_state = "MENU"


def get_level():
    i = 0
    while i < len(LEVEL_SCORES) and LEVEL_SCORES[i] <= score:
        i += 1
    return i

while True:

    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
            
            if event.type == pygame.QUIT: 
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
                        pygame.quit()
                        exit()


            elif game_state == "RUNNING":

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        if player_rect.bottom >= GROUND_HEIGHT and not player_ducking:
                            player_y_speed = -JUMP_POWER

                elif event.type == spawn_event:
                    percentage = random.randint(0,100)
                    if percentage < 30:
                        rect = flying_surf.get_rect()
                        rect.bottomleft = (WIDTH, GROUND_HEIGHT-player_player_standing_height+10)
                        flying_rectangles.append(rect)
                    else:
                        rect = cactus_image.get_rect()
                        rect.bottomleft = (WIDTH, GROUND_HEIGHT+10)
                        cactus_rectangles.append(rect)

                elif event.type == flying_anim_event:
                        flying_frame_index = (flying_frame_index + 1) % len(flying_images)
                        flying_surf = flying_images[flying_frame_index]

    if game_state == "MENU":
        
        # draw
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_HEIGHT))

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

        pygame.display.flip() 

    elif game_state == "RUNNING":

        ### UPDATE
        score = (pygame.time.get_ticks() - start_time) // 100
        score_text_surf = font.render(f"Score: {score}",None,"Black")
        score_text_rect = score_text_surf.get_rect()
        score_text_rect.topleft = (10,10)
        
        level = get_level()
        level_text_surf = font.render(f"Level: {level}",None,"Black")
        level_text_rect = level_text_surf.get_rect()
        level_text_rect.topright = (WIDTH-10,10)

        # spawner update
        if level > last_level:
            last_level = level
            pygame.time.set_timer(spawn_event,level_spawn_delay[level-1])
        
        # player update
        player_rect.y += player_y_speed
        player_y_speed += GRAVITY
        
        if player_rect.bottom > GROUND_HEIGHT:
            player_rect.bottom = GROUND_HEIGHT
            player_y_speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            if player_rect.bottom >= GROUND_HEIGHT and not player_ducking:
                player_ducking = True
                player_surf = player_ducking_frames[player_current_frame]
                player_rect = player_surf.get_rect()
                player_rect.midbottom = (player_standing_x_pos+20,GROUND_HEIGHT)
        else:
            if player_rect.bottom >= GROUND_HEIGHT and player_ducking:
                player_ducking = False
                player_surf = player_standing_frames[player_current_frame]
                player_rect = player_surf.get_rect()
                player_rect.midbottom = (player_standing_x_pos,GROUND_HEIGHT)  

        # all enemies update
        for enemy_rect in cactus_rectangles + flying_rectangles:
            if enemy_rect.colliderect(player_rect):
                game_state = "MENU"
                start_game_button_surf = font.render("Restart",True,"Black")
                start_game_button_rect = start_game_button_surf.get_rect()
                start_game_button_rect.midbottom = (WIDTH/2,HEIGHT/2-border_offset-10)
                intro_text_surf = font.render(f"You died with {score} points.",True,"Black")
                intro_text_rect = intro_text_surf.get_rect()
                intro_text_rect.midtop = (WIDTH/2,40)

        # cactus update
        for cactus_rect in cactus_rectangles:
            cactus_rect.x -= level_base_speed[level-1]
            if cactus_rect.right < 0:
                cactus_rectangles.remove(cactus_rect)

        # flying update
        for flying_rect in flying_rectangles:
            flying_rect.x -= level_base_speed[level-1]
            if flying_rect.right < 0:
                flying_rectangles.remove(flying_rect)
        
        # DRAW
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_HEIGHT))

        # draw cactuses
        for cactus_rect in cactus_rectangles:
            screen.blit(cactus_image,cactus_rect)

        # draw flying
        for flying_rect in flying_rectangles:
            screen.blit(flying_surf,flying_rect)

        # player draw
        if pygame.time.get_ticks() > player_next_anim_time:
            player_current_frame = (player_current_frame + 1) % len(player_standing_frames)
            player_next_anim_time = pygame.time.get_ticks() + player_anim_time
            if not player_ducking:
                player_surf = player_standing_frames[player_current_frame]
            else:
                player_surf = player_ducking_frames[player_current_frame]
        screen.blit(player_surf,player_rect)

        screen.blit(score_text_surf,score_text_rect)
        screen.blit(level_text_surf,level_text_rect)
        pygame.display.flip() 
    
    clock.tick(60)
    