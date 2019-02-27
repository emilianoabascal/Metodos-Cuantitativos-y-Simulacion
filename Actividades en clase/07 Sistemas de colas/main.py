#Emiliano Abascal Gurria A01023234
from funcs import *
import time
import multiprocessing


nOfSimulations = 50000
print("Tamano de equipo: "+ str(sizeOfTeam))

#Paralelo
startTime = time.time()
costAvg = 0
pool = multiprocessing.Pool()
costPerSimulation = pool.map(parallelRun, range(nOfSimulations))
pool.close()
for i in costPerSimulation:
	costAvg += i
costAvg = costAvg/(len(costPerSimulation))
print("Costo Promedio: "+ str(costAvg))
print('Tiempo en terminar {} segundos'.format(time.time() - startTime))


##Secuencial
#startTime = time.time()
#costAvg = 0
#costPerSimulation = []
#for i in range(0, nOfSimulations):
#	costPerSimulation.append(simulation(daysOfSimulation, nOfEmployees, sizeOfTeam))
#for j in costPerSimulation:
#	costAvg += j
#costAvg = costAvg/(len(costPerSimulation))
#print("Costo Promedio: "+ str(costAvg))
#print('Tiempo en terminar {} segundos'.format(time.time() - startTime))