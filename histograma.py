"""Implementar un histograma para la cantidad de 
letras que ingresa un usuario"""

word=input("Ingresar una palabra: ")
d=dict()

for i in word:

	if i not in d:

		d[i]=1

	else:

		d[i]=d[i]+1


print(d)