# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import files_rc

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
"background-color: #3F4969 ;\n"
"    color: rgb(210, 210, 210);\n"
"    border-radius: 15px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.dropShadowFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777211))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.frame_5.setStyleSheet(u"background-color: #1C212F;\n"
"border-radius: 15px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.frame_label_top_btns = QFrame(self.frame_5)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setToolTipDuration(-2)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.horizontalSpacer_4 = QSpacerItem(495, 9, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btn_close = QPushButton(self.frame_5)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.dropShadowFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.label_logo = QLabel(self.frame_2)
        self.label_logo.setObjectName(u"label_logo")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(40)
        self.label_logo.setFont(font1)
        self.label_logo.setStyleSheet(u"color:rgba(30, 136, 229, 255);")
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_logo)

        self.label_description = QLabel(self.frame_2)
        self.label_description.setObjectName(u"label_description")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_description.setFont(font2)
        self.label_description.setStyleSheet(u"")
        self.label_description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_description)

        self.progressBar = QProgressBar(self.frame_2)
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
"    background-color: rgba(30, 136, 229, 255);\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_loading = QLabel(self.frame_2)
        self.label_loading.setObjectName(u"label_loading")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        self.label_loading.setFont(font3)
        self.label_loading.setStyleSheet(u"")
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_loading)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.dropShadowFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777211))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 157, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setStyleSheet(u"background-color: #505E86;\n"
"border-radius: 15px;\n"
"border-top-right-radius:0px;\n"
"border-top-left-radius:0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 12, 0)
        self.horizontalSpacer = QSpacerItem(495, 9, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_credits = QLabel(self.frame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        self.label_credits.setFont(font4)
        self.label_credits.setStyleSheet(u"color: rgb(255, 165, 0);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_credits)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("SplashScreen", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("SplashScreen", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_logo.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:700;\">Synarix</span></p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:700;\">Miltichain</span> Sniper App</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:700;\">License</span>: <a href=\"https://github.com/Synarix/Sniper_Bot_GUI/tree/main?tab=LGPL-2.1-1-ov-file\"><span>LGPL-2.1 license</span></a></p></body></html>", None))
    # retranslateUi

