# Capture-the-Sun
This Python script implements a simple sun popping game using Pygame for graphics and OpenCV for hand tracking. The game window is set to a resolution of 1280x720 pixels.
Libraries Used:

    random: Used for generating random numbers.
    time: Utilized for time-related functionality.
    cv2 (OpenCV): Used for accessing the webcam feed and image processing.
    numpy: Required for numerical operations on arrays.
    pygame: Used for creating the game window and handling graphics.
    cvzone.HandTrackingModule: Module for hand detection.

Game Setup:

    The game window is initialized using Pygame.
    A webcam feed is captured using OpenCV and set to a resolution of 1280x720 pixels.
    An image of a sun is loaded, and its initial position is set.

Variables:

    speed: Initial speed of the sun.
    score: Player's score.
    startTime: Time when the game starts.
    totalTime: Total duration of the game.

Hand Detection:

    Hand detection is performed using the HandDetector class from the cvzone module.

Main Loop:

    The game runs in a while loop until the player closes the window.
    Within the loop, events such as quitting the game are handled.
    The game logic is applied, including updating the position of the sun, checking for collisions with the hand, and updating the score.
    The webcam feed is processed and displayed using OpenCV.
    Sun and text elements are rendered onto the Pygame window.
    The game window is updated at a maximum rate of 30 frames per second.

End of Game:

    Once the time limit is reached, a message displaying the player's score is shown on the screen.

Controls:

    The player interacts with the game by popping the sun with their hand. The hand's position is tracked using a webcam.

Limitations:

    The hand detection and tracking may not be accurate in all conditions, depending on lighting and hand visibility.
    The game does not have complex gameplay mechanics and features.
