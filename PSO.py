from numpy import *
import matplotlib.pyplot as plt

def function(x):
	return ((x*x).sum(axis=1))

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

def evaluate(x, mn, mx):
	vali = x>=mn
	vali2 = x<mx
	prom = (sum(x[vali])+sum(x[vali2])) / (len(x[vali]) + len(x[vali2]))
	vali = x<mn
	x[vali] = prom
	vali = x>mx
	x[vali] = prom
	return x

def principal(function, mn, mx):
	C1 = 1.4
	C2 = 1.4
	W = .7
	nDimen = 30
	nPart = 30
	x = random.random((nPart,nDimen))*(mx-mn)+mn
	x = evaluate(x,mn,mx)
	print x
	fx = function(x)
	pbest = x.copy()
	fx_pbest = fx.copy()
	index = argmin(fx)
	gbest = x[index]
	fx_gbest = fx[index]

	gmax=2000
	i=0
	v = zeros((nPart,nDimen))
	lista = []

	while i<gmax:
		v = W*v+C1*random.random()*(pbest-x)+C2*random.random()*(gbest-x)
		x = x + v
		x = evaluate(x,mn,mx)
		fx = function(x)
		index = fx<fx_pbest
		pbest[index] = x[index].copy()
		fx_pbest[index] = fx[index].copy()
		index = argmin(fx)
		if fx_pbest[index] < fx_gbest:
			gbest = x[index]
			fx_gbest = fx[index]
		lista.append(fx_gbest)
		i+=1

	print fx_gbest," : ",gbest
	plt.scatter(range(gmax),lista)
	plt.show()

def main():
	principal(function,-100,100)
	principal(function2,-10,10)
	principal(function3,-100,100)

if __name__ == "__main__":
    main()
