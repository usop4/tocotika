#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
TocoStickにPythonからコマンドを送るスクリプト
ref.
http://tocos-wireless.com/jp/products/TWE-Lite-USB/control.html
"""

import serial
import time
import sys

s = serial.Serial(
	port='/dev/tty.usbserial-AHXMUX35',
	baudrate=115200)

def analogWrite(pin,value):
	cmd = ':7880010000'
	if pin == 1:
		cmd = cmd + ''+hex4(value)+'FFFFFFFFFFFF'
	if pin == 2:
		cmd = cmd + 'FFFF'+hex4(value)+'FFFFFFFF'
	if pin == 3:
		cmd = cmd + 'FFFFFFFF'+hex4(value)+'FFFF'
	if pin == 4:
		cmd = cmd + 'FFFFFFFFFFFF'+hex4(value)+''
	cmd = cmd + 'XX\r\n'
	s.write(cmd)
	time.sleep(0.1)
	return cmd

def wait(t):
	time.sleep(t)

def hex4(value):
	return "{0:x}".format(value).zfill(4).upper()

if __name__ == '__main__':

	while True:
		
		analogWrite(1,0)
		wait(1)
		analogWrite(1,1024)
		wait(1)
