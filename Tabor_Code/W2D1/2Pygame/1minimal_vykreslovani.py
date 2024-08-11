import pygame

pygame.init()

screen = pygame.display.set_mode((900,600)) 

surface = pygame.Surface((200,100)) # 1. VYTVORIME SURFACE

# TODO: Zmen barvu surface na nejakou jinou
# HINT: surface.fill(barva)

# TODO zmen kod aby vykreslil surface do leveho dolniho rohu
# HINT: screen.blit(koho,kam)

# TODO: zmen kod tak, aby vykresleny obdelnicek byl siroka spageta tahnouci se od leveho okraje k pravemu
# HINT: budes muset zmenit jak velikost obdelnicku, tak i jeho pozici, kde ma zacinat


while True:
    for event in pygame.event.get(): # pygame.event.get() vrati seznam eventu
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    screen.blit(surface,(100,400)) # 2. REKNEME OBRAZOVCE, KAM A KOHO MA NAKRESLIT (ZATIM SE TO JEN NAPLANUJE)
    pygame.display.flip() # 3. REKNEME PYGAME, AT NAKRESLI NAPLANOVANE VECI NA OBRAZOVKU


# BONUS TODO: zkus uz ted zprovoznit pohyb (budes muset menit v case, kam postavicku "vyblitujes")
# HINT: postavy vykreslene na obrazovku z minula si musis mazat sam/a
# HINT: smazat je muzes tak, ze celou obrazovku zaplnis cernou barvou ( screen.fill("Black") )