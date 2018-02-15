# Heel R naar analog input (pin 39)
# Com 1 naar 3.3V (pin 3)
# Tussen Heel R en Analog input: resistor naar ground (pin 1)
# Dan tzelfde voor elke connectie, en elk een aparte res en aparte analog input


import Adafruit_BBIO.ADC as adc
import time
adc.setup()
heelR = "P9_40"
heelL = "P9_39"
met1  = "P9_38"
hallux= "P9_37"
met3  = "P9_36"
toes  = "P9_35"
met5  = "P9_33"

while(1):
	#valueHeelR=adc.read(heelR)
	#print("heelR: "+ str(valueHeelR))

	time.sleep(0.01)
	valueHeelL=adc.read(heelL)
	print("heelL: "+ str(valueHeelL))

	#time.sleep(0.01)
	#valueMet1=adc.read(met1)
	#print("met1: "+ str(valueMet1))

	#time.sleep(0.01)
	#valueHallux=adc.read(hallux)
	#print("hallux: "+ str(valueHallux))

	#time.sleep(0.01)
	#valueMet3=adc.read(met3)
	#print("met3: "+ str(valueMet3))

	#time.sleep(0.01)
	#valueToes=adc.read(toes)
	#print("toes: "+ str(valueToes))

	#time.sleep(0.01)
	#valueMet5=adc.read(met5)
	#print("met5: "+ str(valueMet5))

	time.sleep(0.25)
