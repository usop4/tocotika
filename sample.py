import tocotika
import time

toco = tocotika.Toco('/dev/tty.usbserial-AHXMUX35')

while True:

	toco.analogWrite(1,0)
	toco.digitalWrite(1,toco.LOW)
	time.sleep(1)

	toco.analogWrite(1,1024)
	toco.digitalWrite(1,toco.HIGH)
	time.sleep(1)
