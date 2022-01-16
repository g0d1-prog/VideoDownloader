# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\pedro\Desktop\Programas\Programas Python\Portfolio\VideoDownloader\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import urllib.request
import os
import time
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 900)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 900))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 900))
        MainWindow.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1020, 900))
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.titleFrame = QtWidgets.QFrame(self.centralwidget)
        self.titleFrame.setGeometry(QtCore.QRect(0, 0, 1020, 40))
        self.titleFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.titleFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.titleFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.titleLabel = QtWidgets.QLabel(self.titleFrame)
        self.titleLabel.setGeometry(QtCore.QRect(160, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.creditsLabel = QtWidgets.QLabel(self.titleFrame)
        self.creditsLabel.setGeometry(QtCore.QRect(880, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setObjectName("creditsLabel")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(0, 50, 1021, 851))
        self.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.baixarVideoDoYoutubeLabel = QtWidgets.QLabel(self.mainFrame)
        self.baixarVideoDoYoutubeLabel.setGeometry(QtCore.QRect(260, 57, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(24)
        self.baixarVideoDoYoutubeLabel.setFont(font)
        self.baixarVideoDoYoutubeLabel.setObjectName("baixarVideoDoYoutubeLabel")
        self.inputLinkColorFrame = QtWidgets.QFrame(self.mainFrame)
        self.inputLinkColorFrame.setGeometry(QtCore.QRect(70, 120, 781, 91))
        self.inputLinkColorFrame.setStyleSheet("QFrame{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(110, 221, 0);\n"
"}")
        self.inputLinkColorFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inputLinkColorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputLinkColorFrame.setObjectName("inputLinkColorFrame")
        self.inputLinkFrame = QtWidgets.QFrame(self.inputLinkColorFrame)
        self.inputLinkFrame.setGeometry(QtCore.QRect(10, 10, 761, 71))
        self.inputLinkFrame.setStyleSheet("QFrame{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.inputLinkFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inputLinkFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputLinkFrame.setObjectName("inputLinkFrame")
        self.inputLineEdit = QtWidgets.QLineEdit(self.inputLinkFrame)
        self.inputLineEdit.setGeometry(QtCore.QRect(10, 10, 741, 51))
        self.inputLineEdit.setStyleSheet("QLineEdit {\n"
"    font: 14pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background-color: rgb(0, 0, 0)\n"
"}\n"
"")
        self.inputLineEdit.setObjectName("inputLineEdit")
        self.downloadButton = QtWidgets.QPushButton(self.mainFrame)
        self.downloadButton.setGeometry(QtCore.QRect(860, 120, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(37, 236, 2);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 16pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 16pt \"Arial\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(37, 236, 2);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 16pt \"Arial\";\n"
"}")
        self.downloadButton.setObjectName("downloadButton")
        self.arrowIconLabel = QtWidgets.QLabel(self.mainFrame)
        self.arrowIconLabel.setGeometry(QtCore.QRect(630, 50, 61, 61))
        self.arrowIconLabel.setStyleSheet("QFrame (\n"
"    border: 10px solid\n"
")")
        self.arrowIconLabel.setText("")
        self.arrowIconLabel.setPixmap(QtGui.QPixmap("arrowIcon.png"))
        self.arrowIconLabel.setObjectName("arrowIconLabel")
        self.errorFrame = QtWidgets.QFrame(self.mainFrame)
        self.errorFrame.setGeometry(QtCore.QRect(40, 0, 931, 51))
        self.errorFrame.setStyleSheet("QFrame{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.errorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.errorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.errorFrame.setObjectName("errorFrame")
        self.errorLabel = QtWidgets.QLabel(self.errorFrame)
        self.errorLabel.setGeometry(QtCore.QRect(7, 9, 861, 31))
        self.errorLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.closeErrorPopUpPushButton = QtWidgets.QPushButton(self.errorFrame)
        self.closeErrorPopUpPushButton.setGeometry(QtCore.QRect(880, 10, 41, 31))
        self.closeErrorPopUpPushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 0, 0);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(118, 0, 0);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 87 11pt \"Arial\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 0, 0);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 10pt \"Arial\";\n"
"}")
        self.closeErrorPopUpPushButton.setObjectName("closeErrorPopUpPushButton")
        self.confirmationFrame = QtWidgets.QFrame(self.mainFrame)
        self.confirmationFrame.setGeometry(QtCore.QRect(10, 210, 1001, 631))
        self.confirmationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.confirmationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.confirmationFrame.setObjectName("confirmationFrame")
        self.downloadingFrame = QtWidgets.QFrame(self.confirmationFrame)
        self.downloadingFrame.setGeometry(QtCore.QRect(370, 530, 261, 71))
        self.downloadingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.downloadingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.downloadingFrame.setObjectName("downloadingFrame")
        self.baixandoLabel = QtWidgets.QLabel(self.downloadingFrame)
        self.baixandoLabel.setGeometry(QtCore.QRect(80, 10, 111, 21))
        self.baixandoLabel.setStyleSheet("font: 14pt \"Arial\";\n"
"color: rgb(74, 223, 0);")
        self.baixandoLabel.setObjectName("baixandoLabel")
        self.downloadingProgressBar = QtWidgets.QProgressBar(self.downloadingFrame)
        self.downloadingProgressBar.setGeometry(QtCore.QRect(7, 42, 251, 21))
        self.downloadingProgressBar.setProperty("value", 0)
        self.downloadingProgressBar.setObjectName("downloadingProgressBar")
        self.videoTitleLabel_2 = QtWidgets.QLabel(self.confirmationFrame)
        self.videoTitleLabel_2.setGeometry(QtCore.QRect(30, 40, 951, 31))
        self.videoTitleLabel_2.setStyleSheet("font: 14pt \"Arial\";")
        self.videoTitleLabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.videoTitleLabel_2.setScaledContents(False)
        self.videoTitleLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.videoTitleLabel_2.setIndent(-1)
        self.videoTitleLabel_2.setObjectName("videoTitleLabel_2")
        self.thumbnailFrame = QtWidgets.QFrame(self.confirmationFrame)
        self.thumbnailFrame.setGeometry(QtCore.QRect(20, 80, 971, 411))
        self.thumbnailFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnailFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnailFrame.setObjectName("thumbnailFrame")
        self.thumbnailLabel = QtWidgets.QLabel(self.thumbnailFrame)
        self.thumbnailLabel.setGeometry(QtCore.QRect(150, 60, 671, 311))
        self.thumbnailLabel.setObjectName("thumbnailLabel")
        self.videoBaixadoEmLabel = QtWidgets.QLabel(self.confirmationFrame)
        self.videoBaixadoEmLabel.setGeometry(QtCore.QRect(390, 600, 161, 31))
        self.videoBaixadoEmLabel.setStyleSheet("font: 14pt \"Arial\";")
        self.videoBaixadoEmLabel.setObjectName("videoBaixadoEmLabel")
        self.pathLabel = QtWidgets.QLabel(self.confirmationFrame)
        self.pathLabel.setGeometry(QtCore.QRect(550, 600, 51, 31))
        self.pathLabel.setStyleSheet("font: 14pt \"Arial\";")
        self.pathLabel.setObjectName("pathLabel")
        self.confirmPushButton = QtWidgets.QPushButton(self.confirmationFrame)
        self.confirmPushButton.setGeometry(QtCore.QRect(290, 490, 411, 31))
        self.confirmPushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(37, 236, 2);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 14pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 0);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 14pt \"Arial\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(37, 236, 2);\n"
"    color: rgb(245, 245, 245);\n"
"    border-radius: 5px;\n"
"    font: 75 14pt \"Arial\";\n"
"}\n"
"")
        self.confirmPushButton.setObjectName("confirmPushButton")
        self.inputLinkColorFrame.raise_()
        self.baixarVideoDoYoutubeLabel.raise_()
        self.downloadButton.raise_()
        self.arrowIconLabel.raise_()
        self.errorFrame.raise_()
        self.errorFrame.hide()
        self.confirmationFrame.raise_()
        self.confirmationFrame.hide()
        self.mainFrame.raise_()
        self.titleFrame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        
        #
        #
        # EVENTS
        #
        #
        
        # Link do vídeo
        def catch_video(link):               
                video = YouTube(link)
                self.errorFrame.hide()
                return video
                        
        def confirmation_video():
                try:
                        video = catch_video(self.inputLineEdit.text())
                        self.errorFrame.hide()
                        video_thumbnail = video.thumbnail_url
                        video_title = video.title
                        urllib.request.urlretrieve(video_thumbnail, "thumbnail.png")
                        self.videoTitleLabel_2.setText(video_title)
                        self.thumbnailLabel.setPixmap(QtGui.QPixmap("thumbnail.png"))
                        self.downloadingFrame.hide()
                        self.videoBaixadoEmLabel.hide()
                        self.pathLabel.hide()
                        self.confirmationFrame.show() 
                        self.confirmPushButton.clicked.connect(lambda: os.remove("thumbnail.png"))
                        return video
                except:
                        error_video_catch_thumbnail = "Erro: Link incorreto"
                        self.errorFrame.show()
                        self.errorLabel.setText(error_video_catch_thumbnail)
        
        def check_if_video_is_downloaded(video_highest_resolution, path):
                video_highest_resolution.download(path)
                video_downloaded = True
        
        def download_video(bytes_remaining):
                video = confirmation_video() # Armazenando o retorno da função na variável
                video_highest_resolution = video.streams.get_highest_resolution()
                path = "Downloads"
                self.downloadingFrame.show()
                progress = 0
                video_downloaded = False 
                for progress in range(101):
                        self.downloadingProgressBar.setValue(progress)
                        progress =+ 1
                        check_if_video_is_downloaded(video_highest_resolution, path)
                        if video_downloaded == True:
                                break
                        else:
                                continue
                self.pathLabel.setText(path)       
        
        # Botão de pegar o video
        self.downloadButton.clicked.connect(lambda: confirmation_video())
        
        # Botão para realizar o download
        self.confirmPushButton.clicked.connect(lambda: download_video(100))
        
        # Função para fechar popup
        self.closeErrorPopUpPushButton.clicked.connect(lambda: self.errorFrame.hide())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "VideoDownloader"))
        self.creditsLabel.setText(_translate("MainWindow", "from Pedro Barros"))
        self.baixarVideoDoYoutubeLabel.setText(_translate("MainWindow", "Baixar vídeo do Youtube"))
        self.inputLineEdit.setPlaceholderText(_translate("MainWindow", "Digite o link do vídeo"))
        self.downloadButton.setText(_translate("MainWindow", "Baixar"))
        self.errorLabel.setText(_translate("MainWindow", "Error Fatal!"))
        self.closeErrorPopUpPushButton.setText(_translate("MainWindow", "X"))
        self.baixandoLabel.setText(_translate("MainWindow", "Baixando..."))
        self.videoTitleLabel_2.setText(_translate("MainWindow", "Título do vídeo"))
        self.thumbnailLabel.setText(_translate("MainWindow", "img"))
        self.videoBaixadoEmLabel.setText(_translate("MainWindow", "Video baixado em:"))
        self.pathLabel.setText(_translate("MainWindow", "path"))
        self.confirmPushButton.setText(_translate("MainWindow", "Confirmar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Travando a tela em um certo valor
    MainWindow.setFixedSize(1020,900)
    sys.exit(app.exec_())