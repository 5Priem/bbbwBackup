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
quadricepsLeft   = "P8_11"
quadricepsRight  = "P8_12"
handLeft         = "P8_14"
handRight        = "P8_15"
wristLeft        = "P8_16"
wristRight       = "P8_17"
bicepsLeft       = "P8_18"
bicepsRight      = "P8_26"

backLeft         = "P9_12"
backRight        = "P9_15"
backPelvis       = "P9_23"
frontSternum     = "P9_25"
frontBellybutton = "P9_27"
frontPelvis      = "P9_30"
head             = "P9_41"

print("Initialising GPIO's...")
GPIO.setup(footLeft, GPIO.OUT)
GPIO.setup(footRight, GPIO.OUT)
GPIO.setup(ankleLeft, GPIO.OUT)
GPIO.setup(ankleRight, GPIO.OUT)
GPIO.setup(quadricepsLeft, GPIO.OUT)
GPIO.setup(quadricepsRight, GPIO.OUT)
GPIO.setup(handLeft, GPIO.OUT)
GPIO.setup(handRight, GPIO.OUT)
GPIO.setup(wristLeft, GPIO.OUT)
GPIO.setup(wristRight, GPIO.OUT)
GPIO.setup(bicepsLeft, GPIO.OUT)
GPIO.setup(bicepsRight, GPIO.OUT)

GPIO.setup(backLeft, GPIO.OUT)
GPIO.setup(backRight, GPIO.OUT)
GPIO.setup(backPelvis, GPIO.OUT)
GPIO.setup(frontSternum, GPIO.OUT)
GPIO.setup(frontBellybutton, GPIO.OUT)
GPIO.setup(frontPelvis, GPIO.OUT)
GPIO.setup(head, GPIO.OUT)

fileName = "dataIMUSuit"

print("Initialisation finished, gonna write to " + fileName + " and start reading now")

def resetValues():
    ax=0
    ax=0
    ay=0
    gz=0
    gy=0
    gz=0

data = open(fileName + '.txt', 'a+')

#Misschien overal ook mp=mpu9250.SL_MPU9250(Ox69, 2) schrijven, kweni of het nodig is
#Moet dus NIET, check test.py, ook in deze folder
#*********LOOP*********#
while True:
    #*****Left foot*****#
    try:
        GPIO.output(head, GPIO.LOW)
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

    #****Right ankle*****#
    try:
        GPIO.output(ankleLeft, GPIO.LOW)
        GPIO.output(ankleRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right ankle,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Right ankle failed to connect")

    #*****Left quadriceps*****#
    try:
        GPIO.output(ankleRight, GPIO.LOW)
        GPIO.output(quadricepsLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left quadriceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Left quadriceps failed to connect")

    #*****Right quadriceps*****#
    try:
        GPIO.output(quadricepsLeft, GPIO.LOW)
        GPIO.output(quadricepsRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right quadriceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Right quadriceps failed to connect")

    #*****Left hand*****#
    try:
        GPIO.output(quadricepsRight, GPIO.LOW)
        GPIO.output(handLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left hand,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Left hand failed to connect")

    #*****Right hand*****#
    try:
        GPIO.output(handLeft, GPIO.LOW)
        GPIO.output(handRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right hand,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Right hand failed to connect")

    #*****Left wrist*****#
    try:
        GPIO.output(handRight, GPIO.LOW)
        GPIO.output(wristLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left wrist,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Left wrist failed to connect")

    #*****Right wrist*****#
    try:
        GPIO.output(wristLeft, GPIO.LOW)
        GPIO.output(wristRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right wrist,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Right wrist failed to connect")

    #*****Left biceps*****#
    try:
        GPIO.output(wristRight, GPIO.LOW)
        GPIO.output(bicepsLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Left biceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Left biceps failed to connect")

    #*****Right biceps*****#
    try:
        GPIO.output(bicepsLeft, GPIO.LOW)
        GPIO.output(bicepsRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Right biceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Right biceps failed to connect")

    #*****Back left*****#
    try:
        GPIO.output(bicepsRight, GPIO.LOW)
        GPIO.output(backLeft, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Back left,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Back left failed to connect")

    #*****Back right*****#
    try:
        GPIO.output(backLeft, GPIO.LOW)
        GPIO.output(backRight, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Back right,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Back right failed to connect")

    #*****Back pelvis*****#
    try:
        GPIO.output(backRight, GPIO.LOW)
        GPIO.output(backPelvis, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Back pelvis,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Back pelvis failed to connect")

    #*****Front sternum*****#
    try:
        GPIO.output(backPelvis, GPIO.LOW)
        GPIO.output(frontSternum, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Front sternum,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Front sternum failed to connect")

    #*****Front bellybutton*****#
    try:
        GPIO.output(frontSternum, GPIO.LOW)
        GPIO.output(frontBellybutton, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Front bellybutton,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Front bellybutton failed to connect")

    #*****Front pelvis*****#
    try:
        GPIO.output(frontBellybutton, GPIO.LOW)
        GPIO.output(frontPelvis, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Front pelvis,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    except:
        print("Front pelvis failed to connect")

    #*****Head*****#
    try:
        GPIO.output(frontPelvis, GPIO.LOW)
        GPIO.output(head, GPIO.HIGH)
        ax, ay, az = mp.getAccel()
        gx, gy, gz = mp.getGyro()
        data.write("Head,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
        resetValues()
    	data.close()
    except:
        print("Head failed to connect")

data.close()
GPIO.cleanup()
