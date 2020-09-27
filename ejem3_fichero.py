#Sorpresa en el código
p=0
try:

	a=input("Ingresar nombre del fichero: ")
	if a.lower()=="na na boo boo":

		print("NA NA BOO BOO para ti! >:v")
		p=-1
	line=open(a)
	

except:

	if p==-1:

		quit()

	print("Error al encontrar el archivo: ",a)
	quit()

c=0

for i in line:

	c=c+1

print("El número de líneas es " + str(c)+" de "+a)