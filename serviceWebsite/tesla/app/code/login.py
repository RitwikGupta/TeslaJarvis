# Eric Chen, MHacks IV, Sept 2014
# Login to Tesla.
# curl --cookie-jar cookies.txt --include --request POST --header "Content-Type: application/x-www-form-urlencoded" --data-binary "user_session%5Bemail%5D='mvanvleet@pillartechnology.com'&user_session%5Bpassword%5D=pitt1234" https://portal.vn.teslamotors.com/login
# curl --cookie cookies.txt --include https://portal.vn.teslamotors.sun_roof_control?state=close


from urllib2 import Request, urlopen
from urllib import urlencode
import urllib2
import json, urllib
import requests
import smtplib
import time
import subprocess

def login_tesla():
	# Fake credentials
	login_dict = {
		"email"   : "mvanvleet@pillartechnology.com",
		"password"   : "pitt1234",
	}
	
	values = urlencode(login_dict)
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	try:
		request = Request("https://portal.vn.teslamotors.com/login", data=values, headers=headers)
		response_body = urlopen(request).read()
		print response_body
	except:
		print "failed to connect"

def commandSunRoof(state):
	url = "https://portal.vn.teslamotors.com/vehicles/19403/command/sun_roof_control?state=" + str(state)
	response = urllib.urlopen(url);
	data = json.loads(response.read())

	# if data['result'] == False:
	# 	print 'successful state change'
	# else: 
	# 	print data['reason']

def main():
	curl = ["curl", "--cookie-jar", "cookies.txt", "--include",
	"--request", "POST", "--header", "Content-Type: application/x-www-form-urlencoded",
	"--data-binary", "user_session%5Bemail%5D='mvanvleet@pillartechnology.com'&user_session%5Bpassword%5D=move1234",
	"https://portal.vn.teslamotors.com/login"]

	response = subprocess.check_output(curl)
	print response

main()

#curl --cookie-jar cookies.txt --include --request POST --header Content-Type: application/x-www-form-urlencoded --data-binary user_session%5Bemail%5D='mvanvleet@pillartechnology.com'&user_session%5Bpassword%5D=pitt1234 https://portal.vn.teslamotors.com/login