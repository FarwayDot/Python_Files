"""Contar las palabras del fichero romeo.txt"""

line=open('mbox-short.txt')

cont=dict()

for i in line:

	palabras=i.split()

	for p in palabras:

		if p not in cont:

			cont[p]=1

		else:

			cont[p]+=1


print(cont)