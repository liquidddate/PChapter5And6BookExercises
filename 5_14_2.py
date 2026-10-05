from time import time

seconds_per_day = 60 * 60 * 24
seconds_per_hour = 60 * 60
now = int(time())
days = now // seconds_per_day
print(f"Days: {days}")
remainder = now % seconds_per_day
hours = remainder // seconds_per_hour
print(f"Hours: {hours}")
remainder = remainder % seconds_per_hour
minutes = remainder // 60
print(f"Minutes: {minutes}")
seconds = remainder % 60
print(f"Seconds: {seconds}")