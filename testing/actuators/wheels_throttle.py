import Adafruit_PCA9685

# Initialize the PCA9685 using a specific I2C address (0x60).
pwm = Adafruit_PCA9685.PCA9685(0x60)

# Set the PWM frequency to 1600 Hz.
pwm.set_pwm_freq(1600)

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

print('Max Speed Forward: 4095 || Max Speed Reverse: -4095')

try:
    while True:
        # Motor speed and direction based on user input.
        throttle = int(input('Throttle (-4095 - 4095): '))
        
        if throttle > 0:
            forward(throttle)  # Move forward if throttle is positive.
        else:
            reverse(throttle)  # Move in reverse if throttle is non-positive.

except KeyboardInterrupt:
    stop()  # Stop the motor if Ctrl+C is pressed.
    pass