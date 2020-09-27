#Mostrar horas y paga por hora, así como la paga total


hours=input('Horas: ')
rate_h=input('Paga por hora: ')

#Para verificar que rate_h sea positivo

def pay1(h,r) :

	if (h>40):

		return((h-40)*1.5*r + 40*r)

	else:

		return(h*r)

try :

	rate_h=float(rate_h)

	if rate_h>0 :
		
		#Para verificar que hours sea positivo. Aunque sería mejor colocar el 2do 'if' primero
		if int(hours)>40 :

			paga = pay1(int(hours),rate_h)

		elif int(hours)<=40 and int(hours)>0 :

			paga = pay1(int(hours),rate_h)

		else :

			paga = "No válido"

	else:

		paga = "No válido"

except :

	print("No válido")
	quit()


print('\nPaga = ', paga)