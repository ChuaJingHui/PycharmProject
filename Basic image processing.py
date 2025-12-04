import cv2

#load image
image=cv2.imread('happy.jpg')

#handling error if unable read the file
if image is None:
    print("image not found!")
    exit()

#show original image
cv2.imshow("Happy Life",image)
cv2.waitKey(0)
# 0 means 0 millisecond