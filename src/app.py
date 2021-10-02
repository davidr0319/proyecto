from flask import Flask, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion = MySQL(app)



@app.route('/')
def verJugadores():
	try:
		cursor = conexion.connection.cursor()
		sql="SELECT * FROM jugadores"
		cursor.execute(sql)
		datos=cursor.fetchall()
		print (datos)
		return "OK..."
	except Exception as ex:
		return "Error"

if __name__ == "__main__":
	app.config.from_object(config['development'])
	app.run()
 