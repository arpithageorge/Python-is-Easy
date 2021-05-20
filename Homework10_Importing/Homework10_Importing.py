# Assignment 10: Importing
# Here I am using opencv library which is not discussed earlier.
# Drow Shapes by choosing options.

import numpy as np
import cv2

optn = input("Selct a shape from the options (A) Line, (B) Rectangel, (C) Circle, (D) Polygon), (E) Ellipse:-  ")
print("Please see your selected option in the window")

my_img = np.zeros((400, 400, 3), dtype = "uint8")
cv2.imshow('Window', my_img)

if optn == "A":
	# Creating for Line
	cv2.line(my_img, (202, 220), (100, 160), (0, 20, 200), 10)
	cv2.imshow('Window', my_img)
	my_img = np.zeros((400, 400, 3), dtype = "uint8")

elif optn == "B":
	# Creating a Rectangle
	cv2.rectangle(my_img, (30, 30), (300, 200), (0, 20, 200), 10)
	cv2.imshow('Window', my_img)

elif optn == "C":
	#Creating Circle
	cv2.circle(my_img, (200, 200), 80, (0, 20, 200), 10)
	cv2.imshow('Window', my_img)

elif optn == "D":
	# Creating Polygon
	pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
	pts = pts.reshape((-1,1,2))
	cv2.polylines(my_img,[pts],True,(0,255,255))
	cv2.imshow('Window', my_img)

elif optn == "E":
	# Creating Ellipse 
	cv2.ellipse(my_img,(256,256),(100,50),0,0,180,255,-1)
	cv2.imshow('Window', my_img)

else:
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(my_img, 'No Shape Selected', (50, 50),font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
	cv2.imshow('Window', my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()