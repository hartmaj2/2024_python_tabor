import cv2


# TODO: Nacti obrazek do promenne image
# Use cv2.imread() to read an image from file_path
image = cv2.imread("W1D3/ImgFuncitonsTest/image.jpg")

# TODO: Zobraz obrazek
#   a) dokud se nestiskne klavesa
#   b) presne jednu sekundu
# Use cv2.imshow() to display the image with window_name
# Use cv2.waitKey() to wait a certain amount of time
cv2.imshow("ahoj",image)
cv2.waitKey(0)

# TODO: preved obrazek na cernobily
# Use cv2.cvtColor() with cv2.COLOR_BGR2GRAY to convert the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("cernobily",gray_image)
cv2.waitKey(0)


# TODO: Rozmaz obrazek pomoci funkce gaussian blur
# Use cv2.GaussianBlur() with the given kernel_size  
# (kernel_size rika, kolik vedlejsich pixelu se pouzije k rozmazani a je to dvojice LICHYCH cisel)
# jaky je rozdil mezi kernel size (101,1) a (1,101)
# posledni parametr dej proste 0 (nevim co znamena :D )
blurred_image = cv2.GaussianBlur(image, (101,1), 0)
cv2.imshow("rozmazany",blurred_image)
cv2.waitKey(0)

blurred_image = cv2.GaussianBlur(image, (1,101), 0)
cv2.imshow("rozmazany",blurred_image)
cv2.waitKey(0)


# TODO: Detekuj okraje pomoci Canny
# Use cv2.Canny() with the given threshold1 (budu mu rikat t1) and threshold2 (t2)
# t1 a t2 jsou cisla, ktera rikaji, jak musi byt velka zmena jasu, abychom ji detekovaly jako okraj
# mame dve hranice, 
#   pod t1 urcite neni edge, 
#   mezi t1 a t2 muze byt, ale jen kdyz se dotyka edge, ktery je nad t2
#   nad t2 urcite edge

image = cv2.imread("W1D3/ImgFuncitonsTest/flower.jpg")
edges_image = cv2.Canny(image, 100, 300)
cv2.imshow("okraje",edges_image)
cv2.waitKey(0)

edges_image = cv2.Canny(image, 300,300)
cv2.imshow("okraje",edges_image)
cv2.waitKey(0)

edges_image = cv2.Canny(image, 100, 100)
cv2.imshow("okraje",edges_image)
cv2.waitKey(0)


# TODO: Nakresli kolecko na obrazek
# pozice (0,0) je v levem hornim rohu
# polomer je cislo
# barva se zadava jako trojice RGB 
# use cv2.circle(image,center_pos,radius,color)
kolecko_image = cv2.circle(image,(50,50),20,(0,255,0))
cv2.imshow("koleckovy",kolecko_image)
cv2.waitKey(0)

# TODO: Napis text na obrazek
# def write_text(image, text, position, font, font_scale, color, thickness):
# Use cv2.putText() with the given parameters
text_image = cv2.putText(image, "Ahoj svete", (100,100), cv2.FONT_ITALIC, 3, (0,0,0))
cv2.imshow("s textem",text_image)
cv2.waitKey(0)

# TODO: Image muzes slicovat stejne jako stringy
# image[100:200] ti vyrizne prouzek mezi vyskou 100 a 200 pixelu
sliced_image = image[100:200]
cv2.imshow("uriznuty",sliced_image)
cv2.waitKey(0)

# TODO: Uloz nejaky tvuj upraveny obrazek na danou adresu v pocitaci
# use cv2.imwrite()
cv2.imwrite("W1D3/ImgFuncitonsTest/edited.jpg", kolecko_image)

# TODO: dalsi funkce: rotate, resize, blur, bilateralFilter, boxFilter, copyMakeBorder, Smooth
