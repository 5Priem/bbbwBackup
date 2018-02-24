import mpu9250
import time
mp = mpu9250.SL_MPU9250(0x68,2)

while True:
	ax, ay, az = mp.getAccel()
	gx, gy, gz = mp.getGyro()
	print "Ax: ",ax
	print "Ay: ",ay
	print "Az: ",az

	print "Gx: ",gx
	print "Gy: ",gy
	print "Gz: ",gz

	time.sleep(0.3)
