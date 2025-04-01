# app.py
# Detecção de piscadas com ajustes finos para piscadas naturais

import cv2
import dlib
from scipy.spatial import distance
from imutils import face_utils

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Ajustes otimizados
EAR_THRESHOLD = 0.25
EAR_CONSEC_FRAMES = 1

frame_counter = 0
blink_counter = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        leftHull = cv2.convexHull(leftEye)
        rightHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightHull], -1, (0, 255, 0), 1)

        if ear < EAR_THRESHOLD:
            frame_counter += 1
        else:
            if frame_counter >= EAR_CONSEC_FRAMES:
                blink_counter += 1
            frame_counter = 0

        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        cv2.putText(frame, f"Piscadas: {blink_counter}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        print(f"EAR: {ear:.2f}")

    cv2.imshow("Contador de Piscadas", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
