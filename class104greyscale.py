import cv2

greyscale=cv2.imread("butterfly.jpg")
cv2.imshow("greyscale image",greyscale)

print(greyscale)

greyscales=cv2.cvtColor(greyscale,cv2.COLOR_RGB2GRAY)
cv2.imshow("greyscales",greyscales)
print(greyscales)

cv2.waitKey(0)