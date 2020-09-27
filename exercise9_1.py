""" Escriba un programa que lea las palabras de 
words.txt y las almacene como claves en un diccionario.
No importa qué valores tengan. Después puedes usar
el operador in como un modo rápido de comprobar si
una cadena está en el diccionario"""

line=open('words.txt')

key=dict()
p=0
q=0

for m in line:

	p=p+1
	m=m.rstrip()
	a=m.split()
	if len(a)==0: continue
	
	for n in a:

		if n not in key:

			key[n]=1

		else:

			key[n]=key[n] + 1


for i in key:

	print(i,key[i])



#print(key)


	

