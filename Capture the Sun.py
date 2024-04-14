import random
import time
import cv2
import numpy as np
import pygame
from cvzone.HandTrackingModule import HandDetector
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Capture The Sun")
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
img = pygame.image.load(r"C:\Users\Sam\Desktop\sun.png").convert_alpha()
rectSun = img.get_rect()
rectSun.x,rectSun.y= 500,500
speed = 15
score = 0
startTime = time.time()
totalTime = 100
detector =HandDetector(detectionCon=0.8, maxHands=2)
def resetSun():
    rectSun.x= random.randint(100,img.shape[1]-100)
    rectSun.y=img.shape[0]+050
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    timeRemain = int(totalTime -(time.time()-startTime))
    if timeRemain <0:
        window.fill((255,255,255))
        font = pygame.font.Font(r'C:\Users\Sam\Desktop\g1.ttf', 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP' , True, (50, 50, 255))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))

    else:
        success, img = cap.read()
        img = cv2.flip(img, 1)  # flip image horozontal(1) for 0 it's verticle
        hands, img = detector.findHands(img, flipType=False)
        rectSun.y -= speed  

        if rectSun.y < 0:
            resetSun()
            speed += 5

        if hands:
            hand = hands[0]
            values = hand["lmList"][8]
            x, y = values[0], values[1]  # Extract x and y coordinates
            if rectSun.collidepoint(x, y):
                resetSun()
                score += 10
                speed += 1

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))
        window.blit(img, rectBalloon)
        font = pygame.font.Font(r'C:\Users\Sam\Desktop\g1.ttf', 50)

        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))
    pygame.display.update()
    clock.tick(30)
