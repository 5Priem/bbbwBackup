import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time
import os

#*********SETUP*********#
try:
	mp=mpu9250.SL_MPU9250(0x68, 2)
except:
	print("First IMU (in Setup) not found")
footLeft         = "P8_7"
footRight        = "P8_8"
ankleLeft        = "P8_9"

print("Initialising GPIO's...")
GPIO.setup(footLeft, GPIO.OUT)
GPIO.setup(footRight, GPIO.OUT)
GPIO.setup(ankleLeft, GPIO.OUT)

GPIO.output(footLeft, GPIO.LOW)
GPIO.output(footRight, GPIO.LOW)
GPIO.output(ankleLeft, GPIO.LOW)

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
        GPIO.output(ankleLeft, GPIO.LOW)
        GPIO.output(footLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left foot,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Left foot failed to connect")

    #*****Right foot*****#
    try:
        GPIO.output(footLeft, GPIO.LOW)
        GPIO.output(footRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right foot,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Right foot failed to connect")

    #*****Left ankle*****#
    try:
        GPIO.output(footRight, GPIO.LOW)
        GPIO.output(ankleLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left ankle,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Left ankle failed to connect")

	hey = input("give input")

data.close()
GPIO.cleanup()
