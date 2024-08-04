import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock() # 1. PRIDAME CLOCK OBJEKT, KTERY MA FUNKCI, KTEROU POTREBUJEME
font = pygame.font.Font("W1D5/font/Pixeltype.ttf",50)

background = pygame.image.load("W1D5/graphics/Sky.png")
ground = pygame.image.load("W1D5/graphics/ground.png")

SNAIL_SPEED = 10
JUMP_POWER = 10
GRAVITY = 0.5
GROUND_LEVEL = 300

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
    def __init__(self, surface : pygame.Surface, speed : list[int,int]):
        super().__init__(surface,speed)

    def update(self):
        self.speed.y += GRAVITY
        super().update()
        if player.rect.bottom > GROUND_LEVEL:
            player.rect.bottom = GROUND_LEVEL
            player.speed.y = 0
    
    def try_jump(self):
        if player.rect.bottom >= GROUND_LEVEL:
            player.speed.y = -JUMP_POWER

class StateRunning:

    def update(self):
        global game_state, score
        score = (pygame.time.get_ticks() - start_time) // 100
        score_text.update_text("Score: " + str(score))
        player.update()
        for fly in flys:
            fly.update()
            if fly.rect.left > WIDTH:
                flys.remove(fly)
        snail.update()
        if snail.rect.right < 0:
            snail.rect.left = WIDTH
        if snail.rect.colliderect(player.rect):
            game_state = StateRestartMenu()

    def draw(self):
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_LEVEL))
        for fly in flys:
            fly.draw()
        player.draw()
        snail.draw()
        score_text.draw()
        pygame.display.flip() 
    
    def check_events(self):
        for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player.rect.collidepoint(pygame.mouse.get_pos()):
                        spawn_fly(player.rect.center)
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        player.try_jump()

    def reset(self):
        global start_time
        snail.rect.left = WIDTH
        start_time = pygame.time.get_ticks()

class StateStartMenu:

    start_game_button = Button("Start Game","Grey")
    start_game_button.rect.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        pass

    def draw(self):
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_LEVEL))
        StateStartMenu.start_game_button.draw()
        pygame.display.flip() 
    
    def check_events(self):
        global game_state
        for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if StateStartMenu.start_game_button.mouse_over():
                        game_state = StateRunning()
                        game_state.reset()
                        
class StateRestartMenu:

    restart_game_button = Button("Restart","Grey")
    restart_game_button.rect.midbottom = (WIDTH/2,HEIGHT/2-Button.border_offset-10)

    quit_game_button = Button("Quit","Grey")
    quit_game_button.rect.midtop = (WIDTH/2,HEIGHT/2+Button.border_offset+10)

    def update(self):
        pass

    def draw(self):
        screen.blit(background,(0,0))
        screen.blit(ground,(0,GROUND_LEVEL))
        StateRestartMenu.restart_game_button.draw()
        StateRestartMenu.quit_game_button.draw()
        pygame.display.flip() 
    
    def check_events(self):
        global game_state
        for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if StateRestartMenu.restart_game_button.mouse_over():
                        game_state = StateRunning()
                        game_state.reset()
                    if StateRestartMenu.quit_game_button.mouse_over():
                        pygame.quit()
                        exit()

player = Player(pygame.image.load("W1D5/trexgraphics/trex1.png"),(0,0))
player.rect.midbottom = (100,300)

score_text = Text("Score: 0")
score_text.rect.midtop = (WIDTH/2,10)

flys : list[MovingCharacter] = [] 

snail = MovingCharacter(pygame.image.load("W1D5/trexgraphics/cactus1.png"),(-SNAIL_SPEED,0))
snail.rect.bottomleft = (WIDTH, GROUND_LEVEL)

game_state = StateStartMenu()
start_time = 0
score = 0

def spawn_fly(position):
    fly = MovingCharacter(pygame.image.load("W1D5/graphics/Fly/Fly1.png"),(5,0))
    fly.rect.center = position
    flys.append(fly)

while True:
    
    game_state.check_events()
    game_state.update()
    game_state.draw()
    
    clock.tick(60) # ZADRZDI PROGRAM NA DOBU, KTERA ODPOVIDA 60 FPS (cca 16.6 ms)
    