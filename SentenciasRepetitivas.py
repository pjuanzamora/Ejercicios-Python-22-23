import random
import PySimpleGUI as sg

layout = [[sg.Text('Dime un número')],
          [sg.Input()],
          [sg.OK()] ]

event, values = sg.Window('Enter a number example', layout).Read()
sg.Popup(event, values[0])

numero = random.randint(1,100)
print (numero)