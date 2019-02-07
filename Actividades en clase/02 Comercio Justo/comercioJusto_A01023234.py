from random import randint
from collections import Counter

simulationNumber = 50000
clientCont = 0
storeCont = 0
cont = 0
list = []

for i in range(0, simulationNumber):
	x = randint(0, 100)
	if(x >= .2):
		clientCont = clientCont + 1
		list.append(99)
	else:
		storeCont = storeCont + 1
		list.append(100)
list.sort()
print(Counter(list).most_common(1)[0][1]/50000*100)
		


