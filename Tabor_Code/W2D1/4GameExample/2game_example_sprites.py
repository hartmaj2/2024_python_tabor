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
dino_image = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png")

ENEMY_BASE_SPEED = 10
JUMP_POWER = 12
GRAVITY = 0.5
GROUND_HEIGHT = 300

LEVEL_SCORES = [0,50,100,200,400]

start_time = 0
score = 0
level = 1

class Speed:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Text():
    def __init__(self,text):
        super().__init__()
        self.image = font.render(text,True,"Black")
        self.rect = self.image.get_rect()
    
    def update_text(self,new_text):
        self.image = font.render(new_text,True,"Black")
    
    def draw(self):
        screen.blit(self.image,self.rect)

class Button():
    border_offset = 10

    def __init__(self,text,color):
        self.color = color
        super().__init__()
        self.image = font.render(text,True,"Black")
        self.rect = self.image.get_rect()

    def draw(self):
        background_rect = pygame.Rect(self.rect.left-Button.border_offset,self.rect.top-Button.border_offset,self.rect.width+Button.border_offset*2,self.rect.height+Button.border_offset*1.2)
        pygame.draw.rect(screen,self.color,background_rect)
        pygame.draw.rect(screen,"Black",background_rect,2)
        screen.blit(self.image,self.rect)

    def mouse_over(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

class MovingCharacter(pygame.sprite.Sprite):
    def __init__(self,surface : pygame.Surface, speed : list[int,int] ):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.speed = Speed(speed[0],speed[1])
    
    def update(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
        if self.rect.right < 0:
            self.kill()
    
class Player(MovingCharacter):

    standing_x_pos = 100
    player_standing_height = 0

    standing_frame_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex3.png")
    standing_frame_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex4.png")
    standing_frames = [standing_frame_1,standing_frame_2]

    ducking_frame_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex_duck1.png")
    ducking_frame_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex_duck2.png")
    ducking_frames = [ducking_frame_1,ducking_frame_2]

    anim_interval = 100

    def __init__(self, surface : pygame.Surface, speed : list[int,int]):
        super().__init__(surface,speed)
        self.ducking = False
        Player.player_standing_height = self.rect.height
        self.next_anim_time = pygame.time.get_ticks()  + Player.anim_interval
        self.current_frame = 0
        self.rect.midbottom = (Player.standing_x_pos,GROUND_HEIGHT)

    def animate(self):
        if pygame.time.get_ticks() > self.next_anim_time:
            self.current_frame = (self.current_frame + 1) % len(Player.standing_frames)
            self.next_anim_time = pygame.time.get_ticks() + Player.anim_interval
            if not self.ducking:
                self.image = Player.standing_frames[self.current_frame]
            else:
                self.image = Player.ducking_frames[self.current_frame]
        

    def update_movement(self):
        self.speed.y += GRAVITY
        super().update()
        if self.rect.bottom > GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.speed.y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.try_duck()
        else:
            self.try_set_standing()
        if keys[pygame.K_w]:
            self.try_jump()

    def update(self):
        self.update_movement()
        self.animate()
    
    def set_ducking(self):
        self.ducking = True
        self.image = Player.ducking_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (Player.standing_x_pos+20,GROUND_HEIGHT)

    def set_standing(self):
        self.ducking = False
        self.image = Player.standing_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (Player.standing_x_pos,GROUND_HEIGHT)       

    def try_set_standing(self):
        if self.rect.bottom >= GROUND_HEIGHT and self.ducking:
            self.set_standing()
            
    def try_jump(self):
        if self.rect.bottom >= GROUND_HEIGHT and not self.ducking:
            self.speed.y = -JUMP_POWER
    
    def try_duck(self):
        if self.rect.bottom >= GROUND_HEIGHT and not self.ducking:
            self.set_ducking()

class Enemy(MovingCharacter):

    def __init__(self,surface:pygame.Surface,speed :list[int,int]):
        super().__init__(surface,speed)
    
    def update(self):
        global game_state
        super().update()
        if pygame.sprite.collide_rect(self,player_group.sprite):
            game_state = StateMenu("Restart",f"You died with {score} points.")

class FlyingEnemy(Enemy):

    image_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/flying1.png")
    image_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/flying2.png")
    images = [image_1,image_2]

    anim_interval = 100

    flying_anim_event = pygame.event.custom_type()

    def __init__(self, surface : pygame.Surface, speed : list[int,int]):
        super().__init__(surface,speed)
        self.next_anim = pygame.time.get_ticks() + FlyingEnemy.anim_interval
        self.frame_index = 0
    
    def animate(self):
        if pygame.time.get_ticks() > self.next_anim:
            self.frame_index = (self.frame_index + 1) % len(FlyingEnemy.images)
            self.image = FlyingEnemy.images[self.frame_index]
            self.next_anim = pygame.time.get_ticks() + FlyingEnemy.anim_interval

    def update(self):
        super().update()
        self.animate()
        
class StateRunning:

    score_text = Text(f"Score: {score}")
    score_text.rect.topleft = (10,10)

    level_text = Text(f"Level: {level}")
    level_text.rect.topright = (WIDTH-10,10)

    def update(self):
        global game_state, score, level
        score = (pygame.time.get_ticks() - start_time) // 100
        StateRunning.score_text.update_text("Score: " + str(score))
        level = get_level()
        StateRunning.level_text.update_text("Level: " + str(level))
        spawner.update()
        player_group.update()
        flying_group.update()
        cactus_group.update()  

    def draw(self):
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_HEIGHT))
        player_group.draw(screen)
        flying_group.draw(screen)
        cactus_group.draw(screen)
        StateRunning.score_text.draw()
        StateRunning.level_text.draw()
        pygame.display.flip() 
    
    def check_events(self):
        for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                elif event.type == EventEnemySpawner.spawn_event:
                    spawner.spawn_enemy()
                elif event.type == FlyingEnemy.flying_anim_event:
                    for flying_enemy in flying_group.sprites():
                        flying_enemy.next_frame()


    def reset(self):
        global start_time, level, score
        level = 1
        score = 0
        cactus_group.empty()
        flying_group.empty()
        start_time = pygame.time.get_ticks()
                       
class StateMenu:

    dino_icon = pygame.sprite.Sprite()
    dino_icon.image = dino_image
    dino_icon.image = pygame.transform.scale_by(dino_icon.image,1.5)
    dino_icon.rect = dino_icon.image.get_rect()
    dino_icon.rect.center = (WIDTH/5,HEIGHT/2)

    dino_icon2 = pygame.sprite.Sprite()
    dino_icon2.image = pygame.transform.flip(dino_icon.image,True,False)
    dino_icon2.rect = dino_icon2.image.get_rect()
    dino_icon2.rect.center = (WIDTH*4/5,HEIGHT/2)

    icon_group = pygame.sprite.Group()
    icon_group.add(dino_icon,dino_icon2)

    quit_game_button = Button("Quit","Grey")
    quit_game_button.rect.midtop = (WIDTH/2,HEIGHT/2+Button.border_offset+10)

    def __init__(self,start_text,top_text):
        self.start_game_button = Button(start_text,"Grey")
        self.start_game_button.rect.midbottom = (WIDTH/2,HEIGHT/2-Button.border_offset-10)

        self.intro_text = Text(top_text)
        self.intro_text.rect.midtop = (WIDTH/2,40)

    def update(self):
        pass

    def draw(self):
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_HEIGHT))
        self.start_game_button.draw()
        StateMenu.quit_game_button.draw()
        StateMenu.icon_group.draw(screen)
        self.intro_text.draw()
        pygame.display.flip() 
    
    def check_events(self):
        global game_state
        for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button.mouse_over():
                        game_state = StateRunning()
                        game_state.reset()
                    if StateMenu.quit_game_button.mouse_over():
                        pygame.quit()
                        exit()

class EventEnemySpawner:
    
    cactus_image = pygame.image.load("Tabor_Code/W2D1/trexgraphics/cactus1.png")
    flying_image = pygame.image.load("Tabor_Code/W2D1/trexgraphics/flying2.png")

    spawn_event = pygame.event.custom_type()

    level_base_speed = [9,10,12,14,18]
    level_spawn_delay = [1500,1400,1300,1200,1200]
    spawn_diff_ratio = 1/3

    
    def __init__(self):
        global level
        self.last_level = level
        pygame.time.set_timer(EventEnemySpawner.spawn_event,EventEnemySpawner.level_spawn_delay[level-1])
    
    def update(self):
        global level
        if level > self.last_level:
            self.last_level = level
            pygame.time.set_timer(EventEnemySpawner.spawn_event,EventEnemySpawner.level_spawn_delay[level-1])
    
    def create_cactus(self):
        global level
        cactus = Enemy(EventEnemySpawner.cactus_image,(-EventEnemySpawner.level_base_speed[level-1],0))
        cactus.rect.bottomleft = (WIDTH, GROUND_HEIGHT+10)
        return cactus
    
    def create_flying(self,speed_offset):
        global level
        flying = FlyingEnemy(EventEnemySpawner.flying_image,(-EventEnemySpawner.level_base_speed[level-1]+speed_offset,0))
        flying.rect.bottomleft = (WIDTH, GROUND_HEIGHT-Player.player_standing_height+10)
        return flying

    def spawn_enemy(self):
        percentage = random.randint(0,100)
        
        if percentage < 30:
            speed_offset = random.randint(-2,0)
            enemy = self.create_flying(speed_offset)
            flying_group.add(enemy)
        else:
            enemy = self.create_cactus()
            cactus_group.add(enemy)      

player_group = pygame.sprite.GroupSingle(Player(dino_image,(0,0)))
cactus_group = pygame.sprite.Group()
flying_group = pygame.sprite.Group()

spawner = EventEnemySpawner()

game_state = StateMenu("Start Game","Retro-Rex")

def get_level():
    i = 0
    while i < len(LEVEL_SCORES) and LEVEL_SCORES[i] <= score:
        i += 1
    return i

while True:
    
    game_state.check_events()
    game_state.update()
    game_state.draw()
    
    clock.tick(60)
    