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

HIGH = 1
LOW = 0

class Toko:
	def __init__(self,port):
		self.serial = s = serial.Serial(
			port=port,
			baudrate=115200)

	def digitalWrite(self,pin,value):
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
		self.serial.write(cmd)
		time.sleep(0.1)
		return cmd

	def analogWrite(self,pin,value):
		cmd = ':7880010000'
		if pin == 1:
			cmd = cmd + ''+self.hex4(value)+'FFFFFFFFFFFF'
		if pin == 2:
			cmd = cmd + 'FFFF'+self.hex4(value)+'FFFFFFFF'
		if pin == 3:
			cmd = cmd + 'FFFFFFFF'+self.hex4(value)+'FFFF'
		if pin == 4:
			cmd = cmd + 'FFFFFFFFFFFF'+self.hex4(value)+''
		cmd = cmd + 'XX\r\n'
		self.serial.write(cmd)
		time.sleep(0.1)
		return cmd

	def hex4(self,value):
		return "{0:x}".format(value).zfill(4).upper()

if __name__ == '__main__':

	toko = Toko('/dev/tty.usbserial-AHXMUX35')

	while True:

		toko.analogWrite(1,0)
		toko.digitalWrite(1,LOW)
		time.sleep(1)

		toko.analogWrite(1,1024)
		toko.digitalWrite(1,HIGH)
		time.sleep(1)
