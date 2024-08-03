import os
# Muzes udelat rovnou posledni todo, ale pokud je to pro tebe moc slozite, tak ti pomuze je delat postupne

# TODO: Napis program, ktery dokud uzivatel zadava cisla, tak je bere jako ceny produktu a scita je
# jakmile uzivatel zada -1, tak se zastavi a spocita celkovou sumu a vytiskne

# print("Tento program ti spocita celkovou cenu veci, ktere jsi nakoupil")

# suma = 0
# vstup = -1
# while vstup != 0:
#   vstup = float(input("Zadej kolik stala polozka: "))
#   suma = suma + vstup

# print(f"Celkem jsi nakoupil za {suma:3d} korun.")

# TODO: Stejne jako minule, ale predem zadame, kolik budeme chtit zadat cen 
# uzivatel je pak postupne zada a program mu vytiskne sumu

# print("Tento program ti spocita celkovou cenu veci, ktere jsi nakoupil")

# suma = 0
# pocet = int(input("Kolik chces zadat polozek: "))
# for i in range(pocet):
#   vstup = float(input("Zadej kolik stala polozka: "))
#   suma = suma + vstup

# print(f"Celkem jsi nakoupil za {suma:.2f} korun.")

# TODO: Zepta se uzivatele, kolik chce zadat polozek. Uzivatel vzdy zada jmeno a cenu

# Program pote vytiskne:

# polozka1 cena1
# polozka2 cena2
# ...
# polozkaX cenaX
# --------------
# celkem: soucet

suma = 0
jmena = []
ceny = []
pocet = int(input("Kolik chces zadat polozek: "))
for i in range(pocet):
  os.system("clear")
  jmeno = input("Zadej jmeno polozky: ")
  jmena.append(jmeno.strip())
  cena = float(input("Zadej cenu polozky: "))
  ceny.append(cena)
  suma = suma + cena

os.system("clear")
for i in range(pocet):
  print(jmena[i], ":", ceny[i])
print(15 * "-")
print("celkem:", suma)

# BONUS TODO: V USA pisou cenu bez dani a potom ti pridaji tu dan az na pokladne. 
# Uprav program, aby k celkove sume pricetl dan 4% a vytiskl, kolik mas zaplatit po pridani dane
