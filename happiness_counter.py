import cv2
import sys
import json
from emotion_requester import make_request
import threading

threads =[]
count=0
camera = cv2.VideoCapture(0)
button_pressed=0
#
# def read_camera_button():
#     r,w,x = select([dev], [], [])
#     event = dev.read()
#
#     for event in dev.read():
#         print event.value
#         if event.type == ecodes.EV_KEY and event.value==1:
#             button_pressed=event.value
# #
# # t = threading.Thread(target=read_camera_button)
# # t.daemon=True
# # t.start()

while True:
    return_value,image = camera.read()
    print image
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    # print ":what"
    # if button_pressed:
    #     print "GOOD"
    #     button_pressed = 0
    # if count%10==0:
    #     ret, body = cv2.imencode( '.jpg', image )
    #     t = threading.Thread(target=make_request, args = (body,))
    #     threads.append(t)
    #     t.daemon = True
    #     t.start()
    count+=1
    if cv2.waitKey(1)& 0xFF == ord('x') or count==3000:
        break
camera.release()
cv2.destroyAllWindows()
t.join()
