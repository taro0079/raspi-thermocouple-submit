import MAX6675 as MAX6675
import time
import os
import csv
import requests
import datetime

CLK = 24
CS = 4
DO1 = 25
url = 'https://recievetempflaskapi.herokuapp.com/post'
unit = 'c'

thermocouple = MAX6675.MAX6675(CLK, CS,DO1, unit)

# csv file confirmation


time.sleep(1)
running = True
starttime = time.time() # get start time
while(running):
    try:
        nowtimeforfile = datetime.datetime.now()
        fileName = str(nowtimeforfile.year) + '-' + str(nowtimeforfile.month) + '-' + str(nowtimeforfile.day) + '-data.csv'
        nowtime = time.time() # get now time
        elapsedtime = round(nowtime - starttime) # elapsed time 
        divtime = 0.5 # minuites

        if elapsedtime % (divtime * 60) == 0:
            response = requests.post(url, data= {'test':'test'})
            print(response.status_code)
            print(response.text)
            dtNow = datetime.datetime.now()
            temp = thermocouple.get_temp()
            data = [dtNow, temp]

            # csv file make
            if os.path.exists(fileName) == False:
                with open(fileName, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['date', 'temperature'])
            else:
                with open(fileName, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)





        time.sleep(1)
    except KeyboardInterrupt:
        running = False


