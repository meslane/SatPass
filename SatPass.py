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
    
with open('location.txt') as l:
    locdata = l.read().splitlines()
    lat     = str(locdata[0])
    long    = str(locdata[1])
    alt     = str(locdata[2])
    mindegs = str(locdata[3])

for id in satellites:
    try:
        query = url + "/radiopasses/{}/{}/{}/{}/1/{}".format(id,lat,long,lat,mindegs) + key
        page = urlopen(query).read()
        data = json.loads(page)
    except urllib.error.URLError:
        print("Unable to connect to server\n")
        input("Press ENTER to continue")
        exit(1)
 
    name = str(data["info"]["satname"])
    passes = str(data["info"]["passescount"])
    
    print("{} - {} passes:".format(name,passes))
    
    i = 0
    while 1:
        try:
            startutc = datetime.utcfromtimestamp(int(data["passes"][i]["startUTC"]))
            start = startutc.replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%Y-%m-%d %I:%M %p')
            elev = float(data["passes"][i]["maxEl"])
            dir = str(data["passes"][i]["startAzCompass"])
            print("{0}, {1:.2f} DEG {2}".format(start, elev, dir))
            i+=1
        except (IndexError, KeyError) as e:
            break
    print('')
    
input("Press ENTER to continue")