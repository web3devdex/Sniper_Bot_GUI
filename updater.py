import sys
import platform
import requests
import subprocess
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

## ==> GLOBALS
counter = 0

# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))
        





# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = counter
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong>")
        # Change Texts
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################

    def check_version(self):
        QtCore.QTimer.singleShot(500, lambda: self.ui.label_description.setText("<strong>Check Version</strong>"))
        try:
            # Fetch the latest version from GitHub
            #response = requests.get('https://raw.githubusercontent.com/username/repository/branch/version.txt')
            #response.raise_for_status()
            latest_version = "Version: 1.01" #response.text.strip()
            # Get the local version
            process = subprocess.run(['gui.exe', '--version'], capture_output=True, text=True)
            local_version = process.stdout.strip()
            print(local_version)
            if local_version != latest_version:
                QtCore.QTimer.singleShot(500, lambda: self.ui.label_description.setText("<strong>Download</strong> new gui.exe"))
                self.download_new_version()
            else:
                QtCore.QTimer.singleShot(500, lambda: self.ui.label_description.setText("<strong>Already newest Version</strong>"))

        except requests.RequestException as e:
            self.ui.label_description.setText(f"Error fetching version: {e}")
            print(e)
        except subprocess.SubprocessError as e:
            self.ui.label_description.setText(f"Error checking local version: {e}")
            print(e)

    def download_new_version(self):
        try:
            url = 'https://github.com/username/repository/releases/download/latest/gui.exe'
            response = requests.get(url)
            response.raise_for_status()
            with open('gui.exe', 'wb') as f:
                f.write(response.content)
            self.ui.label_description.setText("<strong>Download complete</strong>")
        except requests.RequestException as e:
            print(e)
            self.ui.label_description.setText(f"Error downloading new version: {e}")
        except Exception as e:
            print(e)

    def progress(self):
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        if self.counter < 10:
            self.ui.label_description.setText("<strong>Initialized</strong>")
            self.check_version()
            self.counter = 10

        # CLOSE SPLASH SCREEN AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW (placeholder for actual main window class)
            self.main = MainWindow()  # Replace with actual main window class
            self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        if self.counter > 9:
            self.counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
