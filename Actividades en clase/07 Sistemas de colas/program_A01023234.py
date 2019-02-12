import random
import time
import multiprocessing

daysOfSimulation = 30
nOfEmployees = 60
sizeOfTeam = 3

def randomProbability(i, j):
	return int(random.randint(i,j*1000)/1000)

def getNumberOfTrucksRightBeforeTheSimulation():
	probability = randomProbability(0, 100)
	if(probability <= 50):
		return 0
	if(probability > 50 and probability <= 75):
		return 1
	if(probability > 75 and probability <= 90):
		return 2
	if(probability > 90 and probability <= 100):
		return 3

def getTimeBetweenArrivals():
	probability = randomProbability(0, 100)
	if(probability <= 2):#0.02
		return 20
	if(probability > 2 and probability <= 10):#0.08
		return 25
	if(probability > 10 and probability <= 22):#.12
		return 30
	if(probability > 22 and probability <= 47):#0.25
		return 35
	if(probability > 47 and probability <= 67):#0.20
		return 40
	if(probability > 67 and probability <= 82):#15
		return 45
	if(probability > 82 and probability <= 92):#0.010
		return 50
	if(probability > 92 and probability <= 97):#0.05
		return 55
	if (probability > 97 and probability <= 100):#0.03
		return 60
	
def getTimeService(teamSize):
	probability = randomProbability(0, 100)
	if(teamSize == 3):
		if(probability <= 5):#0.05
			return 20
		if(probability > 5 and probability <= 15):#0.10
			return 25
		if(probability > 15 and probability <= 35):#0.20
			return 30
		if(probability > 35 and probability <= 60):#0.25
			return 35
		if(probability > 60 and probability <= 72):#0.12
			return 40
		if(probability > 72 and probability <= 82):#0.10
			return 45
		if(probability > 82 and probability <= 90):#0.08
			return 50
		if(probability > 90 and probability <= 96):#0.06
			return 55
		if (probability > 96 and probability <= 100):#0.04
			return 60
	if(teamSize == 4):
		if(probability <= 5):#0.05
			return 15
		if(probability > 5 and probability <= 20):#0.15
			return 20
		if(probability > 20 and probability <= 40):#0.20
			return 25
		if(probability > 40 and probability <= 60):#0.20
			return 30
		if(probability > 60 and probability <= 75):#0.15
			return 35
		if(probability > 75 and probability <= 87):#0.12
			return 40
		if(probability > 87 and probability <= 95):#0.08
			return 45
		if(probability > 95 and probability <= 99):#0.04
			return 50
		if (probability > 99 and probability <= 100):#0.01
			return 55
	if(teamSize == 5):
		if(probability <= 10):#0.10
			return 10
		if(probability > 10 and probability <= 28):#0.18
			return 15
		if(probability > 28 and probability <= 50):#0.22
			return 20
		if(probability > 50 and probability <= 68):#0.18
			return 25
		if(probability > 68 and probability <= 78):#0.10
			return 30
		if(probability > 78 and probability <= 86):#0.08
			return 35
		if(probability > 86 and probability <= 92):#0.06
			return 40
		if(probability > 92 and probability <= 97):#0.05
			return 45
		if(probability > 97 and probability <= 100):#0.03
			return 50
	if(teamSize == 6):
		if(probability <= 12):#0.12
			return 5
		if(probability > 12 and probability <= 27):#0.15
			return 10
		if(probability > 27 and probability <= 53):#0.26
			return 15
		if(probability > 53 and probability <= 68):#0.15
			return 20
		if(probability > 68 and probability <= 80):#0.12
			return 25
		if(probability > 80 and probability <= 88):#0.08
			return 30
		if(probability > 88 and probability <= 94):#0.06
			return 35
		if(probability > 94 and probability <= 98):#0.04
			return 40
		if(probability > 98 and probability <= 100):#0.02
			return 45
	if(teamSize > 6 or teamSize < 3):
		return None
		
def formatTime(minutes):
	hour = minutes/60
	minutes = minutes%60
	minutesInString = str(minutes)
	if(len(minutesInString) == 1):
		minutesInString = '0' + minutesInString
	if(minutesInString == '0'):
		return str(int(hour))+':00'
	else:
		return str(int(hour))+':'+minutesInString
		
def formatTimeOfEachElement(truck):
	truck['TimeOfArrival'] = formatTime(truck['TimeOfArrival'])
	truck['StartService'] = formatTime(truck['StartService'])
	truck['DoneService'] = formatTime(truck['DoneService'])
	return truck
		
	
def attendTruck(truck, currentTime, serviceTime):
	truck['StartService'] = currentTime
	truck['TimeOfService'] = serviceTime
	if(truck['StartService'] < truck['TimeOfArrival']):
		waitingTime =  (truck['StartService'] + 1440) - truck['TimeOfArrival']
	else:
		waitingTime = truck['StartService'] - truck['TimeOfArrival']
	
	truck['WaitingTime'] = waitingTime
	if(truck['TimeBetweenArrivals'] > 0 and truck['WaitingTime'] != 0):
		truck['Ocio'] = truck['TimeBetweenArrivals']
	currentTime += serviceTime
	currentTime = timeChecker(currentTime)
	truck['DoneService'] = currentTime
	return truck, currentTime
	
def timeChecker(time):
	if(time >= 1440):
		time = time - 1440
	return time
	
def createTeams(nOfEmployees, sizeOfTeam):
	team = {'NO': 0, 'TrucksAttended':0, 'ShiftDuration':0, 'HadFood': 0, 'Cost': 0, 'numberOfShifts': 0, 'teamSize': sizeOfTeam, 'salaryPerWorker': 0}
	teams = []
	j = 0
	for i in range(nOfEmployees):
		if(i%sizeOfTeam == 0 and i != 0):
			team['NO'] = j
			teams.append(team.copy())
			j += 1
	return teams
	
def shiftChange(team, trucksAttended, TimeAtShiftStart, TimeOfShiftEnd, ShiftDuration):
	TimeAtShiftStart = timeChecker(TimeAtShiftStart)
	salary = 8 * 25
	team['ShiftDuration'] = formatTime(ShiftDuration)
	if(ShiftDuration > 480):
		ShiftDuration -= 480
		salary += (ShiftDuration / 60) * 37.5
	team['salaryPerWorker'] = salary
	team['TrucksAttended'] = trucksAttended
	team['numberOfShifts'] = team['numberOfShifts'] + 1
	nextTeamNumber = team['NO'] + 1
	return nextTeamNumber
	
def simulation(days, nOfEmployees, teamSize):#Main Simulation
	startTime = 0
	endTimeInDays = days
	endTimeInMinutes = endTimeInDays*24*60

	numberOfTrucksWaiting = getNumberOfTrucksRightBeforeTheSimulation()
	arrivingTruck = {'NO': 0, 'TimeBetweenArrivals': 0, 'TimeOfArrival': 0, 'StartService' : 0, 'TimeOfService' : 0, 'DoneService': 0, 'Ocio': 0, 'WaitingTime': 0, 'stackSize': 0}


	teams = createTeams(nOfEmployees, teamSize)

	team = teams[0]
	truckCount = 0
	currentTime = startTime*60
	shiftTimer = 0
	trucksWaiting = []
	trucksAttended = []
	food = 0
	cost = 0
	timeCounter = 0
	timeBetweenArrivals = None
	trucksAttendedLastTime = 0

	while(timeCounter <= endTimeInMinutes):
		if(shiftTimer > 480):
			trucksAttendedLastTime = len(trucksAttended)
			nextTeamNumber = shiftChange(team, trucksAttendedLastTime, timeCounter - shiftTimer, timeCounter, shiftTimer)
			if(nextTeamNumber == len(teams)):
				nextTeamNumber = 0
			cost += shiftTimer/60 * 500
			team['Cost'] += cost + (team['salaryPerWorker'] * team['teamSize'])
			cost = 0
			food = 0
			team = teams[nextTeamNumber]
			shiftTimer = 0
		if(numberOfTrucksWaiting > 0):
			for i in range(numberOfTrucksWaiting):
				arrivingTruck['NO'] = truckCount
				if(timeBetweenArrivals is not None):
					arrivingTruck['TimeBetweenArrivals'] = timeBetweenArrivals
					timeBetweenArrivals = None
				else:
					arrivingTruck['TimeBetweenArrivals'] = 0
				arrivingTruck['TimeOfArrival'] = currentTime
				arrivingTruck['StartService'] = 0
				arrivingTruck['TimeOfService'] = 0
				arrivingTruck['DoneService'] = 0
				arrivingTruck['Ocio'] = 0
				arrivingTruck['WaitingTime'] = 0
				arrivingTruck['stackSize'] = numberOfTrucksWaiting - 1
				trucksWaiting.append(arrivingTruck.copy())
				arrivingTruck.clear()
				truckCount += 1
			numberOfTrucksWaiting = 0
		serviceTime = getTimeService(3)
		timeBetweenArrivals = getTimeBetweenArrivals()
		
		if(len(trucksWaiting) > 0):
			if(timeCounter >= 240 and food == 0):
				currentTime += 30
				timeCounter += 30
				shiftTimer += 30
				food = 1
				team['HadFood'] += 1
			else:
				tempTruck, currentTime = attendTruck(trucksWaiting.pop(0), currentTime, serviceTime)
				tempTruck = formatTimeOfEachElement(tempTruck)
				if(tempTruck['WaitingTime'] > 60):
					cost += 100 * (tempTruck['WaitingTime']/60)
				trucksAttended.append(tempTruck)
				timeCounter += serviceTime
				shiftTimer += serviceTime
				
		if(serviceTime > timeBetweenArrivals):
			numberOfTrucksWaiting += 1
			currentTime += timeBetweenArrivals
			timeCounter += timeBetweenArrivals
			shiftTimer += timeBetweenArrivals
		currentTime = timeChecker(currentTime)
	totalCost = 0
	
	for i in teams:
		totalCost += i['Cost']
	teams.clear()
	trucksWaiting.clear()
	trucksAttended.clear()
	
	return totalCost
	

def parallelRun(nOfSimulations):
	return simulation(daysOfSimulation, nOfEmployees, sizeOfTeam)


nOfSimulations = 50000

#Paralelo
startTime = time.time()
costAvg = 0
pool = multiprocessing.Pool()
costPerSimulation = pool.map(parallelRun, range(nOfSimulations))
pool.close()
for i in costPerSimulation:
	costAvg += i
costAvg = costAvg/(len(costPerSimulation))
print(costAvg)
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
#print(costAvg)
#print('Tiempo en terminar {} segundos'.format(time.time() - startTime))



