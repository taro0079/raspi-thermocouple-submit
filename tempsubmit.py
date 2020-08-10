import MAX6675 as MAX6675
import time
import os
import csv
import requests
import datatime

CLK = 24
CS = 4
DO1 = 25

unit = 'c'

thermocouple = MAX6675.MAX6675(CLK, CS,DO1, unit)

time.sleep(1)
running = True

while(running):
    try:
        temp = thermocouple.get_temp()

        time.sleep(1)
    except KeyboardInterrupt:
        running = False


