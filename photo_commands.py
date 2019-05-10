import glob
import cv2
import numpy as np
import time
import os

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def takeSnapshotAndSave(number, firstName = "test", lastName = "image"):
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)
    capture = 1

    while capture <= number:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        crop_img = frame[y: y + h, x: x + w]  # Crop from x, y, w, h -> 100, 200, 300, 400
        name = firstName + "_" + lastName + "_" + str(capture)
        cv2.imwrite("./images/" + name + ".jpg", crop_img)
        time.sleep(1)
        capture += 1
    return None

def loadAllImages():
    images = [cv2.imread(file) for file in glob.glob("./images/*.jpg")]
    return images

def resizeImages(images):
    for number in range(len(images)):
        images[number] = cv2.resize(images[number].astype('float32'), dsize=(256, 256))
    return images

def showImages(images):
    for number in range(len(images)):
        cv2.imshow('image', images[number])
        cv2.waitKey(0)
    return None

def applyFilter(images):
    name = "User"
    kernel = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
    diffo = cv2.filter2D(images[-1], -1, kernel)

    del images[-1]
    diff_array = images
    total_diff_array = images
    umbral_array = images

    # Se aplica el filtro de convolucion en 2D con el kernel
    for i in range(len(diff_array)):
        diff_array[i] = cv2.filter2D(images[i], -1, kernel)

    # Obtenemos diferencia total, da como resultado una matriz
    for i in range(len(diff_array)):
        total_diff_array[i] = cv2.absdiff(diffo, diff_array[i])

    # Pasamos la diferencia de una matriz a un valor numerico
    for i in range(len(total_diff_array)):
        umbral_array[i] = np.sum(total_diff_array[i]) / 65536

    minimum = min(umbral_array)

    for i in range(len(umbral_array)):
        if minimum is umbral_array[i] and i < 10:
            name = "Carlos"

        if minimum is umbral_array[i] and i >= 10 and i < 20:
            name = "Miguel"

        if minimum is umbral_array[i] and i >= 20 and i < 30:
            name = "Omar"

    return name

def closeImages():
    cv2.destroyAllWindows()
    return None

def deleteAllPhotos(firstName, lastName):
    photoDetected = True

    for num in range(1, 11):
        if os.path.exists("images" + '/' + firstName + "_" + lastName + "_" + str(num) + ".jpg"):
            os.remove("images" + '/' + firstName + "_" + lastName + "_" + str(num) + ".jpg")
        else:
            photoDetected = False

    return photoDetected

