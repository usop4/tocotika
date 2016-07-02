import tocotika
import time

toco = tocotika.Toco('/dev/tty.usbserial-AHXMUX35')
i = 0

while True:
	i = i + 10;
	toco.digitalWrite(1,toco.HIGH)
	time.sleep(0.1)
	toco.digitalWrite(1,toco.LOW)
	time.sleep(0.1)
