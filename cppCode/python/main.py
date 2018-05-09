import os
import time

name = "dataPYTHON"
counter = 0


start = time.time()
while counter<100:
	counter = counter + 1
	data = open(name+'.txt','a+')
	data.write(str(counter))
	data.write('\n')
	data.close()

end = time.time()
duration = end-start
data = open(name+'.txt','a+')
data.write('\n')
data.write("Duration: ")
data.write(str(duration))
data.write(" seconds.")


	
	
