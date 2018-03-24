import time

ctr = 1
data = open("hey"+'.txt','a+')
timeout = time.time()+10
while True:
	data.write(str(ctr)+'\n')
	ctr=ctr+1
	time.sleep(1)
	if time.time()>timeout:
		data.close()
		break
	
