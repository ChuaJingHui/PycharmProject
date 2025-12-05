import cv2

image=cv2.imread('happy.jpg')
img=cv2.imread('cutie.png')
#error handling,if image not found
if image is None:
    print("Image not found!")
    exit()

#1 convert image to gray scale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#why convert image to gray - better img processing and edge detection

img_change=cv2.resize(img,None,fx=0.7,fy=0.7,interpolation=cv2.INTER_CUBIC)
#blurring image (ksize should be odd number)
blur=cv2.GaussianBlur(image,(3,3),0)
blur_gray=cv2.GaussianBlur(gray,(3,3),0)
canny_blur=cv2.Canny(img_change,100,150)

cv2.imshow("Original",image)
cv2.imshow("Gray",gray)
cv2.imshow("Blur",blur)
cv2.imshow("Blur Gray",blur_gray)
cv2.imshow("Canny Blur",canny_blur)
cv2.waitKey(0) #can quit the window by pressing q

cv2.imwrite("canny_cutie.png",canny_blur)
cv2.imwrite("blur.jpg",blur)
cv2.imwrite("gray.jpg",gray)