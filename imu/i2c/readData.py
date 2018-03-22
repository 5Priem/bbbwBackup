#Library from:
#https://github.com/boyaki-machine/MPU-9250/blob/master/mpu9250.py

#Connections:
#SDA - SDA
#SCL - SCL
#3.3V - VDD
#GND - GND
#Pull up resistor to VDD for each IMU (I used 10k)

import mpu9250
import time
import os

try:
	mp1 = mpu9250.SL_MPU9250(0x68,2)
	mp2 = mpu9250.SL_MPU9250(0x69,2)
except:
	print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")
fileName = "sampleData"

data = open(fileName+ '.txt', 'a+')
data.write("CSV format: Accelerometer x value, acclerometer y value, accelerometer z value, gyroscope x value, gyroscope y value, gyroscope z value"+'\n')
data.close()
while True:
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
		data = open(fileName+ '.txt', 'a+')
		data.write(str(ax1)+','+str(ay1)+','+str(az1)+','+str(gx1)+','+str(gy1)+','+str(gz1)+'\n')
		data.close()


	except:
		print("Finito1")

	#try:
	#	ax2, ay2, az2 = mp2.getAccel()
	#	gx2, gy2, gz2 = mp2.getGyro()
	#	print "Tweede IMU values:"
	#	print "Ax2: ",ax2
	#	print "Ay2: ",ay2
	#	print "Az2: ",az2

	#	print "Gx2: ",gx2
	#	print "Gy2: ",gy2
	#	print "Gz2: ",gz2
	#except:
	#	print("Finito2")

	time.sleep(0.3)
