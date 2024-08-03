def vypis_hurra():
    print("Hurraaaa")

# Spustit kod, co se stane?

def pozdrav(jmeno):
    print("Ahoj " + jmeno)

def damage(attack,defense):
    damage = attack - defense
    if damage < 0: 
        damage = 0
    return damage

def damage2(attack,defense):
    damage = attack - defense
    if damage < 0: 
        damage = 0
    
hp = 100
hp = hp - damage(10,20)
hp = hp - damage2(10,20)