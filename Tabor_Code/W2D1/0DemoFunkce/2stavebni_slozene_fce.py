import turtle
turtle.speed(5)

# Je z tohoto kodu lepe videt, co dela?

# A kdyz uz clovek pise funkce, muze se stat, ze si vsimneme, ze uvnitr jedne funkce se nam 
# muze hodit jeste jina funkce. Z funkci pak jako z kosticek lega muzeme postavit
# slozitejsi funkce, ktere pak zase muzeme poskladat do jeste slozitejsich.

# Nyni uz si muzou praci rozdelit tri lidi Franta, Karel a Pepa

# Pise Pepa - ten vymysli, jak se stavi pyramida a kostka
def postav_kostku(x,y,velikost):
    turtle.teleport(x,y)
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(velikost)
        turtle.left(90)

def postav_pyramidu(x,y,velikost):
    turtle.teleport(x,y)
    turtle.setheading(0)
    for i in range(3):
        turtle.forward(velikost)
        turtle.left(120)
    

# Pise Karel - jak se stavi domy spojenim kostky a pyramidy
def postav_domecek(x,y,velikost):
    postav_kostku(x,y,velikost)
    postav_pyramidu(x,y+velikost,velikost)

# Pise Franta - kam se postavi domy
postav_domecek(-100,-100,50)
postav_domecek(100,-100,25)
postav_domecek(100,100,75)
postav_domecek(-100,100,100)

# (2) Dalsi vyhodou je citelnost kodu, pokud se koukneme na kod Karla a Franty, tak vime co dela
# (3) Posledni vyhodou je to, ze kdyby se najednou klient rozhodl
#     ze chce ty vsechny domy postavit vetsi o 50 dilku, tak staci jen Frantovi upravit 4 udaje
turtle.mainloop()