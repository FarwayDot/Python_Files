"""
Problema 1 de ficheros

Imprimir algunas líneas del fichero mbox-short.txt
Luego convertirlas en mayúsculas e imprimirlas
"""
#Esto imprime pero en base a caracter por caracter
#line=open('mbox-short.txt')
#text=line.read()
#print(text[0:256].upper())

#Esto imprime linea por linea
try:
	a=input("Nombre: ")
	b=int(input("Numero de Lineas: "))
	line=open(a)

except:

	print("No es posible continuar con el procedimiento")
	quit()

c=0
for i in line:

	c=c+1
	i=i.rstrip()
	if c<=b:
		print("%d.- " % c,i)
