import random
import os

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

HANGMAN_WORDS = [
    "python",
    "javascript",
    "hangman",
    "development",
    "algorithm",
    "function",
    "variable",
    "keyboard",
    "condition",
    "iteration"
]

MAX_MISTAKES = 5

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

def vyrob_pocatecni_stav():
    global tajne_slovo
    return len(tajne_slovo) * "_"

def vytiskni_aktualni_stav_slova():
    global aktualni_stav
    for pismeno in aktualni_stav:
        print(pismeno + " ",end="")
    print()

def vytiskni_hangmana():
    global mistakes
    print(HANGMAN_PICS[mistakes])

def vyrob_novy_stav(odhad):
    global tajne_slovo, aktualni_stav
    novy_stav = ""
    for i in range(len(aktualni_stav)):
        if tajne_slovo[i] == odhad:
            novy_stav += odhad
        else:
            novy_stav += aktualni_stav[i]
    return novy_stav

def je_konec():
    global aktualni_stav, mistakes
    if mistakes > MAX_MISTAKES:
        return True
    elif "_" not in aktualni_stav:
        return True
    else:
        return False

def vyhral_jsi():
    global aktualni_stav
    return "_" not in aktualni_stav

print("Vitej ve hre HANGMAN")
mistakes = 0
tajne_slovo = random.choice(HANGMAN_WORDS)
aktualni_stav = vyrob_pocatecni_stav()
input("Stiskni enter pro pokracovani... ")
os.system("clear")
while True:
    vytiskni_hangmana()
    vytiskni_aktualni_stav_slova()
    odhad = input("Hadej pismeno: ")
    os.system("clear")
    if odhad in tajne_slovo:
        print("Spravne!")
        aktualni_stav = vyrob_novy_stav(odhad)
    else:
        print("Spatne!")
        mistakes += 1
    if je_konec():
        break

vytiskni_hangmana()
if vyhral_jsi():
    print("Vyhral jsi")
else:
    print("Prohral jsi")