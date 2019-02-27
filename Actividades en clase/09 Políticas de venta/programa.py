import random
import operator
def randomProbability(i, j):
	return int(random.randint(i,j*1000)/1000)
	
def buyThePainting():
	gainz = {0:0, 1:0, 2:0, "Perdida":0}
	for i in range(50000):
		dayBought = randomProbability(0, 3)
		avalabilityProbability = randomProbability(0, 100)
		if(dayBought == 0 and avalabilityProbability <= 60):
			gainz[0] += 100000
		if(dayBought == 1 and avalabilityProbability > 60 and avalabilityProbability <= 84):
			gainz[1] += 200000
		if(dayBought == 2 and avalabilityProbability > 84 and avalabilityProbability <= 93):
			gainz[2] += 240000
		else:
			gainz["Perdida"] += 1
	return gainz

	

print(buyThePainting())

print("La estrategia que maximiza mas la ganancia es comprarlo el el dia", max(buyThePainting().items(), key=operator.itemgetter(1))[0])