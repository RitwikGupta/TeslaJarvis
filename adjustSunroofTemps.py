import urllib2, re
from change_state import change_state

# Opens the sunroof to vent if inside is hotter than outside by 2 degrees celcius
def adjustSunroofTemps():
    url = "https://private-13a4ee565-timdorr.apiary-mock.com/vehicles/321/command/climate_state"
    webFile = urllib2.urlopen(url).read()
    temps = (webFile[webFile.index("inside_temp")+14:webFile.index("inside_temp")+18], webFile[webFile.index("outside_temp")+15:webFile.index("outside_temp")+19])
    temps_list = list(temps)
    for i in range(len(temps_list)):
        temps_list[i] = float(re.match(r'\d+.\d+', temps[i]).group())
    if temps_list[0] > temps_list[1] + 2:
        change_state("vent")