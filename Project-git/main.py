import urllib.parse
from flask import Flask, request
import requests
import json

bot_name = 'majarzab_grad@webex.bot'
roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vYzc2ODNkNTAtMjExNS0xMWVjLTgzZmItMzdmMGFlOWU5ZDNm'
token = 'MjE2YmM1NzMtY2IyYi00ODFhLWE3MTMtMzYwOWI1ZDZmM2MwZmU1MTI4OGItZDUw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
header = {"content-type": "application/json; charset=utf-8", "authorization": "Bearer " + token}

main_api = "http://www.mapquestapi.com/directions/v2/route?"
key = "XVGyxZ4M0k7n6U2hgHAzfEG9pZBPUoai"
dest = "Baltimore, Md" 


def getroute(orig):
    urlMap = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to": dest})
    get_route = requests.get(url=urlMap, verify=True)

    json_data = requests.get(urlMap).json() 
    json_status = json_data["info"]["statuscode"]
    if json_status == 0: 
        markdown = "---"
        markdown += "\nDirections from " + (orig) + " to " + (dest)
        markdown += "\nTrip Duration: " + (json_data["route"]["formattedTime"])
        markdown += "\n---\n"
        markdown += "\n\n---\n\n"
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            markdown += ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")) 
            markdown += "\n\n---\n\n"
    else:
        markdown = "API Status: " + str(json_status) + " = An unsuccessful route call.\n"
    return markdown


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sendMessage():
    webhook = request.json
    url = 'https://webexapis.com/v1/messages'
    msg = {"roomId": webhook["data"]["roomId"]}
    sender = webhook["data"]["personEmail"]
    message = getMessage()
    if (sender != bot_name):
        markdown = getroute(message)
        msg["markdown"] = markdown
        requests.post(url,data=json.dumps(msg), headers=header, verify=True)
    return "200, OK"

def getMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
	get_msgs = requests.get(url, headers=header, verify=True)
	message = get_msgs.json()['text']
	return message

app.run(debug = True)
