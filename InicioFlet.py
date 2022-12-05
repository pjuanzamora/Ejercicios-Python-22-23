import flet as ft




def main(page: ft.Page):
    page.title="Tkinder buagggg - Flet :-)"
    
    
    def cambiarColor(e):
        t.value= textField_Nombre.value
        page.update()



    #Componente Texto
    t = ft.Text(value="Introducción a Flet", color="red", size=20)
    page.add(t) # add hace dos cosas 1-Añadir 2-Actualizar

    #Componente Boton
    bt = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiarColor)
    page.add(bt)

    textField_Nombre = ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    page.add(textField_Nombre)

    
    dropDown_Menu = ft.Dropdown(width=300 ,options=[ft.dropdown.Option("Lechuga")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Nueva"))
    page.update()
    

    #page.update() Actualiza los datos 





ft.app(target=main)