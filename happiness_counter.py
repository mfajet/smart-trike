import cv2
import sys
import json
from emotion_requester import make_request
import threading

threads =[]
count=0
camera = cv2.VideoCapture(-1)

while True:
    return_value,image = camera.read()
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    if cv2.waitKey(1)& 0xFF == ord('k'):
        ret, body = cv2.imencode( '.jpg', image )
        t = threading.Thread(target=make_request, args = (body,))
        threads.append(t)
        t.daemon = True
        t.start()
    elif cv2.waitKey(1)& 0xFF == ord('x'):
        break
camera.release()
cv2.destroyAllWindows()
t.join()
