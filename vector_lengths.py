#longitud de vectores o norma

import math

p=0

while p==0:

	cant=int(input("Ingresar la dimensión: "))

	vector=list()

	for i in range(0,cant):

		b=float(input("Ingresar un número: "))
		vector.append(b)

	print(vector)

	sum_square=0

	for i  in range(0,cant):

		sum_square=(vector[i]**2)+sum_square


	print(sum_square)
	length=math.sqrt(float(sum_square))
	print("Longitud: "+str(length))

	p=int(input("Desea continuar Si[0] o No[1]"))