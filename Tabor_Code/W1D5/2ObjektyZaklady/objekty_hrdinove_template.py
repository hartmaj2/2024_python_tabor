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
# napriklad: 
# aragorn ma 100 zivotu a 0 killu
# legolas ma 90 zivotu a 0 killu
# gimli ma 110 zivotu a 0 killu
def vypis_hrdiny():
    for i in range(3):
        ...

# TODO: Napis funkci, ktera provede utok jedne vlny skretu
#   1. kazdy hrdina zabije nahodny pocet skretu
#   2. kazdy hrdina dostane nahodny damage
#   nezapomen vypisovat, co se deje jakemu hrdinovi

def zautoc_na_hrdiny():
    ...

# TODO: Opakuj 4 vlny skretu, po kazde vlne vypis, jak si hrdinove vedou
# Po kazde vlne cekej, dokud uzivatel nezada enter pomoci input()
# pouzij svoje hezke funkce


# TODO: Napis funkci, ktera vrati true pokud nejaky hrdina je mrtvy
def umrel_nekdo():
    ...

# TODO: Opakuj vlny skretu, dokud neumre nejaky hrdina


### TED OBJEKTOVE JAKO FRAJERI 8-)

# Tento kod udava jakysi planek, ,ktery rika, ze hrdina se vyrabi zadanim jmena a pocatecniho zdravi
# co je parametr self?
# proc se ta metoda jmenuje tak divne?
# (mozna ukazat v Thonny)
class Hrdina:
    def __init__(self,jmeno_input,pocatecni_zdravy):
        self.jmeno = jmeno_input
        self.zdravi = pocatecni_zdravy
        self.kills = 0
    
hrdinove = [Hrdina("aragorn",100),Hrdina("legolas",90),Hrdina("gimli",110)]

# TODO: Prepis ukoly zezhora na objektovou verzi
def vypis_hrdiny2():
    ...
        
def zautoc_na_hrdiny2():
    ...

def umrel_nekdo2():
    ...



# Jake jsou nevyhody a vyhody tech pristupu vyse?
#   - nekdo muze ty seznamy rozhazet
#   - muzeme si splest, co k cemu ma patrit (treba by jsme meli seznam se zivoty skretu)
#   - nevyhoda trid je, ze to chce vice se nad tim zamyslet (nekdy kvuli uspore casu je lepsi je netvorit)
#   - cim vetsi kod, tim je ale nutnejsi si ho hezky delit na tridy