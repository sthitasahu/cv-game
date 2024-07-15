import numpy as np
import cv2 as cv
import cvzone
from cvzone.HandTrackingModule import HandDetector
import streamlit as st

# Initialize the camera
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Set camera properties
cap.set(3, 1280)
cap.set(4, 720)

# Load images
imgBg = cv.imread("assets/bg.png")
imgGO = cv.imread("assets/gameover.png")
imgBall = cv.imread("assets/ball.png", cv.IMREAD_UNCHANGED)
imgBat1 = cv.imread("assets/bat1.png", cv.IMREAD_UNCHANGED)
imgBat2 = cv.imread("assets/bat2.png", cv.IMREAD_UNCHANGED)

# Initialize other variables
detector = HandDetector(detectionCon=0.8, maxHands=2)
ballPos = [100, 100]
speedX = 25
speedY = 25
gameOver = False
score = [0, 0]

while True:
    # Read a frame from the camera
    success, img = cap.read()
    if not success:
        print("Error: Failed to read frame from camera.")
        break

    # Flip the image horizontally
    img = cv.flip(img, 1)
    
    # Create a copy of the raw image
    imgRaw = img.copy()

    # Rest of your game logic here...

    # Display the image
    cv.imshow("Image", img)
    
    # Check for key press
    key = cv.waitKey(1)
    if key == ord("r"):
        # Reset game state
        ballPos = [100, 100]
        speedX = 25
        speedY = 25
        gameOver = False
        score = [0, 0]
        imgGO = cv.imread("assets/gameover.png")
    elif key == 27:  # ESC key
        break

# Release the camera and close windows
cap.release()
cv.destroyAllWindows()

# Streamlit UI (if needed)
st.title('A basic game')