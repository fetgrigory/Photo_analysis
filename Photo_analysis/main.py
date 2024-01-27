'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/10/10
Ending 2024//

'''
import cv2
# Инициализация распознаватель лиц 
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    # Загрузка изображений
    #img = cv2.imread("1.jpg")
    #img = cv2.imread("2.jpg")
    img = cv2.imread("3.png")
    # Преобразования изображение к оттенкам серого 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  Отобразить прямоугольник вокруг граней лица
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,100),4)
    # Отобразить результирующее изображение
    cv2.imshow('Photo_analysis', img)
     # Для выхода из программы нужно нажать "x" на клавиатуре!
    if cv2.waitKey(1) & 0xff == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
