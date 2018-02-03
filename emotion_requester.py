import httplib, urllib, base64, json
from dotenv import load_dotenv
from threading import Lock
load_dotenv(".env")
import os
import json

mutex = Lock()

def make_request(body):
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': os.environ.get("EMOTION_API_KEY"),
    }

    params = urllib.urlencode({
    })

    # try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    if not parsed == []:
	if(float(parse[0]["scores"]["happiness"]) > 0.89:
		mutex.acquire()
		try:
			F = open("happy.csv", "rw")
			data = F.readlines()
			data[1] = str(int(data[1]) + 1)
			F.writelines( data )
			F.close()
		finally:
			mutex.release()
        print (parsed[0]["scores"]["happiness"])

    conn.close()
