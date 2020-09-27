"""
La función read entendí que te devuelve la información en sí del
fichero. Osea, si continuemos con el fichero mbox-short.txt, el read
devuelve cada caractér con todo y salto de línea
"""

linea=open('mbox-short.txt')
text=linea.read()
p=text.find("Received")
print(p)
print("\n"+text[0:108])