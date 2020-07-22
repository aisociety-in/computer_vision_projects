import cv2
import numpy as np

cap = cv2.VideoCapture('red.mp4') # enter 0 for camera

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Detecting Red color
    low_red = np.array([161,155,84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
        # Detecting Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Detecting Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    
    key = cv2.waitKey(1)
    if key == 27:
        break    