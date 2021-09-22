import requests
import urllib.parse

main_api = "http://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C." 
dest = "Baltimore, Md" 
key = "XVGyxZ4M0k7n6U2hgHAzfEG9pZBPUoai"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to": dest})

print("URL: " + (url)) 
 
json_data = requests.get(url).json() 
json_status = json_data["info"]["statuscode"]

if json_status == 0: 
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("=============================================") 
    print("Directions from " + (orig) + " to " + (dest)) 
    print("Trip Duration:   " + (json_data["route"]["formattedTime"])) 
    print("=============================================\n")

    for each in json_data["route"]["legs"][0]["maneuvers"]: 
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")) 
    print("=============================================\n")
else:
    print("API Status: " + str(json_status) + " = An unsuccessful route call.\n")