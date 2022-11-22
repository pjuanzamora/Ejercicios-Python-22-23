from tkinter import * 
from tkinter import ttk
from pytube import YouTube


def descargarCancion():
    url = datos_Entrada.get()
    youtube = YouTube(url)
    cancion = youtube.streams.get_audio_only()
    cancion.download()


ventana = Tk()
ventana.title("Descargar musica youtube")
ventana.geometry("500x100")
ventana.resizable(False,False)
ventana.config(background="snow3")

datos_Entrada = ttk.Entry(ventana)
datos_Entrada.place(x=180, y=25)

boton_Descargar = ttk.Button(ventana,text="Descargar", command=descargarCancion)
boton_Descargar.place(x=190, y=60)

label_Titulo = ttk.Label(ventana, text="Introduce la url del video:")
label_Titulo.config(background="aquamarine")
label_Titulo.place(x=5, y=27)


ventana.mainloop()