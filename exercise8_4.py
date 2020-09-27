"""Escirbir un programa que abra el archivo romeo.txt y lo 
lea línea a línea. Para cada línea, divídela en una lista
de palabras usando la función split.
Para cada palabra, mira a ver si esa palabra ya existe en la lista.
Si no es así, añádela."""

line=open('romeo.txt')
val=list()
a=list()
for i in line:

	i=i.rstrip()
	a=i.split()
	
	for i in a:

		if i in val:

			continue

		val.append(i)


t=val.sort()
print(val)



