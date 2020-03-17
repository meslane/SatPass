import urllib.error
from urllib.request import urlopen
import json
from datetime import datetime
import time

url = "https://www.n2yo.com/rest/v1/satellite"

class posData:
    def __init__(self, az, elev, timestamp):
        self.az = az
        self.elev = elev
        self.timestamp = timestamp

with open('key.txt', 'r') as k:
    key = "&apiKey=" + k.read().strip()

with open('configs.txt') as c:
    locdata = c.read().splitlines()
    lat     = str(locdata[0])
    long    = str(locdata[1])
    alt     = str(locdata[2])

satID = input("Input satellite's NORAD catalog ID: ")
print()

try:
    tlequery = url + "/tle/{}/{}".format(satID, key)
    tledata = json.loads(urlopen(tlequery).read())
except urllib.error.URLError:
    print("ERROR - Unable to Connect to API")
    exit()

if tledata["info"]["satname"] == None:
    print("ERROR - Uncatalogued ID: the given SATCAT ID is unassigned")
    exit()

print("Object Name: " + tledata["info"]["satname"] + '\n')

if str(tledata["tle"]) == '':
    print("ERROR - Null TLE: object is either decayed or outside of Earth's SOE")
    exit()

while True:
    try:
        query = url + "/positions/{}/{}/{}/{}/300/{}".format(satID, lat, long, alt, key)
        data = json.loads(urlopen(query).read())
    except urllib.error.URLError:
        print("ERROR - Unable to Connect to API")
        break
        
    posList = []

    for entry in data["positions"]:
        posList.append(posData(entry["azimuth"], entry["elevation"], entry["timestamp"]))
    
    if (int(posList[1].timestamp) == 0):
        print ("ERROR - Empty Positional Data: satellite is likely no longer on orbit")
        break
    
    for i in range(300):
        print(posList[i].az)
        print(posList[i].elev)
        print(posList[i].timestamp)
        print('')
        
        if i != 299:
            while int(datetime.now().timestamp()) <  int(posList[i + 1].timestamp):
                pass