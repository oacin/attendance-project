import cv2

personName = input('Digite o nome: ')

if personName:
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
  
      cv2.imwrite(f'resources/img/attendance/{img_name}', img)

      print('photo saved')

    elif pressedKey == ord('q'):
      break
