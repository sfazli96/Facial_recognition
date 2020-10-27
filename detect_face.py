import cv2

## First we will Load the classifier 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

## This will get our web camera 
cap = cv2.VideoCapture(0)     
while True:
	_, img = cap.read()              ## This gets each frame from the video, cap.read returns 2 variables flag - indicate frame is correct and 2nd is f

##img = cv2.imread('Z.png') Then we get our image we want to use
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # This method only works on gray skin images, so we have to convert the gray scale to rgb image

	faces = face_cascade.detectMultiScale(gray, 1.1, 5) ## Next, we detect the faces

	for (x, y, w, h) in faces:   ## We draw a rectangle around the faces so we can see it correctly
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0))         ## The faces will be a list of coordinates 

	cv2.imshow('img', img) ## Last we show the image

	x = cv2.waitKey(30) & 0xff
	if x==27:
		break

cap.release()


'''
## This will do the recognition for the face, so Facial recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('group.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:  
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0)) 

cv2.imshow('img', img)
cv2.waitKey()
'''