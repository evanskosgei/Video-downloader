# importing os module
from pytube import YouTube
import os
from PyQt5 import QtWidgets
import sys

import Front_page as Fr


class Function(Fr.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Function, self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.videoDownload)

    def videoDownload(self):
        # creating folders Directory
        directory = "YouTube Videos"
        parent_dir = "C:/Users/kiongoss/Videos"

        path = os.path.join(parent_dir, directory)

        try:
            os.makedirs(path, exist_ok=True)
            print("Directory '% s' created" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)
        
        #video link for downloading
        LINK = self.lineEdit.text()   
        SAVE_PATH = "C:/Users/kiongoss/Videos/YouTube Videos"
        FILE_NAME = "Rock Blaster Scrach video.mp4"

        try:
            yt = YouTube(LINK)
            yt.streams.filter(res = "720p", progressive= True, file_extension= "mp4").first().download(output_path = SAVE_PATH)
        except:
            print("connection error")

        print("download complete") 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = Function()
    qt_app.show()
    app.exec_()
