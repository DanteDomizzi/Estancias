 #-*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt
import sys

gmax = 2
#nPart = 5 #NP(Numero de particulas) es 5 o 10 veces el valor de D(Dimensiones)
CR = 0.9
F = 0.5 * (1 + random.random()) #Factor de escala (0<=F<=1,2), se aconseja usar
		#un rango de 0.4 a 1.0

def distanciaE(x1,x2):
	suma = 0
	for i in range(len(x1)):
		suma += (x1[i]-x2[i]) * (x1[i]-x2[i])
	return suma ** 0.5

def csMeasure(kmax,x,centroides):

	dividendo,divisor = 0,0
	nEle = numeroElementos(x,kmax)

	for i in range(kmax):
		temp = dividir(x,i)
		dividendo += csMeasureDividendo(temp,centroides)
		divisor += csMeasureDivisor(temp,centroides)
	return dividendo/divisor

	
def csMeasureDividendo(x,centroides):
	suma,ma = 0,0
	for i in range(len(x)-1):
		for j in range(i+1,len(x)):
			dis = distanciaE(x[i],x[j])
			if dis > ma:
				ma = dis
		suma += ma
		ma = 0
	return suma/len(x)

def csMeasureDivisor(x,centroides):
	suma,mi = 0,float("Inf")
	for i in range(len(centroides)-1):
		for j in range(i+1,len(centroides)):
			dis = distanciaE(centroides[i],centroides[j])
			if dis < mi:
				mi = dis
	return mi

def numeroElementos(x,kmax):
	numEle = zeros(kmax)
	for i in range(kmax):
		for j in range(len(x)):
			if x[j][len(x[j])-1] == i:
				numEle[i] += 1
	return numEle


def imprimir(x):
	for i in range(len(x)):
		for j in range(len(x[i])):
			print x[i][j],
		print 

def rand(lim):
    vec = zeros((lim))
    for i in range (lim):
        vec[i]=i
    random.shuffle(vec)
    return vec[:3]


def eva(chrom,kmax):
	return chrom[:kmax] > 0.5

def recalculo(centroides,elementos):
	new_centroides = sum(elementos,axis=0)
	return new_centroides[:len(centroides[0])] / len(elementos)


def dividir(x,n):
	lista = []
	for i in range(len(x)):
		if x[i][len(x[0])-1] == n:
			lista.append(x[i])

	return lista

def calculoDistancia(x,nDimen,centroides):
	mini = float('Inf')
	cen = -1
	distancia = 0

	for i in range(len(x)):
		for j in range(len(centroides)):
			distancia = distanciaE(centroides[j],x[i])
			if(distancia<mini):
				mini = distancia
				cen = j
		x[i][nDimen] = cen
		mini = float('Inf')

	return x


def evolucionDiferencial(x,nDimen,nPart,centroides):
	kmax = 3
	centroides = zeros((kmax,nDimen))
	maxim = zeros(nDimen)
	mini = zeros(nDimen)
	

	for i in range(nDimen):
		mini[i] = min(x[:,i])
		maxim[i] = max(x[:,i])

	j=0
	for i in range(nDimen):
		centroides[:,i] = random.random(len(centroides)) * (maxim[j]-mini[j])+mini[j]
		j+=1
	
	
	x = calculoDistancia(x,nDimen,centroides)
	xC = x.copy()
	

	u = zeros((nPart,nDimen+1))
	fx = zeros(nPart)
	fx_u = zeros(nPart)

	for c in range(len(x)):
		u[c][nDimen] = x[c][nDimen] 

	for g in range(gmax):
		for i in range(len(x)):		
			r = rand(len(x))
			jrand = random.randint(nDimen)
			for j in range(nDimen):
				if random.random() < CR or j == jrand:
					u[i][j] = x[r[2]][j] + F*(x[r[0]][j]-x[r[1]][j])
				else:
					u[i][j] = x[i][j]
			
			for c in range(len(centroides)):
				centroides[c] = recalculo(centroides,dividir(x,c))

			x = calculoDistancia(x,nDimen,centroides)
			fx[i] = csMeasure(kmax,x,centroides)
			fx_u[i] = csMeasure(kmax,u,centroides)
			
			for c in range(len(x)):
				u[c][nDimen] = x[c][nDimen] 
			
			
			if	fx_u[i] <= fx[i]:
				ind = x[i][nDimen]
				x[i] = u[i]
				x[i][nDimen] = ind
		

	for i in range(len(x)):
		xC[i][nDimen] = x[i][nDimen]

	imprimir(xC)
	

def main():

	data = None

	try:
		data = open(sys.argv[1])
		centroides = loadtxt("centroides.txt")
	except:
		print("¡Error File!")

	nlineas = 0
	dimen = 0

	for i in data:
		if nlineas == 0:
			for j in i:
				if j=='\t':
					dimen+=1
		nlineas+=1
	
	data.seek(0)
	x = zeros((nlineas,dimen+1))
	k,l = 0,0

	for i in data:
		i = i.split('\t')
		for j in i:
			x[k][l] = j
			l+=1
		l=0
		k+=1	

	evolucionDiferencial(x,dimen,nlineas,centroides)

if __name__ == "__main__":
    main()
