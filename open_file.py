# Abriendo un fichero

# Para abrir un fichero debe encontrarse en la misma carpeta
# donde se encuentra este script

linea=open('mbox-short.txt')
print(linea) #Se imprimirá información del fichero

c=0

#Cada valor que asume i es una cadena de caracteres igual a una línea
for i in linea:

	c=c+1 

	#Solo mostramos solo una línea de todas
	if c==2:
		i=i.rstrip()#Para que el salto de línea no afecte la salida
		print("Linea "+str(c)+".- "+i)

	

print("Numero de líneas: ", c)

