import os
import random

sila = 0
inteligence = 0
penize = 0
volba = "0"
jmeno = ""


def vytiskni_hrdinu():
  print_line()
  print(jmeno)
  print_line()
  print(f"Síla: {sila}")
  print(f"Inteligence: {inteligence}")
  print(f"Penize: {penize}")

def clear_screen():
  os.system("clear")

def print_line():
  print("--------------------------------")

def ziskej_volbu_uzivatele():
  global volba
  vytiskni_volby()
  volba = input("Zadej volbu: ")

def vytiskni_volby():
  print_line()
  print(f"Co si přeješ, aby {jmeno} šel provádět? ")
  print("(1) Jít mlátit skřety do zapovězených bažin")
  print("(2) Jít do knihovny studovat staré knihy o magii")
  print("(3) Jít do hospody")
  print("(4) Konec")

def nacti_jmeno():
  global jmeno
  print("Vítej v trenažéru hrdiny")
  jmeno = input("Jak chceš, aby se tvůj hrdina jmenoval? ")
  print(jmeno + "... to je hezké jméno.")

def hospoda():
  global penize, inteligence, jmeno
  clear_screen()
  print("Chces hrat kostky nebo chlastat?")
  print("(1) Chlastat")
  print("(2) Kostky")
  volba = input("Zadej volbu: ")
  if volba == "1":
    odumreno = random.randint(5,10)
    inteligence -= odumreno
    print(jmeno + f" se opil a odumřelo mu {odumreno} mozkových buněk")
  else:
    kostky()

def mlaceni_skretu():
    global sila
    skretu = random.randint(5, 10)
    sila += skretu
    print(jmeno + f" umlátil {skretu} skřetů.")

def objeveni_svitku():
  global inteligence
  inteligence += 5
  print(jmeno + " objevil tajný svitek plný magických run.")

def kostky():
  global penize
  clear_screen()
  print("Dobre jdeme hrat kostky!")
  press_enter_to_continue()
  souper = random.randint(1,12)
  ja = random.randint(1,12)
  print_line()
  print("Souper:",souper)
  print(f"{jmeno}:",ja)
  print_line()
  if souper > ja:
    penize -= 10
    print("Prohral jsi 10 forintu!")
  if souper == ja:
    print("Remiza!")
  if souper < ja:
    penize += 10
    print("Vyhral jsi 10 forintu!")

def vyhodnot_moznosti():
  global sila, inteligence
  if volba == "1":
    mlaceni_skretu()

  if volba == "2":
    objeveni_svitku()

  if volba == "3":
    hospoda()

def press_enter_to_continue():
  input("Stiskni enter pro pokračování... ")

nacti_jmeno()
press_enter_to_continue()

while volba != "4":
  clear_screen()
  vytiskni_hrdinu()
  ziskej_volbu_uzivatele()
  print()
  vyhodnot_moznosti()
  press_enter_to_continue()

print("Nashledanou")
