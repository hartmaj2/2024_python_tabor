import turtle
turtle.speed(10)

# Proc jsou dobre funkce? Predstavte si program pro
# stavebni firmu, ktery stavi ctyri domy bez funkci


# vyhody funkci - jeden clovek muze psat, jake potrebuje funkce a vubec nemusi vedet, jak funguji
# mezitim druhy clovek bude ty funkce vytvaret a vubec ho nemusi zajimat, kdo a jak je bude pouzivat

# Predstavme si: dva programatori Franta a Karel se domluvi:  
#   1. Franta naplanuje, kam se presne postavy kostky a jak budou velke. Staci mu jen nazvy funkci
#           postav_kostku(-100,-100,50), postav_kostku(-100,100,50), ...
#   2. Mezitim Karel muze psat definice techto funkci a nemusi ho zajimat, jak je Franta presne bude pouzivat
#   Vysledek: hezky rozdelena prace -> rychleji hotovy kod

# Nasledujici kod nema funkce a neda se rozdelit pro Frantu a Karla
turtle.teleport(-100,-100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.left(90)
turtle.forward(50)
turtle.right(30)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)

turtle.teleport(100,-100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.left(90)
turtle.forward(25)
turtle.right(30)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)

turtle.teleport(100,100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(75)
    turtle.left(90)
turtle.left(90)
turtle.forward(75)
turtle.right(30)
turtle.forward(75)
turtle.right(120)
turtle.forward(75)

turtle.teleport(-100,100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.left(90)
turtle.forward(100)
turtle.right(30)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

# Lepsi kod, kde Karel napise definici toho, jak se stavi kostka a Karel je rozestavi

# Pise Karel - ten vymysli, jak se stavi domy
def postav_domecek(x,y,velikost):
    turtle.teleport(x,y)
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(velikost)
        turtle.left(90)
    turtle.left(90)
    turtle.forward(velikost)
    turtle.right(30)
    turtle.forward(velikost)
    turtle.right(120)
    turtle.forward(velikost)

# Pise Franta - ten vymysli, kam se postavi domy
postav_domecek(-100,-100,50)
postav_domecek(100,-100,25)
postav_domecek(100,100,75)
postav_domecek(-100,100,100)

# (2) Dalsi vyhodou je citelnost kodu, pokud se koukneme na kod Karla a Franty, tak vime co dela
# (3) Posledni vyhodou je to, ze kdyby se najednou klient rozhodl
#     ze chce ty vsechny domy postavit vetsi o 50 dilku, tak staci jen Frantovi upravit 4 udaje
turtle.mainloop()