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

LOW = 0
HIGH = 1

s = serial.Serial(
	port='/dev/tty.usbserial-AHXMUX35',
	baudrate=115200)

def digitalWrite(pin,value):
	cmd = ':788001'
	if pin == 1:
		if value == HIGH:
			cmd = cmd + '0101'+'FFFFFFFFFFFFFFFF'
		if value == LOW:
			cmd = cmd + '0001'+'FFFFFFFFFFFFFFFF'			
	if pin == 2:
		if value == HIGH:
			cmd = cmd + '0202'+'FFFFFFFFFFFFFFFF'
		if value == LOW:
			cmd = cmd + '0002'+'FFFFFFFFFFFFFFFF'
	if pin == 3:
		if value == HIGH:
			cmd = cmd + '0404'+'FFFFFFFFFFFFFFFF'
		if value == LOW:
			cmd = cmd + '0004'+'FFFFFFFFFFFFFFFF'
	if pin == 4:
		if value == HIGH:
			cmd = cmd + '0808'+'FFFFFFFFFFFFFFFF'
		if value == LOW:
			cmd = cmd + '0008'+'FFFFFFFFFFFFFFFF'
	cmd = cmd + 'XX\r\n'
	s.write(cmd)
	time.sleep(0.1)
	return cmd	
	
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
		digitalWrite(1,LOW)
		wait(1)

		analogWrite(1,1024)
		digitalWrite(1,HIGH)
		wait(1)

