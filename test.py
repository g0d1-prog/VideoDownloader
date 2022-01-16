# Teste para ver se highest_resolution está funcionando
from pytube import YouTube
from pytube.cli import on_progress

# link = input("\nInsira: ")

# yt = YouTube(link)

# ys = yt.streams.get_highest_resolution()
# ys.download()
# ("Video baixado!")

# Teste para pegar thumbnail

# def get_thumbnail(video):
#     thumbnail_url = video.thumbnail_url
#     return thumbnail_url

# thumb = get_thumbnail(yt)
# print(thumb)

# Teste para pegar imagem da pasta raiz

# from PyQt5.QtWidgets import *
# from PyQt5 import QtGui
# import sys


# class Window(QMainWindow): 
#     def __init__(self): 
#         super().__init__() 

#         self.setWindowTitle("Image") 
#         self.setGeometry(0, 0, 400, 300) 
#         self.label = QLabel(self) 
#         self.acceptDrops()
#         self.arrowIcon = QLabel(self)
#         self.arrowIcon.move(50, 400)
#         self.arrowIcon.setPixmap(QtGui.QPixmap('arrowIcon.png'))
#         self.show() 
        
# App = QApplication(sys.argv) 
# window = Window() 
# sys.exit(App.exec()) 

# Teste para fazer a função de progressão da barar

link = str(input("\nDigite o link abaixo: \n"))
yt = YouTube(link, on_progress_callback = on_progress)
video = yt.streams.get_highest_resolution()
video.download()
print("\nVideo baixado")
