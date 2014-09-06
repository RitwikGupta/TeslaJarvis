# Eric Chen, MHacks IV, Sept 2014
# Allows the user to adjust the sunroof based on the time of day.

from change_state import change_state
from datetime import datetime

#TO DO - need to set some flag so that the program knows not to keep changing status once it is done once
def adjustSunroofTime(days1, day1_hour, day1_minute, day1_status, days2, day2_hour, day2_minute, day2_status):     
    weekdays = { 0:'u', 1:'m', 2:'t', 3:'w', 4:'r', 5:'f', 6:'s'}
    now = datetime.now()
    today = weekdays[now.weekday()]
    if today in days1:
        if now.hour >= day1_hour and now.minute >= day1_minute:
            change_state(day1_status)
    if today in days2:
        if now.hour >= day2_hour and now.minute >= day2_minute:
            change_state(day2_status)

adjustSunroofTime("smtwrfs", 12, 0,"close", "smtwrfs", 16, 30, "open")