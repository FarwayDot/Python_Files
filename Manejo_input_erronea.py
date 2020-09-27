#Tratar un error de entrada con try except

#a=input("Introduzca las horas: ")
#b=input("Introduzca la paga por horas: ")

try :

	p=int(input("Introduzca las horas: "))
	ph=int(input("Introduzca la paga por horas: "))
	#p=int(a)
	#ph=int(b)

except:

	p,ph=-1,-1

if p>0 and ph>0 :

	print("\nPaga", p*ph )

else:

	print("\nError, por favor ingrese números")