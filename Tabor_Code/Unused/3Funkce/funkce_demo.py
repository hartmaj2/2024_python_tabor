# Zkus si nasledujici kody spustit v debuggeru s breakpointem (cervenou teckou)
# na prikazu print("Zacatek"). Hodne ti to pomuze v pochopeni funkci.
print("Zacatek")

# Funkce, ktera zastavi program, dokud uzivatel nestiskne enter
def press_enter_to_continue():
    input("Press enter to continue... ")

press_enter_to_continue()

# Funkce, ktera pozdravi hrace se zadanym jmenem.
# Promenna jmeno je v tomto pripade parametr. 
# Parametr funguje jako nova promenna, kterou maz k dispozici uvnitr definice funkce ale nikde jinde
def pozdrav_hrace(jmeno):
    print("Vitej ve hre, " + jmeno + "!")

pozdrav_hrace("Franta")
press_enter_to_continue()

# Funkce, ktera vzdy vrati jako vysledek sveho vypoctu 42, ale potrebuje
# abys stiskl/a enter pro pokracovani vypoctu. 

# Vysledek vratime pomoci slova return a za nim napiseme co chceme vratit
def odpoved_na_otazku_vseho():
    print("Hmmm... premyslim nad odpovedi.")
    input("Stiskni enter pro pokracovani vypoctu...")
    print("Uz to mam!")
    return 42

# Vysledek, ktery vrati funkce muzes kontrolovat
if odpoved_na_otazku_vseho() == 42:
    print("To je spravna odpoved")

press_enter_to_continue()
# Nebo si ho ulozit do promennes
odpoved = odpoved_na_otazku_vseho()

# Funkce muze mit vice parametru a zaroven neco vratit
# Vsimni si, ze ten vypocet je komplikovany a to je dobry duvod, proc ho schovat do funkce
# Kdykoliv pak chces spocitat ten damage, tak nemusis tu slozitou formulku opisovat
def spocitej_damage(defense_obrance,attack_utocnika):
    damage = ((attack_utocnika + 10) * 1.5 - defense_obrance * 0.5) / 2
    return damage

skret_attack = 10
hero_defense = 10
hero_health = 10
print("Skret utoci")
press_enter_to_continue()
hero_health = hero_health - spocitej_damage(hero_defense,skret_attack)
print("Hrdina utpel",spocitej_damage(hero_defense,skret_attack),"damage!")

print("Konec")
