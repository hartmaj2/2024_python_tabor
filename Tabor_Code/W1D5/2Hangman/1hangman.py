import random

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

### SOLUTION
mistakes = 0
tajne = random.choice(HANGMAN_WORDS)
stav = len(tajne) * "_"
while True:
    print(HANGMAN_PICS[mistakes])
    print(stav)
    odhad = input("Jake pismeno chces hadat? ")
    if odhad in tajne:
        print("Trefil jsi se")
        novy = ""
        for i in range(len(tajne)):
            if odhad == tajne[i]:
                novy = novy + odhad
            else:
                novy = novy + stav[i]
        stav = novy
    else:
        print("Spatne")
        mistakes = mistakes + 1
        if MAX_MISTAKES == mistakes:
            break
    if not "_" in stav:
        print("Vyhral jsi")
        break

### END OF SOLUTION  

# TODO: Dokazat ziskat pocatecni stav pro nejake slovo
tajne_slovo = "aligator"
# chceme: _ _ _ _ _ _ _ _

# TODO: Ziskat novy stav pro pocatecni stav _ _ _ _ _ _ _
tajne_slovo = "babovka"
pocatecni_stav = "_______"
odhad = "a"
# cheme: _ a _ _ _ _ a

# TODO: Ziskat novy stav pokud stav byl _ a _ _ _ _ a
tajne_slovo = "babovka"
stav = "_a____a"
odhad = "b"
# chceme: b a b _ _ _ a


# TODO: To co jsme doposud vytvorili cele vlozit do while cyklu
#   (a) jake promenne se budou menit a jake budou zustavat stejne?
#   (b) odhad si nechat nacist od uzivatele
#   (c) vzdy si spocitat/vytvorit novy stav a ten potom nahrat do promenne stav


# TODO: Pridat pocet chyb a podle nich kdyztak skoncit cyklus 

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
