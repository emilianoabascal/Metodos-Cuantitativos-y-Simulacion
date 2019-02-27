import random
import operator
import multiprocessing
from Informacion import *
from juegos import *
import time

def getCoolerProbability(x, y):
    return random.randint(x, y * 1000)/1000
    
def calculateRating():
    for i in teams_dictionary:
        teams_dictionary[i][5] = (teams_dictionary[i][0] * 0.5) + teams_dictionary[i][1] * 0.5
        

def calculateProbabilityOfTie():
    for i in teams_dictionary:
        teams_dictionary[i][4] = teams_dictionary[i][2] * 100/ teams_dictionary[i][3]
        
def simularJornada(jornada):
    for i in range(9):
        x = teamProbabilities(jornada[i][0], jornada[i][1])
        probability = getCoolerProbability(0, 100)
        if(probability <= x[0]):
            teams_dictionary[jornada[i][0]][1] += 3
        if(probability > x[0] and probability <= x[1] + x[0]):
            teams_dictionary[jornada[i][1]][1] += 3
        if(probability > x[1] + x[0] and probability <= x[1] + x[2] + x[0]):
            teams_dictionary[jornada[i][0]][1] += 1
            teams_dictionary[jornada[i][1]][1] += 1
            teams_dictionary[jornada[i][0]][2] += 1
            teams_dictionary[jornada[i][1]][2] += 1
        teams_dictionary[jornada[i][0]][3] += 1
        teams_dictionary[jornada[i][1]][3] += 1
    calculateRating()
    calculateProbabilityOfTie()
    

def simulateAdvancedTournament(teams, length):
    SemifinalsTeams = []#list to store the teams that won the Cuartos
    FinalTeams = []#list to store the teams that won the Semifinals
    
    for i in range(length):#Cuartos FOR
        # print(teams[i],teams[length*2-1-i])#print the games from cuartos
        wholeProbability = teams[i][1][5] + teams[length*2-1-i][1][5]#get the 100% from the ranking of each team
        team1Prob = teams[i][1][5]  * 100 / wholeProbability#get the probabilty from the local team
        team2Prob = teams[length*2-1-i][1][5]  * 100 / wholeProbability#get the probabilty from the visitor team
        probability = getCoolerProbability(0, 100)
        if(probability <= team1Prob):
            SemifinalsTeams.append(teams[i])#if team1 wins, it will be store in the semifinals list
        if(probability > team1Prob and probability <= team2Prob + team1Prob):
            SemifinalsTeams.append(teams[length*2-1-i])#if team2 wins, it will be store in the semifinals list

    for i in range(0,4, 2):#here the FOR will count by a count of 2 to go through the list  
        # print(SemifinalsTeams[i],SemifinalsTeams[i+1])#print the games from semifinals
        wholeProbability = SemifinalsTeams[i][1][5] + SemifinalsTeams[i+1][1][5]#get the 100% from the ranking of each team
        team1Prob = SemifinalsTeams[i][1][5]  * 100 / wholeProbability#get the probabilty from the local team
        team2Prob = SemifinalsTeams[i+1][1][5]  * 100 / wholeProbability#get the probabilty from the visitor team
        probability = getCoolerProbability(0, 100)
        if(probability <= team1Prob):
            FinalTeams.append(SemifinalsTeams[i])#if team1 wins, it will be store in the FinalTeams list
        if(probability > team1Prob and probability <= team2Prob + team1Prob):
            FinalTeams.append(SemifinalsTeams[i+1])#if team2 wins, it will be store in the FinalTeams list
    
    # print("")
    # print(FinalTeams[0],FinalTeams[1])#print the final game
    # print("")
    
    wholeProbability = FinalTeams[0][1][5] + FinalTeams[1][1][5]#get the 100% from the ranking of each team
    team1Prob = FinalTeams[0][1][5]  * 100 / wholeProbability#get the probabilty from the local team
    team2Prob = FinalTeams[1][1][5]  * 100 / wholeProbability#get the probabilty from the visitor team
    probability = getCoolerProbability(0, 100)
    winner = ""
    if(probability <= team1Prob):
        winner = FinalTeams[0][0]
        teams_dictionary[FinalTeams[0][0]][6]+= 1#add to the dictionary a won 
    if(probability > team1Prob and probability <= team2Prob + team1Prob):
        winner = FinalTeams[1][0]
        teams_dictionary[FinalTeams[1][0]][6]+= 1#add to the dictionary a won 
    # print("")
    # print(teams_dictionary)
    return winner
    
def teamProbabilities(team1, team2):
    wholeProbability = (teams_dictionary[team1][5] + teams_dictionary[team1][4] + teams_dictionary[team2][5] + teams_dictionary[team2][4])
    return [teams_dictionary[team1][5] * 100 / wholeProbability, teams_dictionary[team2][5] * 100 / wholeProbability, teams_dictionary[team1][4] * 100 / wholeProbability + teams_dictionary[team2][4] * 100 / wholeProbability]

def simularTorneo():
    simularJornada(jornada9)
    simularJornada(jornada10)
    simularJornada(jornada11)
    simularJornada(jornada12)
    simularJornada(jornada13)
    simularJornada(jornada14)
    simularJornada(jornada15)
    simularJornada(jornada16)
    simularJornada(jornada17)
    sorted_x  = sorted(teams_dictionary.items(),reverse=True,key=lambda x: x[1][1])
    for i in range(len(sorted_x)):
        sorted_x[i][1][2] = 0
        sorted_x[i][1][4] = 0
    return simulateAdvancedTournament(sorted_x, 4)
    
def restoreDictionary():
    for i in teams_dictionary:
        teams_dictionary[i][1] = teams_dictionary_backup[i][1]
        teams_dictionary[i][2] = teams_dictionary_backup[i][2]
        teams_dictionary[i][3] = teams_dictionary_backup[i][3]
        teams_dictionary[i][4] = teams_dictionary_backup[i][4]
        teams_dictionary[i][5] = teams_dictionary_backup[i][5]
        teams_dictionary[i][6] = teams_dictionary_backup[i][6]
        
        
def simulateSecuential(n):
    winners = {}
    for i in range(n):
        calculateRating()
        calculateProbabilityOfTie()
        winner = simularTorneo()
        if(winner in winners):
            winners[winner] += 1
        else:
            winners[winner] = 1
        restoreDictionary()
    return winners
    
def simulateParallel(n):
    calculateRating()
    calculateProbabilityOfTie()
    winner = simularTorneo()
    restoreDictionary()
    return winner
    
def parallelCall(nOfSimulations):
    pool = multiprocessing.Pool()
    winnersList = pool.map(simulateParallel, range(nOfSimulations))
    pool.close()
    winners = {}
    for i in winnersList:
        if(i in winners):
            winners[i] += 1
        else:
            winners[i] = 1
    return winners

startTime = time.time()
nOfSimulations = 500000
#Parallel
winners = parallelCall(nOfSimulations)


##Secuential
#winners = simulateSecuential(nOfSimulations)

highestWinner = max(winners.iteritems(), key=operator.itemgetter(1))[0]
print(winners)#Prints the number of times each winner won, and the winner who won in most simulations
print('The most probable candidate to win the liguilla is ' + highestWinner + ".")
print('Time To Finish {} Secs'.format(time.time() - startTime))

