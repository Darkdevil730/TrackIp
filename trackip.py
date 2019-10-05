#!/usr/python
from urllib import requests

import json

from os import *
#Tampilan
system("sleep 3")
system("clear")
system("figlet TrackIp | lolcat")

print ("——————————————————————————————")
print ("| Author : D@rk_Devil#666    |")
print ("|   WA   : 089652884613      |")
print ("|  Team  : | CYZ | OFFICIAL  |")
print ("——————————————————————————————")
print ("  ")
ipadd = input("[+] Masukkan Ip : ")
api = 'http://ip-api.com/json'+ipadd
respon = requests.urlopen(api)
dat = json.loads(respon.read())
system("sleep 2")
print ("[+] Status \t: "+dat["Status"])
print ("[+] AS \t\t: "+dat["as"])
print ("[+] City \t: "+dat["city"])
print ("[+] Country \t: "+dat["country"])
print ("[+] CountryCode \t: "+dat["countrycode"])
print ("[+] ISP \t: "+dat["isp"])
lat = print ("[+] Lat \t: "+str(dat["lat"]))
lon = print ("[+] Lon \t: "+str(dat["lon"]))
print ("[+] Region name \t: "+dat["regionname"])
print ("[+] TimeZone \t: "+dat["timezone"])
print ("[+] Link Google Maps : https://maps.google.com/?q=",str(dat["lat"]),str(dat["lon"]))
print ("")
system("exit")


