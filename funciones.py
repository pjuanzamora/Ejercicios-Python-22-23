#Funciones definidas por el usuario

def imprimirHola(nombre:str, apellido:str):
    print("Hola", nombre, apellido)


def sumarDosNumeros(num1:int, num2:int):
    #print("La suma es", num1+num2)
    return num1+num2


suma = sumarDosNumeros(2,2)
print("La suma es:", suma)