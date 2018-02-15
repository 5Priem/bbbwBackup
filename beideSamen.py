import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.PWM as pwm
import time

adc.setup()
heelR = "P9_40"
heelL = "P9_39"

servopin = "P9_14"
dutyMin = 3
dutyMax = 14.5
dutySpan = dutyMax-dutyMin

pwm.start(servopin,5, 60.0, 1)

# add an extra parameter 1 if servo doesn't turn, 1 changes polarity
#PWM.start(channel, duty, freq, polarity), polarity is 0 by default
ctr=1

while True:
	#angle = raw_input("Angle (0 to 180 x to exit):")
	#if angle == 'x':
	#	pwm.stop(servopin)
	#	pwm.cleanup()
	#	break
	#elif int(angle) >= 0 and int(angle) <= 180:
	#	angle_f = float(angle)
	#	duty = 100 - ((angle_f/180)*dutySpan+dutyMin)
	#	pwm.set_duty_cycle(servopin, duty)
	#else:
	#	print("Not a good format, try again")
	ctr = ctr + 10
	angle = ctr
	angle_f = float(angle)
	duty = 100 - ((angle_f/180)*dutySpan+dutyMin)
	pwm.set_duty_cycle(servopin, duty)
	#print("ctr: %s angle: %s duty: %s"%(ctr,angle,duty))
	if ctr >= 179:
		ctr=1
	time.sleep(0.1)

	valueHeelL=adc.read(heelL)
	print("heelL: "+ str(valueHeelL))
#Test extra tekst voor github
#test nog is extra tekst
