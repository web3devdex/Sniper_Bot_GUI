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

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong>")
        # Change Texts
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        self.timer.start(100)
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################

    def get_local_versions(self):
        response = requests.get('https://raw.githubusercontent.com/Synarix/Sniper_Bot_GUI/main/version.txt')
        response.raise_for_status()
        latest_version = response.text.strip()
        # Get the local version
        process = subprocess.run(['gui.exe', '--version'], capture_output=True, text=True)
        local_version = process.stdout.strip()
        return { "latest": latest_version, "local": local_version}

    def check_version(self):
        self.ui.label_description.setText("<strong>Check Version</strong>")
        try:
            # Fetch the latest version from GitHub
            versions = self.get_local_versions()
            latest_version, local_version = versions["latest"], versions["local"]
            if local_version != latest_version:
                self.ui.label_description.setText("<strong>Download</strong> new gui.exe")
                self.download_new_version()
            else:
                self.ui.label_description.setText("<strong>Already newest Version</strong>")

        except requests.RequestException as e:
            self.ui.label_description.setText(f"Error fetching version: {e}")
            print(e)
        except subprocess.SubprocessError as e:
            self.ui.label_description.setText(f"Error checking local version: {e}")
            print(e)

    def download_new_version(self):
        try:
            url = 'https://github.com/Synarix/Sniper_Bot_GUI/raw/main/gui.exe'
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

        if self.counter < 10:
            self.ui.label_description.setText("<strong>Initialized</strong>")
            self.check_version()
            self.counter = 45
            self.ui.progressBar.setValue(self.counter)

        if self.counter < 46:
            self.ui.label_description.setText("<strong>Check Settings</strong>")
            print(True)

            self.counter = 99
            self.ui.progressBar.setValue(self.counter)


        # CLOSE SPLASH SCREEN AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW (placeholder for actual main window class)
            subprocess.run(['gui.exe', '--start'])
            self.close()

        # INCREASE COUNTER
        if self.counter > 24:
            self.counter += 1
        self.ui.progressBar.setValue(self.counter)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
