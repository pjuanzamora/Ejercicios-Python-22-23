from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

    

#Configuración ventana
ventana = Tk()
ventana.title("Datos usuario")
ventana.geometry("600x500")


#Título principal
label_Titulo = ttk.Label(ventana,text="Venta de productos")


#Componentes para pedir los datos

#Componente Combobox - Seleccionar una opción
combo_tipo_alimento = ttk.Combobox(ventana, values=["Carnes", "Pescados"])
combo_tipo_alimento.set("Seleccione una opción:")

combo_alimentos = ttk.Combobox(ventana)
combo_alimentos.set("Alimentos disponibles:")


#Componente Botón para ejecutar una acción con command
boton_guardar = ttk.Button(ventana, text="Guardar")
boton_salir = ttk.Button(ventana,text="Salir", command=ventana.destroy)

#Pintar en pantalla los componentes
combo_tipo_alimento.grid(row=1, column=1, padx=30, pady=30)
combo_alimentos.grid(row=1, column=2, padx=30, pady=30)

boton_guardar.grid(row=3, column=1, padx=30, pady=50)
boton_salir.grid(row=3, column=2, padx=30, pady=50)


ventana.mainloop()