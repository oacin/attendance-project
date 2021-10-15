def registrar(personName):
  import cv2
  import os
  classificador = cv2.CascadeClassifier('./processing/haarcascade_frontalface_default.xml')

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

      imagem = cv2.imread(f'./processing/resources/img/attendance/{img_name}')
      imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

      facesdetectadas = classificador.detectMultiScale(imagemcinza,scaleFactor=1.1, minNeighbors=8,minSize=(30,30))

      if len(facesdetectadas) == 1:
        nameRegistration = open(f'./processing/resources/src/nameRegistration.csv', 'a')
        nameRegistration.write(personName + "\n")
        break
      elif len(facesdetectadas) > 1:
        print('Muitas pessoas')
        os.remove(f'./processing/resources/img/attendance/{img_name}')
      else:
        print('Não tem ninguem')
        os.remove(f'./processing/resources/img/attendance/{img_name}')

    elif pressedKey == ord('q'):
      break
