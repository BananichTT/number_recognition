import cv2
import random
from imutils import contours
import pytesseract
#путь до тессеракта
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

a = random.randint(1, 4)
print(a)

image = cv2.imread("images/"+str(a)+".jpg")
#размеры изображения
height, width, _ = image.shape

#перевод изображения в серое изображение
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#Выделение активных участков (черного цвета)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]

#выделение всех контуров в массив
conturs = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#сорторовка контуров
conturs, _ = contours.sort_contours(conturs[0])
# cv2.imshow("Test", thresh)
# cv2.waitKey()

# цикл для нахождения области с номеро и его вывод
for c in conturs:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    if area > 500:
        img = image[y:y+h, x:x+w]
        result = pytesseract.image_to_string(img, lang="rus+eng")
        if len(result) > 7:
            print(result)




