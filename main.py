# importing os module
from pytube import YouTube
from pathlib import Path
import os
from PyQt5 import QtWidgets
import sys

# importing front-end
import Front_page as Fr


class Function(Fr.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Function, self).__init__()
        self.setupUi(self)

        # button function
        self.pushButton.clicked.connect(self.videoDownload)
        # self.pushButton.clicked.connect(self.downloading)
        #self.progressBar.setValue(0)

    def videoDownload(self):
        # creating folders Directory
        directory = "YouTube Videos"
        parent_dir = str(Path.home() / "Downloads")

        path = os.path.join(parent_dir, directory)
        #self.label.setText("Am a man")

        try:
            os.makedirs(path, exist_ok=True)
            self.label.setText("Directory '% s' created" % directory)
        except OSError as error:
            self.label.setText("Directory '%s' can not be created" % directory)

        # video link for downloading
        LINK = self.lineEdit.text()
        SAVE_PATH = str(Path.home() / "Downloads/YouTube Videos")

        try:
            yt = YouTube(LINK)
            yt.streams.filter(res="720p", progressive=True, file_extension="mp4").first(
            ).download(output_path=SAVE_PATH)
            self.downloading()
            self.label.setText("download complete")
        except:
            self.label.setText("connection error")

    def downloading(self):
        n = 100
        for i in range(n):
            self.progressBar.setValue(i+1)            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = Function()
    qt_app.show()
    app.exec_()
