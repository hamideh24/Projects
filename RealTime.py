import cv2
from simple_facerec import SimpleFacerec


#encode faces from other folder
simpface = SimpleFacerec()
simpface.load_encoding_images("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy")
#Load Camera
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    face_locations, face_names = simpface.detect_known_faces(frame)
    for face_locations, name in zip(face_locations, face_names):
        t, l, b, r = face_locations[0], face_locations[1], face_locations[2], face_locations[3]



        cv2.putText(frame, name, (r, t - 10),cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (r, t), (l, b), (0, 0, 255), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()