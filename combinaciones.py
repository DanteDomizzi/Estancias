from numpy import *

def combina(x):
	tam_T = 1

	for i in range(len(x)):
		tam_T *= x[i]

	iteraciones = zeros(len(x))
	contadores = zeros(len(x))
	valores = zeros(len(x))
	aux_tam = tam_T
	resultado = zeros((tam_T,len(x)))
	index = None
	respaldo = zeros(len(x))

	for i in range(len(x)): 
		respaldo[i] = x[i]

	for i in range(len(x)):
		aux_tam/=x[i]
		iteraciones[i] = aux_tam

	for i in range(tam_T):
		resultado[i] = valores
		contadores += 1
		index = contadores >= iteraciones
		valores[index] += 1
		for j in range(len(x)):
			if valores[j] == respaldo[j] and contadores[j] >= iteraciones[j]:
				valores[j] = 0
		index = contadores >= iteraciones
		contadores[index] = 0
	print resultado

def main():
	x = input()
	combina(x)

main()
	
