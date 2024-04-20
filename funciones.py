from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

# conexion BD
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
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
        return -1
    
    if(usuario[4] != contrasena):
        return -2
    
    return {
        "ID": usuario[0],
        "USUARIO": usuario[1],
        "NOMBRE": usuario[2],
        "DNI": usuario[3],
        "EMAIL": usuario[5],
        "ROL": usuario[6]
    }
    
def allBienesPatrimoniales(top, codigo, ubicacion):
    try:
        cursor = conexion.cursor()
        cadena = "SELECT ID, IDUSER, DESCRIPCIONDELBIEN, MARCA, MODELO, SERIE, ESTADO, UBICACION, DETALLEUBICACION, OBS, INV2023, INV2022, INV2021, INV2020 "
        cadena += "FROM bienespatrimoniales WHERE 1=1 "
        if not codigo in [None, ""]:
            cadena += "AND ID = {0} ".format(codigo)
        if not ubicacion in [None, ""]:
            cadena += "AND UPPER(UBICACION) = '{0}' ".format(ubicacion.upper())
        cadena += "ORDER BY ID ASC "
        if top > 0:
            cadena += "LIMIT {0}".format(top)

        cursor.execute(cadena)
        bienes = cursor.fetchall()
        
        # REGRESAR COMO DICTIONARY
        bienes_dict = []
        for bien in bienes:
            bienes_dict.append({
                "ID": bien[0],
                "IDUSER": bien[1],
                "DESCRIPCIONDELBIEN": bien[2],
                "MARCA": bien[3],
                "MODELO": bien[4],
                "SERIE": bien[5],
                "ESTADO": bien[6],
                "UBICACION": bien[7],
                "DETALLEUBICACION": bien[8],
                "OBS": bien[9],
                "INV2023": bien[10],
                "INV2022": bien[11],
                "INV2021": bien[12],
                "INV2020": bien[13]
            })

        cursor.close()
        return bienes_dict

    except Exception as e:
        return "Error: {0}".format(e)

def addBienPatrimonial(coleccion):
    try:
        cursor = conexion.cursor()
        cadena = "INSERT INTO bienespatrimoniales (IDUSER, DESCRIPCIONDELBIEN, MARCA, MODELO, SERIE, ESTADO, UBICACION, DETALLEUBICACION, OBS, INV2023, INV2022, INV2021, INV2020) VALUES ("
        
        valores = []
        for key in ['IDUSER', 'DESCRIPCIONDELBIEN', 'MARCA', 'MODELO', 'SERIE', 'ESTADO', 'UBICACION', 'DETALLEUBICACION', 'OBS', 'INV2023', 'INV2022', 'INV2021', 'INV2020']:
            valor = coleccion.get(key, '') 
            valores.append("'{0}'".format(valor)) 
        
        cadena += ", ".join(valores) + ")"  
        
        cursor.execute(cadena)
        conexion.commit()
        last_inserted_id = cursor.lastrowid
        cursor.close()
        return last_inserted_id
    
    except Exception as e:
        return str("Error: {0}".format(e))

def updateBienPatrimonial(coleccion):
    try:
        cursor = conexion.cursor()
        cadena = "UPDATE bienespatrimoniales SET "
        
        valores = []
        for key in ['DESCRIPCIONDELBIEN', 'MARCA', 'MODELO', 'SERIE', 'ESTADO', 'UBICACION', 'DETALLEUBICACION', 'OBS', 'INV2023', 'INV2022', 'INV2021', 'INV2020']:
            valor = coleccion.get(key, '') 
            valores.append("{0} = '{1}'".format(key, valor)) 
        
        cadena += ", ".join(valores) + " WHERE ID = {0}".format(coleccion.get('ID', 0))  
        
        cursor.execute(cadena)
        conexion.commit()
        cursor.close()
        return True
    
    except Exception as e:
        return str("Error: {0}".format(e))

def deleteBienPatrimonial(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM bienespatrimoniales WHERE ID = {0}".format(id))
        conexion.commit()
        cursor.close()
        return True
    
    except Exception as e:
        return str("Error: {0}".format(e))