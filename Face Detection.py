import cv2

#load haarcascades file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#we are using haarcascade pre-trained model
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5, minSize=(50,50))
    #1.1 is scale factor, smaller number detect more faces
    #5 is minNeighbors = lower number more detection
    #minSize to ignore more faces

    #drawing green boxes
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #x+y = top left corner
        #x+w,y+h = bottom right corner
        #2 = thickness

        #put text : "face"
        cv2.putText(frame,"face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
        #font style

        #show live webcam video
        cv2.imshow("HaarCascade Face Detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to exit
        break

cap.release()
cv2.destroyAllWindows()
