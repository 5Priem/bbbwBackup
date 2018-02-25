#!/usr/bin/python

#SPIO_CSO  P9.17 => SS   purple
#SPIO_DO   P9.21 => MISO green
#SPIO_D1   P9.18 => MOSI yellow
#SPIO_SCLK P9.22 => SCK  blue

#DGND gnd                gray
#3V3                     orange

#OM SPI TE ENABLEN
#config-pin P9.20 spi
#en da me alle pins



from Adafruit_BBIO.SPI import SPI

import Adafruit_BBIO.GPIO as GPIO
import time

spi=SPI(0,0)#4 busses, this is bus 0
spi.msh=10000#Frequency
spi.bpw=8#bits per word
spi.cshigh=False#true means you select the chip, depends on the chip, here low means active, normally Low for IMU
spi.threewire=False#if it is true, you just read, otherwise you also send commands
spi.lsbfirst=False#Least significant bit first (left)
spi.open(0,0)#open

#GPIO.setup("P8_11",GPIO.OUT)
#GPIO.output("P8_11",GPIO.HIGH)

try:
	while True:
                res = spi.xfer2([0xFFFF,0xFFFF])#deliver two bytes

                res1 = spi.readbytes(2)#Read 2 bytes
                angle=(res1[0]<<8)|res1[1]#merge leftbyte and rightbyte
                angle1=angle&0x3FFF#move the first two bits
                angle2=float(angle1)/16363*360
                print("data is")
                print(angle2)
                time.sleep(.25)
except KeyboardInterrupt:
        spi.close()
