import cv2
import face_recognition

img = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Basem.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img_2 = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Wafa.png")
rgb_img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
img_encoding_2 = face_recognition.face_encodings(rgb_img_2)[0]

img_3 = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Yasmine.png")
rgb_img_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2RGB)
img_encoding_3 = face_recognition.face_encodings(rgb_img_3)[0]

img_4 = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Miriam.png")
rgb_img_4 = cv2.cvtColor(img_4, cv2.COLOR_BGR2RGB)
img_encoding_4 = face_recognition.face_encodings(rgb_img_4)[0]

img_5 = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Mohammed.png")
rgb_img_5 = cv2.cvtColor(img_5, cv2.COLOR_BGR2RGB)
img_encoding_5 = face_recognition.face_encodings(rgb_img_5)[0]

img_6 = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Noor.png")
rgb_img_6 = cv2.cvtColor(img_6, cv2.COLOR_BGR2RGB)
img_encoding_6 = face_recognition.face_encodings(rgb_img_6)[0]

img_7 = cv2.imread("/Users/wreckit/PycharmProjects/FaceRecognition/image/Family_Pics copy/Malak.png")
rgb_img_7 = cv2.cvtColor(img_7, cv2.COLOR_BGR2RGB)
img_encoding_7 = face_recognition.face_encodings(rgb_img_7)[0]

img_8 = cv2.imread("/Users/wreckit/Desktop/Unknown_Pics/Basem_Unknown.png")
rgb_img_8 = cv2.cvtColor(img_8, cv2.COLOR_BGR2RGB)
img_encoding_8 = face_recognition.face_encodings(rgb_img_8)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding_8)
print(result)
