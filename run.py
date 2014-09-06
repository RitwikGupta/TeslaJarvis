import urllib2
import json, urllib
import requests

def commandSunRoof(state):
	url = "https://private-887d5272e-timdorr.apiary-mock.com/vehicles/321/command/sun_roof_control?state=" + str(state)
	response = urllib.urlopen(url);
	data = json.loads(response.read())

	if data['result'] == False:
		print 'successful state change'
	else: 
		print data['reason']

def getLatLng():
	url = 'https://private-7faca7132-timdorr.apiary-mock.com/vehicles/321/command/drive_state'
	webFile = urllib2.urlopen(url).read()
	latLngTup = (webFile[webFile.index("latitude")+11:webFile.index("latitude")+20], webFile[webFile.index("longitude")+12:webFile.index("longitude")+22])
	return latLngTup

def parseWeather(lat, lon):
    url = "http://forecast.wdfweather.gov/MapClick.php?lat=" + str(lat) + "&lon=" + str(lon)+"&FcstType=dwml"
    try:
        response = requests.get(url)
    except:
        print "Url request ailed"
        return "URL request failed"
    probIndex = response.content.find('<probability-of-precipitation')
    if probIndex == -1:
        return "No precipitation data"
    probEndIndex = response.content.find('/probability-of-precipitation>')
    valueIndex = response.content.find('<value>', probIndex)
    if probEndIndex < valueIndex:
        return "No precipitation value found"
    length = len('<value>')
    prob =  int(response.content[valueIndex + length:valueIndex+ length + 2])
    return prob

latLngTup = getLatLng()
prob = parseWeather(latLngTup[0], latLngTup[1])

if int(prob) >= 50:
	commandSunRoof("close")
else:
	