import requests
import cv2

# TODO: Uloz si jmena do seznamu, at je muzes hezky projit jeden po druhem
jmena = ...

# TODO: Pro kazde jmeno proved http get request a uloz si ho

for jmeno in jmena:
    ...

# TODO: Postupne nacti vsechny obrazky, ktere sis prave ulozil a nahraj je do seznamu images
# pridani do seznamu provedes pomoci `images.append(...)`
images = []


# Sestav je do jednoho pomoci cv2.hconcat(...) ktere predas seznam obrazku
result = ...
cv2.imshow("result",result)
cv2.waitKey(0)