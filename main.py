import requests
import json
import pymysql

db = pymysql.connect(host="localhost", port=3308, user="root", password="",db="fifa")
cursor = db.cursor()

def save_data(data,conn):
    cursor = conn.cursor()
    cursor.execute('insert into jugadores(jugador) values(%s)', (data,))
    conn.commit()
    #conn.close()


#Obtener los datos de la API y convertirlos a formato JSON
def get_player(url="https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1", offset=0):
	response = requests.get(url)

	#Codigo 200 que representa respuesta exitosa del servidor
	if response.status_code == 200:
		#print(response.content)
		#Capturamos los items de la API
		content = response.json()
		items = content.get('items', [])
		#print(items)

		if items:
			#cursor = db.cursor()
			for player in items:
				jugador = player
				#print(jugador)
				#nombre = jugador.get('firstName', [])
				#print(nombre)
				# sql = "INSERT INTO jugadores(jugador) values(jugador)"
				# cursor.execute(sql)
				# db.commit()
				#print(json.dumps(jugador))
				save_data(json.dumps(jugador), db)


#Iniciar el servidor 
if __name__ == '__main__':
	url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"
	
	get_player(url)

		#print (content)