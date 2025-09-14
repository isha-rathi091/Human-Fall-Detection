import cv2
import tensorflow as tf
import numpy as np
from sms_alert import send_sms_alert
from sensors.heartbeat_sensor import read_heartbeat
from sensors.buzzer import buzz_alert

# Load trained CNN model
model = tf.keras.models.load_model('models/fall_detection_model.h5')

# Video file path (replace with your MP4 file)
video_path = 'test_videos/fall1.mp4'
cap = cv2.VideoCapture(video_path)

# Thresholds
FALL_THRESHOLD = 0.5
HEARTBEAT_THRESHOLD = 100  # example bpm limit

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame
    img = cv2.resize(frame, (64, 64))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict fall
    prediction = model.predict(img)
    is_fall = prediction[0][0] > FALL_THRESHOLD

    # Check heartbeat
    heartbeat = read_heartbeat()
    abnormal_vitals = heartbeat > HEARTBEAT_THRESHOLD

    # Trigger alerts if needed
    if is_fall or abnormal_vitals:
        message = "Fall detected! Check immediately."
        send_sms_alert(message, "+91XXXXXXXXXX")
        buzz_alert(duration=2)
        cv2.putText(frame, "ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display
    cv2.imshow('Fall Detection', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):  # slower frame rate for video
        break

cap.release()
cv2.destroyAllWindows()
