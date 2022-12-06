# pip install pytube
# pip install moviepy

from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Link do vídeo e o local para salvar o MP3
link = input("Link do vídeo: ")
path = input("Diretório para baixar o arquivo: ")
yt = YouTube(link)

# Iniciar o Download
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download concluído!")

# Convertendo de MP4 para MP3
print("Convertendo arquivo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Conversão concluída!")
