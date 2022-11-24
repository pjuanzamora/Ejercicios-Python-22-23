from tkinter import * 
from tkinter import ttk

#Configuración ventana
ventana = Tk()
ventana.geometry("600x500")


#Título principal
label_Titulo = ttk.Label(ventana,text="Datos usuario")


#Componentes para pedir los datos

label_nombre_usuario = ttk.Label(ventana, text="Nombre usuario:")
entry_nombre_usuario = ttk.Entry(ventana)

label_pass_usuario = ttk.Label(ventana, text="Contraseña:")
entry_pass_usuario = ttk.Entry(ventana)

label_repite_pass_usuario = ttk.Label(ventana, text="Confirma contraseña:")
entry_repite_pass_usuario = ttk.Entry(ventana)

boton_guardar = ttk.Button(ventana, text="Guardar")
boton_salir = ttk.Button(ventana,text="Salir")


#Pintar en pantalla los componentes
label_Titulo.grid(row=0, column=0)
label_nombre_usuario.grid(row=1, column=0)
entry_nombre_usuario.grid(row=1, column=1)

label_pass_usuario.grid(row=2, column=0)
entry_pass_usuario.grid(row=2, column=1)

label_repite_pass_usuario.grid(row=3, column=0)
entry_repite_pass_usuario.grid(row=3, column=1)

boton_guardar.grid(row=4, column=0)
boton_salir.grid(row=4, column=1)


ventana.mainloop()