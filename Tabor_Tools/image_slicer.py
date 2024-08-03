## skript vezme obrazek - v pripade tabora Python nefunkcni kod - a rozreze ho 
## na "pieces" prouzku
pieces = 5

import cv2
from os.path import abspath, join, dirname
imgpath = join(abspath(dirname(__file__)), "image.png")
print(imgpath)
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)


height,width = img.shape[:2] 
strip_size = width // pieces
index = 0
for i in range(0,width,strip_size):
    crop_img = img[0:height, i:i+strip_size]    
    cv2.imwrite(f"cropped/piece{index}.jpg", crop_img)
    index += 1
    