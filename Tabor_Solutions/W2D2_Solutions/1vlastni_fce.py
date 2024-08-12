# V jedne vesnici v Madarsku maji zajimavy system na pocitani
# dani. Napiseme funkci, ktera dan spocita. Rovnice pro vypocet je:
# pocet_pismenek_v_krestnim_jmene * vek_v_rocich - vaha_na_mesici_v_kg

# Uz mas k dispozici funkci, ktera pro zadanou vahu na zemi vrati 
# vahu na mesici.

def vaha_na_mesici(vaha):
    return (vaha / 9.81) * 1.66

mesic1 = vaha_na_mesici(78)
mesic2 = vaha_na_mesici(50)

print(mesic1)
print(mesic2)

# TODO: Napis definici funkce madarska_dan(jmeno,vek,vaha)
# HINT: Vypoctenou hodnotu vrat pomoci prikazu return

def madarska_dan(jmeno,vek,vaha):
    return len(jmeno) * vek - vaha_na_mesici(vaha)

# TODO: vypis, kolik forintu na dani zaplati: 
# Franta, kteremu je 59 let a vazi 80 kg
# Jan, 18 let, 100 kg
# Maximilian, 75 let, 65 kg
print(madarska_dan("Franta",30,80))
print(madarska_dan("Jan",18,100))
print(madarska_dan("Maximilian",75,65))

# TODO: Definuj funkci muzu_na_pivo(vek,zeme), ktera
# ti pro zadany vek a zemi rekne, zda tam muzes na pivo
# naprogramuj, aby fungovala aspon pro tri ruzne zeme

def muzu_na_pivo(vek,zeme):
    if vek >= 21:
        return True
    if vek >= 20 and zeme != "usa":
        return True
    if vek >= 18 and zeme not in ["japonsko","thajsko","island","usa"]:
        return True
    if vek >= 16 and zeme in ["nemecko","belgie"]:
        return True
    return False

