#Tipos de datos y variables

#Numéricos
#enteros -- int
#real -- float
#Cadenas de caracteres -- str
#Lógico -- bool
'''
nombre="Juan Francisco"
edad = 25
mayorOmenorEdad=False

#Entrada y salida de datos
#Salida con print()

print("Buenos dias", nombre, "tu edad es", edad)

#Entrada de datos -- input()
nombre = input("Dime tu nombre:\n") #\n Permite hacer un salto de linea
edad = input("Dime tu edad: ")



print("Buenos dias", nombre, "tu edad es", edad)
'''
#Bucle while
i=0
bandera = True
num=0
num = int(input("Dime un número: "))

while (i <= 10):
    print(num, " * ", i, " = ", num*i)
    i = i + 1