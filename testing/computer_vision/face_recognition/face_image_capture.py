import cv2
import os

name = 'Ariffin'  # Replace with the name of the person for whom you are capturing images

# Define the directory where the dataset for the specified person will be stored
dataset_dir = 'dataset/' + name

# Create the directory if it doesn't exist, and ensure any intermediate directories are also created
os.makedirs(dataset_dir, exist_ok=True)

# Initialize the camera capture
cam = cv2.VideoCapture(0)

# Create a named window for displaying the camera feed
cv2.namedWindow('Hit Space Bar to Take Photo', cv2.WINDOW_NORMAL)

# Resize the window for better visualization
cv2.resizeWindow('Hit Space Bar to Take Photo', 500, 300)

# Initialize a counter for the captured images
img_counter = 0

# Start an infinite loop for capturing images
while True:
    ret, frame = cam.read()
    
    # Check if capturing the frame was successful
    if not ret:
        print('Failed to Capture Image!')
        break
    
    # Display the current frame in the window
    cv2.imshow('Hit Space Bar to Take Photo', frame)

    # Wait for a key press (1ms delay) and store the key code in 'k'
    k = cv2.waitKey(1)
    
    # Check if the 'ESC' key (key code 27) was pressed to exit the loop
    if k % 256 == 27:
        print('ESC ... exited!')
        break
    # Check if the 'SPACE' key (key code 32) was pressed to capture an image
    elif k % 256 == 32:
        # Define the image name and save the current frame as an image
        img_name = f'{dataset_dir}/image_{img_counter}.jpg'
        cv2.imwrite(img_name, frame)
        print(f'{img_name} written!')
        img_counter += 1

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
