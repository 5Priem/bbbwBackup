import os

x=1
name = "fileNaam"

data = open(name+ '.txt', 'a+')
data.write(str(x) + '\n')
data.close()
