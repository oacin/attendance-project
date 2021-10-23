def registrar(personName):
  import cv2
  import os
  from PyQt5.QtWidgets import QMessageBox

  msg = QMessageBox()
  msg.setIcon(QMessageBox.Critical)

  classifier = cv2.CascadeClassifier('./processing/resources/src/haarcascade_frontalface_default.xml')

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

      image = cv2.imread(f'./processing/resources/img/attendance/{img_name}')
      grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      detectedfaces = classifier.detectMultiScale(grayimage,scaleFactor=1.1, minNeighbors=8,minSize=(30,30))

      if len(detectedfaces) == 1:
        msg.setIcon(QMessageBox.Information)
        msg.setText("Imagem Registrada.")
        msg.setInformativeText(f'O cadastro com nome {personName} foi realizado com sucesso!')
        msg.setWindowTitle("Cadastro confirmado")
        msg.exec_()
        break
      elif len(detectedfaces) > 1:
        msg.setText("Existem muitas pessoas na imagem.")
        msg.setInformativeText('É permitido o cadastro de apenas uma pessoa por vez, por favor fique apenas uma na imagem')
        msg.setWindowTitle("Muitas pessoas")
        msg.exec_()
        os.remove(f'./processing/resources/img/attendance/{img_name}')
      else:
        msg.setText("Nenhuma pessoa identificada na imagem")
        msg.setInformativeText('É necessário ter uma pessoa na imagem (Caso ja tenha uma pessoa, favor retirar qualquer objeto do rosto, como por exemplo mascaras e afins).')
        msg.setWindowTitle("Nenhuma pessoa encontrada")
        msg.exec_()
        os.remove(f'./processing/resources/img/attendance/{img_name}')

    elif pressedKey == ord('q'):
      break
