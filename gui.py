import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from app_modules import *
from ui_styles import Style
import argparse

parser = argparse.ArgumentParser(description='GUI Application')
parser.add_argument('--version', action='store_true', help='Display the version information')
args = parser.parse_args()



class Popup(QFrame):
    def __init__(self, message, color, parent=None):
        super().__init__(parent)
        self.setStyleSheet("border: 1px solid black; border-radius:5%; background:#1C212F;")
        layout = QVBoxLayout(self)
        label = QLabel(message, self)
        label.setStyleSheet(f"color: {color};")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.popup = None
        UIFunctions.removeTitleBar(True)
        WindowTitle = 'Synarix - Multichain Sniper Bot'
        self.setWindowTitle(WindowTitle)
        UIFunctions.labelTitle(self, WindowTitle)

        UIFunctions.labelDescription(self, 'Unlock or Create PWD')

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        self.ui.lineEdit_UnlockPwd.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_UnlockPwd.setPlaceholderText("Enter your password")
        self.ui.button_Unlock.clicked.connect(self.unlockWallet)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

        def moveWindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.show()



    def unlockWallet(self):
        print("unlock")
        UIFunctions.show_incorrect_animation(self, self.ui.lineEdit_UnlockPwd)
        self.show_popup("This is a red popup!", "red")


    def show_popup(self, message, color):
        if self.popup is not None:
            self.remove_popup()

        self.popup = Popup(message, color, self.ui.frame_popup)
        
        # Position the popup off-screen to the right
        start_rect = QRect(self.ui.frame_popup.width(), 
                           self.ui.frame_popup.rect().center().y() - 50, 
                           200, 100)
        self.popup.setGeometry(start_rect)
        self.popup.show()

        # Animate the popup in
        self.animate_popup_in(self.popup)

        # Set a timer to animate the popup out after 3 seconds
        QTimer.singleShot(3000, self.animate_popup_out)

    def animate_popup_in(self, widget):
        self.animation_in = QPropertyAnimation(widget, b"geometry")
        self.animation_in.setDuration(1000)  # 1 second
        end_rect = QRect(self.ui.frame_popup.rect().center().x() - 100, 
                         self.ui.frame_popup.rect().center().y() - 50, 
                         200, 100)
        self.animation_in.setStartValue(widget.geometry())
        self.animation_in.setEndValue(end_rect)
        self.animation_in.start()

    def animate_popup_out(self):
        if self.popup:
            self.animation_out = QPropertyAnimation(self.popup, b"geometry")
            self.animation_out.setDuration(1000)  # 1 second
            end_rect = QRect(self.ui.frame_popup.width(), 
                             self.popup.geometry().y(), 
                             200, 100)  # Off-screen to the right
            self.animation_out.setStartValue(self.popup.geometry())
            self.animation_out.setEndValue(end_rect)
            self.animation_out.start()
            self.animation_out.finished.connect(self.remove_popup)

    def remove_popup(self):
        if self.popup:
            self.popup.hide()
            self.popup.deleteLater()
            self.popup = None


    def Login(self):
        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Wallet", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Swap", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        UIFunctions.addNewMenu(self, "Sniper", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.selectStandardMenu(self, "btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        UIFunctions.userIcon(self, "WM", "", True)



    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
        print(event.buttons())
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MiddleButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    if args.version:
        print("Version: 0.1b")
    else: 
        print("Running gui.exe")
        app = QApplication(sys.argv)
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
        window = MainWindow()
        sys.exit(app.exec())
