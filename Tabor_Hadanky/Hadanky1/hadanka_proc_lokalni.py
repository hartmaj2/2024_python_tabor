
# tady neco budu pocitat
a = 10
b = 14
mezivysledek = a + b

def zeptej_se_zdvorile_a_uprav():
    mezivysledek = input("Mily pane, napiste mi sem cislo: ")
    return int(mezivysledek) + 10

vysledek = mezivysledek + zeptej_se_zdvorile_a_uprav() 

print(mezivysledek)
print(vysledek)

# Proc python takto funguje?