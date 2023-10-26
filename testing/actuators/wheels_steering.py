import Adafruit_PCA9685

# Initialize the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set the PWM frequency to 60 Hz.
pwm.set_pwm_freq(60)

try:
    while True:
        # Prompt the user to input a servo angle within the range 280-420.
        steering = int(input('Servo Angle (280-420): '))
        
        # Check if the input angle is within the valid range (280-420).
        if 280 <= steering <= 420:
            # Set the PWM signal for channel 0 to the specified servo angle.
            pwm.set_pwm(0, 0, steering)
        else:
            # Display an error message for invalid input.
            print('Invalid input! Angle must be between 280 and 420.')

except KeyboardInterrupt:
    # Handle a keyboard interrupt (Ctrl+C) by setting the servo to a default middle position (350).
    pwm.set_pwm(0, 0, 350)  # Set to middle position
    pass