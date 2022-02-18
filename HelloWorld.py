!/usr/bin/python3

from datetime import datetime
from datetime import date
today = date.today()
now = datetime.now()

todays_date = today.strftime("%B %d, %Y")
current_time = now.strftime("%H:%M:%S")

print("Integrating Jenkins with GIT")
print("Date : ", todays_date)
print("Current Time : ", current_time)