import cv2
import numpy as np

texttoshow="i like coding"
rocket=cv2.imread("poster.jpg")
cv2.imshow("rocket picture",rocket)

rocket1=rocket[120:360,400:500]
rocket[0:240,500:600]=rocket1

cv2.putText(rocket,texttoshow,(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

cv2.imshow("rocket",rocket)

print(rocket)

cv2.waitKey(0)