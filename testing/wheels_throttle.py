import donkeycar as dk
from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle

# Initialize car
V = dk.vehicle.Vehicle()

# Initialize PCA9685 controllers and actuators
throttle_controller = PCA9685(channel=0, address=0x60, frequency=1600, busnum=None)
throttle = PWMThrottle(controller=throttle_controller, max_pulse=4095, zero_pulse=0, min_pulse=-4095)

# Add actuators to the vehicle
V.add(throttle, inputs=['throttle'])

# Define a function to update the inputs from the terminal
def update_inputs():
    # Capture throttle input from the terminal
    throttle_input = float(input("Enter throttle input (-1 to 1): "))
    
    # Ensure the input is within the valid range
    throttle_input = max(-1.0, min(1.0, throttle_input))

    # Set the inputs for throttle
    V.input['throttle'] = throttle_input

# Run the vehicle with the defined inputs
V.start(update_inputs)

# Stop the vehicle when done
V.stop()
