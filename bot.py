""" 
- Instalar Bibliotecas para rodar:
   >pip3 install pytube
   >pip3 install moviepy

- Agora você precisa adicionar a lista de links no Array lista_musicas, ali tem um exemplo.
- Depois de instalar as bibliotecas, entre na pasta e rode o comando no cmd/terminal> python3 bot.py 
"""

from pytube import YouTube
import os
from moviepy.editor import *


def mp3_downloader():

    lista_musicas = [
        'SEU_LINK_1_DO_YOUTUBE_AQUI',
        'SEU_LINK_2_DO_YOUTUBE_AQUI',
        'SEU_LINK_3_DO_YOUTUBE_AQUI',
    ]

    for musica in lista_musicas:
        try:

            VIDEO_URL = musica

            yt = YouTube(VIDEO_URL)

            print('\n\nEncontrando melhor resolução...')
            video_mp4 = yt.streams.get_highest_resolution()

            print('Baixando vídeo do Youtube...')
            video_mp4.download()

            for diretorio, subpastas, arquivos in os.walk('./'):
                for arquivo in arquivos:
                    if '.mp4' in arquivo:
                        mp4 = os.path.join(diretorio, arquivo)
                        mp3 = mp4.replace('.mp4', '.mp3')
                        print('Convertendo MP4 para MP3...')
                        video = VideoFileClip(mp4)
                        video.audio.write_audiofile(mp3)
                        os.remove(mp4)
                        print('Música baixada.')
        except:
            print('Erro: Seu link precisa ser do Youtube')


mp3_downloader()
