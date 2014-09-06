import json, urllib

def vehicleId():
    url = "https://private-7faca7132-timdorr.apiary-mock.com/vehicles"
    jsonurl = urllib.urlopen(url);
    text = json.loads(jsonurl.read())
    return text[0]["vehicle_id"]