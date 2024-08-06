import random

# Seznamy se zábavnými a poutavými položkami
superpowers = [
    "vystřelující lízátka", 
    "telekinetického smažení palačinek", 
    "hypnotizující tanečních pohybů", 
    "dokonalé přípravy sendvičů", 
    "neomezených tátovských vtipů", 
    "okamžitého stavění polštářových pevností"
]

superweaknesses = [
    "lechtivé nohy", 
    "strach z balónků", 
    "nezvladatelný smích", 
    "závislost na videích s koťátkami", 
    "trvalou opilost", 
    "zaražené prdy"
]

hero_name_start = [
    "Kapitán", 
    "Profesor", 
    "Velký", 
    "Sir", 
    "Dáma", 
    "Doktor"
]

hero_name_middle = ["Vašek","David","Oliver","Sam","Ami","Alča","Ráďa","Ševa"]

hero_name_ending = [
    "Chechtal", 
    "Bourák", 
    "Bombarďák", 
    "Kazisvět", 
    "Mrakoplaš", 
    "Vrtichvost"
]

# TODO 1: Vytiskněte všechny seznamy, abyste se seznámili s položkami
print("Super síly:", superpowers)
print("Super slabosti:", superweaknesses)
print("Začátky jmen hrdinů:", hero_name_start)
print("Konce jmen hrdinů:", hero_name_ending)

# TODO 2: Vyberte náhodnou super sílu a vytiskněte ji
random_superpower = random.choice(superpowers)
print("Náhodná super síla:", random_superpower)

# TODO 3: Vyberte náhodnou super slabost a vytiskněte ji
random_superweakness = random.choice(superweaknesses)
print("Náhodná super slabost:", random_superweakness)

# TODO 4: Vyberte náhodný začátek a konec jména hrdiny, vytvořte celé jméno hrdiny a vytiskněte jej
random_hero_name_start = random.choice(hero_name_start)
random_hero_name_ending = random.choice(hero_name_ending)
random_hero_name_middle = random.choice(hero_name_middle)
random_hero_name = random_hero_name_start + " "+ random_hero_name_middle + " " + random_hero_name_ending
print("Náhodné jméno hrdiny:", random_hero_name)

# TODO 5: Kombinujte náhodnou super sílu, super slabost a jméno hrdiny, vytvořte vtipný popis a vytiskněte jej
print(f"Objevil se nový superhrdina {random_hero_name}, který má schopnost {random_superpower}, ale je zranitelný, jelikož má {random_superweakness}!")

# BONUS TODO: Změn program tak, aby holky byly vždy Kapitánka,Profesorka atd.
# a kluci byly jako do teď (ale ne Dáma)
# HINT: budes muset pridat dalsi seznam ktery bude udavat, jake jmeno je holcici a jake klucici