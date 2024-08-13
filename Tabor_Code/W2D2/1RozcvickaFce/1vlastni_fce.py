# V jedne vesnici v Madarsku maji zajimavy system na pocitani
# dani. Napiseme funkci, ktera dan spocita. Rovnice pro vypocet je:
# pocet_pismenek_v_krestnim_jmene * vek_v_rocich - vaha_na_mesici_v_kg

# Uz mas k dispozici funkci, ktera pro zadanou vahu na zemi vrati 
# vahu na mesici.

def vaha_na_mesici(vaha):
    return (vaha / 9.81) * 1.66

print(vaha_na_mesici(78))
print(vaha_na_mesici(50))

# TODO: Napis definici funkce madarska_dan(jmeno,vek,vaha)
# HINT: Vypoctenou hodnotu vrat pomoci prikazu return

# TODO: vypis, kolik forintu na dani zaplati: 
# Franta, kteremu je 59 let a vazi 80 kg
# Jan, 18 let, 100 kg
# Maximilian, 75 let, 65 kg


# TODO: Definuj funkci muzu_na_pivo(vek,zeme), ktera
# ti pro zadany vek a zemi rekne, zda tam muzes na pivo
# naprogramuj, aby fungovala aspon pro tri ruzne zeme
# HINT: ta funkce vrati True nebo False


# TODO: Zavolej funkci na hodnotach od uzivatele a podle
# vysledku funkce muzu_na_pivo(vek,zeme) mu vypis bud
# ze ma smulu nebo at klidne zajde na pivo, ale at se moc neozere
# vek = int(input("Zadej svuj vek: "))
# zeme = input("Zadej svou zemi: ")
