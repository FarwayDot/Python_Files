"""Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”.
 Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y 
 la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número,
  detecta su fallo usando try y except, muestra un mensaje de error y pasa al número siguiente."""

c=0
acum=0
med=0
b=0

while True:
	
	a=input("Numero: ")

	if a=="fin":

		print("Terminado")
		break

	try :
		 
		b=int(a)

	except:

		print("\nError")
		continue
	c = c + 1
	acum = acum + b

med = acum/c

print("\nTotal: ",acum,"\nCantidad: ",c,"\nMedia: ",med)