#librerias
import requests
import json
import pymysql
from flask import Flask, request, jsonify

#Servidor flask
app = Flask(__name__)

#Creación de la conexión con la base de datos local
db = pymysql.connect(host="localhost", port=3308, user="root", password="",db="fifa")
cursor = db.cursor()

#Ruta del servidor para consultar jugadores en la base de datos
@app.route('/listar')
def verJugadores(conn=db):
	try:
		cursor = conn.cursor()
		#Ejecucion sentencia sql para consulta
		cursor.execute('select * from jugadores')
		datos=cursor.fetchall()
		print (datos)
		return jsonify(datos)
	except Exception as ex:
		return "Error"

#Función para almacenar los datos recibidos de la API
def save_data(data,conn):
    cursor = conn.cursor()
    #sentencia sql que enviamos al servidor bd
    cursor.execute('insert into jugadores(jugador) values(%s)', (data,))
    conn.commit()
    #conn.close()


#Obtener los datos de la API y convertirlos a formato JSON
def get_player(url="https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1", offset=0):
	response = requests.get(url)

	#Codigo 200 que representa respuesta exitosa del servidor
	if response.status_code == 200:

		#Capturamos los items de la API
		content = response.json()
		items = content.get('items', [])
		#print(items)

		#Si encontramos items desde la API
		if items:
			#Vamos añadiendo cada item 1 por 1
			for player in items:
				jugador = player
				save_data(json.dumps(jugador), db)




#Iniciar el servidor 
if __name__ == '__main__':
	#url de la api que vamos a consumir
	url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"
	
	#Recogemos los datos de la api y los subimos a nuestra bd
	get_player(url)

	#Iniciamos el servidor flask
	app.run(debug = True, use_reloader=False)