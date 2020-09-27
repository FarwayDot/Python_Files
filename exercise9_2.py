"""
Escribe un programa que ordene en categorias cada mensaje de correo segun el dia 
de la semana en que fue hecho el envio. Para lograrlo, busca las
lineas que comienzan por “From”, luego localiza la tercera palabra y manten un 
contador actualizado de cada uno de los dias de la semana. Al final del programa
imprime en pantalla el contenido de tu diccionario (el orden no importa).

"""

line=open('mbox-short.txt')

day=dict()

for i in line:
	
	i=i.rstrip()#Para eliminar los saltos de línea
	p=i.split()	#Para repartir por palabras en una lista

	#Para las cadenas que solo sea espacioin en blanco
	if len(i)==0:

		continue

	#Para continuar con otra iteración cuando no encuentre coincidencia
	if p[0]!="From":
		continue
	#Los días son la 3 cadena de texto
	#Si existe ya en el dict, se aumenta en 1
	if p[2] not in day:

		day[p[2]]=1

	else:

		day[p[2]]=day[p[2]]+1

#Solo impresión en la cmd
for i in day:

	print(i,day[i])
