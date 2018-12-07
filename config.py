#!/usr/bin/env python
import os.path
import sys 
 
# change dhcpcd file 
add_dhcpcd = sys.argv[1]
filename = "dhcpcd.conf"
check_ID = "    static ip_address=192.168.4.1/24"
des_string = "    static ip_address=" + add_dhcpcd +"/24"
print(des_string)

des_file = open("dhcpcd_v1.conf","w+")

if not os.path.isfile(filename):
    print 'File does not exist.'
else:
    with open(filename) as f:
        content = f.read().splitlines()
        for line in content:
             if(line == check_ID):
                des_file.write(des_string)
                des_file.write("\n")
               
             else:
                des_file.write(line) 
                des_file.write("\n")
print("coppied dhcpcd.conffig to dhcpcd_v1")
if os.path.isfile(filename):
     os.remove("dhcpcd.conf")
     print("removed dhcpcd")
os.rename("dhcpcd_v1.conf","dhcpcd.conf")
print("rename dhcpcd_v1")

#change hostapd.conf ssid , passwords
add_hostapd = sys.argv[2]
add_hostapd_pass = sys.argv[3]
filename_hostapd = "hostapd.conf"
check_ID_hostapd = "ssid=la_ya"
check_Pass_hostapd = "wpa_passphrase=yamatookada"
des_string_hostapd = "ssid=" + add_hostapd
des_string_hostapd_pass = "wpa_passphrase=" + add_hostapd_pass
print(des_string_hostapd)
print(des_string_hostapd_pass)

des_file_hostapd = open("hostapd_v1.conf","w+")

if not os.path.isfile(filename_hostapd):
    print 'File does not exist.'
else:
    with open(filename_hostapd) as f:
        content = f.read().splitlines()
        for line in content:
             if(line == check_ID_hostapd):
                des_file_hostapd.write(des_string_hostapd)
                des_file_hostapd.write("\n")
               
             elif(line == check_Pass_hostapd):
                des_file_hostapd.write(des_string_hostapd_pass)
                des_file_hostapd.write("\n")
             else:
                des_file_hostapd.write(line) 
                des_file_hostapd.write("\n")
print("coppied dhcpcd.conffig to dhcpcd_v1")
if os.path.isfile(filename_hostapd):
     os.remove("hostapd.conf")
os.rename("hostapd_v1.conf","hostapd.conf")
print("rename hostapd_v1")

