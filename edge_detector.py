import cv2
import numpy as np

image = cv2.imread('image.jpg',0)

height, width = image.shape

# Extract Sobel Edges- It emphasis Horizontal and Vertical Edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.imshow('Sobel X', sobel_x) #horizontal
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobel_y) #Vertical
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel_OR', sobel_OR) #both combined
cv2.waitKey(0)

#Gets all orientation-length and breadth

laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian) #laplacian
cv2.waitKey(0)

#Applies thresholds i.e if a pixel is within upper and lower
#thresholds, it is is considered as an edge

canny = cv2.Canny(image, 50, 120)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()