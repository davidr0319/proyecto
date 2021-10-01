import numpy as np
from random import randrange


def cansplit(array):
	sum = 0
	tam = np.size(array)

	for i in range(0, tam):
		sum += array[i]

	print (array)


	if (sum%2 == 0):
		aux = 0
		cont = 0
		a = 0
		while (cont < (sum/2)):
			cont += array[aux]
			aux += 1

		if cont == (sum/2):
			array2 = np.zeros(shape = aux)
			array3 = np.zeros(shape = tam-aux)
			for i in range(0, aux):
				array2[i] = array[i]

			for i in range(aux, tam):
				array3[a] = array[i]
				a = a + 1

			print (array2)
			print (array3)
			return 1
		
		else:
			return 0


	else:
		return 0


def main():
	tam = int(input('De que tamano desea el vector? \n'))
	array = np.zeros(shape = tam)

	for i in range(0,tam):
		array[i] = int(input('Valor '+str(i)+':'))


	respuesta = cansplit(array)
	
	print (respuesta)

main()



