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
        cadena = "SELECT A.ID, A.CODPATR, A.IDUSER, A.DESCRIPCIONDELBIEN, A.MARCA, A.MODELO, A.SERIE, B.NOMBRE ESTADO, "
        cadena += "C.DESCRIPCION UBICACION, A.DETALLEUBICACION, A.OBS, A.INV2023, A.INV2022, A.INV2021, A.INV2020, A.CESTDO "
        cadena += "FROM bienespatrimoniales A "
        cadena += "LEFT JOIN estados_bienes B ON B.ID = A.ESTADO "
        cadena += "LEFT JOIN ubicaciones_bienes C ON C.ID = A.UBICACION "        
        cadena += "WHERE 1=1 AND A.ESTADO IS NOT NULL"

        if not codigo in [None, ""]:
            cadena += " AND ID = {0} ".format(codigo)
        if not ubicacion in [None, ""]:
            cadena += " AND UPPER(UBICACION) = '{0}' ".format(ubicacion.upper())
        cadena += " ORDER BY ID ASC "
        if top > 0:
            cadena += "LIMIT {0}".format(top)

        cursor.execute(cadena)
        bienes = cursor.fetchall()
        
        # REGRESAR COMO DICTIONARY
        bienes_dict = []
        for bien in bienes:
            bienes_dict.append({
                "ID": 0 if bien[0] == None else bien[0],
                "CODPATR": "" if bien[1] == None else bien[1],
                "IDUSER": "" if bien[2] == None else bien[2],
                "DESCRIPCIONDELBIEN": "" if bien[3] == None else bien[3],
                "MARCA": "" if bien[4] == None else bien[4],
                "MODELO": "" if bien[5] == None else bien[5],
                "SERIE": "" if bien[6] == None else bien[6],
                "ESTADO": "" if bien[7] == None else bien[7],
                "UBICACION": "" if bien[8] == None else bien[8],
                "DETALLEUBICACION": "" if bien[9] == None else bien[9],
                "OBS": "" if bien[10] == None else bien[10],
                "INV2023": "" if bien[11] == None else bien[11],
                "INV2022": "" if bien[12] == None else bien[12],
                "INV2021": "" if bien[13] == None else bien[13],
                "INV2020": "" if bien[14] == None else bien[14],
                "CESTDO": "Activo" if bien[15] == "A" else "Inactivo"
        })

        cursor.close()
        return bienes_dict

    except Exception as e:
        return "Error: {0}".format(e)

def obtenerBienPatrimonial(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT ESTADO, UBICACION FROM bienespatrimoniales WHERE ID = {0}".format(id))
        bien = cursor.fetchone()
        cursor.close()
        return {
            "ID": id,
            "ESTADO": bien[0],
            "UBICACION": bien[1]
        }
    except Exception as e:
        return {
            "ID": 0,
            "ESTADO": "",
            "UBICACION": ""
        }

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
        for key in ['CODPATR', 'DESCRIPCIONDELBIEN', 'MARCA', 'MODELO', 'SERIE', 'ESTADO', 'UBICACION', 'DETALLEUBICACION', 'OBS', 'INV2023', 'INV2022', 'INV2021', 'INV2020']:
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

def rankings():
    try:
        cursor = conexion.cursor()
        cadena = """
        SELECT 
            (SELECT COUNT(Z.ID) FROM bienespatrimoniales Z WHERE Z.CESTDO = 'A') AS TOTAL,
            SUM(CASE WHEN A.ESTADO = 1 THEN 1 ELSE 0 END) AS OPERATIVO,
            SUM(CASE WHEN A.ESTADO = 2 THEN 1 ELSE 0 END) AS BAJA,
            SUM(CASE WHEN A.UBICACION = 1 THEN 1 ELSE 0 END) AS ALMACEN,
            SUM(CASE WHEN A.UBICACION != 1 THEN 1 ELSE 0 END) AS USO
        FROM 
            bienespatrimoniales A
        """

        cursor.execute(cadena)
        ranking = cursor.fetchone()
        cursor.close()
        return {
            "TOTAL": 0 if ranking[0] == None else ranking[0],
            "OPERATIVO": 0 if ranking[1] == None else ranking[1],
            "BAJA": 0 if ranking[2] == None else ranking[2],
            "ALMACEN": 0 if ranking[3] == None else ranking[3],
            "USO": 0 if ranking[4] == None else ranking[4]
        }
    except Exception as e:
        print(e)

        return {
            "TOTAL": 0,
            "OPERATIVO": 0,
            "BAJA": 0,
            "ALMACEN": 0,
            "USO": 0
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

def actualizarDatosDesplazamiento(id, base64, nombre):
    # actualizar campo ACTAFIRMADA
    try:
        cursor = conexion.cursor()
        cadena = "UPDATE datosdesplazamiento SET ACTAFIRMADA = '{0}', NOMBRE = '{1}' WHERE ID = {2}".format(base64, nombre, id)
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
        cadena += "A.DRBIEN, A.DRABIEN, A.NOMBRE FROM datosdesplazamiento A INNER JOIN bienespatrimoniales B on B.ID = A.IDBIEN WHERE 1 = 1 "
        if not codigo in [None, ""]:
            codigo = codigo.strip().upper()
            cadena += " AND UPPER(B.ID) LIKE '%{0}%'".format(codigo)

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
                "DRABIEN": dato[11],
                "NOMBRE": dato[12]
            })
        cursor.close()
        return datos_dict
    except Exception as e:
        return []