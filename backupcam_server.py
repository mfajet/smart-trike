
from flask import Flask, render_template, Response
import cv2

def overlay_transparent(background_img, img_to_overlay_t):
    bg_img = background_img.copy()

    b,g,r,a = cv2.split(img_to_overlay_t)
    overlay_color = cv2.merge((b,g,r))
    mask = a
    h, w, _ = overlay_color.shape
    original = bg_img[:,:]
    img1_bg = cv2.bitwise_and(original.copy(),original.copy(),mask = cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)
    bg_img[:,:] = cv2.add(img1_bg, img2_fg)

    return bg_img

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        return_value,image = camera.read()
        overlay = cv2.imread("overlay.png",-1)
        alpha=0.5
        # cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
        image = overlay_transparent(image,overlay)
        ret, frame = cv2.imencode( '.jpg', image )
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    app.run(host='10.108.212.238')
