'''
Opción 1: 
Lista para nombres
Lista para telefonos

Opción 2:
Lista para nombres y telefonos
Ejemplo [Juan - Teléfono, Pepe - Teléfono]
'''

#Opción 1:
vNombres = []
vTelefonos = []

#Creamos el menu de la agenda
'''
1- Insertar contacto
2- Borrar contacto
3- Buscar contacto
4- Ver todos los contactos
5- Salir
'''
opc = 0
while (opc != 5):
    print("******* Menú Agenda *******")
    print("1- Insertar contacto")
    print("2- Borrar contacto")
    print("3- Buscar contacto")
    print("4- Ver todos los contactos")
    print("5- Salir")
    print("***************************")
    try:
        opc = int(input("Seleccione una opción: "))
    except:
        print("Las opciones son de la 1 al 5")

# El telefono de juan es 1