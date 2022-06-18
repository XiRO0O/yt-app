import PySimpleGUI as sg
from pytube import YouTube

sg.theme('DarkBlack')
start_layout = [[sg.Input(key = '-INPUT-'),sg.Button('Sumbit')]]
info_tab = [
    [sg.Text('Title:'),sg.Text('',key = '-TITLE-')],
    [sg.Text('Length:'),sg.Text('',key = '-LENGTH-')],
    [sg.Text('Views:'),sg.Text('',key = '-VIEWS-')],
    [sg.Text('Author:'),sg.Text('',key = '-AUTHOR-')],
    [
        sg.Text('Description:'),
        sg.Multiline('', key = '-DESCRIPTION-', size = (40,20), no_scrollbar = True, disabled = True)
    ]]
download_tab = [
    [sg.Frame('Best Quality',[[sg.Button('Download', key = '-BEST-'),sg.Text('', key = '-BESTRES-'),sg.Text('', key = '-BESTSIZE-')]])],
    [sg.Frame('Worst Quality',[[sg.Button('Download', key = '-WORST-'),sg.Text('', key = '-WORSTRES-'),sg.Text('', key = '-WORSTSIZE-')]])],
    [sg.Frame('Audio',[[sg.Button('Download', key = '-AUDIO-'),sg.Text('', key = '-AUDIOSIZE-')]])],
    [sg.VPush()],
    [sg.Progress(100, size = (20,20), expand_x = True, key = '-PROGRESSBAR-')]]
layout = [[sg.TabGroup([[
    sg.Tab('INFO',info_tab),sg.Tab('DOWNLOAD',download_tab)]])]]

window = sg.Window('Downtube', start_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Sumbit':
        video_object = YouTube(values['-INPUT-'])
        window.close()
        window = sg.Window('Downtube', layout, finalize = True)
        window['-TITLE-'].update(video_object.title)
        window['-LENGTH-'].update(f'{round(video_object.length / 60,2)} minutes')
        window['-VIEWS-'].update(video_object.views)
        window['-AUTHOR-'].update(video_object.author)
        window['-DESCRIPTION-'].update(video_object.description)

    window['-BESTSIZE-'].update(f'{round(video_object.streams.get_highest_resolution().filesize / 1048576,1)} MB')
    window['-BESTRES-'].update(video_object.streams.get_highest_resolution().resolution)

    window['-WORSTSIZE-'].update(f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576,1)} MB')
    window['-WORSTRES-'].update(video_object.streams.get_lowest_resolution().resolution)

    window['-AUDIOSIZE-'].update(f'{round(video_object.streams.get_audio_only().filesize / 1048576,1)} MB')

window.close()