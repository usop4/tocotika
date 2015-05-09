import tocotika
import time

toko = tocotika.Toko('/dev/tty.usbserial-AHXMUX35')

while True:

	toko.analogWrite(1,0)
	toko.digitalWrite(1,toko.LOW)
	time.sleep(1)

	toko.analogWrite(1,1024)
	toko.digitalWrite(1,toko.HIGH)
	time.sleep(1)
