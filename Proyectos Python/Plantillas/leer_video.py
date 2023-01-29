import cv2
import os
dir = os.path.dirname(os.path.abspath(__file__)) + '/nate.mp4'
captura = cv2.VideoCapture(dir)
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(30) == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()