def registrar(personName):
  import cv2

  cap = cv2.VideoCapture(0)

  while True:
    success, img = cap.read()

    if not success:
      print("couldn't grab the frame")
      break

    cv2.imshow('Register', img)

    pressedKey = cv2.waitKey(1)

    if pressedKey == ord(' '):
      img_name = f'{personName}.jpg'
    
      cv2.imwrite(f'./processing/resources/img/attendance/{img_name}', img)

      print('photo saved')

      break

    elif pressedKey == ord('q'):
      break
