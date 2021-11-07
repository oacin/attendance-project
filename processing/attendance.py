import cv2
import numpy as np
import face_recognition
import os
import requests
from datetime import datetime

url = "http://localhost:8081/attendance"

headers = {
  'Accept':'application/json',
  'Content-type':'application/json'
}

known_faces = './processing/resources/img/attendance'

images      = []
classNames  = []

knownFacesList = os.listdir(known_faces)

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
  today = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

  r = requests.get(url = url)
  data = r.json()
  attendanceList = data['object']

  appointedDays = []

  for attendance in attendanceList:
    if name == attendance['name']:
      appointedDays.append(attendance['datetime'].split('T')[0])
  
  if today.split('T')[0] not in appointedDays:
    payload = {'name': name, 'datetime': today}

    r = requests.post(
      url = url,
      json = payload,
      headers = headers
    )

    print(f'New attendance log status: {r.status_code}')

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
    matches     = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.35)
    faceDist    = face_recognition.face_distance(encodeListKnown, encodeFace)

    # prints the array with the distances between each 'known face' and the frame that is currently being processed
    # print(faceDist)

    matchIndex  = np.argmin(faceDist) # grabs lowest value (means best match)
 
    if matches[matchIndex]:
      name = classNames[matchIndex].upper()
      # prints who was the best match
      # print(name)
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

  cv2.imshow('Class Check-in', img)
  
  if cv2.waitKey(1) == ord('q'):
    break
