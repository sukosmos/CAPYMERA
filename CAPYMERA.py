import cv2
import numpy as np
import os
from collections import deque

# Initialize webcam
cap = cv2.VideoCapture(0)

# Get frame dimensions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

# Load Haar cascade for face detection
haar_cascade_path = 'haarcascade_frontalface_default.xml'
if not os.path.exists(haar_cascade_path):
    raise FileNotFoundError(f"Haar cascade file '{haar_cascade_path}' not found!")

face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# Load the filter image (Ensure this file exists)
filter_path = 'capy.png'
filter_img = cv2.imread(filter_path, cv2.IMREAD_UNCHANGED)
if filter_img is None:
    raise FileNotFoundError(f"Filter image '{filter_path}' not found.")

# Queue to store face positions for smoothing
face_history = deque(maxlen=10)  # Store last 5 detections

# Toggle flag for filter display
filter_enabled = False

# Function to overlay an image with transparency on a frame
def overlay_image(background, overlay, x, y, w, h):
    overlay_resized = cv2.resize(overlay, (w, h))

    if overlay_resized.shape[2] == 4:
        mask = overlay_resized[:, :, 3] / 255.0
        overlay_rgb = overlay_resized[:, :, :3]

        # Ensure within bounds
        y1, y2 = max(0, y), min(background.shape[0], y + h)
        x1, x2 = max(0, x), min(background.shape[1], x + w)

        # Adjust overlay and mask dimensions
        overlay_cropped = overlay_rgb[:y2 - y1, :x2 - x1]
        mask_cropped = mask[:y2 - y1, :x2 - x1]

        # Blend overlay with background
        for c in range(3):
            background[y1:y2, x1:x2, c] = (1 - mask_cropped) * background[y1:y2, x1:x2, c] + mask_cropped * overlay_cropped[:, :, c]

# Mode flag for recording
recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

    if len(faces) > 0:
        x, y, w, h = faces[0]  # Take the first detected face

        # Store face positions for smoothing
        face_history.append((x, y, w, h))

        # Compute moving average of the last 5 frames
        x = int(np.mean([pos[0] for pos in face_history]))
        y = int(np.mean([pos[1] for pos in face_history]))
        w = int(np.mean([pos[2] for pos in face_history]))
        h = int(np.mean([pos[3] for pos in face_history]))

        # Apply filter if enabled
        if filter_enabled:
            overlay_image(frame, filter_img, x - int(w * 0.1), y - int(h * 0.4), int(w * 1.4), int(h * 1.5))

    # Display recording status
    display_frame = frame.copy()
    cv2.putText(display_frame, 'Record: Space | Exit: ESC | Filter: F', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    if recording:
        out.write(frame)
        cv2.putText(display_frame, 'Recording...', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (10, 10, 200), 2)
    else:
        cv2.putText(display_frame, 'Ready to Record', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 200, 50), 2)

    # Show frame
    cv2.imshow('Video Recorder', display_frame)

    # Handle key events
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        break
    elif key == 32:  # Space key to toggle recording mode
        recording = not recording
    elif key == ord('f'):  # Toggle filter with 'F' key
        filter_enabled = not filter_enabled

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
