# -*- coding: utf-8 -*-

from venv import main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from backend import main

class Ui_VideoDownloader(object):
    def setupUi(self, VideoDownloader):
        VideoDownloader.setObjectName("VideoDownloader")
        VideoDownloader.resize(632, 510)
        self.centralwidget = QtWidgets.QWidget(VideoDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setMinimumSize(QtCore.QSize(253, 0))
        self.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Navbar = QtWidgets.QFrame(self.mainFrame)
        self.Navbar.setMinimumSize(QtCore.QSize(0, 0))
        self.Navbar.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navbar.setObjectName("Navbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Navbar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Logo = QtWidgets.QLabel(self.Navbar)
        self.Logo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Logo.setObjectName("Logo")
        self.horizontalLayout.addWidget(self.Logo)
        self.Author = QtWidgets.QLabel(self.Navbar)
        self.Author.setMinimumSize(QtCore.QSize(0, 0))
        self.Author.setStyleSheet("font: 63 16pt \"Yu Gothic UI Semibold\";\n"
"background-color: #5cc304;")
        self.Author.setAlignment(QtCore.Qt.AlignCenter)
        self.Author.setWordWrap(True)
        self.Author.setObjectName("Author")
        self.horizontalLayout.addWidget(self.Author)
        self.verticalLayout_3.addWidget(self.Navbar)
        self.MainApp = QtWidgets.QFrame(self.mainFrame)
        self.MainApp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainApp.setStyleSheet("")
        self.MainApp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainApp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainApp.setObjectName("MainApp")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MainApp)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Message = QtWidgets.QFrame(self.MainApp)
        self.Message.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Message.setStyleSheet("background-color: rgb(255, 66, 66);")
        self.Message.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Message.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Message.setObjectName("Message")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Message)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MsgLabel = QtWidgets.QLabel(self.Message)
        self.MsgLabel.setStyleSheet("font: 87 14pt \"Arial\";")
        self.MsgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MsgLabel.setObjectName("MsgLabel")
        self.horizontalLayout_2.addWidget(self.MsgLabel)
        self.CloseButton = QtWidgets.QPushButton(self.Message)
        self.CloseButton.setMinimumSize(QtCore.QSize(50, 48))
        self.CloseButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.CloseButton.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(173, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 66, 66);\n"
"}")
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.CloseButton)
        self.verticalLayout_4.addWidget(self.Message)
        self.TitleLabel = QtWidgets.QLabel(self.MainApp)
        self.TitleLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.TitleLabel.setStyleSheet("font: 24pt \"Microsoft Sans Serif\";")
        self.TitleLabel.setText("Insert your link in the input below:")
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_4.addWidget(self.TitleLabel)
        self.Link = QtWidgets.QLineEdit(self.MainApp)
        self.Link.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Link.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(221, 221, 221);\n"
"    border: 1px solid;\n"
"    border-radius: 8px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-color: rgb(255, 255, 0);\n"
"}")
        self.Link.setText("")
        self.Link.setAlignment(QtCore.Qt.AlignCenter)
        self.Link.setObjectName("Link")
        self.verticalLayout_4.addWidget(self.Link)
        self.VideoShowFrame = QtWidgets.QFrame(self.MainApp)
        self.VideoShowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VideoShowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VideoShowFrame.setObjectName("VideoShowFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.VideoShowFrame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Title = QtWidgets.QLabel(self.VideoShowFrame)
        self.Title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Title.setStyleSheet("font: 75 14pt \"Microsoft JhengHei\";")
        self.Title.setText("")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_5.addWidget(self.Title)
        self.Thumbnail = QtWidgets.QLabel(self.VideoShowFrame)
        self.Thumbnail.setStyleSheet("border: 0.8px solid; border-radius: 4px;")
        self.Thumbnail.setMaximumSize(QtCore.QSize(16777215, 361))
        self.Thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.Thumbnail.setText("")
        self.Thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.Thumbnail.setObjectName("Thumbnail")
        self.verticalLayout_5.addWidget(self.Thumbnail)
        self.verticalLayout_4.addWidget(self.VideoShowFrame)
        self.ConfirmButton = QtWidgets.QPushButton(self.MainApp)
        self.ConfirmButton.setMinimumSize(QtCore.QSize(0, 30))
        self.ConfirmButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ConfirmButton.setAutoFillBackground(False)
        self.ConfirmButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid;\n"
"    border-radius: 7px;\n"
"    font: 14pt \"MingLiU-ExtB\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"}")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.ResetButton = QtWidgets.QPushButton(self.MainApp)
        self.ResetButton.setMinimumSize(QtCore.QSize(0, 30))
        self.ResetButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ResetButton.setAutoFillBackground(False)
        self.ResetButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(219, 212, 6, 1);\n"
"    border: 1px solid;\n"
"    border-radius: 7px;\n"
"    font: 14pt \"MingLiU-ExtB\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(219, 212, 6, 1);\n"
"}")
        self.ResetButton.setObjectName("ResetButton")
        self.ResetButton.setText("Reset")
        self.verticalLayout_4.addWidget(self.ConfirmButton)
        self.verticalLayout_4.addWidget(self.ResetButton)
        self.Downloading = QtWidgets.QLabel(self.MainApp)
        self.Downloading.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Downloading.setStyleSheet("color: rgb(76, 229, 0);\n"
"font: 63 12pt \"Lucida Sans\";\n"
"")
        self.Downloading.setAlignment(QtCore.Qt.AlignCenter)
        self.Downloading.setObjectName("Downloading")
        self.verticalLayout_4.addWidget(self.Downloading)
        self.verticalLayout_3.addWidget(self.MainApp)
        self.verticalLayout.addWidget(self.mainFrame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        VideoDownloader.setCentralWidget(self.centralwidget)
        
        
        #
        # Created by: Pedro Barros
        # EVENTS
        #
        
        # Hide message frame as it's only appear when the procedure is successfull, or had a failure
        self.Message.hide()
        
        # Hide VideoShowFrame until the user insert a link
        self.VideoShowFrame.hide()
        
        # Hide Downloading label until it's not downloading any video until the user clicks confirm
        self.Downloading.hide()
        
        # Close error notification
        self.CloseButton.clicked.connect(lambda: self.Message.hide())
        
        # Do all the preprocedures to the main process
        def preprocedure():
                link = self.Link.text()
                
                # Check if input is empty
                if link == "":
                        self.VideoShowFrame.hide()
                        self.Message.show()
                        self.MsgLabel.setText("The input is empty, please insert a valid link")
                # Check if input is numeric
                elif link.isnumeric():
                        self.VideoShowFrame.hide()
                        self.Message.show()
                        self.MsgLabel.setText("The input is numeric, please insert a valid link")
                else:
                        try:
                                #Hide message frame
                                self.Message.hide()
                                
                                # Modules from main
                                video = main.catch_video(link)
                                main.confirm_video(video)
                                
                                # Set video title
                                video_title = video.title
                                self.VideoShowFrame.show()
                                
                                # Show thumbnail and title
                                self.Thumbnail.setPixmap(QtGui.QPixmap("thumbnail_last_video.png"))
                                self.Title.setText(video_title)
                                
                                # Change the text to confirm button
                                self.ConfirmButton.setText("Confirm video to download")
                        
                        except BaseException:
                                self.Message.show()
                                self.MsgLabel.setText("Please insert a valid link!")
        
        # Function to reset the video
        def reset_video():
                self.Message.hide()
                self.VideoShowFrame.hide()
                self.ConfirmButton.setText("Catch Video from Youtube")
                self.Link.setText("")
        
        # Reset video before confirmation
        self.ResetButton.clicked.connect(lambda: reset_video())
        
        # Function main process
        def main_procedure():
                if self.ConfirmButton.text() == "Confirm video to download":
                        self.Downloading.show()
                        link = self.Link.text()
                        video = main.YouTube(link)
                        main.download_video(video)
                        self.Message.setStyleSheet("background-color: rgb(85, 255, 0)")
                        self.MsgLabel.setText("Vídeo baixado com sucesso!")
                        self.Message.show()
                        self.Downloading.hide()
                else:
                        preprocedure()
        
        # Catch video or download video
        self.ConfirmButton.clicked.connect(lambda: main_procedure())

        self.retranslateUi(VideoDownloader)
        QtCore.QMetaObject.connectSlotsByName(VideoDownloader)
                
    def retranslateUi(self, VideoDownloader):
        _translate = QtCore.QCoreApplication.translate
        VideoDownloader.setWindowTitle(_translate("VideoDownloader", "VideoDownloader"))
        self.Logo.setText(_translate("VideoDownloader", "<html><head/><body><p><img src=\":/imgPath/logo.png\"/></p></body></html>"))
        self.Author.setText(_translate("VideoDownloader", "Video Downloader by Pedro Barros"))
        self.MsgLabel.setText(_translate("VideoDownloader", "ERROR!"))
        self.CloseButton.setText(_translate("VideoDownloader", "X"))
        self.Link.setPlaceholderText(_translate("VideoDownloader", "Insert the link right here!"))
        self.ConfirmButton.setText(_translate("VideoDownloader", "Catch Video from Youtube"))
        self.Downloading.setText(_translate("VideoDownloader", "Downloading..."))
from static.img import QtResourceFile


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VideoDownloader = QtWidgets.QMainWindow()
    ui = Ui_VideoDownloader()
    ui.setupUi(VideoDownloader)
    VideoDownloader.show()
    sys.exit(app.exec_())