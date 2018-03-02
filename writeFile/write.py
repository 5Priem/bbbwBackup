import os

x=1
name = "fileNaam"
#final_name = os.path.join('C:', 'Users', 'boktor', 'Desktop', name + '.txt')
while x < 10:
	data = open(name + '.txt', 'a+')
	data.write(str(x) + '\n')
	x = x + 1
data.close()
