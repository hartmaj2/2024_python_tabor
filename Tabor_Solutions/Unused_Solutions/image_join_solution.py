import requests
import cv2

# TODO: Uloz si jmena do seznamu, at je muzes hezky projit jeden po druhem
jmena = ["Gc616mGbgI","Hs56N981uA","ALdCEgaVnM","90VIBfxVhv","pjjdX8SpuY"]

# TODO: Pro kazde jmeno proved http get request a uloz si ho
index = 0
for jmeno in jmena:
    request = requests.get(f"https://www.ms.mff.cuni.cz/~hartmaj2/{jmeno}.jpg")
    file = open(f"image{index}.jpg","wb")
    file.write(request.content)
    file.close()
    index += 1

# TODO: Postupne nacti vsechny obrazky, ktere sis prave ulozil a nahraj je do seznamu
images = []
for i in range(5):
    img = cv2.imread(f"image{i}.jpg")
    images.append(img)

# Sestav je do jednoho pomoci cv2.hconcat(...) ktere predas seznam obrazku
result = cv2.hconcat(images)
cv2.imshow("result",result)
cv2.waitKey(0)