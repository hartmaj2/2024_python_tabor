# Co se stane po spusteni kodu kdyz mi padne na zacatku 5? Co kdyz 1?

import random

nahodne = random.randint(1,6)
print("Nahodne cislo:",nahodne)

if nahodne != 6:
    random = random.randint(1,6)
    nahodne = random.randint(1,6)

print("Nahodne:",nahodne)