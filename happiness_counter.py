import cv2
import sys
import json
from emotion_requester import make_request
import threading
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

threads =[]
count=0
camera = cv2.VideoCapture(-1)
last = time.time()
while True:
    return_value,image = camera.read()
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    input_state = GPIO.input(8) & GPIO.input(10)
    if not input_state and time.time() - last >= 1.5:
        print "Pic Taken"
        ret, body = cv2.imencode( '.jpg', image )
        last=time.time()
        t = threading.Thread(target=make_request, args = (body,))
        threads.append(t)
        t.daemon = True
        t.start()
    elif cv2.waitKey(1)& 0xFF == ord('x'):
        break
camera.release()
cv2.destroyAllWindows()
for thread in threads:
    thread.join()
