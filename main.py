from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg

#Gets video, sets it to highest quality and displays messages to user
def video_download():
    video = YouTube(values[0])
    sg.popup_timed('Downloading video, please wait...')
    video.streams.get_highest_resolution().download(output_path = values[1])
    sg.popup_ok('Download Finished! Enjoy :)')

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Input the link: '), sg.InputText()],
    [sg.Text('Choose Folder: '), sg.InputText(), sg.FolderBrowse()],
    [sg.Button('Download')]
]

#Window
window = sg.Window('YouTube Downloader', layout)

#Events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #
        break
    if event == 'Download':
        video_download()

window.close()