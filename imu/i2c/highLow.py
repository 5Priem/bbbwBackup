import Adafruit_BBIO.GPIO as GPIO

adPin="P8_10"
adPin1="P8_9"

GPIO.setup(adPin, GPIO.OUT)
GPIO.setup(adPin1, GPIO.OUT)

GPIO.output(adPin, GPIO.LOW)
GPIO.output(adPin1, GPIO.HIGH)
