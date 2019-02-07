import numpy as np
import random
import math
from collections import Counter
from statistics import mode
import numpy as np 
import scipy as sp 
import scipy.stats 
import matplotlib.pyplot as plt 
import seaborn as sns


def intervaloDeConfianza(datos):
	m = np.mean(1 * np.array(datos))
	se = scipy.stats.sem(1 * np.array(datos))
	h = se * sp.stats.t._ppf((1 + 0.95)/2, len(1 * np.array(datos))-1) 
	return m, m-h, m+h
def desviacionEstandard(comision):
	return pow((((comision/5000) * 200) - 17),2)
	
def plotThisShit():
	sns.set_palette("deep", desat = 1)
	sns.set_context(rc={"figure.figsize": (8, 8)})
	mu = np.mean(comisionList)
	sigma = np.std(comisionList)
	s = np.random.normal(mu, sigma, nOfSimulations)
	cuenta, cajas, ignorar = plt.hist(s, 30, density=True)
	normal = plt.plot(cajas, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (cajas - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
	plt.show()

comision = 0
comisionList = []
creditosList = []
rand_general = 0
mujeres = 0
hombres = 0
sumaDesvEst = 0
creditosOtorgados=0
nOfSimulations = 50000
mujeresDict = {5:0, 10:0, 15:0}
hombresDict = {5:0, 10:0, 15:0, 20:0}


for j in range(nOfSimulations):
	genRandNum = random.randint(1,100)
	tValue = 0
	if (genRandNum <= 30):
		genero = random.randint(1,100)
		tarjeta = random.randint(1,100)
		if (genero <= 20):
			hombres += 1
			if (tarjeta <= 25):
				credito = random.randint(1,100)
				if (credito <= 10):
					creditosList.append(50000)
					creditosOtorgados += 1
					hombresDict[5] += 1
					comisionList.append(200)
					sumaDesvEst += desviacionEstandard(200)
				if (credito >  10 and credito <= 50):
					creditosList.append(100000)
					creditosOtorgados += 1
					hombresDict[10] += 1
					comisionList.append(400)
					sumaDesvEst += desviacionEstandard(400)
				if (credito >  50 and credito <= 80):
					creditosList.append(150000)
					creditosOtorgados += 1
					hombresDict[15] += 1
					comisionList.append(600)
					sumaDesvEst += desviacionEstandard(600)
				if (credito >  80 and credito <= 100):
					creditosList.append(200000)
					creditosOtorgados += 1
					hombresDict[20] += 1
					comisionList.append(800)
					sumaDesvEst += desviacionEstandard(800)
		else:
			mujeres += 1
			if (tarjeta <= 15):
				credito = random.randint(1,100)
				if (credito <= 60):
					creditosList.append(50000)
					creditosOtorgados += 1
					mujeresDict[5] += 1
					comisionList.append(200)
					sumaDesvEst += desviacionEstandard(200)
				if (credito > 60 and credito <= 90):
					creditosList.append(100000)
					creditosOtorgados += 1
					mujeresDict[10] += 1
					comisionList.append(400)
					sumaDesvEst += desviacionEstandard(400)
				if (credito > 90 and credito <= 100):
					creditosList.append(150000)
					creditosOtorgados += 1
					mujeresDict[15] += 1
					comisionList.append(600)
					sumaDesvEst += desviacionEstandard(600)
					
plotThisShit()
print("Las creditos son de :", sum(creditosList))
print("n de creditos: ", hombres + mujeres)
print("mediana creditos:", np.median(creditosList))
print("media creditos:", np.mean(creditosList))
print("varianza creditos",np.var(creditosList))
print("desviacion estandar creditos es: ",np.std(creditosList))
print("moda creditos: ",mode(creditosList))
print("intervalos de confianza creditos",intervaloDeConfianza(creditosList))
print("comisiones", sum(comisionList))
print("n comisiones ", hombres + mujeres)
print("media comision",np.mean(comisionList))
print("mediana comision",np.median(comisionList))
print("varianza comisiones",np.var(comisionList))
print("desviacion estandar comision",np.std(comisionList))
print("moda comision",mode(comisionList))
print("intervalos confianza ",intervaloDeConfianza(comisionList))
print("creditos mujeres 5000 10000 - 15000:", mujeresDict[5], mujeresDict[10], mujeresDict[15])
print("creditos hombres 5000 - 10000 - 15000 - 20000):", hombresDict[5], hombresDict[10], hombresDict[15], hombresDict[20])



