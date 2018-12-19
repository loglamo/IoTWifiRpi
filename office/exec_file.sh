#!/bin/bash
<<<<<<< HEAD
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
python ./config.py $1 $2 $3
=======
sudo apt-get install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
>>>>>>> 97120bad6f5345dbcb1bffc0f66f8dd2955aad22
sudo cp ./dhcpcd.conf /etc/dhcpcd.conf
sudo service dhcpcd restart
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo cp ./dnsmasq.conf /etc/dnsmasq.conf
sudo cp ./hostapd.conf /etc/hostapd/hostapd.conf
sudo cp ./hostapd /etc/default/hostapd
sudo systemctl start hostapd
sudo systemctl start dnsmasq
sudo cp ./sysctl.conf /etc/sysctl.conf
<<<<<<< HEAD
sudo reboot
=======
sudo reboot
>>>>>>> 97120bad6f5345dbcb1bffc0f66f8dd2955aad22
