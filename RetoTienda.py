import flet as ft




def main(page: ft.Page):
    page.title="Tienda Juanfra"

    def añadirProducto(e):
      listView_Compra.controls.append(ft.Text(dropDown_Tipo_Comida.value))
      page.update()
    
    #Componente Texto
    rotulo_tienda = ft.Text(value="La tienda de Juanfra, todo al mejor precio", color="red", size=60)
    page.add(rotulo_tienda)
    text_selecion = ft.Text(value="Seleccione sus productos", size=40)
    page.add(text_selecion)

   

    textField_Nombre = ft.TextField(label="Nombre Cliente", hint_text="Nombre Cliente", width=300)    
    dropDown_Tipo_Comida = ft.Dropdown(width=300 ,options=[ft.dropdown.Option("Bebidas"), ft.dropdown.Option("Carnes"), ft.dropdown.Option("Pescados")])
    dropDown_Seleccion_Comida = ft.Dropdown(width=300 ,options=[ft.dropdown.Option("Elija un producto")])
    boton_añadir = ft.ElevatedButton(text="Añadir producto", width=200, icon=ft.icons.ADD, on_click=añadirProducto)
    
    #Crear fila
    fila = ft.Row(controls=[textField_Nombre,dropDown_Tipo_Comida, dropDown_Seleccion_Comida, boton_añadir])
    page.add(fila)

    

    text_lista_Compra = ft.Text(value="Lista compra:", size=40)
    page.add(text_lista_Compra)

    #Lista de la compra
    listView_Compra = ft.ListView(expand=True, spacing=10)
    page.add(listView_Compra)



ft.app(target=main)