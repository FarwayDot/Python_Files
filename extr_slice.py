"""
Rebanar el número que se coloca luego de los 2 puntos
Este es un ejemplo en el que obviamente exista tal número
Imagínense un pedido de filtrado donde quieren obtener el
número de algún modelo que tiene una nomenclatura standarizada

Algo así como xt4 : 5897

"""
st1=input("cadena: ")

p1=st1.find(":")

#print(p1) #opcional

st2=st1[p1+1:]

print(float(st2))