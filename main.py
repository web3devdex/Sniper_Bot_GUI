import sys, os, platform
import requests
import subprocess
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from ui_styles import Style

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen


## ==> GLOBALS
counter = 0
executable = False
python_executable = sys.executable

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

print(f"Script Directory: {script_dir}")
print(f"Python Directory: {python_executable}")
print('System: ' + platform.system())
print('Version: ' + platform.release())


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = counter

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        WindowTitle = 'Synarix - Updater'
        self.ui.label_title_bar_top.setText(WindowTitle)
        self.ui.btn_close.clicked.connect(lambda: self.close())

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.ui.label_description.setText("<strong>WELCOME</strong>")


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
        if executable:
            process = subprocess.run([os.path.join(script_dir, 'gui.exe'), '--version'], capture_output=True, text=True)
        else:
            process = subprocess.run([os.path.join(script_dir, 'gui.py'), '--version'], capture_output=True, text=True)
        local_version = process.stdout.strip()
        return { "latest": latest_version, "local": local_version}

    def check_version(self):
        self.ui.label_description.setText("<strong>Check Version</strong>")
        try:
            versions = self.get_local_versions()
            try:
                # Fetch the latest version from GitHub
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
        except Exception as e:
            if type(FileNotFoundError()) == type(e):
                self.download_new_version()
                

    def download_new_version(self):
        try:
            url = 'https://github.com/Synarix/Sniper_Bot_GUI/raw/main/gui.exe'
            response = requests.get(url)
            response.raise_for_status()
            with open(f'{script_dir}/gui.exe', 'wb') as f:
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
            self.counter = 90
            self.ui.progressBar.setValue(self.counter)

        if self.counter > 100:
            self.timer.stop()
            self.close()
            subprocess.run([python_executable, os.path.join(script_dir, 'gui.py')])

        if self.counter > 24:
            self.counter += 1
        self.ui.progressBar.setValue(self.counter)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
