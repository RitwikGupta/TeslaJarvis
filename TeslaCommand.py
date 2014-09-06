# Commands to change the state of the sun_roof

import json, urllib

def change_state(end_state):
    if (end_state not in ["open", "close", "vent", "comfort"]):
		print "bad end_state given"
		return
	url = "https://private-887d5272e-timdorr.apiary-mock.com/vehicles/321/command/sun_roof_control?state=" + end_state
	response = urllib.urlopen(url);
	data = json.loads(response.read())

	if data['result'] == False:
		print "successful state change to " + end_state
	else: 
		print data['reason']