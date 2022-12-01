from tkinter import * 
from tkinter import ttk
from tkinter import messagebox


usuario = ""
contraseña = ""
contraseña_Repetida = ""
vUsuarios = []

def guardarDatos():
    usuario = entry_nombre_usuario.get()
    contraseña = entry_pass_usuario.get()
    contraseña_Repetida = entry_repite_pass_usuario.get()
    if (contraseña == contraseña_Repetida):
        vUsuarios.append(usuario)
        vUsuarios.append(contraseña)
        entry_nombre_usuario.delete(0, len(usuario))
        entry_pass_usuario.delete(0, len(contraseña))
        entry_repite_pass_usuario.delete(0, len(contraseña_Repetida))
        messagebox.showinfo("Usuario Guardado", f"Usuario {usuario} guardado correctamente")
    

#Configuración ventana
ventana = Tk()
ventana.title("Datos usuario")
ventana.geometry("600x500")


#Título principal
label_Titulo = ttk.Label(ventana,text="Datos usuario")


#Componentes para pedir los datos
#Componente Label
label_nombre_usuario = ttk.Label(ventana, text="Nombre usuario:")
#Compoenente Entry - Caja de texto
entry_nombre_usuario = ttk.Entry(ventana)

label_pass_usuario = ttk.Label(ventana, text="Contraseña:")
entry_pass_usuario = ttk.Entry(ventana, show="*")

label_repite_pass_usuario = ttk.Label(ventana, text="Confirma contraseña:")
entry_repite_pass_usuario = ttk.Entry(ventana, show="*")

#Componente Botón para ejecutar una acción con command
boton_guardar = ttk.Button(ventana, text="Guardar", command=guardarDatos)
boton_salir = ttk.Button(ventana,text="Salir", command=ventana.destroy)

#Componente Combobox - Seleccionar una opción
combo_sexo = ttk.Combobox(ventana, values=["Hombre", "Mujer"])
combo_sexo.set("Seleccione una opción")
combo_sexo.grid(row=4, column=1, pady=30)


#Pintar en pantalla los componentes
label_Titulo.grid(row=0, column=0,pady=10)
label_nombre_usuario.grid(row=1, column=0,pady=10)
entry_nombre_usuario.grid(row=1, column=1,pady=10)

label_pass_usuario.grid(row=2, column=0,pady=10)
entry_pass_usuario.grid(row=2, column=1,pady=10)

label_repite_pass_usuario.grid(row=3, column=0,pady=10, padx=15)
entry_repite_pass_usuario.grid(row=3, column=1,pady=10)

boton_guardar.grid(row=5, column=0,pady=30)
boton_salir.grid(row=5, column=1,pady=30)


ventana.mainloop()