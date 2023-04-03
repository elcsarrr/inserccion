from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1', 
        database='condominio'
    )
    if conexion.is_connected():
        print("conexion exitosa")
        cursor=conexion.cursor()#un cursor es un objeto relacionado con las bases de datos, hace lecturas de datos, inserciones,actualiza
        nombree = input("Ingresa un nombre: ")
        cursor.execute("INSERT INTO tipousuario (Nombre) VALUES ('" + nombree + "')")
        #  cursor.execute("UPDATE tipousuario SET Nombre " 'NOMBRE QUE QUIERO CAMBIAR' WHERE Codigo = 7  y se puede poner un mensaje
        conexion.commit() # confirmar la accion que estamos ejecutando
        print("registro insertado con exito")
except Error as ex:
    print("error durante la conexion",ex )
finally:
    if conexion.is_connected():
        conexion.close() # se cerro la conexion a la 80.
        print ("la conexion ha finalizado")

