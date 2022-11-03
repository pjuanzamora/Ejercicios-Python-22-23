

#Función que devuelve una lista de números introducidos

def pideNumeros():
    vNum = []
    num = 1
    while (num!=0):
        try:
            contador = len(vNum)
            num = int(input(f"Dime el número {contador+1}: "))
            if (num!=0):
                vNum.append(num)
        except:
            print("Tienes que introducir números")

    return vNum

def realizarCalculos(vDatos, limiteInferior, limiteSuperior):
    suma = 0
    fuera = 0
    igualesAlimites=0
    vLimites = list(range(limiteInferior+1,limiteSuperior))
    for i in vDatos:
        if (i in vLimites):
            suma += i
        else:
            fuera += 1
        if (i == limiteInferior or i == limiteSuperior):
            igualesAlimites += 1

    print("La suma total dentro de los límites es:", suma)
    print(f"Has introducido {fuera} números fuera de los límites")
    print(f"Has introducido {igualesAlimites} números iguales a los límites")


#Pedir Limites Inferior y Superior

limiteInferior=1
limiteSuperior=0

while limiteInferior > limiteSuperior:
    try:
        limiteInferior = int(input("Dime el límite inferior: "))
        limiteSuperior = int(input("Dime el límite superior: "))
        if limiteInferior > limiteSuperior:
            print("Es obligatorio que el límite inferior sea menor que el superior")
            print("********\n")
    except:
        print("Tienes que introducir números")


#Pido los números

vNum = pideNumeros()

#Realizar cálculos

realizarCalculos(vNum,limiteInferior,limiteSuperior)
