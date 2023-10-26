import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)

try:
    while True:
        # Move servo based on input
        angle = int(input('Servo Angle (280-420): '))
        if 280 <= angle <= 420:
            pwm.set_pwm(0, 0, angle)
        else:
            print('Invalid input! Angle must be between 280 and 420.')

except KeyboardInterrupt:
    pwm.set_pwm(0, 0, 350)  # Set to middle position
    pass