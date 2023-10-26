from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2

currentname = 'Unknown'

encodingsP = 'encodings.pickle'  # File containing face encodings

print('[INFO] Loading Encodings + Face Detector...')
data = pickle.loads(open(encodingsP, 'rb').read())  # Load the known face encodings

# Start the video stream
vs = VideoStream(src=2, framerate=10).start()

time.sleep(2.0)

fps = FPS().start()

while True:
	
	frame = vs.read()  # Read a frame from the video stream
	frame = imutils.resize(frame, width=500)  # Resize the frame for faster processing
	
	# Detect face locations in the frame
	boxes = face_recognition.face_locations(frame)
	
	# Encode faces in the frame
	encodings = face_recognition.face_encodings(frame, boxes)
	names = []

	for encoding in encodings:
		# Compare the face encoding with known encodings
		matches = face_recognition.compare_faces(data['encodings'], encoding)
		name = 'Unknown'

		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# Determine the most likely name based on matching
			for i in matchedIdxs:
				name = data['names'][i]
				counts[name] = counts.get(name, 0) + 1

			name = max(counts, key=counts.get)

			if currentname != name:
				currentname = name
				print(currentname)

		names.append(name)

	for ((top, right, bottom, left), name) in zip(boxes, names):
		
		# Draw a pink rectangle around detected faces
		cv2.rectangle(frame, (left, top), (right, bottom),
			(255, 0, 255), 2)
		
		# Create a background for the name
		cv2.rectangle(frame, (left, bottom - 25), (right, bottom),
			(0, 0, 0), cv2.FILLED)
		
		# Draw the name in white color on the black background
		cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX,
			0.6, (255, 255, 255), 1)

	cv2.imshow('Facial Recognition is Running', frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord('q'):
		break

	fps.update()

fps.stop()
print('[INFO] Elasped Time: {:.2f}'.format(fps.elapsed()))
print('[INFO] Approx. FPS: {:.2f}'.format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
