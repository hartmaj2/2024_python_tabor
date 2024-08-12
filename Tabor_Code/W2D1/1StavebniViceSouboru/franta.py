import turtle
import karel

# Pise Franta - kam se postavi domy
karel.postav_domecek(-100,-100,50)
karel.postav_domecek(100,-100,25)
karel.postav_domecek(100,100,75)
karel.postav_domecek(-100,100,100)

# (2) Dalsi vyhodou je citelnost kodu, pokud se koukneme na kod Karla a Franty, tak vime co dela
# (3) Posledni vyhodou je to, ze kdyby se najednou klient rozhodl
#     ze chce ty vsechny domy postavit vetsi o 50 dilku, tak staci jen Frantovi upravit 4 udaje
turtle.mainloop()