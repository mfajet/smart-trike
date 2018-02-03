import cv2
import subprocess

def make_lp_request(image):
#	camera = cv2.VideoCapture(0)

#	count = 0
#	while(True):
#		return_value, image = camera.read()
#		img_file = 'test' +str( count ) + '.jpg'
	cv2.imwrite('lol_image.jpg', image)
	data = subprocess.check_output(['alpr', 'lol_image.jpg']).split("\n")
	print data
	print data[1]

	if (not data[0] == "No license plates found."):
		data_split = data[1].strip().split(" ")
		print data_split[1]
		print data_split[3]
 
		if data_split[3] > 0.85: 
			F = open("plate.csv", "r")
			data = F.readlines()
			F.close()
			F = open("plate.csv", "w")
			F.writelines("plate\n")
			F.writelines(data_split[1])
			F.close()

#		count+=1
#		if cv2.waitKey(1) & 0xFF == ord('x') or count==3000:
#			break
#	camera.release()

