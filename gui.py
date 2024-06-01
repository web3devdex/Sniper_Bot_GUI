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
        UIFunctions.labelDescription(self, '')
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
        if True:
            self.Login()
        else:
            UIFunctions.show_incorrect_animation(self, self.ui.lineEdit_UnlockPwd)
            UIFunctions.show_popup(self.ui.frame_popup,"Wrong Password", "red")


    
    def Login(self):
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Wallet", "btn_wallet", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Swap", "btn_swap", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        UIFunctions.addNewMenu(self, "Sniper", "btn_sniper", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Sniper", "btn_sniper", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Sniper", "btn_sniper", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Stake", "btn_stake", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Preferences", "btn_preferences", "url(:/16x16/icons/16x16/cil-user-follow.png)", False)
        UIFunctions.selectStandardMenu(self, "btn_wallet")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)



    def Button(self):
        btnWidget = self.sender()
        
        if btnWidget.objectName() == "btn_wallet":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_wallet")
            UIFunctions.labelPage(self, "Wallet")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "btn_swap":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_swap")
            UIFunctions.labelPage(self, "Swap Tokens")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "btn_sniper":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_sniper")
            UIFunctions.labelPage(self, "Snip Token Launche")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))


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

if __name__ == "__main__":
    if args.version:
        print("Version: 0.1b")
    else: 
        print("Running GUI")
        app = QApplication(sys.argv)
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
        window = MainWindow()
        sys.exit(app.exec())
