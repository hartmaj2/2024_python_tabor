import pygame

pygame.init() # Tohle je dulezite, provede to nejakou magii, ktera vse pripravi

screen = pygame.display.set_mode((300,200)) # Vytvorime okno tzv. DISPLAY SURFACE, zkusime spustit 

# Nyni vyrobime herni smycku, aby se okno vubec ukazalo tak (asi) potrebujeme prochazet
# vsechny eventy, muzeme vyzkouset, co se vypise

# TODO: blbost challenge, zprovozni zavirani okna, je to trochu detektivni prace
# HINT: stisknuti zaviraciho tlacitka ma svuj event
# HINT: pouzij VSCode naseptavac a pomocne tisky

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        ...
        
