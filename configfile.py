import os
from shutil import copyfile
import sys 
#/home/pi/Desktop/IoTWifiRpi
#modify dhcpcd file 
changeIP = sys.argv[1]
with open('dhcpcd.conf', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('192.168.4.1', changeIP)
# Write the file out again
with open('dhcpcd.conf', 'w') as file:
  file.write(filedata)
print("modify dhcpcd")

# modify hostapd file
# change ssid 
changeSSID = sys.argv[2]
with open('hostapd.conf', 'r') as file :
  filedata_ssid = file.read()
filedata_ssid = filedata_ssid.replace('hiro', changeSSID)
# Write the file out again
with open('hostapd.conf', 'w') as file:
  file.write(filedata_ssid)
print("modify hostapd file ")

# change passw
changePW = sys.argv[3]
with open('hostapd.conf', 'r') as file :
  filedata_pw = file.read()
filedata_pw = filedata_pw.replace('yamato', changePW)
# Write the file out again
with open('hostapd.conf', 'w') as file:
  file.write(filedata_pw)
print("modify hostapd file ")
