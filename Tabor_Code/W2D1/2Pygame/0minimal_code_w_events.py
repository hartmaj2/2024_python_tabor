import pygame

pygame.init() # Tohle je dulezite, provede to nejakou magii, ktera vse pripravi

screen = pygame.display.set_mode((300,200)) # Vytvorime okno tzv. DISPLAY SURFACE, zkusime spustit 

# Nyni vyrobime herni smycku, aby se okno vubec ukazalo tak (asi) potrebujeme prochazet
# vsechny eventy, muzeme vyzkouset, co se vypise

# TODO: zkus nastavit velikost obrazovky, aby byla hodne vysoka ale malo siroka

# TODO: zkus si schvalne neco vytisknout na terminal uvnitr herni smycky

while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        ...
        
# BONUS TODO: blbost challenge: zprovozni ukonceni "hry" zavrenim okna, je to trochu detektivni prace
# HINT: kliknuti na cervene zaviraci tlacitko na liste okna ma svuj event
# HINT: pouzij VSCode naseptavac (co muzes zjistit o eventu a vytisknout to?)