import flet as ft




def main(page: ft.Page):
    page.title="Tkinder buagggg - Flet :-)"
    
    def cambiarColor(e):
        for i in range(10):
            text = ft.Text(value=f"Texto numero {i}", size=30)
            page.add(text)  



    #Componente Texto
    t = ft.Text(value="Introducción a Flet", color="red", size=20)
    page.add(t) # add hace dos cosas 1-Añadir 2-Actualizar

    #Componente Boton
    bt = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiarColor)
    page.add(bt)

    #page.update() Actualiza los datos 





ft.app(target=main)