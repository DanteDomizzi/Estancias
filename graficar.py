# -*- coding: utf-8 -*-
import sys
from pylab import *
from numpy import *


try:
	data = open(sys.argv[1])
except:
	print("¡Error File!")


arr = []
i=0

for line in data:
	arr.append(float(line))

figure(1)
boxplot(arr)
title('Grafica de resultados')
show()

