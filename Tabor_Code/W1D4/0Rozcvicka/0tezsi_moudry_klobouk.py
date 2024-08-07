# V tomto programu budes simulovat moudry klobouk z harryho pottera, ktery musi rozradit
# vsechny prvaky ze seznamu do odpovidajicich koleji dle jejich vlastnosti

# zde mas seznam studentu
students = ["Harry Potter","Hermione Granger","Ron Weasley","Draco Malfoy","Neville Longbottom","Luna Lovegood","Cedric Diggory","Cho Chang","Padma Patil","Pansy Parkinson"]

# zde mas postupne seznam jejich vlastnosti
traits = ["bravery","bravery","courage","competitiveness","courage","creativity","kindness","creativity","curiousness","ambition"]

# zde mas pro kazdou kolej seznam vlastnosti, diky kterym te do nich moudry klobouk zaradi
gryffindoor_traits = ["bravery","courage"]
slytherin_traits = ["ambition","competitiveness"]
hufflepuff_traits = ["kindness","friendliness","patience"]
ravenclaw_traits = ["couriousness","creativity"]

# budes potrebovat umet udelat kontrolu, zda je prvek v seznamu, to uz jsme delali ale jde to jednim prikazem
if "bravery" in gryffindoor_traits:
    print("The trait bravery is in gryffindoor traits")
if "bravery" in slytherin_traits:
    print("The trait bravery is in slytherin traits")

# tady jsou seznamy, kam bude treba studenty rozradit
gryffindoor = []
slytherin = []
hufflepuff = []
ravenclaw = []

# pouzij tedy prikazy podobne tem ukazkam vyse k splneni toho ukolu

# TODO: zkus nejprve zda ti to funguje aspon na samotnem prvnim studentovi

# TODO: ted pouzij for cyklus k rozrazeni vsech studentu (nejlepe for i in range s delkou seznamu)