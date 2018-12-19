#!/bin/bash
python ./configfile.py $1 $2 $3
sudo apt-get install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
sudo cp ./dhcpcd.conf /etc/dhcpcd.conf
sudo service dhcpcd restart
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo cp ./dnsmasq.conf /etc/dnsmasq.conf
sudo cp ./hostapd.conf /etc/hostapd/hostapd.conf
sudo cp ./hostapd /etc/default/hostapd
sudo systemctl start hostapd
sudo systemctl start dnsmasq
sudo cp ./sysctl.conf /etc/sysctl.conf
sudo reboot
