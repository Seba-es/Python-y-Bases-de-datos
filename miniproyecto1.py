# Instalar conector SQL Pip install mysql-connector-python

import mysql.connector as db

# Definir consultas SQL
first_query = "SELECT * FROM sociedades WHERE rut = 77882427-2" 

second_query = "SELECT nombre FROM sociedades WHERE capital >= 400000000"

base = db.connect(
    host= "127.0.0.1", 
    user= "root",
    passwd= "Casa123",
    database = "mp1"
)
    
my_cursor = base.cursor() # Permite interacturar con el motor SQL

my_cursor.execute(first_query) # Ejecuta la primer consulta

print("Toda la información de la sociedad con Rut 77.882.427-2")

rows = my_cursor.fetchall()
for row in rows:
    print(row)

my_cursor.execute(second_query) # Ejecuta la segunda consulta

print("Obtener todas las sociedades cuyo capital es mayor o igual a $400.000.000 (400 millones de pesos)")

rows = my_cursor.fetchall()
for row in rows:
    print(row)

# Insertar una nueva fila en la Base de datos   

