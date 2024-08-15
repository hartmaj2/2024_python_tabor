import pygame
import random
import math

pygame.init()

height = 600
width = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

font = pygame.font.Font("Tabor_Code/W2D1/font/Pixeltype.ttf",50)

spawn_event = pygame.event.custom_type()
pygame.time.set_timer(spawn_event,1000)

asteroid_group = pygame.sprite.Group()
player_shot_group = pygame.sprite.Group()
enemy_shot_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
game_start_time = 0
highscore = 0
score = 0
level = 0


class FileManager:
    def load_highscore():
        global highscore
        file = open("Tabor_Code/W2D4/ast_highscore.txt","r")
        data = file.readline()
        if data != "":
            highscore = int(data)
        file.close()

    def save_highscore():
        global highscore
        file = open("Tabor_Code/W2D4/ast_highscore.txt","w")
        file.write(str(highscore))
        file.close()

class GameManager:

    level_scores = [0,5,10,12,14,20]

    state_running = 0
    state_game_over = 1

    def clear_groups():
        asteroid_group.empty()
        enemy_group.empty()
        enemy_shot_group.empty()
        player_shot_group.empty()

    def reset_game():
        global game_start_time
        game_start_time = pygame.time.get_ticks()
        GameManager.clear_groups()
    
    def update_score():
        global score, highscore
        score = int((pygame.time.get_ticks() - game_start_time) / 1000)
        if score > highscore:
            highscore = score 

    def update_level():
        global score
        # if score > GameManager.level_scores[len(GameManager.level_scores)-1]:
        #     return len(GameManager.level_scores)-1
        for i in range(len(GameManager.level_scores)):
            if score < GameManager.level_scores[i]:
                return i - 1
        return i

def get_dir_to_mouse(x,y):
    mx,my = pygame.mouse.get_pos()
    return math.atan2(my-y,mx-x)

def get_dir_to_pos(start_rect : pygame.Rect ,goal_rect : pygame.Rect):
    return math.atan2(goal_rect.centery-start_rect.centery,goal_rect.centerx-start_rect.centerx)


class Player(pygame.sprite.Sprite):

    player_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/better_rocket_game.png")
    player_surf = pygame.transform.scale_by(player_surf,0.1)
    speed = 5
    shot_interval = 500

    def __init__(self):
        super().__init__()
        self.image = Player.player_surf
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width/2,height-20)
        self.next_shot_time = pygame.time.get_ticks()

    def is_loaded(self):
        return pygame.time.get_ticks() > self.next_shot_time

    def update(self):
        global player_shot_group, game_state
        keys = pygame.key.get_pressed()
        delta_x = 0
        if keys[pygame.K_a]:
            delta_x -= Player.speed
        if keys[pygame.K_d]:
            delta_x += Player.speed
        self.rect.x += delta_x
        if keys[pygame.K_SPACE] and self.is_loaded():
            dir = get_dir_to_mouse(self.rect.centerx,self.rect.centery)
            player_shot_group.add(Shot(self.rect.center,dir,"cyan"))
            self.next_shot_time = pygame.time.get_ticks() + Player.shot_interval
        if pygame.sprite.groupcollide(player_group,enemy_shot_group,False,False):
            game_state = GameManager.state_game_over

class Asteroid(pygame.sprite.Sprite):

    asteroid_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/asteroid.png")
    asteroid_surf = pygame.transform.scale_by(asteroid_surf,0.15)
    speed = 5
    anim_interval = 100

    def __init__(self):
        super().__init__()
        self.image = Asteroid.asteroid_surf
        self.image = pygame.transform.scale_by(Asteroid.asteroid_surf,random.randint(25,100)/100)
        self.rect = self.image.get_rect()
        self.rect.midleft = (random.randint(0,width),0)
        self.next_anim = pygame.time.get_ticks() + Asteroid.anim_interval

    def animate(self):
        time_now = pygame.time.get_ticks()
        if time_now > self.next_anim:
            self.image = pygame.transform.rotate(self.image,90)
            self.next_anim = time_now + Asteroid.anim_interval

    def update(self):
        global game_state
        self.animate()
        self.rect.y += Asteroid.speed
        if self.rect.top > height:
            self.kill()
        if pygame.sprite.groupcollide(asteroid_group,player_group,False,False,pygame.sprite.collide_circle_ratio(0.5)):
            game_state = GameManager.state_game_over

class Shot(pygame.sprite.Sprite):

    shot_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/laser.png")
    shot_surf = pygame.transform.scale_by(shot_surf,0.15)
    speed = 10

    def __init__(self,position,direction,color):
        super().__init__()
        self.image = pygame.surface.Surface((30,5)).convert_alpha()
        self.image.fill(color)
        self.image = pygame.transform.rotate(self.image,-math.degrees(direction))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.direction = direction
    
    def update(self):
        self.rect.y += Shot.speed * math.sin(self.direction)
        self.rect.x += Shot.speed * math.cos(self.direction)
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.groupcollide(player_shot_group,asteroid_group,True,True):
            pass

class Enemy(pygame.sprite.Sprite):

    enemy_surf = pygame.image.load("Tabor_Code/W2D1/graphics/Player/player_stand.png")
    base_speed = 3
    shot_interval = 3000

    def __init__(self):
        super().__init__()
        self.image = Enemy.enemy_surf
        self.rect = self.image.get_rect()
        self.rect.midtop = (random.randint(50,width-50),10)
        self.next_shot_time = pygame.time.get_ticks() + Enemy.shot_interval
        self.speed_x = random.randint(-Enemy.base_speed,Enemy.base_speed)
    
    def update(self):
        if self.rect.right > width or self.rect.left < 0:
            self.speed_x *= -1
        self.rect.x += self.speed_x
        if pygame.sprite.groupcollide(enemy_group,player_shot_group,True,True):
            print("enemy hit")
        if pygame.time.get_ticks() > self.next_shot_time:
            dir = get_dir_to_pos(self.rect,player_group.sprite.rect)
            enemy_shot_group.add(Shot(self.rect.center,dir,"red"))
            self.next_shot_time = pygame.time.get_ticks() + Enemy.shot_interval + random.randint(-2000,2000)

class ScoreText(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
    
    def update(self):
        global score
        self.image = font.render(f"Score: {score}",True,"white")
        self.rect  = self.image.get_rect()
        self.rect.topright = (width-10,10)

class LevelText(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
    
    def update(self):
        global level
        self.image = font.render(f"Level: {level}",True,"white")
        self.rect  = self.image.get_rect()
        self.rect.topleft = (10,10)

class HighscoreText(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
    
    def update(self):
        global highscore
        self.image = font.render(f"Highscore: {highscore}",True,"white")
        self.rect  = self.image.get_rect()
        self.rect.midbottom = (width/2,height/2-50)
    
class GameOverText(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image = font.render("GAME OVER",True,"red")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
    
class RestartGameText(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image = font.render("Press \"r\" to restart game",True,"red")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2+60)

class QuitGameText(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image = font.render("Press \"q\" to quit game",True,"red")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2+120)

class Spawner(pygame.sprite.Sprite):

    asteroid_spawn_intervals = [3000,2000,1000,500,300,100]
    enemy_spawn_intervals = [10000,7000,5000,4000,2000,1000]

    def __init__(self):
        global level
        super().__init__()
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + Spawner.asteroid_spawn_intervals[level]
        self.next_enemy_spawn_time = pygame.time.get_ticks() + Spawner.enemy_spawn_intervals[level]

    def try_spawn_asteroid(self):
        global level
        if pygame.time.get_ticks() > self.next_asteroid_spawn_time:
            randomness = Spawner.asteroid_spawn_intervals[level] // 2
            self.next_asteroid_spawn_time = pygame.time.get_ticks() + Spawner.asteroid_spawn_intervals[level] + random.randint(-randomness,randomness) 
            asteroid_group.add(Asteroid())

    def try_spawn_enemy(self):
        global level
        randomness = Spawner.enemy_spawn_intervals[level] // 2
        if pygame.time.get_ticks() > self.next_enemy_spawn_time:
            self.next_enemy_spawn_time = pygame.time.get_ticks() + Spawner.enemy_spawn_intervals[level] + random.randint(-randomness,randomness) 
            enemy_group.add(Enemy())

    def update(self):
        self.try_spawn_asteroid()
        self.try_spawn_enemy()
    
    

spawner_group = pygame.sprite.GroupSingle(Spawner())
player_group = pygame.sprite.GroupSingle(Player())
running_text_group = pygame.sprite.Group()
running_text_group.add(ScoreText(),LevelText())
game_over_text_group = pygame.sprite.Group()
game_over_text_group.add(HighscoreText(),RestartGameText(),GameOverText(),QuitGameText())

game_state = GameManager.state_running
FileManager.load_highscore()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            FileManager.save_highscore()
            pygame.quit()
            exit()

        if game_state == GameManager.state_game_over:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    GameManager.reset_game()
                    game_state = GameManager.state_running
                if keys[pygame.K_q]:
                    FileManager.save_highscore()
                    pygame.quit()
                    exit()

        if game_state == GameManager.state_running:
            if event.type == spawn_event:
                asteroid_group.add(Asteroid())
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    enemy_group.add(Enemy())

    if game_state == GameManager.state_running:  

        GameManager.update_score()
        level = GameManager.update_level()      

        asteroid_group.update()
        player_group.update()
        player_shot_group.update()
        enemy_shot_group.update()
        enemy_group.update()
        running_text_group.update()
        spawner_group.update()

        screen.fill("black")
        player_group.draw(screen)
        asteroid_group.draw(screen)
        player_shot_group.draw(screen)
        enemy_shot_group.draw(screen)
        enemy_group.draw(screen)
        running_text_group.draw(screen)
    
    elif game_state == GameManager.state_game_over:

        screen.fill("black")
        
        game_over_text_group.update()

        running_text_group.draw(screen)
        game_over_text_group.draw(screen)


    pygame.display.update()
    clock.tick(60)
    

    