#Emiliano Abascal Gurria A01023234
import random
import time
import math
import numpy as np 
import scipy as sp 
import scipy.stats 
import multiprocessing

def mean_confidence_interval(data, confidence): 
	a = np.array(data) 
	n = len(a) 
	m, se = np.mean(a), scipy.stats.sem(a) 
	h = se * sp.stats.t._ppf((1+confidence)/2., n-1) 
	return m, m-h, m+h

def simulateArravingCarsInADay():
	probability = random.randint(1, 100)
	if(probability <= 5):
		numberOfCars = 3
	if(probability > 5 and probability <= 20):
		numberOfCars = 4
	if(probability > 20 and probability <= 50):
		numberOfCars = 5
	if(probability > 50 and probability <= 75):
		numberOfCars = 6
	if(probability > 75 and probability <= 90):
		numberOfCars = 7
	if(probability > 90 and probability <= 100):
		numberOfCars = 8
	return numberOfCars
	
def checkCarSizesInADay(numberOfCars):
	carsInADay = {'C': 0, 'M': 0, 'G': 0}
	for i in range(numberOfCars):
		probability = random.randint(1, 100)
		if(probability <= 45):
			carType = "C"
			carsInADay['C'] += 1
		if(probability > 45 and probability <= 80):
			carType = "M"
			carsInADay['M'] += 1
		if(probability > 80 and probability <= 100):
			carType = "G"
			carsInADay['G'] += 1
	return carsInADay

def serviceDefiner(carSize, numberOfCars):
	cost = 0
	for i in range(numberOfCars):
		probability = random.randint(1, 100)
		if(carSize == 'C'):
			if(probability <= 45):
				cost += 350
			if(probability > 45 and probability <= 60):
				cost += 1575
			if(probability > 60 and probability <= 80):
				cost += 1975
			if(probability > 80 and probability <= 90):
				cost += 2540
			if(probability > 90 and probability <= 100):
				cost += 700
		if(carSize == 'M'):
			if(probability <= 25):
				cost += 550
			if(probability > 25 and probability <= 50):
				cost += 1975
			if(probability > 50 and probability <= 65):
				cost += 2545
			if(probability > 65 and probability <= 85):
				cost += 2925
			if(probability > 85 and probability <= 100):
				cost += 700
		if(carSize == 'G'):
			if(probability <= 10):
				cost += 750
			if(probability > 10 and probability <= 25):
				cost += 2275
			if(probability > 25 and probability <= 55):
				cost += 2845
			if(probability > 55 and probability <= 95):
				cost += 3415
			if(probability > 95 and probability <= 100):
				cost += 700
	return cost

def getCostForEachDay(i):
	y = simulateArravingCarsInADay()
	cars = checkCarSizesInADay(y)
	l = 0
	for j in cars:
		l += serviceDefiner(j, cars[j])
	return l

startTime = time.time()
nOfSimulations = 50000
costPerDay = []

#Paralelo
pool = multiprocessing.Pool()
costPerDay = pool.map(getCostForEachDay, range(nOfSimulations))
pool.close()

##Secuencial
#for i in range(nOfSimulations):
#	costPerDay.append(getCostForEachDay(i))
	
print("70%", mean_confidence_interval(costPerDay, .70))
print("80%",mean_confidence_interval(costPerDay, .80))
print("90%",mean_confidence_interval(costPerDay, .90))
print("95%",mean_confidence_interval(costPerDay, .95))
print("99%",mean_confidence_interval(costPerDay, .99))
print('Tiempo en terminar {} segundos'.format(time.time() - startTime))