#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Martin Ellguth
This temporary script file is located here:
/home/sc/.spyder2/.temp.py
"""

# TEST OF PI C 884K004 communication via TCP/IP

import time
import sys
import serial

DEVICE='/dev/ttyUSB0'

s = serial.Serial(DEVICE, baudrate=9600)
    
if not s.isOpen():
    print "Connection to", DEVICE, "not succesful."
    exit(0) 
print "connected"
while True:
    userstr = sys.stdin.readline()
    if userstr.startswith('exit'):
        break
    command=userstr.strip('\n\r')
    print "sending:", command
    s.write(command+chr(10))#"\n\r")
    time.sleep(0.1)
    try:
	buf = s.read(s.inWaiting())
    	print "answer:", buf
    except:
		pass

s.close()