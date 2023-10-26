# Import the necessary libraries
import cv2  # OpenCV for image processing
import libcamera  # Library for camera configuration
from picamera2 import Picamera2  # Library for Raspberry Pi camera control
import numpy as np

# A callback function that does nothing; required for creating trackbars
def empty(a):
    pass

# Create a new window with trackbars for HSV color selection
cv2.namedWindow('Range HSV')
cv2.resizeWindow('Range HSV', 500, 350)
cv2.createTrackbar('HUE Min', 'Range HSV', 0, 180, empty)
cv2.createTrackbar('HUE Max', 'Range HSV', 180, 180, empty)
cv2.createTrackbar('SAT Min', 'Range HSV', 0, 255, empty)
cv2.createTrackbar('SAT Max', 'Range HSV', 255, 255, empty)
cv2.createTrackbar('VALUE Min', 'Range HSV', 0, 255, empty)
cv2.createTrackbar('VALUE Max', 'Range HSV', 255, 255, empty)

# Create an instance of the Picamera2 class
picam2 = Picamera2()

# Configure the camera with the desired settings for the preview
picam2.configure(picam2.create_preview_configuration(
    main={'format': 'XRGB8888', 'size': (640, 480)},
    transform=libcamera.Transform(vflip=1, hflip=1)))  # Apply vertical and horizontal flips to the image

# Start capturing images from the camera
picam2.start()

while True:
    # Start reading the webcam feed frame by frame.
    image = picam2.capture_array()

    # Get the new values of the trackbar in real-time as the user changes them
    h_min = cv2.getTrackbarPos('HUE Min', 'Range HSV')
    h_max = cv2.getTrackbarPos('HUE Max', 'Range HSV')
    s_min = cv2.getTrackbarPos('SAT Min', 'Range HSV')
    s_max = cv2.getTrackbarPos('SAT Max', 'Range HSV')
    v_min = cv2.getTrackbarPos('VALUE Min', 'Range HSV')
    v_max = cv2.getTrackbarPos('VALUE Max', 'Range HSV')

    # Set the lower and upper HSV range according to the values selected by the trackbars
    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])

    # Convert the frame to a 3-channel image
    image_3_channel = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    
    # Convert the BGR image to HSV image
    image_hsv = cv2.cvtColor(image_3_channel, cv2.COLOR_BGR2HSV)

    # Filter the image and get the binary mask, where white represents your target color
    image_threshold = cv2.inRange(image_hsv, lower_range, upper_range)

    # Convert the binary mask to a 3-channel image
    image_threshold_3_channel = cv2.cvtColor(image_threshold, cv2.COLOR_GRAY2BGR)

    # You can also visualize the real part of the target color (Optional)
    image_bitwise_3_channel = cv2.bitwise_and(image_3_channel, image_3_channel, mask=image_threshold)

    # Stack the mask, original frame, and the filtered result horizontally
    stacked = np.hstack((image_threshold_3_channel, image_bitwise_3_channel, image_3_channel))

    # Show the combined window with trackbars and output
    cv2.imshow('HSV Image Processing', stacked)

    # If the user presses ESC then exit the program
    key = cv2.waitKey(1)
    if key == 27:
        break

    # If the user presses `p`, then print this array.
    if key == ord('p'):
        the_array = [[h_min, s_min, v_min], [h_max, s_max, v_max]]
        print(the_array)

        # Also save this array as hsv_value.npy
        np.save('hsv_value', the_array)
        break

# Release the camera & destroy the windows.
cv2.destroyAllWindows()
picam2.close()
