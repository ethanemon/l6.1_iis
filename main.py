from PIL import Image
import pytesseract
import cv2
import os
image = 'C:/Users/korys/Desktop/help.png'

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

preprocess = "thresh"
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

text = pytesseract.image_to_string(Image.open("C:/Users/korys/Desktop/help.png"))
os.remove("C:/Users/korys/Desktop/help.png")

print(text)
cv2.imshow("Image", image)
cv2.imshow("Output", gray)

cv2.waitKey(0)