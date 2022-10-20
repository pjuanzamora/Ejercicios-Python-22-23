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


descargaCancion("https://www.youtube.com/watch?v=phgH6Pobvw8")
