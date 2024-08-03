# Co se stane po spusteni nasledujiciho kodu?
# Je mozne vytisknout prvni_hlaska a druha_hlaska?
# Co se stane kdyz jako prvni zadam Dobre.

odpoved = input("Ted zadej neco jen tak: ")

while odpoved != "Dobre":
    prvni_hlaska = "Hola hej!"
    druha_hlaska = "Jak se mas?"
    odpoved = input(prvni_hlaska + " " + druha_hlaska + " ")
    if odpoved == "Dobre":
        print("Tak to mam radost")
    else:
        print("Spatna odpoved")
    
print(prvni_hlaska)
print(druha_hlaska)
print(odpoved)