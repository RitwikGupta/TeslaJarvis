
import urllib2

def getLatLng():
	url = 'https://private-7faca7132-timdorr.apiary-mock.com/vehicles/321/command/drive_state'
	webFile = urllib2.urlopen(url).read()
	latLngTup = (webFile[webFile.index("latitude")+11:webFile.index("latitude")+20], webFile[webFile.index("longitude")+12:webFile.index("longitude")+22])
	return latLngTup