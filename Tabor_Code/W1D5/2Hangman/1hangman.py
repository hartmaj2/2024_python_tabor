# Postupne si naprogramujes hangmana. K tomu te navedou nasledujici ukoly.

# TODO: Predstav si, ze tajne 

# TODO: Predstav si. Ze tajne slovo je "aligator" a ze uzivatel 
# dava prvni odhad pismeno "a". Vytvor retezec "a _ _ _ a _ _ "
tajne = "aligator"
odhad = "a"

# TODO: Napis funkci, ktera zjisti, zda je pismenko b ve slove
slovo1 = "aligator"

def pismenko_b_ve_slove1():
    global slovo1
    ...
    # return True / return False 

if pismenko_b_ve_slove1() == True:
    print("Pismenko b je ve slove1")

# TODO: Napis funkci, ktera zjisti, zda zadane pismenko je v zadanem slove
def pismeno_ve_slove(pismeno,slovo):
    ...

if pismeno_ve_slove("t","platidlo") == True:
    print("Tva funkce asi funguje!")

if not pismeno_ve_slove("t","pernicek"):
    print("Tva funkce asi funguje")

# TODO: Dale uz nestihnu pripravit podukoly, ale tady mas pseudokot, ktery ti snad pomuze

### PSEUDOCODE ###
# 0. Privitej hrace
# 1  Vyber nahodne slovo  
# 2. Opakuj, dokud neni pocet chyb vetsi nez maximalni povoleny:
# 3.        Vytiskni stav sibenice
# 4.        Vytiskni aktualni stav slova
# 5.        Nech hrace zadat pismenko
# 6.        Pokud je pismenko ve slove:
# 7.            Uprav aktualni stav slova
# 8.        Jinak:
# 9.            Zvys aktualni pocet chyb 
# 10.       Pokud pocet chyb > max_povoleny:
# 11.           break
# 12. Pokud aktualni stav slova neobsahuje neuhadnute znaky:
# 13.       Vytiskni "Vyhral jsi"
# 14s. Jinak:
# 15.       Vytiskni "Prohral jsi"

# HINT: Nech ChatGPT vygenerovat ten seznam slov, ze kterych budes vybirat
# HINT: Nech si take vygenerovat seznam, ktery ti umozni podle poctu chyb vytisknout spravny "obrazek" sibenice
# HINT: Aktualni stav slova vypada napr "a__ga___"
# HINT: jestli je letter in word muzes zkontrolovat pomoci
# if letter in word:
#       udelej neco

# HINT: pokud hrac uhadl znak tak vytvor novy aktualni stav tim, ze
# postupne pojedes pres vsechny znaky a 
#   pokud se znak rovna tomu hadanemu, tak ho pridej do noveho aktualniho stavu
#   jinak pouzij pismeno ze stareho aktualniho stavu