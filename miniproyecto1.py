# Miniproyecto 1

import mysql.connector as db  # Importar SQL para Python

# Crear conexión

mp1 = db.connect(
    host = "127.0.0.1",
    user = "root", 
    passwd = "Daniel2023",
    database = "mp1"
)

my_cursor = mp1.cursor()     # Permite interactuar con el motor SQL

primera_consulta = "SELECT * FROM sociedades WHERE rut = '77886308-1'"  # Obtener la información de la sociedad con rut 77886308-1

my_cursor.execute(primera_consulta)

print("Toda la información de la sociedad con Rut 77.886.308-1")

rows = my_cursor.fetchall()     # Extrae todo el conetenido guardado en el cursor
for row in rows:                # Imprimir Filas
    print(row)

segunda_consulta = "SELECT * FROM sociedades WHERE capital >= 400000000" 

my_cursor.execute(segunda_consulta) # Obtener todas las sociedades cuyo capital es mayor o igual a 400.000.000

print("Todas las sociedades cuyo capital es mayor o igual a MM$400")

rows = my_cursor.fetchall()
for row in rows:
    print(row)

# Insertar nueva sociedad a la Tabla

nueva_fila = "INSERT INTO sociedades(id, rut, nombre, registro, comuna, capital) VALUES (%s, %s, %s, %s, %s, %s)" 
fila = (5156305, "77721389-K", "Estrellas SpA", "2024-03-11",  "PROVIDENCIA", 1000000)
my_cursor.execute(nueva_fila, fila)

mp1.commit()













