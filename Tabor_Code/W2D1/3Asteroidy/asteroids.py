import pygame
import random

pygame.init()

height = 600
width = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)

game_state = "running"

game_over_text_surf = font.render("GAME OVER",True,"red")
game_over_rect = game_over_text_surf.get_rect()
game_over_rect.center = (width/2,height/2)

restart_text_surf = font.render("Press \"r\" to restart game",True,"red")
restart_text_rect = restart_text_surf.get_rect()
restart_text_rect.center = (width/2,height/2+60)

spawn_event = pygame.event.custom_type()
pygame.time.set_timer(spawn_event,1000)

class Player(pygame.sprite.Sprite):

    player_surf = pygame.image.load("Tabor_Code/W2D1/asteroidgraphics/better_rocket_game.png")
    player_surf = pygame.transform.scale_by(player_surf,0.1)
    speed = 5

    def __init__(self):
        super().__init__()
        self.image = Player.player_surf
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width/2,height-20)


    def update(self):
        keys = pygame.key.get_pressed()
        delta_x = 0
        if keys[pygame.K_a]:
            delta_x -= Player.speed
        if keys[pygame.K_d]:
            delta_x += Player.speed
        self.rect.x += delta_x


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
            game_state = "game over"

asteroid_group = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_state == "game over":
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    game_state = "running"
                    asteroid_group.empty()
        if game_state == "running":
            if event.type == spawn_event:
                asteroid_group.add(Asteroid())

    if game_state == "running":
        screen.fill("black")
        print(len(asteroid_group))

        asteroid_group.update()
        player_group.update()

        player_group.draw(screen)
        asteroid_group.draw(screen)
    
    elif game_state == "game over":
        screen.fill("black")
        screen.blit(game_over_text_surf,game_over_rect)
        screen.blit(restart_text_surf,restart_text_rect)


    pygame.display.update()
    clock.tick(60)
    

    