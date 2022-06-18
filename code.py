import PySimpleGUI as sg

info_tab = [[]]
download_tab = [[]]

layout = [[sg.TabGroup([[
    sg.Tab('info',info_tab),sg.Tab('download',download_tab)]])]]

window = sg.Window('Downtube', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()