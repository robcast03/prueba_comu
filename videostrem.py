from flask import Flask, render_template, Response
import cv2
app=Flask(__name__)
camera = cv2.VideoCapture(0)


def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
           
            faces=detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, 'planta', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2,
                    cv2.LINE_AA) 
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/start_streaming')
def start_streaming():
    global streaming
    streaming = True
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)


