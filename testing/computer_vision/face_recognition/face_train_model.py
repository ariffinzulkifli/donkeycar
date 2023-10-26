from imutils import paths
import face_recognition
import pickle
import cv2
import os

# Print a message indicating the start of face processing
print('[INFO] Start Processing Faces...')

# Get a list of image file paths in the 'dataset' folder
imagePaths = list(paths.list_images('dataset'))

knownEncodings = []  # Initialize lists to store face encodings and names
knownNames = []

# Loop over each image in the dataset
for (i, imagePath) in enumerate(imagePaths):
    print('[INFO] Processing Image {}/{}'.format(i + 1, len(imagePaths)))
    
    # Extract the name from the image path (assuming folder structure)
    name = imagePath.split(os.path.sep)[-2]

    # Read the image, convert it to RGB format (required by face_recognition)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces in the image using the HOG model
    boxes = face_recognition.face_locations(rgb, model='hog')

    # Encode the faces in the image
    encodings = face_recognition.face_encodings(rgb, boxes)

    # Append the encodings and corresponding names to the lists
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

# Serialize the encodings and names to a pickle file
print('[INFO] Serializing Encodings...')
data = {'Encodings': knownEncodings, 'names': knownNames}
f = open('encodings.pickle', 'wb')
f.write(pickle.dumps(data))
f.close()