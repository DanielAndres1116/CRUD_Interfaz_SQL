from tkinter import messagebox
import sqlite3

def eliminar(Nombre_Base_Datos, numID):

	miConexion=sqlite3.connect(Nombre_Base_Datos)

	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + numID)

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro borrado con éxito")