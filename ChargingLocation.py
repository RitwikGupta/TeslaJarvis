from urllib2 import Request, urlopen

def chargingLocation(lat, lon):

	request = Request("https://private-887d5272e-timdorr.apiary-mock.com/vehicles/{id}/command/drive_state")
	response_body = urlopen(request).read()
	print response_body


	//If location is home
	if abs(response_body['latitude'] - lat) < .0005 and abs(response_body['longitude'] - lon) < .0005:

		//if not charging
		from urllib2 import Request, urlopen
		request = Request("https://private-887d5272e-timdorr.apiary-mock.com/vehicles/321/command/charge_state")
		response_body = urlopen(request).read()
		print response_body

		if response_body['charging_state'] != "Complete" and response_body['battery_current'] >= -.01:

			//send text

			//open charge port
			from urllib2 import Request, urlopen
			request = Request("https://private-887d5272e-timdorr.apiary-mock.com/vehicles/{id}/command/charge_port_door_open")
			response_body = urlopen(request).read()
			print response_body

		else		
			return True
	else:
		return False
		

