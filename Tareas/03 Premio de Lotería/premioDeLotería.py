from random import randint
from collections import Counter
import time
import multiprocessing
starttime = time.time()

lotteryNumberHolder = []
numberOfRepetitions = []
mostCommonNumbers = []
n = 6
nOfJobs = 16

def chanceToWin(i):
	cont = 0
	lotterySimulation = lotteryNumbers()
	x = 0
	while x == 0:
		if(all(i in lotterySimulation for i in mostCommonNumbers)):
			x = 1
		else:
			lotterySimulation = lotteryNumbers()
			cont = cont + 1
	print("El thread",i, "ha acabado", mostCommonNumbers, lotterySimulation, "Con", cont, "boletos.")
	return cont


def lotteryNumbers():
	numbersToReturn = []
	while len(numbersToReturn) < n:
		if len(numbersToReturn) <= 4:
			x = randint(1, 70)		
		else:
			x = randint(1, 25)
		if(x not in numbersToReturn):
			numbersToReturn.append(x)
	return numbersToReturn
	
def getTheMostCommonCombination():
	for i in range(50000):
		lotteryNumberHolder.append(lotteryNumbers())
	for j in range(n):	
		tempList = []
		for i in lotteryNumberHolder:
			tempList.append(i[j])
		mostCommonNumbers.append(Counter(tempList).most_common(1)[0][0])
		numberOfRepetitions.append(Counter(tempList).most_common(1)[0][1])
	tempList.clear()
	lotteryNumberHolder.clear()


getTheMostCommonCombination()
x = 0
while x <= 5:
	for i in mostCommonNumbers:
		if mostCommonNumbers.count(i) > 1:
			mostCommonNumbers.clear()
			numberOfRepetitions.clear()
			getTheMostCommonCombination()
			x = 0
			break
		else:
			x = x + 1
	
print("A)Los numeros que mas se repiten son:",mostCommonNumbers, "y se repitieron", numberOfRepetitions, "respectivamente.")
#processes = []
pool = multiprocessing.Pool()
results = pool.map(chanceToWin, range(nOfJobs))
pool.close()



sumForAverage = 0
for i in results:
	sumForAverage = sumForAverage + i
print("En promedio se necesitan", sumForAverage/nOfJobs, "Boletos.")
print('That took {} sec'.format(time.time() - starttime))
