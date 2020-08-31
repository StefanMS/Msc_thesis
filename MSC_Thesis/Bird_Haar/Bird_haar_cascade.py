import numpy as np
import cv2

bird_cascade = cv2.CascadeClassifier('data/cascade.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    #print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = bird_cascade.detectMultiScale(gray, 100)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+100,y+100),(0,0,255),2)
        print(x,",",y)
        rectan = cv2.rectangle(img,(x,y),(x+100,y+100),(0,0,255),2)
        cv2.circle(img,(x+50,y+50), 7, (255,0,0), -1)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Bird',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()




