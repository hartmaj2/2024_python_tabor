import pytesseract
import cv2

# TODO: pouzij pytesseract.image_to_string() pro prevod obrazku na text
image = cv2.imread("img_to_join.png")
text = pytesseract.image_to_string(image)
print(text)