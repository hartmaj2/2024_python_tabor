import random

def tisksklepu(lvl):
    print(len(lvl), "rozmery")
    for i in lvl:
        for j in i:
            print(j, end="")                 #tam, kde tohle pouzivam, je to jine!!!!!!!!!!!!!!!!!!!!!!
        print()

def randomsklep():
    randomrozmer = random.randint(6, 20)
    lvlradek = []
    lvl = []

    for i in range(randomrozmer):
        lvlradek.append(0)

    for i in range(randomrozmer):
        lvl.append(lvlradek[:])                     #ctverec se samyma nulama


    x = random.randint(0, randomrozmer - 1)
    y = random.randint(0, randomrozmer - 1)
    lvl[y][x] = 2               #random zacatek


    kolikrat = random.randint(randomrozmer - 2, randomrozmer + 10)
    while kolikrat != 0:

        smer = random.randint(0, 3)
        if smer == 0:
            delkachodby = random.randint(0, x)
            for i in range(delkachodby):
                x = x - 1
                if lvl[y][x] != 2:
                    lvl[y][x] = 1
            if lvl[y][x] != 2 and kolikrat == 1:
                lvl[y][x] = 3
            elif lvl[y][x] == 2 and kolikrat == 1:
                if x == 0:
                    lvl[y][x + 1] = 3
                else:
                    lvl[y][x - 1] = 3
        elif smer == 1:
            delkachodby = random.randint(0, y)
            for i in range(delkachodby):
                y = y - 1
                if lvl[y][x] != 2:
                    lvl[y][x] = 1
            if lvl[y][x] != 2 and kolikrat == 1:
                lvl[y][x] = 3
            elif lvl[y][x] == 2 and kolikrat == 1:
                if x == 0:
                    lvl[y][x + 1] = 3
                else:
                    lvl[y][x - 1] = 3
        elif smer == 2:
            delkachodby = random.randint(0, randomrozmer - 1 - x)
            for i in range(delkachodby):
                x = x + 1
                if lvl[y][x] != 2:
                    lvl[y][x] = 1
            if lvl[y][x] != 2 and kolikrat == 1:
                lvl[y][x] = 3
            elif lvl[y][x] == 2 and kolikrat == 1:
                if x == 0:
                    lvl[y][x + 1] = 3
                else:
                    lvl[y][x - 1] = 3
        else:
            delkachodby = random.randint(0, randomrozmer - 1 - y)
            for i in range(delkachodby):
                y = y + 1
                if lvl[y][x] != 2:
                    lvl[y][x] = 1
            if lvl[y][x] != 2 and kolikrat == 1:
                lvl[y][x] = 3
            elif lvl[y][x] == 2 and kolikrat == 1:
                if x == 0:
                    lvl[y][x + 1] = 3
                else:
                    lvl[y][x - 1] = 3

        kolikrat = kolikrat - 1                       #random cesticky + konec


    lvl.append(lvlradek[:])
    lvl.insert(0, lvlradek[:])

    for radecek in lvl:
        radecek.append(0)
        radecek.insert(0, 0)




    return lvl





lvl = randomsklep()
tisksklepu(lvl)














#lvl1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#lvl10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]