import cv2
import math
import libcamera
import numpy as np
import Adafruit_PCA9685
from picamera2 import Picamera2
from adafruit_servokit import ServoKit

# Initialize the PCA9685 using a specific I2C address (0x60).
pwm = Adafruit_PCA9685.PCA9685(0x60)

# Set the PWM frequency to 1600 Hz.
pwm.set_pwm_freq(1600)
servo = ServoKit(channels=16)

horizon_line = 280
servo_center = 85

# Define a function to move the motor forward with a given throttle value.
def forward(throttle):
    pwm.set_pwm(0, 0, throttle)
    pwm.set_pwm(1, 0, 4095)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 0)
    pwm.set_pwm(4, 0, throttle)
    pwm.set_pwm(7, 0, throttle)
    pwm.set_pwm(6, 0, 4095)
    pwm.set_pwm(5, 0, 0)

# Define a function to move the motor in reverse with a given throttle value.
def reverse(throttle):
    pwm.set_pwm(0, 0, -throttle)
    pwm.set_pwm(2, 0, 4095)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(3, 0, -throttle)
    pwm.set_pwm(4, 0, 0)
    pwm.set_pwm(7, 0, -throttle)
    pwm.set_pwm(5, 0, 4095)
    pwm.set_pwm(6, 0, 0)

# Define a function to stop the motor.
def stop():
    pwm.set_pwm(0, 0, 0)
    pwm.set_pwm(2, 0, 4095)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(3, 0, 0)
    pwm.set_pwm(4, 0, 0)
    pwm.set_pwm(7, 0, 0)
    pwm.set_pwm(5, 0, 4095)
    pwm.set_pwm(6, 0, 0)

# Grab images as numpy arrays and leave everything else to OpenCV.
cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(
    main={'format': 'XRGB8888', 'size': (640, 480)},
    transform=libcamera.Transform(vflip=1, hflip=1)))
picam2.start()

try:
    while True:
        forward(700)

        image = picam2.capture_array()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        low = np.array([000, 100, 163])
        high = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, low, high)

        blur = cv2.GaussianBlur(mask, (25, 25), 0)
        edge = cv2.Canny(blur, 100, 200)

        horizon_line_pixels = np.asarray(edge)
        horizon_line_white_pixel = np.where(horizon_line_pixels[horizon_line - 1] == 255)
        
        white_pixel_index = np.asarray(horizon_line_white_pixel[0])
        if white_pixel_index.size > 0:
            index_pixel_left = white_pixel_index[0]
            index_pixel_right = white_pixel_index[-1]
            index_pixel_centre = int(((index_pixel_right - index_pixel_left)/2) + index_pixel_left)
            # print('WHITE PIXEL INDEX  {}, {}, {}'.format(index_pixel_left, index_pixel_centre, index_pixel_right))
            
            x = index_pixel_centre - 320
            y = 480 - horizon_line
            #print (x)
            
            theta = int(math.degrees(math.atan(x/y)))
            #print (theta)

            if theta is not None: 
                if theta > 0:
                    if theta > 35 :
                        servo.servo[0].angle = 135
                    else:
                        servo_out = servo_center + theta
                        servo.servo[0].angle = servo_out
                if theta < 0:
                    if theta > -35 :
                        servo.servo[0].angle = 35
                    else:
                        servo_out = servo_center + theta
                        servo.servo[0].angle = servo_out 
                if theta == 0:
                    servo.servo[0].angle = servo_center

            cv2.circle(image, (index_pixel_centre,horizon_line), 5, (255, 0, 0), -1)
            cv2.line (image , (320, 480), (320, 0), (0, 0, 255), 1)
            cv2.line (image , (320, 480), (index_pixel_centre, horizon_line) , (0, 0, 255), 1)
            
        #yellow = cv2.bitwise_and(image, image, mask = mask1)
        cv2.line(image, (0, horizon_line), (640, horizon_line),(0, 0, 255), 1)
        cv2.imshow('Original', image)
        #cv2.imshow('HSV', hsv)
        #cv2.imshow('Mask', mask1)
        #cv2.imshow('Detect', yellow)
        #cv2.imshow('Blur', blur)
        cv2.imshow('Edge', edge)

        # Check if the 'ESC' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    cv2.destroyAllWindows()
    picam2.close()
    servo.servo[0].angle = servo_center
    stop()

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    picam2.close()
    servo.servo[0].angle = servo_center
    stop()