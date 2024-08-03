import os
import random

sila = 0
inteligence = 0
volba = "0"
jmeno = ""


def vytiskni_hrdinu():
  print("------------------")
  print(jmeno)
  print("------------------")
  print(f"Síla: {sila}")
  print(f"Inteligence: {inteligence}")


def vytiskni_volby():
  print("------------------")
  print(f"Co si přeješ, aby {jmeno} šel provádět? ")
  print("1 - Jít mlátit skřety do zapovězených bažin")
  print("2 - Jít do knihovny studovat staré knihy o magii")
  print("3 - Jít do hospody")
  print("4 - Konec")


def nacti_jmeno():
  global jmeno
  print("Vítej v trenažéru hrdiny")
  jmeno = input("Jak chceš, aby se tvůj hrdina jmenoval? ")
  print(jmeno + "... to je hezké jméno.")


def vyhodnot_moznosti():
  global sila, inteligence
  if volba == "1":
    skretu = random.randint(1, 5)
    sila += skretu
    print(jmeno + f" umlátil {skretu} skřetů.")

  if volba == "2":
    inteligence += 5
    print(jmeno + " objevil tajný svitek plný magických run.")

  if volba == "3":
    inteligence -= 5
    print(jmeno + " se opil a odumřelo mu 11 mozkových buněk")


nacti_jmeno()
input("Stiskni enter pro pokračování... ")

while volba != "4":
  os.system("clear")
  vytiskni_hrdinu()
  vytiskni_volby()

  volba = input("Zadej volbu: ")
  print()
  vyhodnot_moznosti()
  input("Stiskni enter pro pokračování... ")

print("Nashledanou")
