#Librerias
import numpy as np
from random import randrange


#Función cansplit para verificar si un vector se puede dividir en 2 partes iguales,
#tal que la suma de los valores de cada parte sean iguales

def cansplit(array):

	#Inicializamos variable suma para conocer valor de la suma de todas las variables,
	#ya que si este es impar quiere decir que no se puede dividir en 2 partes iguales

	sum = 0
	#Capturamos el tamaño del vector
	tam = np.size(array)

	#Realizamos la suma
	for i in range(0, tam):
		sum += array[i]

	print (array)

	#Comprobamos que se pueda dividir en 2 partes (Teoricamente:: es decir que la suma
	#de sus valores sea par)
	if (sum%2 == 0):
		#Si es par, intentamos dividirla

		#aux para controlar las posiciones del vector; cont va acumulando la suma de los valores
		#desde la primera posición, si esta supera la mitad de la suma total quiere decir que no 
		#se puede dividir en partes iguales
		aux = 0
		cont = 0

		#variables auxiliar para controlar posiciones de vector
		a = 0
		while (cont < (sum/2)):
			cont += array[aux]
			aux += 1

		#Si se cumple, damos por terminado el proceso al final del if con retorno de 1
		if cont == (sum/2):
			#Si cont es igual a la mitad del valor del vector quiere decir que se puede dividir
			#Construimos entonces las dos mitades
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
		#Si el cont fue mayor a la mitad del valor total del vector damos por terminado el proceso
		else:
			return 0

	#Si no es par, damos por concluído el proceso
	else:
		return 0


def main():
	tam = int(input('De que tamano desea el vector? \n'))
	array = np.zeros(shape = tam)

	for i in range(0,tam):
		array[i] = int(input('Valor '+str(i)+':'))


	respuesta = cansplit(array)
	
	print (respuesta)

if __name__ == "__main__":
	main()



