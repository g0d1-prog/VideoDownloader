# Importações necessárias
from pytube import YouTube
import urllib.request
import os
import shutil

# Definições de variáveis globais
link = ""
   
# Definições das funções
def catch_video(link):
    try:
        video = YouTube(link)
        return video
    except:
        link_error = "\nLink incorreto!"
        print(link_error)

def confirmation_video():
    try: 
        video = catch_video(link)
        video_thumbnail = video.thumbnail_url
        video_title = video.title
        urllib.request.urlretrieve(video_thumbnail, "thumbnail.png")
        os.remove("C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/Portfolio/VideoDownloader/thumbimages/thumbnail.png")
        thumbnail_old_adress = "C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/thumbnail.png"
        thumbnail_new_adress = "C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/Portfolio/VideoDownloader/thumbimages"
        shutil.move(thumbnail_old_adress, thumbnail_new_adress)
        print(video_title)
        confirmation_user = str(input("\nEste é o vídeo que gostaria de baixar? \n")).title()
        if confirmation_user == "Sim":
            os.remove("C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/Portfolio/VideoDownloader/thumbimages/thumbnail.png")
            return video
        else:
            not_confirmation_error = "\nVídeo não confirmado"
            print(not_confirmation_error)
    except FileNotFoundError:
        thumbnail_old_adress = "C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/thumbnail.png"
        thumbnail_new_adress = "C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/Portfolio/VideoDownloader/thumbimages"
        shutil.move(thumbnail_old_adress, thumbnail_new_adress)
        print(video_title)
        confirmation_user = str(input("\nEste é o vídeo que gostaria de baixar? \n")).title()
        if confirmation_user == "Sim":
            os.remove("C:/Users/user/OneDrive/Área de Trabalho/Trabalho/Programas/Programas Python/Portfolio/VideoDownloader/thumbimages/thumbnail.png")
            return video
        else:
            not_confirmation_error = "\nVídeo não confirmado"
            print(not_confirmation_error)
    except:
        error_video_catch_thumbnail = "\nErro ao pegar a thumbnail do vídeo"
        print(error_video_catch_thumbnail)           
    
def download_video():
    try:
        video = confirmation_video() # Armazenando o retorno da função na variável
        video_highest_resolution = video.streams.get_highest_resolution()
        path = "C:/Users/user/Downloads"
        video_downloading = "\nBaixando..."
        print(video_downloading)
        video_highest_resolution.download(path)
        video_downloaded = "\nVideo baixado"
        print(video_downloaded + " em " + path)
    except:
        error_download_video = "\nErro ao baixar o vídeo!"
        print(error_download_video)