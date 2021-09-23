import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

known_faces = 'resources/img/attendance'

images      = []
classNames  = []

knownFacesList = os.listdir(known_faces)

print(knownFacesList)

for knownFace in knownFacesList:
  currImg = cv2.imread(f'{known_faces}/{knownFace}')

  images.append(currImg)

  classNames.append(os.path.splitext(knownFace)[0])

def findEncodings(images):
  encodeList = []

  for img in images:
    img     = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode  = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)

  return encodeList

def markAttendance(name):
  file_path = 'resources/src/attendance.csv'

  with open(file_path, 'r+') as f:
    myDataList  = f.readlines()
    nameList    = []

    for line in myDataList:
      entry = line.split(',')
      nameList.append(entry[0])

    if name not in nameList:
      now = datetime.now()
      dtString = now.strftime('%H:%M:%S')
      f.writelines(f'\n{name}, {dtString}')

encodeListKnown = findEncodings(images)

cap = cv2.VideoCapture(0)
 
while True:
  success, img = cap.read()

  if not success:
    print("couldn't grab the frame")
    break

  optimized_img = cv2.resize(
    img,
    (0,0),
    None,
    0.25, # a quarter of original size
    0.25  # a quarter of original size
  )

  optimized_img     = cv2.cvtColor(optimized_img, cv2.COLOR_BGR2RGB)
  facesCurrFrame    = face_recognition.face_locations(optimized_img)
  encodesCurrFrame  = face_recognition.face_encodings(optimized_img, facesCurrFrame)

  for encodeFace, faceLoc in zip(encodesCurrFrame, facesCurrFrame):
    matches     = face_recognition.compare_faces(encodeListKnown, encodeFace)
    faceDist    = face_recognition.face_distance(encodeListKnown, encodeFace)

    print(faceDist)

    matchIndex  = np.argmin(faceDist) # lowest value means best match
 
    if matches[matchIndex]:
      name = classNames[matchIndex].upper()
      print(name)
      y1, x2, y2, x1 = faceLoc

      # in order to 'revive' the image that was rescaled to .25 we can multiply it by 4
      y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

      cv2.rectangle(
        img,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
      )

      cv2.rectangle(
        img,
        (x1, y2-35),
        (x2, y2),
        (0, 255, 0),
        cv2.FILLED
      )

      cv2.putText(
        img,
        name,
        (x1+6, y2-6),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (255, 255, 255),
        2
      )
      
      markAttendance(name)

  cv2.imshow('Webcam', img)
  
  if cv2.waitKey(1) == ord('q'):
    break
