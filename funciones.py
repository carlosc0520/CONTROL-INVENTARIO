from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

# conexion BD
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="controldeinventario"
)

# CRUD
def listarUsuarios():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def ValidarUsuario(usuario, contrasena):
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE NOMBREUSUARIO = %s", (usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    if(not usuario):
        return 0
    
    if(usuario[4] != contrasena):
        return 1
    
    return 2
    
    