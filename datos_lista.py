"""Pedir al usuario que ingrese números hasta que se
escriba la palabra 'done'. Luego imprimir los valores
máximo, mínimo, y el promedio de los elementos que
se ingresó"""

p=list()

while True:

	a=input("Ingresar un número: ")

	if a.lower()=='done': break

	a=float(a)

	p.append(a)

print("Maximo: ",max(p),"\nMinimo: ",min(p),"\nPromedio: ",sum(p)/len(p))