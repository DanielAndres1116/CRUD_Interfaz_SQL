from tkinter import messagebox
import sqlite3

def crear(Nombre_Base_Datos, Nombre, Password, Apellido, Direccion, Comentario):

	miConexion=sqlite3.connect(Nombre_Base_Datos)

	miCursor=miConexion.cursor()

	datos=Nombre,Password,Apellido,Direccion,Comentario
	"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
		"','" + miPass.get() +
		"','" + miApellido.get() +
		"','" + miDireccion.get() +
		"','" + textoComentario.get("1.0", END) + "')")"""

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito")