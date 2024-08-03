import cv2


# TODO: Nacti obrazek do promenne image
# Use cv2.imread() to read an image from file_path
image = ...

# TODO: Zobraz obrazek
#   a) dokud se nestiskne klavesa
#   b) presne jednu sekundu
# Use cv2.imshow() to display the image with window_name
# Use cv2.waitKey() to wait a certain amount of time


# TODO: preved obrazek na cernobily
# Use cv2.cvtColor() with cv2.COLOR_BGR2GRAY to convert the image
gray_image = ...



# TODO: Rozmaz obrazek pomoci funkce gaussian blur
# Use cv2.GaussianBlur() with the given kernel_size  
# (kernel_size rika, kolik vedlejsich pixelu se pouzije k rozmazani a je to dvojice LICHYCH cisel)
# jaky je rozdil mezi kernel size (101,1) a (1,101)
# posledni parametr dej proste 0 (nevim co znamena :D )
blurred_image = ...

blurred_image = ...


# TODO: Detekuj okraje pomoci Canny
# Use cv2.Canny() with the given threshold1 (budu mu rikat t1) and threshold2 (t2)
# t1 a t2 jsou cisla, ktera rikaji, jak musi byt velka zmena jasu, abychom ji detekovaly jako okraj
# mame dve hranice, 
#   pod t1 urcite neni edge, 
#   mezi t1 a t2 muze byt, ale jen kdyz se dotyka edge, ktery je nad t2
#   nad t2 urcite edge

image = cv2.imread("W1D3/ImgFuncitonsTest/flower.jpg")
edges_image = ...


# TODO: Nakresli kolecko na obrazek
# pozice (0,0) je v levem hornim rohu
# polomer je cislo
# barva se zadava jako trojice RGB 
# use cv2.circle(image,center_pos,radius,color)
kolecko_image = ...

# TODO: Napis text na obrazek
# def write_text(image, text, position, font, font_scale, color, thickness):
# Use cv2.putText() with the given parameters
text_image = ...

# TODO: Image muzes slicovat stejne jako stringy
# image[100:200] ti vyrizne prouzek mezi vyskou 100 a 200 pixelu
sliced_image = ...

# TODO: Uloz nejaky tvuj upraveny obrazek na danou adresu v pocitaci
# use cv2.imwrite()

# TODO: dalsi funkce: rotate, resize, blur, bilateralFilter, boxFilter, copyMakeBorder, Smooth
