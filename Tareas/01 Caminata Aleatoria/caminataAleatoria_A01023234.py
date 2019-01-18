#Emiliano Abascal Gurria A01023234
import random
numberOfRuns = 50000
positions = []
cont = 0
def run(cont):
	currentPosition = [0, 0]
	currentPosition[0] = 0
	currentPosition[1] = 0
	for i in range(0, 10):
		direction = random.randint(0, 99)
		if(direction <= 24):
			currentPosition[1] = currentPosition[1] + 1
		if(direction > 24 and direction <= 49):
			currentPosition[1] = currentPosition[1] - 1
		if(direction > 49 and direction <= 74):
			currentPosition[0] = currentPosition[0] + 1
		if(direction > 74 and direction <= 99):
			currentPosition[0] = currentPosition[0] - 1
	positions.append(currentPosition)
	if(currentPosition[0] ==  -2 and currentPosition[1] == 0 or currentPosition[0] ==  2 and currentPosition[1] == 0 or currentPosition[0] ==  0 and currentPosition[1] == 2 or currentPosition[0] ==  0 and currentPosition[1] == -2):
		cont=cont+1
	if(currentPosition[0] ==  -1 and currentPosition[1] == 1 or currentPosition[0] ==  1 and currentPosition[1] == -1 or currentPosition[0] ==  1 and currentPosition[1] == 1 or currentPosition[0] ==  -1 and currentPosition[1] == -1 or currentPosition[0] == 0 and currentPosition[1] == 0):
		cont=cont + 1
	return cont
for j in range(0, numberOfRuns):
	cont = run(cont)
print("A)La probabilidad de que caiga a dos o menos cuardas es de " + str(cont/numberOfRuns) + "%.")
cont = 0
positions.sort()
for i in positions:
	c = positions.count(i)
	if cont == 0:
		mostCommon = i
		mostCommonCount = c
		cont = 1
	if(mostCommonCount < c):
		mostCommon = i
		mostCommonCount = c
	for j in range(0, c):
		positions.remove(i)
positions.clear()
print("B)La posición en donde más veces cae es en " + str(mostCommon) + " y la probabilidad de que caiga ahi es de " + str(mostCommonCount/numberOfRuns*100) + "%.")	

		
