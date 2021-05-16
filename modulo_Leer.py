import sqlite3

def leer(Nombre_Base_Datos, NumId):

	miConexion=sqlite3.connect(Nombre_Base_Datos)

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + NumId)

	elUsuario=miCursor.fetchall()

	return elUsuario

	miConexion.commit()