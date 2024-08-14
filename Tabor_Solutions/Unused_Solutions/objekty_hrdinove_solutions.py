# Objekty jsou v dnesnim svete programovani to nejdulezitejsi.
# K cemu nam jsou? 
# Tridy jsou jako planek, podle ktereho muzeme stavet jednotlive objekty.
# Trida NPC napriklad rika, ze kazdy NPC ma jmeno, zdravi a utok
# Trida Hrac pak muze 

import random
#   1. abychom nemeli tunu promennuych rozhazenych po programu, souvisle celky maji spolecny kod
#   - ktery neni videt odjinud, takze neprekazi
#   2. abychom mohli pracovat na ruznych nezavislych castech programu zvlast
#       - nekdo napise kod, co s objektem chce delat (jako mi piseme co cheme po zelve)
#       - nekdo jiny pak uplne v jinem zdrojaku muze psat kod o tom, jak to ta zelva provadi


jmena = ["aragorn","legolas","gimli"]
zivoty = [100,90,110]
kills = [0,0,0]

# TODO: Rozcvicka, vypis vsechny postavy a jejich odpovidajici hodnoty
def vypis_hrdiny():
    print("Jak si vedou nasi hrdinove: ")
    for i in range(len(jmena)):
        print(f"{jmena[i]} ma {zivoty[i]} zivotu a zabil {kills[i]} skretu")

# TODO: Napis funkci, ktera provede utok jedne vlny skretu
#   1. kazdy hrdina zabije nahodny pocet skretu
#   2. kazdy hrdina dostane nahodny damage
#   nezapomen vypisovat, co se deje jakemu hrdinovi

def zautoc_na_hrdiny():
    for i in range(len(jmena)):
        damage = random.randint(0,50)
        zabitych_skretu = random.randint(0,5)
        zivoty[i] = zivoty[i] - damage
        kills[i] = kills[i] + zabitych_skretu
        print(f"{jmena[i]} utrpel {damage} poskozeni a zabil {zabitych_skretu} skretu")

# TODO: Opakuj 4 vlny skretu, po kazde vlne vypis, jak si hrdinove vedou
# Po kazde vlne cekej, dokud uzivatel nezada enter pomoci input()

# vypis_hrdiny()
# input()
# for i in range(4):
#     zautoc_na_hrdiny()
#     input()
#     vypis_hrdiny()
#     input()

# TODO: Napis funkci, ktera vrati true pokud nejaky hrdina je mrtvy
def umrel_nekdo():
    nekdo_umrel = False
    for hp in zivoty:
        if hp <= 0:
            nekdo_umrel = True
    return nekdo_umrel

# TODO: Opakuj vlny skretu, dokud neumre nejaky hrdina

# vypis_hrdiny()
# input()
# while not umrel_nekdo():
#     zautoc_na_hrdiny()
#     input()
#     vypis_hrdiny()
#     input()


# Pro takoveto ukoly by se ale lepe hodily objekty. Muzete sami zhodnotit, zda vam ten
# kod bude pripadat lepsi

class Hrdina:

    def __init__(self,jmeno_input,pocatecni_zdravy):
        self.jmeno = jmeno_input
        self.zdravi = pocatecni_zdravy
        self.kills = 0
    
hrdinove = [Hrdina("aragorn",100),Hrdina("legolas",90),Hrdina("gimli",110)]

# TODO: Prepis ukoly zezhora na objektovou verzi
def vypis_hrdiny2():
    print("Jak si vedou nasi hrdinove: ")
    for hrdina in hrdinove:
            print(f"{hrdina.jmeno} ma {hrdina.zdravi} zivotu a zabil {hrdina.kills} skretu") 
        
def zautoc_na_hrdiny2():
    for hrdina in hrdinove:
        damage = random.randint(0,50)
        zabitych_skretu = random.randint(0,5)
        hrdina.zdravi -= damage
        hrdina.kills += zabitych_skretu
        print(f"{hrdina.jmeno} utrpel {damage} poskozeni a zabil {zabitych_skretu} skretu")

def umrel_nekdo2():
    nekdo_umrel = False
    for hrdina in hrdinove:
        if hrdina.zdravi <= 0:
            nekdo_umrel = True
    return nekdo_umrel

vypis_hrdiny2()
input()
while not umrel_nekdo2():
    zautoc_na_hrdiny2()
    input()
    vypis_hrdiny2()
    input()

# Jake jsou nevyhody a vyhody tech pristupu vyse?
#   - nekdo muze ty seznamy rozhazet
#   - muzeme si splest, co k cemu ma patrit (treba by jsme meli seznam se zivoty skretu)
#   - nevyhoda trid je, ze to chce vice se nad tim zamyslet (nekdy kvuli uspore casu je lepsi je netvorit)
#   - cim vetsi kod, tim je ale nutnejsi si ho hezky delit na tridy