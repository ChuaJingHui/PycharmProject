import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#put filter image here
filter_image=cv2.imread("sunglasses.png",cv2.IMREAD_UNCHANGED)

#start webcam
cap=cv2.VideoCapture(0)

#Always checking the video
while True:
    ok, frame = cap.read()

    if not ok:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #find faces
    faces=face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        #add filter to match your face
        filter_image_resize=cv2.resize(filter_image,(w,int(h*0.5)))

        #position on eye
        fx=x
        fy=y+int(h*0.2)

        fh,fw=filter_image_resize.shape[:2]

        #put filter within boundary
        if fy+fh > frame.shape[:1]:
            continue

        for i in range(fh):
            for j in range(fw):
                #get RGBA of filter
                b,g,r,a = filter_image[i,j]


            #if not transparent
                if a>0:
                    frame[fy+i , fx+j]=(b,g,r)

        #show result
        cv2.imshow("Hahaha",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

