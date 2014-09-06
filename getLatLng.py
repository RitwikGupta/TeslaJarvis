# import json, urllib

# url = "https://private-7faca7132-timdorr.apiary-mock.com/vehicles"
# response = urllib.urlopen(url);
# data = json.loads(response.read())
# print data[0]["vehicle_id"]

#Importing modules
import urllib2

url = 'https://private-7faca7132-timdorr.apiary-mock.com/vehicles/321/command/drive_state'
webFile = urllib2.urlopen(url).read()
latLngTup = (webFile[webFile.index("latitude")+11:webFile.index("latitude")+20], webFile[webFile.index("longitude")+12:webFile.index("longitude")+22])
print latLngTup