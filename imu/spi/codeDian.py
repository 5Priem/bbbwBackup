#!/usr/bin/python

from Adafruit_BBIO.SPI import SPI

import Adafruit_BBIO.GPIO as GPIO
import time

spi=SPI(1,1)#4 busses, this is bus 0
spi.msh=500000#Frequency
spi.bpw=8#bits per word
spi.cshigh=True#true means you select the chip, depends on the chip, here low means active, normally Low for IMU
spi.threewire=False#if it is true, you just read, otherwise you also send commands
spi.lsbfirst=False#Least significant bit first (left)
#spi.mode=3
spi.open(0,0)#open

#GPIO.setup("P8_11",GPIO.OUT)
#GPIO.output("P8_11",GPIO.HIGH)

try:
	while True:
                res = spi.xfer2([0xFFFF,0xFFFF])#deliver two bytes
		#spi.cshigh=False

                res1 = spi.readbytes(10)
                angle=(res1[0]<<8)|res1[1]#merge leftbyte and rightbyte
                angle1=angle&0x3FFF#move the first two bits
                angle2=float(angle1)/16363*360
		#print("res    is", str(res))
		print("res1   is", str(res1))
		print("angle  is", str(angle))
                print("angle2 is", str(angle2))
                
                time.sleep(.25)
		#spi.cshigh=True

except KeyboardInterrupt:
        spi.close()
