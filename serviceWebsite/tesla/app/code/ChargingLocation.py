import urllib2
import smtplib
import urllib
import json

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'teslajarvis@gmail.com', 'fuckitshipit' )

def chargingLocation(lat, lon):

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
			server.sendmail( 'teslaalert@tls.com', '4129252235@vtext.com', 'You forgot to plug in your car!' )

		else:
			return True
	else:
		return False
		

chargingLocation("1", "2")