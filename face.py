import cv2

import sys

img=cv2.imread("cat.jpg")

if img is None:
    print("テスト画像が正しく読み込めませんでした")
    sys.exit()


cascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face=cascade.detectMultiScale(gray, minNeighbors=3, minSize=(10,10))

if not len(face)==0:
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,200),3)

else:
    print("ごめんなさい。猫の顔がみつかりませんでした。")
    sys.exit()

cv2.imwrite("result.jpg",img)

cv2.imshow("image",img)
cv2.waitKey(0)
