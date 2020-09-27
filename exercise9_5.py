"""
Este programa debe guardar el nombre de dominio
desde donde se envió el mensaje envez de quién
mandó el mensaje(es decir, la dirección de correo
completo). Al final del programa, imprime en pantalla
el contenido de tu diccionario.
"""

line=open('mbox-short.txt')

direccion=dict()


for i in line:

	i=i.rstrip()
	p=i.split() #Una lista para toda la línea

	if len(p)==0: continue
	if p[0]!="From": continue #Solo entran las líneas que contengan From

	q=p[1].split("@") #El elemento 2(p[1]) es donde se encuentra la dirección
					  #y separamos en 2 "antes del @" y "despues del @"
	print(q)

	if q[1] not in direccion:

		direccion[q[1]]=1

	else:

		direccion[q[1]]=direccion.get(q[1],0) + 1


for i in direccion:

	print(i,direccion[i])

print(direccion);
