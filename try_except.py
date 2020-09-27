# Try_except

num1 = input('Enter a number: ')

#Intenta convertir num1 a tipo int
try:

	num2 = int(num1)

#Si no puedo o no es válido, entonces se le asigna -1
#-1 es un número obviamente, pero solo es para confirmar
except: 
	
	num2 = -1

# Para los mensajes de confirmación
if num2 > 0:

	print('Nice Work')

else: 
	
	print('Not a number')