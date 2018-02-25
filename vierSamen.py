# Servo: 
# + in P9.7
# gnd in P9.2
# analog in P9.14

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

# IMU's: (MPU9250)
# SDA - SDA
# SCL - SCL
# 3.3V - VDD
# GND - GND
# Pull up resistor to VDD for each IMU (I used 10k)


import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.PWM as pwm
from Adafruit_BBIO.SPI import SPI
import time
import mpu9250

#Servo
servopin = "P9_14"
dutyMin = 3
dutyMax = 14.5
dutySpan = dutyMax-dutyMin
pwm.start(servopin,5, 60.0, 1)

#Insole
adc.setup()
heelR = "P9_40"
heelL = "P9_39"

#Encoder
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

#IMU's
try:
	mp1 = mpu9250.SL_MPU9250(0x68,2)
	mp2 = mpu9250.SL_MPU9250(0x69,2)
except:
	print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")

while True:
	#Servo
	ctr = ctr + 10
	angle = ctr
	angle_f = float(angle)
	duty = 100 - ((angle_f/180)*dutySpan+dutyMin)
	pwm.set_duty_cycle(servopin, duty)
	#print("ctr: %s angle: %s duty: %s"%(ctr,angle,duty))
	if ctr >= 179:
		ctr=1
	#time.sleep(0.1)

	#Insole
	valueHeelL=adc.read(heelL)
	print("heelL: "+ str(valueHeelL))
	#time.sleep(0.1)
	
	#Encoder
	res = spi.xfer2([0xFFFF,0xFFFF])#deliver two bytes
        res1 = spi.readbytes(2)#Read 2 bytes
        angle=(res1[0]<<8)|res1[1]#merge leftbyte and rightbyte
        angle1=angle&0x3FFF#move the first two bits
        angle2=float(angle1)/16363*360
        print("Angle is: "+str(angle2))


	#IMU's: MPU9250
	try:
		ax1, ay1, az1 = mp1.getAccel()
		gx1, gy1, gz1 = mp1.getGyro()
		print "Eerste IMU values:"
		print "Ax1: ",ax1
		print "Ay1: ",ay1
		print "Az1: ",az1

		print "Gx1: ",gx1
		print "Gy1: ",gy1
		print "Gz1: ",gz1
	except:
		print("Finito1")

	try:
		ax2, ay2, az2 = mp2.getAccel()
		gx2, gy2, gz2 = mp2.getGyro()
		print "Tweede IMU values:"
		print "Ax2: ",ax2
		print "Ay2: ",ay2
		print "Az2: ",az2

		print "Gx2: ",gx2
		print "Gy2: ",gy2
		print "Gz2: ",gz2
	except:
		print("Finito2")

        time.sleep(0.1)
