import cv2
import numpy as np

#why numpy? --is to create array similar to list function

#define function
def nothing(x):
    pass        #this is an empty function which do nothing

#1: create a window
cv2.namedWindow("Track Bars")

#Lower threshold value
cv2.createTrackbar("LHue","Track Bars",0,179,nothing)
cv2.createTrackbar("LSat","Track Bars",0,255,nothing)
cv2.createTrackbar("LVal","Track Bars",0,255,nothing)

#Upper threshold value
cv2.createTrackbar("UHue","Track Bars",179,179,nothing)
cv2.createTrackbar("USat","Track Bars",255,255,nothing)
cv2.createTrackbar("UVal","Track Bars",255,255,nothing)

#turn on webcam
cap=cv2.VideoCapture(0) # 0 means use default camera

#loop to non-stop capturing video until you quit
while True:
    #read the frame of webcam
    _, frame=cap.read()

    #convert BGR to Hue , Saturation, Value (HSV format)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Set the value of HSV color by dragging Track Bars
    l_hue = cv2.getTrackbarPos("LHue","Track Bars")
    l_sat = cv2.getTrackbarPos("LSat", "Track Bars")
    l_val = cv2.getTrackbarPos("LVal", "Track Bars")

    u_hue = cv2.getTrackbarPos("UHue","Track Bars")
    u_sat = cv2.getTrackbarPos("USat", "Track Bars")
    u_val = cv2.getTrackbarPos("UVal", "Track Bars")

    #create array for these 2 values
    lower=np.array([l_hue,l_sat,l_val])
    upper=np.array([u_hue,u_sat,u_val])

    #show result
    mask = cv2.inRange(hsv,lower,upper)

    #this is the final result
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Original",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)

    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit
        break

#turn off webcam
cap.release()
cv2.destroyAllWindows()