#Funciones definidas por el usuario
from pytube import YouTube


def imprimirHola(nombre:str, apellido:str):
    print("Hola", nombre, apellido)


def sumarDosNumeros(num1:int, num2:int):
    #print("La suma es", num1+num2)
    return num1+num2


def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()


#Calcular Area y Perimetro

def calcularArea(lado1:int,lado2:int):
    area = lado1*lado2
    return area

def calcularPerimetro(lado1:int,lado2:int):
    perimetro = (2*lado1 + 2*lado2)
    return perimetro

#Devuelvo una lista con [area, perimetro]
def calcularAreaYperimetro(lado1:int,lado2:int):
    vDatos=[]
    area = calcularArea(lado1,lado2)
    perimetro= calcularPerimetro(lado1,lado2)
    vDatos.append(area)
    vDatos.append(perimetro)
    return vDatos

#Principal
lado1 = int(input("Dime el valor del lado1"))
lado2 = int(input("Dime el valor del lado2"))

vNum = calcularAreaYperimetro(lado1,lado2)
print("El area es:", vNum[0])
print("El perimetro es:", vNum[1])