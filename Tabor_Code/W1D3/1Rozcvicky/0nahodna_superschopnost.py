import random

superschopnosti = ["telekinetického smažení palačinek", "vystřelujících lízátek", "hypnotizujících tanečních pohybů", "dokonalé přípravy sendvičů", "neomezených tátovských vtipů", "okamžitého stavění polštářových pevností"]

superneschopnosti = ["lechtivé nohy", "strach z balónků", "nezvladatelný smích", "závislost na videích s koťátkami", "trvalou opilost", "zaražené prdy"]

hero_name_start = ["Kapitán", "Profesor", "Velký", "Sir", "Dáma", "Doktor"]

hero_name_middle = ["Vašek","David","Oliver","Sam","Ami","Alča","Ráďa","Ševa"]

hero_name_ending = ["Chechtal", "Bourák", "Bombarďák", "Kazisvět", "Mrakoplaš", "Rakeťák","Drsoň"]

# TODO 1: Vytiskni všechny seznamy, aby ses seznamil/a s jejich obsahy


# TODO 2: Vyber náhodnou super sílu a vytiskni ji
# HINT: pouzij len abys zjistil/a pocet prvku a pak si vygeneruj cislo od 0 do posledniho mozneho indexu (ten souvisi s len, tedy s delkou seznamu)
# HINT2: to si uloz do promenne a pote pomoci te hodnoty indexuj seznam, tim vyberes nahodny prvek

# TODO 3: Vyber náhodnou super slabost a vytiskni ji

# TODO 4: Vyber náhodný začátek a konec jména hrdiny, vytvor celé jméno hrdiny a vytiskni jej
...
random_hero_name = random_hero_name_start + " " + random_hero_name_middle + " " + random_hero_name_ending
print("Náhodné jméno hrdiny:", random_hero_name)

# TODO 5: Kombinujte náhodnou super sílu, super slabost a jméno hrdiny, vytvořte vtipný popis a vytiskněte jej
print(f"Objevil se nový superhrdina {random_hero_name}, který má schopnost {random_superpower}, ale je zranitelný, jelikož má {random_superweakness}!")

# BONUS TODO: Změn program tak, aby holky byly vždy Kapitánka,Profesorka atd.
# a kluci byly jako do teď (ale ne Dáma)
# HINT: budes muset pridat dalsi seznam ktery bude udavat, jake jmeno je holcici a jake klucici