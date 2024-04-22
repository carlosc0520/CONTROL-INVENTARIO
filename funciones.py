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
    
def addUsuario(coleccion):
    try:
        # validar que nombre de usuario no exista
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE NOMBREUSUARIO = %s", (coleccion.get('NOMBREUSUARIO'),))
        usuario = cursor.fetchone()
        cursor.close()
        if(usuario):
            # ya existe
            return -1
        
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (NOMBREUSUARIO, NOMBRESYAPELLIDOS, DNI, PASSWORD, CORREOLABORAL, IDROL, IDCREADOR) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (coleccion.get('NOMBREUSUARIO'), coleccion.get('NOMBRESYAPELLIDOS'), coleccion.get('DNI'), coleccion.get('PASSWORD'), coleccion.get('CORREOLABORAL'), coleccion.get('IDROL'), coleccion.get('IDCREADOR')))
        conexion.commit()
        cursor.close()
        return cursor.lastrowid
    except Exception as e:
        return "Error: {0}".format(e)
    

# **** SELECT
def ubicaciones():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT DISTINCT ID, DESCRIPCION FROM ubicaciones_bienes")
        ubicaciones = cursor.fetchall()
        cursor.close()
        ubicaciones = list(map(lambda x: {"ID": x[0], "LABEL": x[1]}, ubicaciones))
        return ubicaciones
    except Exception as e:
        return []
    
def estados():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT DISTINCT ID, NOMBRE FROM estados_bienes")
        estados = cursor.fetchall()
        cursor.close()
        estados = list(map(lambda x: {"ID": x[0], "LABEL": x[1]}, estados))
        return estados
    except Exception as e:
        return []


# **** BIENES PATRIMONIALES
def allBienesPatrimoniales(top, codigo, ubicacion):
    try:
        cursor = conexion.cursor()
        cadena = "SELECT ID, IDUSER, DESCRIPCIONDELBIEN, MARCA, MODELO, SERIE, ESTADO, UBICACION, DETALLEUBICACION, OBS, INV2023, INV2022, INV2021, INV2020, CESTDO "
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
                "INV2020": bien[13],
                "CESTDO": "Activo" if bien[14] == "A" else "Inactivo"
            })

        cursor.close()
        return bienes_dict

    except Exception as e:
        return "Error: {0}".format(e)

def addBienPatrimonial(coleccion):
    try:
        cursor = conexion.cursor()
        cadena = "INSERT INTO bienespatrimoniales (IDUSER, DESCRIPCIONDELBIEN, MARCA, MODELO, SERIE, ESTADO, UBICACION, DETALLEUBICACION, OBS, INV2023, INV2022, INV2021, INV2020, CODPATR, CESTDO) VALUES ("
        
        valores = []
        for key in ['IDUSER', 'DESCRIPCIONDELBIEN', 'MARCA', 'MODELO', 'SERIE', 'ESTADO', 'UBICACION', 'DETALLEUBICACION', 'OBS', 'INV2023', 'INV2022', 'INV2021', 'INV2020', 'CODPATR']:
            valor = coleccion.get(key, '') 
            valores.append("'{0}'".format(valor)) 
        
        cadena += ", ".join(valores) + ", 'A')"  
        
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
        # SI CESTDO YA ES 'A' PONERLE 'I' SI ES 'I' PONERLE 'A'
        cursor.execute("UPDATE  bienespatrimoniales SET CESTDO = IF(CESTDO = 'A', 'I', 'A') WHERE ID = {0}".format(id))
        conexion.commit()
        cursor.close()
        return True
    
    except Exception as e:
        return str("Error: {0}".format(e))

def obtenerListCodigoBienPatrimonial():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT ID, CODPATR FROM bienespatrimoniales")
        bienes = cursor.fetchall()
        cursor.close()
        bienes = list(map(lambda x: {"ID": x[0], "LABEL": x[1]}, bienes))
        return bienes
    except Exception as e:
        return []

def obtenerBien(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT  ID, DESCRIPCIONDELBIEN, MARCA, MODELO, SERIE, ESTADO FROM bienespatrimoniales WHERE ID = {0}".format(id))
        bien = cursor.fetchone()
        cursor.close()
        return {
            "ID": bien[0],
            "DESCRIPCIONDELBIEN": bien[1],
            "MARCA": bien[2],
            "MODELO": bien[3],
            "SERIE": bien[4],
            "ESTADO": bien[5],
        }
    except Exception as e:
        return {
            "ID": 0,
            "DESCRIPCIONDELBIEN": "",
            "MARCA": "",
            "MODELO": "",
            "SERIE": "",
            "ESTADO": "",
        }


# **** DESPLAZAMIENTOS

def obtenerIdDatosdesplazamiento():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT (MAX(ID) + 1) id FROM datosdesplazamiento")
        id = cursor.fetchone()
        idGenerate = 0
        if id[0] == None:
            idGenerate = 1
        else:
            idGenerate = id[0]
        cursor.close()
        return idGenerate
    except Exception as e:
        return 0
    
def insertarDatosDesplazamiento(coleccion):
    try:
        cursor = conexion.cursor()
        cadena = "INSERT INTO datosdesplazamiento (FECHA, INTERNO, EXTERNO, DISPOSICION, MANTENIMIENTO, REASIGNACION, DUBIEN, DUABIEN, DRBIEN, DRABIEN, ACTAFIRMADA, IDUSER, IDBIEN) VALUES (NOW(), "
    
        valores = []
        for key in ['INTERNO', 'EXTERNO', 'DISPOSICION', 'MANTENIMIENTO', 'REASIGNACION', 'DUBIEN', 'DUABIEN', 'DRBIEN', 'DRABIEN', 'ACTAFIRMADA', 'IDUSER', 'IDBIEN']:
            valor = coleccion.get(key, '') 
            if isinstance(valor, int):
                valores.append(str(valor))
            else:
                valores.append("'{0}'".format(valor))
                
        cadena += ", ".join(valores) + ")"
        cursor.execute(cadena)
        conexion.commit()
        last_inserted_id = cursor.lastrowid
        cursor.close()
        return last_inserted_id

    except Exception as e:
        return "Error: {0}".format(e)

def actualizarDatosDesplazamiento(id, base64):
    # actualizar campo ACTAFIRMADA
    try:
        cursor = conexion.cursor()
        cadena = "UPDATE datosdesplazamiento SET ACTAFIRMADA = '{0}' WHERE ID = {1}".format(base64, id)
        cursor.execute(cadena)

        conexion.commit()
        cursor.close()
        return 1
    except Exception as e:
        return "Error: {0}".format(e)

def descargarDatosDesplazamiento(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT ACTAFIRMADA FROM datosdesplazamiento WHERE ID = {0}".format(id))
        acta = cursor.fetchone()
        cursor.close()
        return acta[0]
    except Exception as e:
        return "Error: {0}".format(e)

def obtenerDatoDesplazamientoBien(id):
    try:
        cursor = conexion.cursor()
        cadena = "SELECT A.ID, A.FECHA, B.CODPATR, A.INTERNO, A.EXTERNO, A.DISPOSICION, A.MANTENIMIENTO, A.REASIGNACION, A.DUBIEN, A.DUABIEN,"
        cadena += "A.DRBIEN, A.DRABIEN, B.DESCRIPCIONDELBIEN, B.MARCA, B.MODELO, B.SERIE, C.NOMBRE "
        cadena += "FROM datosdesplazamiento A INNER JOIN bienespatrimoniales B on B.ID = A.IDBIEN LEFT JOIN estados_bienes C ON C.ID = B.ESTADO WHERE A.ID = {0}".format(id)

        cursor.execute(cadena)
        
        dato = cursor.fetchone()
        cursor.close()
        return {
            "ID": dato[0],
            "FECHA": dato[1].strftime("%Y/%m/%d"),
            "CODPATR": dato[2],
            "INTERNO": "X" if dato[3] == 1 else "",
            "EXTERNO": "X" if dato[4] == 1 else "",
            "DISPOSICION": "X" if dato[5] == 1 else "",
            "MANTENIMIENTO": "X" if dato[6] == 1 else "",
            "REASIGNACION": "X" if dato[7] == 1 else "",
            "DUBIEN": dato[8],
            "DUABIEN": dato[9],
            "DRBIEN": dato[10],
            "DRABIEN": dato[11],
            "DESCRIPCIONDELBIEN": dato[12],
            "MARCA": dato[13],
            "MODELO": dato[14],
            "SERIE": dato[15],
            "ESTADO": dato[16]
        }
    except Exception as e:
        # retornar un diccionario vacio
        return {
            "ID": 0,
            "FECHA": "",
            "CODPATR": "",
            "INTERNO": "",
            "EXTERNO": "",
            "DISPOSICION": "",
            "MANTENIMIENTO": "",
            "REASIGNACION": "",
            "DUBIEN": "",
            "DUABIEN": "",
            "DRBIEN": "",
            "DRABIEN": "",
            "DESCRIPCIONDELBIEN": "",
            "MARCA": "",
            "MODELO": "",
            "SERIE": "",
            "ESTADO": ""
        }


def listarDatosDesplazamiento(top, codigo):
    try:
        cursor = conexion.cursor()
        cadena = "SELECT A.ID, A.FECHA, B.CODPATR, A.INTERNO, A.EXTERNO, A.DISPOSICION, A.MANTENIMIENTO, A.REASIGNACION, A.DUBIEN, A.DUABIEN,"
        cadena += "A.DRBIEN, A.DRABIEN FROM datosdesplazamiento A INNER JOIN bienespatrimoniales B on B.ID = A.IDBIEN WHERE 1 = 1 "
        if not codigo in [None, ""]:
            codigo = codigo.strip().upper()
            cadena += " AND UPPER(B.CODPATR) LIKE '%{0}%'".format(codigo)

        cadena += " ORDER BY A.ID ASC "
        if top > 0:
            cadena += " LIMIT {0}".format(top)


        cursor.execute(cadena)
        datos = cursor.fetchall()
        datos_dict = []
        for dato in datos:
            datos_dict.append({
                "ID": dato[0],
                "FECHA": dato[1].strftime("%Y-%m-%d"),  
                "CODPATR": dato[2],
                "INTERNO": "X" if dato[3] == 1 else "",
                "EXTERNO": "X" if dato[4] == 1 else "",
                "DISPOSICION": "X" if dato[5] == 1 else "",
                "MANTENIMIENTO": "X" if dato[6] == 1 else "",
                "REASIGNACION": "X" if dato[7] == 1 else "",
                "DUBIEN": dato[8],
                "DUABIEN": dato[9],
                "DRBIEN": dato[10],
                "DRABIEN": dato[11]
            })
        cursor.close()
        return datos_dict
    except Exception as e:
        return []