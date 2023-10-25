import donkeycar as dk
from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle

# Initialize car
V = dk.vehicle.Vehicle()

# Initialize PCA9685 controllers and actuators
steering_controller = PCA9685(channel=0, address=0x40, busnum=None)
steering = PWMSteering(controller=steering_controller, left_pulse=270, right_pulse=490)

# Add actuators to the vehicle
V.add(steering, inputs=['steering'])

# Define a function to update the inputs from the terminal
def update_inputs():
    # Capture steering input from the terminal
    steering_input = float(input("Enter steering input (-1 to 1): "))
    
    # Ensure the input is within the valid range
    steering_input = max(-1.0, min(1.0, steering_input))

    # Set the inputs for steering 
    V.input['steering'] = steering_input

# Run the vehicle with the defined inputs
V.start(update_inputs)

# Stop the vehicle when done
V.stop()