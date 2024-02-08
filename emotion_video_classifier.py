from keras.models import load_model
import numpy as np
import cv2
from keras.preprocessing import image
from keras.utils import img_to_array

detection_model_path = 'C:/Users/acer/Documents/college/Music Player/Music-recommendation-system/haarcascade_files/haarcascade_frontalface_default.xml'
# print(cv2.CascadeClassifier.empty)
emotion_model_path = 'C:/Users/acer/Documents/college/Music Player/Music-recommendation-system/final_model.h5'
# print(cv2.CascadeClassifier.load('haarcascade_files/haarcascade_frontalface_default.xml'))
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["happy", "sad"]


def emotion_testing():
    print("top")
    cap = cv2.VideoCapture(0)
    while True:
        ret, test_img = cap.read()
        if not ret:
            continue
        gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

        faces_detected = face_detection.detectMultiScale(gray_img, 1.32, 5)
        predicted_emotion=''
        for (x, y, w, h) in faces_detected:
            print("here")
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
            roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
            roi_gray = cv2.resize(roi_gray, (48, 48))
            img_pixels = img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255

            predictions = emotion_classifier.predict(img_pixels)

            # find max indexed array
            max_index = np.argmax(predictions[0])
            predicted_emotion = EMOTIONS[max_index]

            cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('Facial emotion analysis ', resized_img)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            print("i am here ")
            break
    cap.release()
    cv2.destroyAllWindows
    return predicted_emotion
    
# emotion_testing()