import random
import multiprocessing
import time
def generateDays(simulations):
	breadBoughtPerDay = []
	xList = {}
	for i in range(simulations):
		tortaNumber = random.randint(0, 12)
		if tortaNumber%2 != 0:
			i = i - 1
		else:
			if(tortaNumber == 0):
				tortaNumber = 2
			breadBoughtPerDay.append(tortaNumber * 12)
			if(tortaNumber not in xList):
				xList[tortaNumber] = 1
			else:
				xList[tortaNumber] = xList[tortaNumber] + 1
	return breadBoughtPerDay, xList
	
				
def getUtilitiesParallel(i): #Paralel
	x = 0
	egresos = 0
	utilidad = 0
	boughtThatDay = random.randint(1, 144)
	if(boughtThatDay > i):
		egresos = (i*18) - (i*(2)) - ((boughtThatDay - i) * 10)
	if(boughtThatDay < i):
		egresos = ((i/2) * 1.5) - (i*18) - (boughtThatDay*(2))
	if(boughtThatDay == i):
		egresos = (i*18) - (boughtThatDay*(2))
	utilidad = (boughtThatDay * 45) - egresos
	temp = i/12
	return temp, utilidad
	
def getUtilities(breadBoughtPerDay):
	utilidades = {}
	for i in breadBoughtPerDay:
		x = 0
		egresos = 0
		utilidad = 0
		boughtThatDay = random.randint(1, 144)
		if(boughtThatDay > i):
			egresos = (i*18) - (i*(2)) - ((boughtThatDay - i) * 10)
		if(boughtThatDay < i):
			egresos = ((i/2) * 1.5) - (i*18) - (boughtThatDay*(2))
		if(boughtThatDay == i):
			egresos = (i*18) - (boughtThatDay*(2))
		utilidad = (boughtThatDay * 45) - egresos
		temp = i/12
		if(temp not in utilidades):
			utilidades[temp] = (boughtThatDay * 45) - egresos
		else:
			utilidades[temp] = utilidades[temp] +(boughtThatDay * 45) - egresos
	return utilidades
			
def parallelRun():
	utilidades = {}
	x = {}
	pool = multiprocessing.Pool()
	x = pool.map(getUtilitiesParallel, breadBoughtPerDay)
	pool.close()
	breadBoughtPerDay.clear()
	for i in x:
		if i[0] not in utilidades:
			utilidades[i[0]] = i[1]
		else:
			utilidades[i[0]] = utilidades[i[0]] + i[1]
	return utilidades

starttime = time.time()
#Run program linearly
#breadBoughtPerDay, xList = generateDays(5000000)
#utilidades = getUtilities(breadBoughtPerDay) 

#Run program in Parallel
breadBoughtPerDay, xList = generateDays(5000000)
utilidades = parallelRun() 

for i in xList:
	print(i,":", utilidades[i]/xList[i])
print('Tiempo en terminar {} segundos'.format(time.time() - starttime))
