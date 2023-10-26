import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

try:
    while True:
        # Move servo based on input
        steering = int(input('Servo Angle (280-420): '))
        if 280 <= steering <= 420:
            pwm.set_pwm(0, 0, steering)
        else:
            print('Invalid input! Angle must be between 280 and 420.')

except KeyboardInterrupt:
    pwm.set_pwm(0, 0, 350)  # Set to middle position
    pass