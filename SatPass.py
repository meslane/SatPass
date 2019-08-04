import urllib.error
from urllib.request import urlopen
import json
from datetime import datetime
import pytz
import tzlocal

k = open('key.txt', 'r')
key = "&apiKey=" + k.read().strip()
k.close()
url = "https://www.n2yo.com/rest/v1/satellite" 

local_tz = tzlocal.get_localzone()

with open('tracked_satellites.txt') as s:
    satellites = s.read().splitlines()
    
with open('location.txt') as l:
    locdata = l.read().splitlines()
    lat = str(locdata[0])
    long = str(locdata[1])
    alt = str(locdata[2])
    mindegs = str(locdata[3])

for id in satellites:
    query = url + "/radiopasses/{}/{}/{}/{}/1/{}".format(id,lat,long,lat,mindegs) + key
    page = urlopen(query).read()
    data = json.loads(page)
 
    name = str(data["info"]["satname"])
    passes = str(data["info"]["passescount"])
    
    print("{} - {} passes:".format(name,passes))
    
    i = 0
    while 1:
        try:
            startutc = datetime.utcfromtimestamp(int(data["passes"][i]["startUTC"]))
            start = startutc.replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%Y-%m-%d %I:%M %p')
            elev = str(data["passes"][i]["maxEl"])
            print("{}, {} DEG".format(start, elev))
            i+=1
        except (IndexError, KeyError) as e:
            break
    print('')
    
input("Press ENTER to continue")