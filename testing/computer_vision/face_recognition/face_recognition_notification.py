from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import requests
import telegram

# Replace with your Telegram bot token
bot_token = 'YOUR_BOT_TOKEN'

# Replace with your chat ID
chat_id = 'YOUR_CHAT_ID'

bot = telegram.Bot(token=bot_token)

currentname = 'unknown'
encodingsP = 'encodings.pickle'
cascade = 'haarcascade_frontalface_default.xml'

# Function to send a message to Telegram
def send_message(name):
    message = f'{name} is at your door.'
    bot.send_message(chat_id=chat_id, text=message)

# Load face recognition data (encodings)
print('[INFO] Loading encodings + face detector...')
data = pickle.loads(open(encodingsP, 'rb').read())

# Load the face detection classifier (Haar Cascade)
detector = cv2.CascadeClassifier(cascade)

# Start the video stream
print('[INFO] Starting video stream...')
vs = VideoStream(src=0).start()
time.sleep(2.0)

fps = FPS().start()

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=500)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the frame using the Haar Cascade
    rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
        minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)

    # Convert detected rectangles to face location boxes
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data['encodings'],
            encoding)
        name = 'Unknown'

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data['names'][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)
            
            if currentname != name:
                currentname = name
                print(currentname)
                img_name = 'image.jpg'
                cv2.imwrite(img_name, frame)
                print('Taking a picture.')
                
                # Send a message to Telegram when an unknown person is detected
                send_message(name)
                
        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
        # Draw a rectangle around the detected face (pink color)
        cv2.rectangle(frame, (left, top), (right, bottom),
            (255, 192, 203), 2)

        # Display the name of the detected person (black text on a white background)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
            .8, (0, 0, 0), 2)

    # Display the processed frame with face recognition results
    cv2.imshow('Facial Recognition is Running', frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    fps.update()

fps.stop()
print('[INFO] Elapsed time: {:.2f} seconds'.format(fps.elapsed()))
print('[INFO] Approximate FPS: {:.2f}'.format(fps.fps()))

# Close all OpenCV windows and stop the video stream
cv2.destroyAllWindows()
vs.stop()
