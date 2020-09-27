"""Escriba un programa que lea a través de 
los datos de un buzón de correo, y cuando 
una línea que empieze por 'From', la divida}
en palabras usando la función split. Estamos
interesado en quién nos envían el mensaje, que
es la segunda palabra de la línea From."""

line=open('mbox-short.txt')
p=list()
name=list()
q=list()

for i in line:

	i=i.rstrip()
	p=i.split()
	if len(p)==0: continue
	if p[0]!="From" : continue
	name.append(p[1])

for i in name:

	q=i.split("@")
	print(q[0])

print("Existen ",len(name)," lineas que comienzan con 'From'")
