import pepa

# Pise Karel - jak se stavi domy spojenim kostky a pyramidy
def postav_domecek(x,y,velikost):
    pepa.postav_kostku(x,y,velikost)
    pepa.postav_pyramidu(x,y+velikost,velikost)