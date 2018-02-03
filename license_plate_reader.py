import cv2
import subprocess

def make_lp_request():
	camera = cv2.VideoCapture(0)

	count = 0
	while(True):
		return_value, image = camera.read()
		img_file = 'test' +str( count ) + '.jpg'
		cv2.imwrite(img_file, image)

		print subprocess.check_output(['alpr', img_file])
		count+=1
		if cv2.waitKey(1) & 0xFF == ord('x') or count==3000:
			break
	camera.release()
