"""
El siguiente programa debería evaluar ciertas puntuaciones de entradas(entre 0 y 1) y clasificarlas
por medio de un comentario como SOBRESALIENTE, NOTABLE, etc.
También debo manejar entradas erróneas como 10 e incluso palabras

"""

def clasif (p) :

	if p>=0 and p<=1:

		if p>=0.9 :

			print("\nSobresaliente")
		
		elif p>=0.8 :

			print("\nNotable")

		elif p>=0.7 :

			print("\nBien")

		elif p>=0.6 :

			print("\nSuficiente")

		else:

			print("\nInsuficiente") 

	else :

		print("\nPuntuación incorrecta")	

try :

	puntuacion = float(input("Ingresar puntuación: "))

except:

	print("\nNo number")
	quit()

clasif(puntuacion)

