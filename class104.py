import cv2

img=cv2.imread("poster.jpg")
cv2.imshow("display image",img)

print(img)
cv2.waitKey(0)