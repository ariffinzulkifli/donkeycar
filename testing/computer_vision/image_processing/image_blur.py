# Import the necessary libraries
import cv2  # OpenCV for image processing
import libcamera  # Library for camera configuration
from picamera2 import Picamera2  # Library for Raspberry Pi camera control

# Create an instance of the Picamera2 class
picam2 = Picamera2()

# Configure the camera with the desired settings for the preview
picam2.configure(picam2.create_preview_configuration(
    main={'format': 'XRGB8888', 'size': (640, 480)},
    transform=libcamera.Transform(vflip=1, hflip=1)))  # Apply vertical and horizontal flips to the image

# Start capturing images from the camera
picam2.start()

# Continuously capture and display images from the camera
while True:
    # Capture an image from the camera
    image = picam2.capture_array()
    
    # Apply Gaussian blur with a kernel size of (15, 15) to the original image
    image_blur1 = cv2.GaussianBlur(image, (15, 15), 0)
    
    # Apply Gaussian blur with a larger kernel size of (101, 101) to the original image
    image_blur2 = cv2.GaussianBlur(image, (101, 101), 0)

    # Display the original image and the two blurred images in separate windows
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image #1', image_blur1)
    cv2.imshow('Blurred Image #2', image_blur2)

    # If the user presses the ESC key, exit the program
    key = cv2.waitKey(1)
    if key == 27:
        break

# Close the OpenCV windows and release camera resources
cv2.destroyAllWindows()
picam2.close()
