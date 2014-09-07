import urllib2
import json, urllib
import requests
import smtplib
import time
import sys

value = sys.argv

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'teslajarvis@gmail.com', 'fuckitshipit' )

PNUMBER = sys.argv[3]
PPROVIDER = sys.argv[4]

if PPROVIDER.lower() == "verizon":
	PPROVIDER = "@vtext.com"
elif PPROVIDER.lower() == "att":
	PPROVIDER = "@txt.att.net"
elif PPROVIDER.lower() == "sprint":
	PPROVIDER = "@messaging.sprintpcs.com"
else:
	PPROVIDER = "@tmomail.net"

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
	url = "http://forecast.weather.gov/MapClick.php?lat=" + lat + "&lon=" + lon + "&FcstType=dwml"
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

def vehicleId():
    url = "https://private-7faca7132-timdorr.apiary-mock.com/vehicles"
    jsonurl = urllib.urlopen(url);
    text = json.loads(jsonurl.read())
    return text[0]["vehicle_id"]

def main1():
    latLngTup = getLatLng()
    prob = parseWeather(latLngTup[0], latLngTup[1])
    prob = 60
    if int(prob) >= 50:
    	commandSunRoof("close")
    	server.sendmail( 'teslaalert@tls.com', PNUMBER + PPROVIDER, 'We closed your roof because the probablity of precipitation in your area was ' + str(prob) + "%")
    else:
    	print "To be implemented"
def main2():
	url = 'https://private-7faca7132-timdorr.apiary-mock.com/vehicles/321/command/drive_state'
	webFile = urllib2.urlopen(url).read()
	latLngTup = (webFile[webFile.index("latitude")+11:webFile.index("latitude")+20], webFile[webFile.index("longitude")+12:webFile.index("longitude")+22])
	url = "https://private-887d5272e-timdorr.apiary-mock.com/vehicles/321/command/charge_state"
	webFile = urllib2.urlopen(url).read()
	chargingBatCurrTup = (webFile[webFile.index("state")+9:webFile.index("state")+17], webFile[webFile.index("battery_current")+18:webFile.index("battery_current")+22])
	print chargingBatCurrTup
	lat = float(latLngTup[0])
	lon = float(latLngTup[1])
	#If location is home
	print "Out"
	if abs(float(latLngTup[0]) - lat) < .0005 and abs(float(latLngTup[1]) - lon) < .0005:
		print "In"
		#if not charging

		if chargingBatCurrTup[0] != "Charging" and float(chargingBatCurrTup[1]) <= -.01:
			print "sent"
			server.sendmail( 'teslaalert@tls.com', PNUMBER + PPROVIDER, 'You forgot to plug in your car!' )

		else:
			return True
	else:
		return False


if __name__ == '__main__':
	x = 1
	while x == 1:
		if value[1] == '0' and value[2] == 'None':
			main1()
			break
		elif value[1] == 'None' and value[2] == '1':
			main2()
			break
		elif value[1] == '0' and value[2] == '1':
			main2()
			main1()
			break
		else:
			break

