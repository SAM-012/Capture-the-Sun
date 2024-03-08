import random
import time
import cv2
import numpy as np
import pygame
from cvzone.HandTrackingModule import HandDetector
# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("balloon pop")
#webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
#images
imgBalloon = pygame.image.load(r"C:\Users\Sam\Desktop\bollon.png").convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x,rectBalloon.y= 500,500
#variables
speed = 15
score = 0
startTime = time.time()
totalTime = 100
#hand Detection
detector =HandDetector(detectionCon=0.8, maxHands=2)
def resetBalloon():
    rectBalloon.x= random.randint(100,img.shape[1]-100)
    rectBalloon.y=img.shape[0]+50
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # Apply Logics
    timeRemain = int(totalTime -(time.time()-startTime))
    if timeRemain <0:
        window.fill((255,255,255))
        font = pygame.font.Font(r'C:\Users\Sam\Desktop\g1.ttf', 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP' , True, (50, 50, 255))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))

    else:

        # fill the window with a color to wipe away anything from           last frame
        # window.fill("white")
        # open camera (cv)
        success, img = cap.read()
        img = cv2.flip(img, 1)  # flip image horozontal(1) for 0 it's verticle
        # find Hands programs
        hands, img = detector.findHands(img, flipType=False)

        # RENDER YOUR GAME HERE
        # logic here

        # flip() the display to put your work on window
        # pygame.display.flip()
        rectBalloon.y -= speed  # Move the  balloon up
        # Check if balloon has reached the top without pop

        if rectBalloon.y < 0:
            resetBalloon()
            speed += 5

        if hands:
            hand = hands[0]
            values = hand["lmList"][8]
            x, y = values[0], values[1]  # Extract x and y coordinates

            # Check if the balloon collides with the hand landmark
            if rectBalloon.collidepoint(x, y):
                resetBalloon()
                score += 10
                speed += 1

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

        window.blit(imgBalloon, rectBalloon)

      
        font = pygame.font.Font(r'C:\Users\Sam\Desktop\g1.ttf', 50)

        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    pygame.display.update()
    clock.tick(30)  # limits FPS to 60 