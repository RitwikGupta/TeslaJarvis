

import json, urllib

url = "https://private-887d5272e-timdorr.apiary-mock.com/vehicles/321/command/sun_roof_control?state=open"
response = urllib.urlopen(url);
data = json.loads(response.read())

if data['result'] == False:
	print 'successful state change'
else: 
	print data['reason']