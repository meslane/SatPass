import urllib.error
from urllib.request import urlopen
import json
from datetime import datetime
import pytz
import tzlocal

url = "https://www.n2yo.com/rest/v1/satellite" 

local_tz = tzlocal.get_localzone()

with open('key.txt', 'r') as k:
    key = "&apiKey=" + k.read().strip()

with open('tracked_satellites.txt') as s:
    satellites = s.read().splitlines()
    
with open('configs.txt') as c:
    locdata = c.read().splitlines()
    lat     = str(locdata[0])
    long    = str(locdata[1])
    alt     = str(locdata[2])
    days    = str(locdata[3])
    mindegs = str(locdata[4])

for id in satellites:
    try:
        query = url + "/radiopasses/{}/{}/{}/{}/{}/{}".format(id,lat,long,alt,days,mindegs) + key
        page = urlopen(query).read()
        data = json.loads(page)
    except urllib.error.URLError:
        print("Unable to connect to server\n")
        input("Press ENTER to continue")
        exit(1)
 
    name = str(data["info"]["satname"])
    passes = str(data["info"]["passescount"])
    
    print("{} ({}) - {} passes:".format(name, id, passes))
    
    i = 0
    while 1:
        try:
            startutc = datetime.utcfromtimestamp(int(data["passes"][i]["startUTC"]))
            start = startutc.replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%Y-%m-%d %I:%M %p')
            elev = float(data["passes"][i]["maxEl"])
            saz = float(data["passes"][i]["startAz"]) 
            sazc = str(data["passes"][i]["startAzCompass"])
            maz = float(data["passes"][i]["maxAz"])
            mazc = str(data["passes"][i]["maxAzCompass"])
            eaz = float(data["passes"][i]["endAz"])
            eazc = str(data["passes"][i]["endAzCompass"])
            print("{0}, START: {1:06.2f} DEG {2} MAX: {3:06.2f} DEG {4} ELEV {5:.2f} DEG END: {6:06.2f} DEG {7}".format(start, saz, sazc.ljust(3), maz, mazc.ljust(3), elev, eaz, eazc.ljust(3)))
            i+=1
        except (IndexError, KeyError) as e:
            break
    print('')
    
input("Press ENTER to continue")