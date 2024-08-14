# V jedne RPG hre si ukladame data o vsech hracich hezky do radku, ale to neni moc citelne.
# Chteli bychom hracum jejich profily vypsat hezky do kazdeho souboru zvlast

# V souboru profiles.txt mas ulozene informace o hracich. Na kazdem radku
# je informace o jednom hraci. Jednotlive polozky jsou oddelene carkou.
# V hracove inventari jsou predmety oddelene strednikem

# TODO: Tvym ukolem bude pro kazdeho hrace vyrobit soubor a do nej vypsat:

# Nickname: mandalore195
# Class: Warrior
# Level: 20

# Stats:
# Health Points (HP): 150
# Mana Points (MP): 30

# Loadout:
# - Sword of Valor
# - Shield of Eternity
# - Iron Armor

# ---------------------------
# End of Loadout File

# TODO: prvni zkus soubor "profiles.txt" otevrit a precist vsechny radky
# HINT: pouzij prikaz open(filename,mode)     (mode je zpusob, kterym chces soubor otevrit, treba pro cteni,zapis atd.)
# HINT: https://www.w3schools.com/python/ref_func_open.asp

# TENTO EXAMPLE PROJET V THONNY
# file = open("Tabor_Code/W2D3/2Soubory/profiles.txt","r")
# nactene = ""
# for i in range(4):
#     nactene = file.readline()
#     print(nactene,end="")
# file.close()


# TODO: zkus kazdy radek ze vstupniho souboru prepsat do jeho vlastniho vystupniho souboru
# file = open("profiles.txt","r")
# file = open("Tabor_Code/W2D3/2Soubory/profiles.txt","r")
# nactene = ""
# for i in range(4):
#     nactene = file.readline()
#     nazev_souboru = "vystupni" + str(i) + ".txt"
#     output_file = open(nazev_souboru,"w")
#     output_file.write(nactene)
#     output_file.close()
#     i += 1


# TODO: nyni funkci split(oddelovac) kazdy radek rozsekej na slova 
# jednotliva slova pak do vystupnich souboru pis kazde na vlastni radek
# HINT: oddelovac bude ","
# file = open("Tabor_Code/W2D3/2Soubory/profiles.txt","r")
# nactene = ""
# for i in range(4):
#     nactene = file.readline()
#     slova = nactene.split(",")
#     nazev_souboru = "vystupni" + str(i) + ".txt"
#     output_file = open(nazev_souboru,"w")
#     for slovo in slova:
#         output_file.write(slovo + "\n")
#     output_file.close()
#     i += 1


# TODO: zbytek uz neni tezky, staci jen na spravna mista psat vhodne
# veci jako Nickname:, Class: atd. 
# a pak na konec souboru napsat ukoncovaci hlasku
file = open("Tabor_Code/W2D3/2Soubory/profiles.txt","r")
nactene = ""
file.readline()
for i in range(3):
    nactene = file.readline()
    slova = nactene.split(",")
    print(slova)
    nazev_souboru = "vystupni" + str(i) + ".txt"
    output_file = open(nazev_souboru,"w")
    output_file.write("Nickname: " + slova[0] + "\n")
    output_file.write("Class: " + slova[1] + "\n")
    output_file.write("Level: " + slova[2] + "\n")
    output_file.write("\n")
    output_file.write("Stats: \n")
    output_file.write("HP: " + slova[3] + "\n")
    output_file.write("MP: " + slova[4] + "\n")
    output_file.write("\n")
    output_file.write("Items: \n")
    output_file.write(slova[5] + "\n")
    output_file.close()
    i += 1

