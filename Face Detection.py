import cv2

alg="C:/Users/SIVA/Downloads/Day_5/Day_5/haarcascade_frontalface_default.xml"

haar_cascade=cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _,img=cam.read()

    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=haar_cascade.detectMultiScale(grayimg,1.3,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y) ,(x + w, y + h),(0, 255, 0), 2)
    cv2.imshow("faceDetection",img)

    key= cv2.waitKey(10)
    print(key)
    if key== 27:
        break
cam.release()
cv2.destroyAllWindows()    
