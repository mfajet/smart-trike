
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        return_value,image = camera.read()
        print image.shape
        ret, frame = cv2.imencode( '.jpg', image )
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    app.run(host='10.108.212.238')
