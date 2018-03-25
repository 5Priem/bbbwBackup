import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time
import os

#*********SETUP*********#
try:
	mp=mpu9250.SL_MPU9250(0x69, 2)
except:
	print("First IMU (in Setup) not found")
footLeft         = "P8_7"
footRight        = "P8_8"
ankleLeft        = "P8_9"
ankleRight       = "P8_10"

print("Initialising GPIO's...")
GPIO.setup(footLeft, GPIO.OUT)
GPIO.setup(footRight, GPIO.OUT)
GPIO.setup(ankleLeft, GPIO.OUT)
GPIO.setup(ankleRight, GPIO.OUT)

GPIO.output(footLeft, GPIO.LOW)
GPIO.output(footRight, GPIO.LOW)
GPIO.output(ankleLeft, GPIO.LOW)
GPIO.output(ankleRight, GPIO.LOW)

fileName = "dataIMUSuit_test"

print("Initialisation finished, gonna write to" + fileName + "and start reading now")

def resetValues():
    ax=0
    ax=0
    ay=0
    gz=0
    gy=0
    gz=0

data = open(fileName + '.txt', 'a+')

#Misschien overal ook mp=mpu9250.SL_MPU9250(Ox68, 2) schrijven, kweni of het nodig is
#*********LOOP*********#
while True:
    #*****Left foot*****#
    try:
        GPIO.output(ankleRight, GPIO.LOW)
        GPIO.output(footLeft, GPIO.HIGH)
#	mp=mpu9250.SL_MPU9250(0x69, 2)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()

	print "Left foot"
	print "Ax1: ",ax
	print "Ay1: ",ay
	print "Az1: ",az

        data.write("Left foot,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
	time.sleep(0.5)
    except:
        print("Left foot failed to connect")

    #*****Right foot*****#
    try:
        GPIO.output(footLeft, GPIO.LOW)
        GPIO.output(footRight, GPIO.HIGH)
	#mp=mpu9250.SL_MPU9250(0x69, 2)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()

	print "Right foot"
	print "Ax1: ",ax
	print "Ay1: ",ay
	print "Az1: ",az

        data.write("Right foot,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
	time.sleep(0.5)
    except:
        print("Right foot failed to connect")

    #*****Left ankle*****#
    try:
        GPIO.output(footRight, GPIO.LOW)
        GPIO.output(ankleLeft, GPIO.HIGH)
	#mp=mpu9250.SL_MPU9250(0x69, 2)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()

	print "Left ankle"
	print "Ax1: ",ax
	print "Ay1: ",ay
	print "Az1: ",az

        data.write("Left ankle,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
	time.sleep(0.5)
    except:
        print("Left ankle failed to connect")

    #*****Right ankle*****#
    try:
        GPIO.output(ankleLeft, GPIO.LOW)
        GPIO.output(ankleRight, GPIO.HIGH)
	#mp=mpu9250.SL_MPU9250(0x69, 2)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()

	print "Right ankle"
	print "Ax1: ",ax
	print "Ay1: ",ay
	print "Az1: ",az

        data.write("Right ankle,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
	time.sleep(0.5)
    except:
        print("Right ankle failed to connect")

	hey = input("give input")

data.close()
GPIO.cleanup()
