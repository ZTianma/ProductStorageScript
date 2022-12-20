import json
import PySimpleGUI as sg
data = [{}]
layout = [[sg.Combo(values=data,  key='fac', size=(20,1))],
          [sg.Text('Number:   ', size=(20, 1)), sg.InputText(key='num')],
          [sg.Button('Save'), sg.Button('close'),sg.Button('Delete')]
          ]


window = sg.Window('Test', layout, margins=(100, 100))
window.read()



while True:
    event, values = window.read()
    if event == 'close' or event == sg.WINDOW_CLOSED:
        break
    if event == 'Save':
        data[0][values['fac']] = values['num']
        print(data)




    if event == 'Delete':
        break




