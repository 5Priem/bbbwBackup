import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time

mp=mpu9250.SL_MPU9250(0x68, 2)
adPin="P8_7"
adPin1="P8_8"

GPIO.setup(adPin, GPIO.OUT)
GPIO.setup(adPin1, GPIO.OUT)

GPIO.output(adPin, GPIO.LOW)
GPIO.output(adPin1, GPIO.HIGH)


print("Eerste is Low nu voor 5 sec")
timeout= time.time()+5
while True:
  if time.time() > timeout:
      break
  ax1, ay1, az1 = mp.getAccel()
  time.sleep(0.1)
  print "Az1: ", az1
  
GPIO.output(adPin, GPIO.HIGH)
GPIO.output(adPin1, GPIO.LOW)
timeout= time.time()+5
#mp=mpu9250.SL_MPU9250(0x68, 2)
print("ANDERE********************************************")
time.sleep(2)
while True:
  if time.time() > timeout:
      break
  ax1, ay1, az1 = mp.getAccel()
  time.sleep(0.1)
  print "Az1: ", az1
  
GPIO.cleanup()
