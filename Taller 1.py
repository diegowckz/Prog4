import sqlite3

db = sqlite3.connect('db/taller1_libro')
cursor = db.cursor()

#Creacion de Tabla
cursor.execute('''CREATE TABLE LIBRO(ISBN INTEGER PRIMARY KEY,
                  cant_pags INTEGER, Autor TEXT, public INTEGER)''')

#Lectura
ISBN = input("ISBN de libro: ")
cant_pags = input("Cantidad de paginas: ")
Autor = input("Nombre del Autor: ")
public = input("Año de publicacion: ")

#Insertar en Tabla
cursor.execute('''INSERT INTO LIBRO(ISBN, cant_pags, Autor, public)''')

db.commit()
