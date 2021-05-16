from tkinter import messagebox
import sqlite3

def actualizar(Nombre_Base_Datos, numID, Nombre, Password, Apellido, Direccion, Comentario):

	miConexion=sqlite3.connect(Nombre_Base_Datos)

	miCursor=miConexion.cursor()

	datos=Nombre,Password,Apellido,Direccion,Comentario

	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?" +
		"WHERE ID=" + numID, (datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con éxito")