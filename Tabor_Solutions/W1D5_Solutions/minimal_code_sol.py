import pygame

pygame.init() # Tohle je dulezite, provede to nejakou magii, ktera vse pripravi

WIDTH = 300
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Vytvorime okno tzv. DISPLAY SURFACE, zkusime spustit 

# Nyni vyrobime herni smycku, aby se okno vubec ukazalo tak (asi) potrebujeme prochazet
# vsechny eventy, muzeme vyzkouset, co se vypise

# TODO: blbost challenge, zprovozni zavirani okna, je to trochu detektivni prace
# HINT: pouzij VSCode naseptavac a pomocne tisky
running = True
while running:
    for event in pygame.event.get():
        if event.type == 256:
            running = False
        
