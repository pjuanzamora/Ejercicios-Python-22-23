import flet as ft




def main(page: ft.Page):
    page.title="Tienda Juanfra"
    
      #Componente Texto
    rotulo_tienda = ft.Text(value="La tienda de Juanfra, todo al mejor precio", color="red", size=60)
    page.add(rotulo_tienda)
    text_selecion = ft.Text(value="Seleccione sus productos", size=40)
    page.add(text_selecion)

   

    textField_Nombre = ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    #page.add(textField_Nombre)

    
    dropDown_Menu = ft.Dropdown(width=300 ,options=[ft.dropdown.Option("Lechuga")])
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Nueva"))
    page.update()
    
    #Crear fila
    fila = ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)

    slider_edad = ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}")
    page.add(slider_edad)

    #page.update() Actualiza los datos 





ft.app(target=main)