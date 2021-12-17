""" 
TUTORIAL EM PORTUGUÊS
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

    list_musics = [
        # This is a list and if you want to add 50 links, it's okay.
        'YOUR_YOUTUBE_LINK_HERE_1',
        'YOUR_YOUTUBE_LINK_HERE_2',
        'YOUR_YOUTUBE_LINK_HERE_3',
    ]

    for music in list_musics:
        try:

            VIDEO_URL = music

            yt = YouTube(VIDEO_URL)

            print('\n\nFinding the best resolution...')
            video_mp4 = yt.streams.get_highest_resolution()

            print('Downloading Youtube Video...')
            video_mp4.download()

            for directory, subdirectory, archives in os.walk('./'):
                for archive in archives:
                    if '.mp4' in archive:
                        mp4 = os.path.join(directory, archive)
                        mp3 = mp4.replace('.mp4', '.mp3')
                        print('Converting MP4 to MP3...')
                        video = VideoFileClip(mp4)
                        video.audio.write_audiofile(mp3)
                        os.remove(mp4)
                        print('Download success!')
        except:
            print(
                'Error: The links must be Youtube links, add a Youtube link to download.')


mp3_downloader()
