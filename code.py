import PySimpleGUI as sg

sg.theme('DarkBlack')

info_tab = [
    [sg.Text('Title:'),sg.Text('',key = '-TITLE-')],
    [sg.Text('Length:'),sg.Text('',key = '-LENGTH-')],
    [sg.Text('Views:'),sg.Text('',key = '-VIEWS-')],
    [sg.Text('Author:'),sg.Text('',key = '-AUTHOR-')],
    [
        sg.Text('Description:'),
        sg.Multiline('', key = '-DESCRIPTION-', size = (40,20), no_scrollbar = True, disabled = True)
    ]
]
download_tab = [[]]

layout = [[sg.TabGroup([[
    sg.Tab('INFO',info_tab),sg.Tab('DOWNLOAD',download_tab)]])]]

window = sg.Window('Downtube', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()