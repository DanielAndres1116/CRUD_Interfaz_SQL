from tkinter import *
from tkinter import messagebox
from modulo_Conexion import *
from modulo_Crear import *
from modulo_Leer import *
from modulo_Actualizar import *
from modulo_Borrar import*
#import sqlite3

def salirAplicacion():

	valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():

	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	textoComentario.delete(1.0, END)

def leer_local():

	los_datos_son=leer("Usuarios", miId.get())

	for dato_leido in los_datos_son:
		miId.set(dato_leido[0])
		miNombre.set(dato_leido[1])
		miPass.set(dato_leido[2])
		miApellido.set(dato_leido[3])
		miDireccion.set(dato_leido[4])
		textoComentario.insert(1.0, dato_leido[5])

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=lambda:conexionBBDD("Usuarios"))
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=lambda:crear("Usuarios",miNombre.get(),miApellido.get(),miDireccion.get(),miPass.get(), textoComentario.get("1.0", END)))
crudMenu.add_command(label="Leer", command=leer_local)
crudMenu.add_command(label="Actualizar", command=lambda:actualizar("Usuarios",miId.get(),miNombre.get(),miApellido.get(),miDireccion.get(),miPass.get(), textoComentario.get("1.0", END)))
crudMenu.add_command(label="Borrar", command=lambda:eliminar("Usuarios",miId.get()))

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

#-----------------------Aqui se crean los Campos------------------------

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#-------------------Aqui se crean los label---------------------------

idLabel=Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


root.mainloop()
