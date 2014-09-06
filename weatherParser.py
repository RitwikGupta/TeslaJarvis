# Eric Chen, MHacks IV, Sept 2014
# TeslaJarvis - closes sunroof if rain on Tesla Model S
# Returns probability of rain given a latitude and longitude.

import requests

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
    print prob
    return prob
    

parseWeather(42.46943, -83.51851943162569)
