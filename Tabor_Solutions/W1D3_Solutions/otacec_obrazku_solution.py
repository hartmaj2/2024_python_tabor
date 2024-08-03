import cv2

# ve slozce pootacene mame 10 obrazku, ktere chceme vsechny otocit zpet o 180 stupnu a zmenit na cernobile
# jmenuji se "image_1.jpg" az "image_10.jpg"

# TODO: vypis postupne relativni cesty, ktere budes muset navstivit

for i in range(1,10):
    path_start = "W1D3/Otoceni deseti obrazku/pootacene/image_"
    path_end = ".jpg"
    print(path_start + str(i) + path_end)

# TODO: napis funkci, ktera prijme adresu a otevre obrazek na 100ms 

def otevri_obrazek(cesta):
    image = cv2.imread(cesta)
    cv2.imshow(cesta,image)
    cv2.waitKey(1000)

# otevri_obrazek("W1D3/Otoceni deseti obrazku/pootacene/image_1.jpg")

# TODO: napis funkci, ktera prijme cislo obrazku a vrati potrebnou adresu

def vrat_adresu_dle_cisla(cislo):
    path_start = "W1D3/Otoceni deseti obrazku/pootacene/image_"
    path_end = ".jpg"
    return path_start + str(cislo) + path_end

# TODO: napis cyklus, kterym pooteviras vsechny obrazky
def vrat_otevreny_obrazek(cesta):
    return cv2.imread(cesta)

def uloz_obrazek(image,cislo):
    cv2.imwrite("results/image_" + str(cislo) + ".jpg",image)

for i in range(1,11):
    adresa = vrat_adresu_dle_cisla(i)
    image = vrat_otevreny_obrazek(adresa)
    image = cv2.rotate(image,cv2.ROTATE_180)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    uloz_obrazek(image,i)

# TODO: funkci, ktera ulozi objekt s obrazkem na spravnou adresu ( cv2.imwrite(cesta,obrazek) )






