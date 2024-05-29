import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from app_modules import *
import argparse


parser = argparse.ArgumentParser(description='GUI Application')
parser.add_argument('--version', action='store_true', help='Display the version information')
args = parser.parse_args()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        UIFunctions.removeTitleBar(True)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        UIFunctions.labelTitle(self, 'Main Window - Python Base')
        UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)

        UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        UIFunctions.selectStandardMenu(self, "btn_home")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        UIFunctions.userIcon(self, "WM", "", True)

        def moveWindow(event):

            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)


            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()


        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.show()

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
