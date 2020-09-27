"""
Escribe un programa que pida el nombre de un fichero y despues
lea ese fichero, buscando lineas que tengan la forma:
X-DSPAM-Confidence: 0.8475
Cuando encuentres una l´ınea que comience por “X-DSPAM-Confidence:”, separa
esa lınea para extraer el numero en punto flotante que figure en ella. Cuenta esas 
l´ınea y calcula tambien el total de los valores de probabilidad de spam (spam con-
fidence) de estas lıneas. Cuando alcances el final del archivo, muestra en pantalla
el valor medio de probabilidad de spam.
"""
try:

	name=input("Nombre del fichero: ")
	line=open(name)

except: 

	print("Error en encontrar el archivo")
	quit()


c=0
ac=0

for i in line:

	#Para imprimir la las líneas correctamente
	i=i.rstrip()

	#Condición si es que no encuentra el texto en la línea correspondiente
	if i.find('X-DSPAM-Confidence: ')==-1:

		continue

	#Como encuentra el texto, entonces, sigue esta parte de código
	p=i.find(" ")		#En la línea, encontramos " "(Espacio en blanco)
	s=float(i[p+1:])	#Convertimos a flotante el número de probabilidad
	ac=ac+s 			#Suma las probabilidades obtenidas
	#print("%d.-" % c,i) #Se puede omitir esto
	c=c+1				#Suma la cantidad de probabilidades

print("Total de spam: ",c)
m=ac/c
print("Media de Spam: %.4f" % m)



