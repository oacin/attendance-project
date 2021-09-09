import cv2
import face_recognition

"""
infos
  enconde: 128 measures of the face that was found

  available imgs:
    elon1.jpeg
    elon2.jpg
    bill1.jpg
    nicollas1.jpeg
"""

imgTarget = face_recognition.load_image_file('resources/img/basic/elon2.jpg')
imgTarget = cv2.cvtColor(imgTarget,  cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('resources/img/basic/bill1.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

encodeTarget  = face_recognition.face_encodings(imgTarget)[0]
encodeTest    = face_recognition.face_encodings(imgTest)[0]

results = face_recognition.compare_faces(
  [encodeTarget], # since theres only one img in our "images database", only one encode for target image could be generated
  encodeTest      # encode about the image to be tested
)

faceDist = face_recognition.face_distance(
  [encodeTarget],
  encodeTest
) # the lower the distance between reference enconde and test encode the best the match is

cv2.putText(
  imgTest,
  f'{results[0]} {round(faceDist[0], 2)}',
  (0, 30),
  cv2.FONT_HERSHEY_COMPLEX,
  1,
  (0, 0, 255),
  2
)

cv2.imshow('Target', imgTarget)
cv2.imshow('Test', imgTest)
cv2.waitKey(0)
