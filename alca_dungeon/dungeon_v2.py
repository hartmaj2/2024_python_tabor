#v2 je pokus o to, aby se vykreslovala pouze ta cast sklepu, kde jsi uz byl
#ZMENA - v2 je pokus o bosslevel

#bugy ve v2:
#nekdy se mob spawne na stene
#po bosslvlu stale bezi songa2


import pygame
import random
import generacesklepicku

pygame.init() 
icon = pygame.image.load("alca_dungeon/mob3.png")
pygame.display.set_caption('◦•●◉✿ the PETRŽEL Dungeon ✿◉●•◦')
pygame.display.set_icon(icon)

pygame.mixer.init()

#channel1 = pygame.mixer.Channel(1)
#channel2 = pygame.mixer.Channel(2)

songa = pygame.mixer.Sound("alca_dungeon/song.mp3")
songa.set_volume(0.5)
songa2 = pygame.mixer.Sound("alca_dungeon/song2.wav")
songa2.set_volume(0.2)
spawn = pygame.mixer.Sound("alca_dungeon/spawn.wav")
hitsound = pygame.mixer.Sound("alca_dungeon/hit.mp3")
#pygame.mixer.music.load(songa)
#pygame.mixer.music.play(-1)
# channel1.play( songa, -1 )
songa.play(loops=-1)

def robimlvl(dokonceno):  #jestli je bosslvl
    print("robim lvl")
    if dokonceno % 5 == 0 and dokonceno != 0:
        lvlradek = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        lvl1 = [0, 1, 0, 0, 0, 3, 1, 0, 0, 0, 1, 0]
        lvl2 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        lvl3 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        lvl4 = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        lvl5 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        lvl6 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        lvl7 = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        lvl8 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        lvl9 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        lvl10 = [0, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0]
        lvl = [lvlradek, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10, lvlradek]
        print("bude bosslvl")
    else:
        lvl = generacesklepicku.randomsklep()
    return lvl


def tisksklepu(lvl, x, y, kdemobove, barvymobu, blitbosse):
    hratspawn = False
    stena = pygame.image.load("alca_dungeon/stena.png")
    stena = pygame.transform.scale_by(stena, 2)
    chodba = pygame.image.load("alca_dungeon/chodba.png")
    chodba = pygame.transform.scale_by(chodba, 2)
    start = pygame.image.load("alca_dungeon/start.png")
    start = pygame.transform.scale_by(start, 2)
    cil = pygame.image.load("alca_dungeon/cil.png")
    cil = pygame.transform.scale_by(cil, 2)

    typek = pygame.image.load("alca_dungeon/typek.png")
    typek = pygame.transform.scale_by(typek, 2)

    mob1 = pygame.image.load("alca_dungeon/mob1.png")
    mob1 = pygame.transform.scale_by(mob1, 2)
    #mob1.fill("magenta")
    mob2 = pygame.image.load("alca_dungeon/mob2.png")
    mob2 = pygame.transform.scale_by(mob2, 2)
    #mob2.fill("cyan")
    mob3 = pygame.image.load("alca_dungeon/mob3.png")
    mob3 = pygame.transform.scale_by(mob3, 2)
    #mob3.fill("yellow")
    boss = pygame.image.load("alca_dungeon/boss.png")
    boss = pygame.transform.scale_by(boss, 2)

    if dokonceno % 5 - 1 == 0 and zacatek and dokonceno != 1:
        #channel1.play( songa2, -1)
        songa2.play(loops = -1)
        hratspawn = True

        print("boss se generuje doufam")
        souradnicemobu = [5, 5]
        kdemobove.append(souradnicemobu[:])
        barvymobu.append(3)
        mobhp.append(random.randint(150, 200))

    print(len(lvl), "rozmery")
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if i == y and j == x:
                print("*", end="")
            else:
                print(lvl[i][j], end="")
                if dokonceno % 5 - 1 != 0:
                    if random.randint(0, 6) == 0 and zacatek and lvl[i][j] != 0:   #random generace mobu
                        souradnicemobu = [j, i]
                        kdemobove.append(souradnicemobu[:])
                        ktery = random.randint(0, 2)
                        if ktery == 0:
                            barvymobu.append(0)
                            mobhp.append(random.randint(5, 25))
                        elif ktery == 1:
                            barvymobu.append(1)
                            mobhp.append(random.randint(15, 35))
                        else:
                            barvymobu.append(2)
                            mobhp.append(random.randint(10, 25))
        print()

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            odsazenix = j * 32
            odsazeniy = i * 32
            if lvl[i][j] == 0:
                screen.blit(stena, (odsazenix, odsazeniy)) #vykresluje se lvl
            elif lvl[i][j] == 1:
                screen.blit(chodba, (odsazenix, odsazeniy))
            elif lvl[i][j] == 2:
                screen.blit(start, (odsazenix, odsazeniy))
            else:
                screen.blit(cil, (odsazenix, odsazeniy))
            if i == y and j == x:  #typek
                screen.blit(typek, (odsazenix, odsazeniy))
            
            if dokonceno % 5 - 1 != 0:
                #print("neni bosslvl")
                for souradnicemobu in kdemobove:  #mobove
                    if souradnicemobu == [j, i]:
                        if barvymobu[kdemobove.index(souradnicemobu)] == 0:
                            screen.blit(mob1, (odsazenix, odsazeniy))
                        elif barvymobu[kdemobove.index(souradnicemobu)] == 1:
                            screen.blit(mob2, (odsazenix, odsazeniy))
                        else:
                            screen.blit(mob3, (odsazenix, odsazeniy))

    if dokonceno % 5 - 1 == 0 and dokonceno != 1 and blitbosse: #boss
        print("boss se vykresluje")
        odsazenix = kdemobove[0][0] * 32
        odsazeniy = kdemobove[0][1] * 32
        screen.blit(boss, (odsazenix, odsazeniy))
    
    if dokonceno % 5 - 2 == 0 and dokonceno != 2 and zacatek:
        songa2.stop()
    
    return kdemobove, barvymobu, mobhp, hratspawn
            

def hledam2(lvl):
    for radek in lvl:
        if 2 in radek:
            y = lvl.index(radek)
            break
    x = radek.index(2)

    return x, y
    #urci souracnice startu(2)
    #[0, 0] je vlevo nahore


def chozenisklepem(kamjit, lvl, stojimna, x, y, sila, magie, hp, mobhp, kdemobove, barvymobu):
    nedosteny = pygame.image.load("alca_dungeon/nechoddosteny.png")
    nedosteny = pygame.transform.scale_by(nedosteny, 5)
    
    stenawarning = pygame.image.load("alca_dungeon/stenawarning.png")
    stenawarning = pygame.transform.scale_by(stenawarning, 5)
    
    if hp < 100:
        hp += 1

    souradnice = [x, y]  

    xtest = x
    ytest = y

    print(souradnice)

    blitbosse = False
    if dokonceno % 5 - 1 == 0 and dokonceno != 1 and len(kdemobove) != 0: 
        blitbosse = True

    #print(colorama.Fore.MAGENTA, "Zdravi", hp, ", sila", sila, ", magicke skills", magie,", zkusenosti", xp, "zabitych mobu", kills, ", inventar:", inventory)

    #print(colorama.Fore.MAGENTA, "Muzes jit doleva(0), nahoru(1), doprava(2), dolu(3)")
    #print("Souradnice:", souradnice)
    #print("Stojis na", stojimna) #udelani pozice podle souradnic
    #print("Vlevo, nahore, vpravo a dole vidis:", lvl[y][x - 1], lvl[y - 1][x], lvl[y][x + 1], lvl[y + 1][x])

    if kamjit == 0:
        xtest = x - 1
        #ytest = y
    elif kamjit == 1:
        #xtest = x
        ytest = y - 1
    elif kamjit == 2:
        xtest = x + 1
        #ytest = y
    elif kamjit == 3:
        #xtest = x
        ytest = y + 1
    


    if lvl[ytest][xtest] == 0:
        print("nechod do steny")            #abys nechodil do steny
        screen.blit(stenawarning, (1290, 442))
    else:
        x = xtest
        y = ytest
        souradnice = [x, y]
        stojimna = lvl[y][x]

        screen.blit(nedosteny, (1290, 442))

    
    kdemobove, barvymobu, mobhp, hratspawn = tisksklepu(lvl, x, y, kdemobove, barvymobu, blitbosse)


    canhit = False
    screen.blit(hitdisabled, (1290, 550))
                                                    #urci, jestli stojis na mobovi
    for souradnicemobu in kdemobove:
        if souradnicemobu == [x, y]:
            canhit = True
            hitrect.topleft = (1290, 550)
            screen.blit(hit, hitrect)
            print("bude mobfight")
            break
        
        #else:
            

    
    if kamjit == 5:             #kdyz hitnes moba
        print("hit2")
        if barvymobu[kdemobove.index(souradnicemobu)] == 0:
            print("mob1")
            mobdamage = 10
        elif barvymobu[kdemobove.index(souradnicemobu)] == 1:
            print("mob2")
            mobdamage = 20
        elif barvymobu[kdemobove.index(souradnicemobu)] == 3:
            print("boss")
            #sila = 1000  # DELETE
            mobdamage = 50
        else:
            print("mob3")
            mobdamage = 30
            
        
        damage = sila + magie * 1.1 + random.randint(5, 15)

        hp -= mobdamage
        print(hp)
        mobhp[kdemobove.index(souradnicemobu)] -= damage
    
        if mobhp[kdemobove.index(souradnicemobu)] <= 0:
            canhit = False
            if mobdamage == 10:
                sila += 5
            elif mobdamage == 20:
                magie += 5
            else:
                sila += 5
                magie += 5
            
            print("mob umrel")
            if barvymobu[kdemobove.index(souradnicemobu)] == 3: 
                blitbosse = False #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #songa2.stop()
                
            
            #barvymobu.remove(barvymobu[kdemobove.index(souradnicemobu)])
            del barvymobu[kdemobove.index(souradnicemobu)]
            #mobhp.remove(mobhp[kdemobove.index(souradnicemobu)])
            del mobhp[kdemobove.index(souradnicemobu)]
            kdemobove.remove(souradnicemobu)
            tisksklepu(lvl, x, y, kdemobove, barvymobu, blitbosse)



    return stojimna, x, y, sila, magie, hp, canhit, mobhp, kdemobove, barvymobu, hratspawn
    
    

WIDTH = 1600
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()


textlevo = pygame.image.load("alca_dungeon/levo.png")
textlevo = pygame.transform.scale_by(textlevo, 5)
#textlevo.fill("magenta")
texthore = pygame.image.load("alca_dungeon/hore.png")
texthore = pygame.transform.scale_by(texthore, 5)
#texthore.fill("cyan")
textpravo = pygame.image.load("alca_dungeon/pravo.png")
textpravo = pygame.transform.scale_by(textpravo, 5)
#textpravo.fill("yellow")
textdolu = pygame.image.load("alca_dungeon/dolu.png")
textdolu = pygame.transform.scale_by(textdolu, 5)
#textdolu.fill("white")

cernyctverec = pygame.image.load("alca_dungeon/cernyctverec.png") #prekryje predchozi sklep, nemazat !POTOM SE MU TAKY MUSI NASTAVIT TEXTURA POZADI!
cernyctverec = pygame.transform.scale_by(cernyctverec, 10)               
kontajner = pygame.image.load("alca_dungeon/kontajner.png")    #kontajner s poctem lvlu, hp, ...
kontajner = pygame.transform.scale_by(kontajner, 8)
#kontajner.fill("cyan")
hitdisabled = pygame.image.load("alca_dungeon/hitdisabled.png")
hitdisabled = pygame.transform.scale_by(hitdisabled, 5)
#hitdisabled.fill("gray")
hit = pygame.image.load("alca_dungeon/hit.png")
hit = pygame.transform.scale_by(hit, 5)
#hit.fill("white")
hitrect = hit.get_rect()

pozadi = pygame.image.load("alca_dungeon/pozadi.png")
pozadi = pygame.transform.scale_by(pozadi, 10)
umrelsiscreen = pygame.image.load("alca_dungeon/umrelsiscreen.png")
umrelsiscreen = pygame.transform.scale_by(umrelsiscreen, 10)

title = pygame.image.load("alca_dungeon/title.png")
title = pygame.transform.scale_by(title, 5)

levorect = textlevo.get_rect()
horerect = texthore.get_rect()
pravorect = textpravo.get_rect()
dolurect = textdolu.get_rect()

font = pygame.font.Font("alca_dungeon/IMMORTAL.ttf", 30)
font2 = pygame.font.Font("alca_dungeon/IMMORTAL.ttf", 40)
font3 = pygame.font.Font("alca_dungeon/IMMORTAL.ttf", 100)

sila = 1
magie = 1
hp = 100


hratspawn = False

canhit = False
mobhp = []
kdemobove = []
barvymobu = []
zacatek = True
dokonceno = 0
kamjit = 4
stojimna = 2
lvl = robimlvl(0) #na zacatku dokonceno = 0
x, y = hledam2(lvl)


screen.blit(pozadi, (0, 0))
screen.blit(title, (10, 50))
while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and levorect.collidepoint(pygame.mouse.get_pos()):
            kamjit = 0
            if hratspawn:
                print("alca_dungeon/mel by se hrat spawn.wav")
                print(hratspawn)
                # channel2.play(spawn)
                spawn.play()
        elif event.type == pygame.MOUSEBUTTONDOWN and horerect.collidepoint(pygame.mouse.get_pos()):
            kamjit = 1
            if hratspawn:
                print("alca_dungeon/mel by se hrat spawn.wav")
                print(hratspawn)
                # channel2.play(spawn)
                spawn.play()
        elif event.type == pygame.MOUSEBUTTONDOWN and pravorect.collidepoint(pygame.mouse.get_pos()):
            kamjit = 2
            if hratspawn:
                print("alca_dungeon/mel by se hrat spawn.wav")
                print(hratspawn)
                # channel2.play(spawn)
                spawn.play()
        elif event.type == pygame.MOUSEBUTTONDOWN and dolurect.collidepoint(pygame.mouse.get_pos()):
            kamjit = 3
            if hratspawn:
                print("alca_dungeon/mel by se hrat spawn.wav")
                print(hratspawn)
                # channel2.play(spawn)
                spawn.play()
        elif event.type == pygame.MOUSEBUTTONDOWN and hitrect.collidepoint(pygame.mouse.get_pos()) and canhit:
            print("hit!")
            hitsound.play()
            kamjit = 5



    if kamjit != 4:  #zapne se chozenisklepem
        screen.blit(cernyctverec, (0, 0))
        
        stojimna, x, y, sila, magie, hp, canhit, mobhp, kdemobove, barvymobu, hratspawn = chozenisklepem(kamjit, lvl, stojimna, x, y, sila, magie, hp, mobhp, kdemobove, barvymobu)
        

        kamjit = 4

        zacatek = False


        if stojimna == 3:         #kdyz dolozes k cili(3 v poli, zlaty zebricek)
            print("Prosel jsi tohle patro!")
            stojimna = 2
            lvl = robimlvl(dokonceno)
            x, y = hledam2(lvl)
            screen.blit(cernyctverec, (0, 0))
            #-----------------------------------------------------------------------------------------------------------------
            dokonceno += 1
            zacatek = True
            kdemobove = []
            barvymobu = []
            mobhp = []
            

        
    #pygame.time.delay(kolik milisekund)
    

    text = font2.render("Dokončeno levelů          Zdraví           Síla             Magické skills", True, "#a78020")

    textdokonceno = font.render(str(dokonceno), True, "#775a13")
    texthp = font.render(str(hp) + "/100", True, "#775a13")
    textsila = font.render(str(sila), True, "#775a13")
    textmagie = font.render(str(magie), True, "#775a13")

    textumrelsi = font3.render("Umřel jsi...", True, "#72504e")

    levorect.topleft = (1290, 10)
    horerect.topleft = (1290, 118)
    pravorect.topleft = (1290, 226)
    dolurect.topleft = (1290, 334)


    screen.blit(textlevo, levorect)
    screen.blit(texthore, horerect)
    screen.blit(textpravo, pravorect)
    screen.blit(textdolu, dolurect)

    screen.blit(kontajner, (0, 660))
    screen.blit(text, (70, 700))
    screen.blit(textdokonceno, (220, 790))
    screen.blit(texthp, (597, 790))
    screen.blit(textsila, (955, 790))
    screen.blit(textmagie, (1390, 790))


    
    
    if hp <= 0:
        screen.blit(umrelsiscreen, (0, 0))
        screen.blit(textumrelsi, (540, 500))
        
    
    clock.tick(60)
    pygame.display.flip()
