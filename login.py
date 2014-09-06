# Eric Chen, MHacks IV, Sept 2014
# Login to Tesla.

from urllib2 import Request, urlopen
from urllib import urlencode

def login_tesla():
	# Fake credentials
	login_dict = {
		"email"   : "hello@tesla.com",
		"password"   : "teslaRules",
	}
	
	values = urlencode(login_dict)
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	try:
		request = Request("https://private-13a4ee565-timdorr.apiary-mock.com/login", data=values, headers=headers)
		response_body = urlopen(request).read()
		print response_body
	except:
		print "failed to connect"