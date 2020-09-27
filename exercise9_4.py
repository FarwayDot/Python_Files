"""
Añade el código al programa anterior para
localizar quién tiene más mensajes en el fichero.
Desspués de que los datos hayan siido leídos y el
diccionario haya sido creado, busca a través del
diccionario usando en bucle máximo para encontrar 
quién es el que tiene más mensajes e imprime cuántos
mensajes tiene esa persona.

"""

line=open('mbox-short.txt')
c=0
direccion=dict()

for i in line:

	c=c+1
	i=i.rstrip() #Para los saltos de línea
	p=i.split()

	if len(p)==0: continue
	if p[0]!="From": continue

	if p[1] not in direccion:

		direccion[p[1]]=1

	else:

		direccion[p[1]]=direccion.get(p[1],0)+1

#Imprime todos los valores
b=max(direccion.values())

for i in direccion:

	print(i,direccion[i])

	if direccion[i]>=b:

		q=i

print("\nEl mayor de todos es " + str(q)+" con " + str(b) + " mensajes.")
