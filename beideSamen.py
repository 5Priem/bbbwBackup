# Servo: 
# + in 7
# gnd in 2
# analog in 14

# Insole: 
# Heel R naar analog input (pin 39)
# Com 1 naar 3.3V (pin 3)
# Tussen Heel R en Analog input: resistor naar ground (pin 1)
# Dan tzelfde voor elke connectie, en elk een aparte res en aparte analog input

# Encoder:
# SPIO_CSO  P9.17 => SS   purple
# SPIO_DO   P9.21 => MISO green
# SPIO_D1   P9.18 => MOSI yellow
# SPIO_SCLK P9.22 => SCK  blue
# DGND gnd                gray
# 3V3                     orange
# OM SPI TE ENABLEN
# config-pin P9.20 spi
# en da me alle pins


import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.PWM as pwm
from Adafruit_BBIO.SPI import SPI
import time

servopin = "P9_14"
dutyMin = 3
dutyMax = 14.5
dutySpan = dutyMax-dutyMin
pwm.start(servopin,5, 60.0, 1)

adc.setup()
heelR = "P9_40"
heelL = "P9_39"

spi=SPI(0,0)#4 busses, this is bus 0
spi.msh=10000#Frequency
spi.bpw=8#bits per word
spi.cshigh=False#true means you select the chip, depends on the chip, here low means active, normally Low for IMU
spi.threewire=False#if it is true, you just read, otherwise you also send commands
spi.lsbfirst=False#Least significant bit first (left)
spi.open(0,0)#open

# add an extra parameter 1 if servo doesn't turn, 1 changes polarity
#PWM.start(channel, duty, freq, polarity), polarity is 0 by default
ctr=1

while True:
	ctr = ctr + 10
	angle = ctr
	angle_f = float(angle)
	duty = 100 - ((angle_f/180)*dutySpan+dutyMin)
	pwm.set_duty_cycle(servopin, duty)
	#print("ctr: %s angle: %s duty: %s"%(ctr,angle,duty))
	if ctr >= 179:
		ctr=1
	time.sleep(0.1)

	valueHeelL=adc.read(heelL)
	print("heelL: "+ str(valueHeelL))
	time.sleep(0.1)
	
	res = spi.xfer2([0xFFFF,0xFFFF])#deliver two bytes
        res1 = spi.readbytes(2)
        angle=(res1[0]<<8)|res1[1]#merge leftbyte and rightbyte
        angle1=angle&0x3FFF#move the first two bits
        angle2=float(angle1)/16363*360
        print("Angle is: "+angle2)
        #print(angle2)
	time.sleep(0.1)
