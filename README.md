# Prueba Técnica desarrollador Backend

###### David Esteban Ramirez Cardona
###### Ingeniero de Sistemas
###### C.C 1088017828

#### Para instalar las dependencias correspondientes, se debe utilizar el archivo *requeriments.txt* que se encuentra en el repositorio.

## Prueba 1: Algoritmia
Para correr la primera parte de la prueba, basta con ejecutar el archivo *prueba1.py* o desde una linea de comandos mediante la instrucción *python prueba1.py*.
Una vez ejecutado el archivo py, se solicita al usuario defina el tamaño del vector, seguido de los valores que almacenará el mismo.

## Prueba 2: Manejo de Python
Para ejecutar el archivo referente a la segunda parte de la prueba (*main.py*), primero se deben tener en cuenta los siguientes requisitos:
* Se debe contar con un sistema de gestión de bases de datos y un servidor web, en mi caso, utilicé XAMPP para gestionar la base de datos con MySQL de forma local y Apache para el servidor web.
* Se debe crear una base de datos con el nombre *fifa* y una tabla con nombre *jugadores* que contenga 2 columnas; la primera un id identificador automatico y la segunda un campo *jugador* de tipo JSON NOT NULL, a continuación dejo la sentencia sql para crearla:

```
CREATE TABLE jugadores(
	 id BIGINT PRIMARY KEY AUTO_INCREMENT,
     jugador JSON NOT NULL
);
```

* Para la conexión con la base de datos se utilizaron los siguientes parametros:

```
host="localhost"
port=3308
user="root"
password=""
db="fifa"
```

En caso de necesitar cambiar algún parametro, estos se encuentran en la fila 11 del archivo *main.py*

* Para el servidor web, se utilizó la conexión por defecto, localhost:8000

Una vez se completen los requisitos y se tenga en ejecución los dos servidores (Web y Gestor de BD), se procede a ejecutar el archivo *main.py* por consola mediante la instrucción *python main.py*. Una vez se ejecuta se suben los datos de la API de fifa a la base de datos correspondiente.
Para visualizar los datos se debe utilizar la siguiente dirección en el navegador, referente a la ruta de dicha operación:

> localhost:8000/listar
