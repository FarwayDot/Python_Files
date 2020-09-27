"""
Escriba un programa que lea a través de un registro de correo,
contruya un histograma usando un diccionario para contar
cuántos mensajes han llegado desde cada dirección de correo,
e imprimir el diccionario
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


for i in direccion:

	print(i,direccion[i])