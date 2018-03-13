import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time
import os

#*********SETUP*********#
mp=mpu9250.SL_MPU9250(0x68, 2)
footLeft         = "P8_7"
footRight        = "P8_8"
ankleLeft        = "P8_9"
ankleRight       = "P8_10"
quadricepsLeft   = "P8_11"
quadricepsRight  = "P8_12"
handLeft          = "P8_14"
handRight         = "P8_15"
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


#*********LOOP*********#
def resetValues():
    ax=0
    ax=0
    ay=0
    gz=0
    gy=0
    gz=0
#Misschien overal ook mp=mpu9250.SL_MPU9250(Ox68, 2) schrijven, kweni of het nodig is
while True:
    #*****Left foot*****#
    GPIO.output(head, GPIO.LOW)
    GPIO.output(footLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Left foot,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Right foot*****#
    GPIO.output(footLeft, GPIO.LOW)
    GPIO.output(footRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Right foot,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Left ankle*****#
    GPIO.output(footRight, GPIO.LOW)
    GPIO.output(ankleLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Left ankle,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #****Right ankle*****#
    GPIO.output(ankleLeft, GPIO.LOW)
    GPIO.output(ankleRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Right ankle,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Left quadriceps*****#
    GPIO.output(ankleRight, GPIO.LOW)
    GPIO.output(quadricepsLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Left quadriceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Right quadriceps*****#
    GPIO.output(quadricepsLeft, GPIO.LOW)
    GPIO.output(quadricepsRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Right quadriceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Left hand*****#
    GPIO.output(quadricepsRight, GPIO.LOW)
    GPIO.output(handLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Left hand,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Right hand*****#
    GPIO.output(handLeft, GPIO.LOW)
    GPIO.output(handRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Right hand,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Left wrist*****#
    GPIO.output(handRight, GPIO.LOW)
    GPIO.output(wristLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Left wrist,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Right wrist*****#
    GPIO.output(wristLeft, GPIO.LOW)
    GPIO.output(wristRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Right wrist,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Left biceps*****#
    GPIO.output(wristRight, GPIO.LOW)
    GPIO.output(bicepsLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Left biceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Right biceps*****#
    GPIO.output(bicepsLeft, GPIO.LOW)
    GPIO.output(bicepsRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Right biceps,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Back left*****#
    GPIO.output(bicepsRight, GPIO.LOW)
    GPIO.output(backLeft, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Back left,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Back right*****#
    GPIO.output(backLeft, GPIO.LOW)
    GPIO.output(backRight, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Back right,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Back pelvis*****#
    GPIO.output(backRight, GPIO.LOW)
    GPIO.output(backPelvis, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Back pelvis,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Front sternum*****#
    GPIO.output(backPelvis, GPIO.LOW)
    GPIO.output(frontSternum, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Front sternum,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Front bellybutton*****#
    GPIO.output(frontSternum, GPIO.LOW)
    GPIO.output(frontBellybutton, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Front bellybutton,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Front pelvis*****#
    GPIO.output(frontBellybutton, GPIO.LOW)
    GPIO.output(frontPelvis, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Front pelvis,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()

    #*****Head*****#
    GPIO.output(frontPelvis, GPIO.LOW)
    GPIO.output(head, GPIO.HIGH)
    ax, ay, az = mp.getAccel()
    gx, gy, gz = mp.getGyro()
    data = open(fileName + '.txt', 'a+')
    data.write("Head,"+str(ax)+','+str(ay)+','+str(az)+','+str(gx)+','+str(gy)+','+str(gz) + '\n')
    resetValues()
    data.close()

GPIO.cleanup()
