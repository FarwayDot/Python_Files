"""
	Pedir numeros para luego imprimir el max y minimo de ellos

"""
c=0
b=[]

while True:
	
	a=input("Numero: ")

	if a=="fin":

		print("Terminado")
		break

	try :
		 
		c=int(a)

	except:

		print("\nError")
		continue
	
	b.append(c)

print("\nMaximo: ",max(b),"\nMinimo: ",min(b))
	

