# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenGlxQBy.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(675, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(51, 51, 51); \n"
"    color: rgb(0, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 15, 40, 5)
        self.label_logo = QLabel(self.dropShadowFrame)
        self.label_logo.setObjectName(u"label_logo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(40)
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"color:rgba(30, 136, 229, 255);")
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_logo)

        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"")
        self.label_description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_description)

        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 35))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(0, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0.511364, \n"
"        x2:1, y2:0.523, \n"
"        stop:0 rgba(30, 136, 229, 255),\n"
"        stop:1 rgba(255, 165, 0, 255)  \n"
"    );\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"")
        self.label_loading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_loading)

        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(255, 165, 0);")
        self.label_credits.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_credits)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_logo.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:700;\">Synarix</span></p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:700;\">SNIPER</span>  App</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:700;\">License</span>: <a href=\"https://github.com/Synarix/Sniper_Bot_GUI/tree/main?tab=LGPL-2.1-1-ov-file\"><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Noto Sans','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:14px; color:#000000;\">LGPL-2.1 license</span></a></p></body></html>", None))
    # retranslateUi

