import pygame
import random

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME
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

class Speed:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Character:
    def __init__(self,surface : pygame.Surface):
        self.surf = surface
        self.rect = self.surf.get_rect()
    
    def draw(self):
        screen.blit(self.surf,self.rect)

class Text(Character):
    def __init__(self,text):
        super().__init__(font.render(text,True,"Black"))
    
    def update_text(self,new_text):
        self.surf = font.render(new_text,True,"Black")

class Button(Character):
    border_offset = 10

    def __init__(self,text,color):
        self.color = color
        super().__init__(font.render(text,True,"Black"))

    def draw(self):
        background_rect = pygame.Rect(self.rect.left-Button.border_offset,self.rect.top-Button.border_offset,self.rect.width+Button.border_offset*2,self.rect.height+Button.border_offset*1.2)
        pygame.draw.rect(screen,self.color,background_rect)
        pygame.draw.rect(screen,"Black",background_rect,2)
        super().draw()

    def mouse_over(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

class MovingCharacter(Character):
    def __init__(self,surface : pygame.Surface, speed : list[int,int] ):
        super().__init__(surface)
        self.speed = Speed(speed[0],speed[1])
    
    def update(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
    
class Player(MovingCharacter):

    standing_x_pos = 100
    player_standing_height = 0

    standing_frame_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex3.png")
    standing_frame_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex4.png")
    standing_frames = [standing_frame_1,standing_frame_2]
    ducking_frame_1 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex_duck1.png")
    ducking_frame_2 = pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex_duck2.png")
    ducking_frames = [ducking_frame_1,ducking_frame_2]
    anim_time = 100

    def __init__(self, surface : pygame.Surface, speed : list[int,int]):
        super().__init__(surface,speed)
        self.ducking = False
        Player.player_standing_height = self.rect.height
        self.next_anim_time = pygame.time.get_ticks()  + Player.anim_time
        self.current_frame = 0

    def draw(self):
        if pygame.time.get_ticks() > self.next_anim_time:
            self.current_frame = (self.current_frame + 1) % len(Player.standing_frames)
            self.next_anim_time = pygame.time.get_ticks() + Player.anim_time
            if not self.ducking:
                player.surf = Player.standing_frames[self.current_frame]
            else:
                player.surf = Player.ducking_frames[self.current_frame]
        screen.blit(self.surf,self.rect)

    def update(self):
        self.speed.y += GRAVITY
        super().update()
        if player.rect.bottom > GROUND_HEIGHT:
            player.rect.bottom = GROUND_HEIGHT
            player.speed.y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.try_duck()
        else:
            self.try_set_standing()
    
    def set_ducking(self):
        self.ducking = True
        player.surf = Player.ducking_frames[self.current_frame]
        player.rect = player.surf.get_rect()
        player.rect.midbottom = (Player.standing_x_pos+20,GROUND_HEIGHT)

    def set_standing(self):
        self.ducking = False
        player.surf = Player.standing_frames[self.current_frame]
        player.rect = player.surf.get_rect()
        player.rect.midbottom = (Player.standing_x_pos,GROUND_HEIGHT)       

    def try_set_standing(self):
        if player.rect.bottom >= GROUND_HEIGHT and self.ducking:
            self.set_standing()
            
    def try_jump(self):
        if player.rect.bottom >= GROUND_HEIGHT and not self.ducking:
            player.speed.y = -JUMP_POWER
    
    def try_duck(self):
        if player.rect.bottom >= GROUND_HEIGHT and not self.ducking:
            self.set_ducking()
            

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
        player.update()
        for cactus in enemies:
            cactus.update()
            if cactus.rect.right < 0:
                enemies.remove(cactus)

    def draw(self):
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_HEIGHT))
        for cactus in enemies:
            cactus.draw()
        player.draw()
        StateRunning.score_text.draw()
        StateRunning.level_text.draw()
        pygame.display.flip() 
    
    def check_events(self):
        for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        player.try_jump()
                if event.type == EventEnemySpawner.spawn_event:
                    spawner.spawn_enemy()

    def reset(self):
        global start_time, enemies, level, score
        level = 1
        score = 0
        enemies = []
        start_time = pygame.time.get_ticks()
                       
class StateMenu:

    dino_icon = Character(pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png"))
    dino_icon.surf = pygame.transform.scale_by(dino_icon.surf,1.5)
    dino_icon.rect = dino_icon.surf.get_rect()
    dino_icon.rect.center = (WIDTH/5,HEIGHT/2)

    dino_icon2 = Character(pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png"))
    dino_icon2.surf = pygame.transform.scale_by(dino_icon2.surf,1.5)
    dino_icon2.surf = pygame.transform.flip(dino_icon2.surf,True,False)
    dino_icon2.rect = dino_icon2.surf.get_rect()
    dino_icon2.rect.center = (WIDTH*4/5,HEIGHT/2)

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
        StateMenu.dino_icon.draw()
        StateMenu.dino_icon2.draw()
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

class Enemy(MovingCharacter):

    def __init__(self,surface:pygame.Surface,speed :list[int,int]):
        super().__init__(surface,speed)
    
    def update(self):
        global game_state
        super().update()
        if self.rect.colliderect(player.rect):
            game_state = StateMenu("Restart",f"You died with {score} points.")


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
        flying = Enemy(EventEnemySpawner.flying_image,(-EventEnemySpawner.level_base_speed[level-1]+speed_offset,0))
        flying.rect.bottomleft = (WIDTH, GROUND_HEIGHT-Player.player_standing_height+10)
        return flying

    def spawn_enemy(self):
        global enemies
        percentage = random.randint(0,100)
        
        if percentage < 30:
            speed_offset = random.randint(-2,0)
            enemy = self.create_flying(speed_offset)
        else:
            enemy = self.create_cactus()
        enemies.append(enemy)
    

class EnemySpawner:

    level_base_speed = [9,10,12,14,18]
    level_spawn_delay = [1500,1400,1300,1200,1200]
    spawn_diff_ratio = 1/3

    def __init__(self):
        self.schedule_next_spawn()
    
    def update(self):
        if pygame.time.get_ticks() >= self.next_spawn:
            self.schedule_next_spawn()
            self.spawn_enemy()
    
    def create_cactus(self):
        global level
        cactus = Enemy(pygame.image.load("Tabor_Code/W2D1/trexgraphics/cactus1.png"),(-EnemySpawner.level_base_speed[level-1],0))
        cactus.rect.bottomleft = (WIDTH, GROUND_HEIGHT+10)
        return cactus
    
    def create_flying(self,speed_offset):
        global level
        flying = Enemy(pygame.image.load("Tabor_Code/W2D1/trexgraphics/flying2.png"),(-EnemySpawner.level_base_speed[level-1]+speed_offset,0))
        flying.rect.bottomleft = (WIDTH, GROUND_HEIGHT-Player.player_standing_height+10)
        return flying

    def spawn_enemy(self):
        global enemies
        percentage = random.randint(0,100)
        
        if percentage < 30:
            speed_offset = random.randint(-2,0)
            enemy = self.create_flying(speed_offset)
        else:
            enemy = self.create_cactus()
        enemies.append(enemy)
    
    def schedule_next_spawn(self):
        spawn_diff = int(EnemySpawner.spawn_diff_ratio * EnemySpawner.level_spawn_delay[level-1])
        self.next_spawn = pygame.time.get_ticks() + EnemySpawner.level_spawn_delay[level-1] + random.randint(-spawn_diff,spawn_diff)
        

player = Player(pygame.image.load("Tabor_Code/W2D1/trexgraphics/trex1.png"),(0,0))
player.rect.midbottom = (Player.standing_x_pos,GROUND_HEIGHT)

enemies : list[Enemy] = [] 

spawner = EventEnemySpawner()

game_state = StateMenu("Start","Retro-Rex")


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
    