from math import sqrt
from random import uniform as rng
import matplotlib.pyplot as plottalo
import sys

def random_gen(N):
	random_list=[]
	for i in range (1,N+1):
		random_list.append([rng(-1,1),rng(-1,1)])
	return random_list

def pi(punti):
	M=0
	for punto in punti:
		if punto[0]**2+punto[1]**2<=1:
			M+=1
	pi=4*M/len(punti)
	return pi

def multiple_pi(N,K):
	result=[]
	for i in range (K):
		punti=random_gen(N)
		pigreco=pi(punti)
		result.append(pigreco)
	return result

def avarage(list):
	somma=0
	for i in range (len(list)):
		somma+=list[i]
	return somma/len(list)

def stdev(list):
	val=0
	for i in range (len(list)):
		val+=(list[i]-avarage(list))**2
	return sqrt(val/len(list))

def result(N,K):
	lista=[]
	for i in range (N):
		pivalues=multiple_pi(i+1,K)
		media=avarage(pivalues)
		dev=stdev(pivalues)
		listinit=[]
		listinit.append(media)
		listinit.append(dev)
		lista.append(listinit)
	return lista

if __name__ == "__main__" :
	if len(sys.argv)<3:
		print("Dammi due numeri")
	else:
		N = int(sys.argv[1])
		K = int(sys.argv[2])
		risultato=result(N,K)
		print(risultato)

		x = []
		y = []
		for i in range(len(risultato)):
        		x.append(i + 1)
        		y.append(risultato[i][1])
		plottalo.loglog(x, y)
		plottalo.xlabel("N")
		plottalo.ylabel("Deviazione standard")
		plottalo.title("Deviazione standard vs N")
		plottalo.show()


