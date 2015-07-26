import tocotika
import time

toco = tocotika.Toco('/dev/tty.usbserial-AHXMUX35')
i = 0

while True:
	i = i + 10;
	toco.analogWrite(1,i % 256)
	time.sleep(0.01)

