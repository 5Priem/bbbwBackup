import Adafruit_BBIO.GPIO as GPIO
import mpu9250
import time

mp=mpu9250.SL_MPU9250(Ox68, 2)
adPin="P8_10"
adPin1="P8_9"

GPIO.setup(adPin, GPIO.OUT)
GPIO.setup(adPin1, GPIO.OUT)

GPIO.output(adPin, GPIO.LOW)
GPIO.output(adPin1, GPIO.HIGH)

#GPIO.setup(adPin, GPIO.IN)
#GPIO.setup(adPin1, GPIO.IN)
print("Eerste pin: ")
print(GPIO.input(adPin))
print("Tweede pin: ")
print(GPIO.input(adPin1))

print("Eerste is Low nu voor 5 sec")
timeout= time.time()+210
while True:
  if time.time() > timeout:
      break
  ax1, ay1, az1 = mp.getAccel()
  time.sleep(0.1)
  print "Az1: ", az1
  
GPIO.output(adPin, GPIO.HIGH)
GPIO.output(adPin1, GPIO.LOW)
timeout= time.time()+210
mp=mpu9250.SL_MPU9250(Ox68, 2)
print("ANDERE********************************************")
time.sleep(2)
while True:
  if time.time() > timeout:
      break
  ax1, ay1, az1 = mp.getAccel()
  time.sleep(0.1)
  print "Az1: ", az1
  
GPIO.cleanup()
