import cv2 
from sms_notificaton import send_notification
phone_number='+917356196142'
def generate_frames(app):
    print (app.config['DETECTION_ON'])
    print ('hello')

    video = cv2.VideoCapture(0)  # Use 0 for webcam, or provide the path to your video file

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect humans in the grayscale frame
        humans, _ = hog.detectMultiScale(gray, winStride=(8, 8), padding=(16, 16), scale=1.05)
      #  if len(humans) > 0:
       #     yield True
        #else:
         #   yield False
       
        # Draw green bounding boxes around detected humans on the original color frame
        if(app.config['DETECTION_ON']):
            for (x, y, w, h) in humans:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    send_notification(phone_number)
                    break

        # Encode frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    video.release()
    cv2.destroyAllWindows()

