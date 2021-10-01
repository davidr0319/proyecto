import requests
import json


def get_player(url="https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1", offset=0):
	response = requests.get(url)


	if response.status_code == 200:
		#print(response.content)
		content = response.json()
		items = content.get('items', [])

		if items:
			for player in items:
				jugador = player
				#print(jugador)
				nombre = jugador.get('firstName', [])
				print(nombre)


if __name__ == '__main__':
	url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"
	
	get_player()

		#print (content)