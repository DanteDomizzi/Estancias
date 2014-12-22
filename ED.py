from numpy import *
import matplotlib.pyplot as plt
import sys


gmax = int(sys.argv[1])
nDimen = int(sys.argv[2])
nPart = 80 #NP(Numero de particulas) es 5 o 10 veces el valor de D(Dimensiones)
mx = int(sys.argv[3])
mn = int(sys.argv[4])
CR = 0.9
F = 0.5 #Factor de escala (0<=F<=1,2), se aconseja usar
		#un rango de 0.4 a 1.0



def function(x):
	return (x*x).sum(axis=1)

def function2(x):
	return abs(x).sum(axis=1) + abs(x).prod(axis=1)

def function3(x):
	suma = zeros(len(x))
	sumatoria = 0
	for c in range(len(x)):
		sumatoria = 0
		for i in range(len(x[c])):
			for j in range(i+1):
				sumatoria += x[c][j]
			suma[c] += sumatoria * sumatoria
	return suma

def imprimir(fx):
	for i in range(len(fx)):
		print fx[i]

def rand(lim):
    vec = zeros((lim))
    for i in range (lim):
        vec[i]=i
    random.shuffle(vec)
    return vec[:3]



def evolucionDiferencial(function):
	x = random.random((nPart,nDimen))*(mx-mn)+mn
	u = zeros((nPart,nDimen))
	for g in range(gmax):
		for i in range(len(x)):


			r = rand(len(x))
			jrand = random.randint(nDimen)
			for j in range(nDimen):
				if random.random() < CR or j == jrand:
					u[i][j] = x[r[2]][j] + F*(x[r[0]][j]-x[r[1]][j])
				else:
					u[i][j] = x[i][j]

			fx = function(x)
			
			fx_u = function(u)
			print fx_u[0]
			
			if	fx_u[i] <= fx[i]:
				x[i] = u[i]
			else:
				x[i] = x[i]

	imprimir(fx)

def main():
	if sys.argv[5] == '1':
		evolucionDiferencial(function)
	elif sys.argv[5] == '2':
		evolucionDiferencial(function2)
	else:
		evolucionDiferencial(function3)

if __name__ == "__main__":
    main()
