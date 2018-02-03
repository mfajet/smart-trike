import httplib, urllib, base64, json
from dotenv import load_dotenv
load_dotenv(".env")
import os
import json
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
        print (parsed[0]["scores"]["happiness"])

    conn.close()
