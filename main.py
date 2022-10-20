from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg

#Gets video, sets it to highest quality and displays messages to user
def video_download():
    video = YouTube(values[0])
    sg.popup_timed('Downloading video, please wait...')
    # video.streams.get_highest_resolution().download(output_path = values[1])
    video = video.streams.filter(progressive=True, file_extension='mp4')
    video.get_highest_resolution().download(output_path=values[1])
    sg.popup_ok('Download finished! Enjoy :)')

#Gets audio file in MP4 format
def audio_download():
    audio = YouTube(values[0])
    sg.popup_timed('Downloading audio file, please wait...')
    audio = audio.streams.get_audio_only()
    audio.download(output_path=values[1])
    sg.popup_ok('Download finished! Enjoy :)')

#Layout
sg.theme('DarkRed1')
layout = [
    [sg.Text('Input the link: ', size=(11, 1)), sg.InputText()],
    [sg.Text('Choose Folder: ', size=(11, 1)), sg.InputText(), sg.FolderBrowse()],
    [sg.Button('Download Video'), sg.Button('Download Audio Only')]
]

#Window
window = sg.Window('YouTube Downloader', layout)

#Events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    if event == 'Download Video':
        video_download()
    elif event == 'Download Audio Only':
        audio_download()

window.close()