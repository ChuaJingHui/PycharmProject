import cv2

#load image
image=cv2.imread('happy.jpg')

#handling error if unable read the file
if image is None:
    print("image not found!")
    exit()

#show original image
cv2.imshow("Happy Life",image)
cv2.waitKey(0)  # 0 means 0 millisecond

#variation 1:resize using scaling
#smaller the size with 80%
#Clearer compared to cv2.INTER_AREA
smaller_my_image=cv2.resize(image,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Smaller image",smaller_my_image)
cv2.waitKey(0)

#Clearer compared to cv2.INTER_LINEAR
smaller_my_image=cv2.resize(image,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Smaller image",smaller_my_image)
cv2.waitKey(0)

#variation 2:resize using resolution/pixel
new_width=800
new_height=800
resize_img=cv2.resize(image,(new_width,new_height),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized image",resize_img)
cv2.waitKey(0)

resize_img=cv2.resize(image,(new_width,new_height),interpolation=cv2.INTER_NEAREST)
cv2.imshow("Resized image",resize_img)
cv2.waitKey(0)