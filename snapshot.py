import numpy as np
import cv2
import time

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def TakeSnapshotAndSave(firstName, lastName, number):
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    capture = 1
    while capture <= number:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        crop_img = frame[y: y + h, x: x + w]  # Crop from x, y, w, h -> 100, 200, 300, 400
        name = firstName[0] + lastName[0] + str(capture)
        cv2.imwrite(name + ".jpg", crop_img)
        capture += 1
        time.sleep(5)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return None

if __name__ == "__main__":
    TakeSnapshotAndSave(firstName="Omar", lastName="Angulo", number=10)
