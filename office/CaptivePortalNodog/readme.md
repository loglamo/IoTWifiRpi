# Building Raspberry Pi Captive Portal with nodogsplash

## 1. Abstract
This instruction helps to make Raspberry Pi be an Wireless Access Point(AP). You want to access the Internet but the number of cable links is limited. On the other hand, the cost of Wifi Routers maybe quite expensive. Building Raspberry Pi as an access point, the range of your LAN can be extended. 
You should have:
     
     - Raspberry Pi connect to Internet through cable or wifi USB 
     - Configuring Raspberry Pi as an Access point 
     - Using nodogsplash to build a captive portal if you want to manage clients 

## 2. Configure Raspberry Pi as AP
[instruction_build_AP]("https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md") 

- <b> Configure static IP</b>

Generally, you must install some software as hostapd, dhcpcd,dnsmasq as the link instructs.

hostapd package makes Linux system act as an Wifi AP.

      sudo apt-get install hostapd 

install dnsmasq package:

       sudo apt-get install dnsmasq

as the instruction, you must stop them after installing and reboot system.
After system reboot. It is configuring a static IP. It means that we will assign the server the IP address 192.168.4.1, wlan0 in /etc/dhcpcd.conf.
using:

       sudo nano /etc/dhcpcd.conf

to configure the static address as below:

       interface wlan0
             static ip_address=192.168.4.1/24
             nohook wpa_supplicant

Restart dhcpcd Daemon to set up new wlan configuration:

         sudo service dhcpcd restart

Configure dnsmasq as the instruction 

- <b> Configure the Access Point using hostapd</b>

Using file hostapd.conf to configure 

          sudo nano /etc/hostapd/hostapd.conf

Pay attention to configure 'driver', 'channel'. Configure as 'hostapd.conf' file. 

ACt as above link: Start hostapd, start dnsmasq, add routing and masquerade. And reboot. And stop. Do not do with bridge.

Next, configure '/etc/network/interfaces'file as the file interfaces. 

## 3. Install nodogsplash 
[Github address]('https://github.com/nodogsplash/nodogsplash')

[Nodogsplash Doc]('https://nodogsplashdocs.readthedocs.io/en/stable/install.html')

It is a Captive Portal that offers a simple way to provide restricted access to the Internet by showing a splash page to the user before Internet access is granted

Install Nodogsplash as the instruction in Docs. Clone repo from Github, cd to Repo. After that:

      make 

Be sure that the Raspberry Pi had 'libmicrohttpd-dev' package. Without this package, 'Make' will fail.

      sudo apt-get install debhelper dpkg-dev dh-systemd libmicrohttpd-dev

Use 'nodogsplash.conf' file to configure Nodogsplash:

      sudo nano /etc/nodogsplash/nodogsplash.conf

Be sure below informations to be configured:

      GatewayInterface wlan0
      GatewayAddress [your eth0 address]
      MaxClient [as you want]
      ClientIdleTimeout [as you want]

You want to change the interface of server Nodogsplash, you access splash.html to edit:

      sudo nano /etc/nodogsplash/htdocs/splash.html 

Start nodogsplash with:

       sudo nodogsplash 

Use ndsctl in root mode to check informations about Nodogsplash:

        ndsctl status # check status
        # ...etc...Check above Nodogsplash docs for more informations

Now, You can check everything.
Be sure that nodogsplash starts. 