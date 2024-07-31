import pytz
from datetime import datetime
from pyfiglet import figlet_format
import os
from time import sleep

class timeZones():
    def __init__(self, tz):
        self.tz = tz

    def update(self):
        os.system("clear")
        chosen_tz = pytz.timezone(self.tz)
        dt = datetime.now(chosen_tz).strftime("%A : %H : %M : %S %p")
        print(f"{self.tz}: ")
        ff = figlet_format(f"{dt}", width = 200)
        print(ff)
        sleep(1)
        self.update()


def main():
    tz = pytz.common_timezones
    # tz = ["US/Eastern", "US/Central", "US/Mountain", "US/Pacific"]
    for i, time in enumerate(tz, start = 1):
        print(f"{i}: {time}")

    choice = int(input("Which timezone would you like to see the clock for? (type number): "))

    time_choice = tz[choice-1]
    
    oClock = timeZones(time_choice)
    oClock.update()

main()