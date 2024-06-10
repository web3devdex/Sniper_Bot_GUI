# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top"
                        "-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
""
                        "     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
""
                        "    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255"
                        ");	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"  "
                        "  background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(80, 94, 134);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(28, 33, 47);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.widget_icon_top_bar = QWidget(self.frame_label_top_btns)
        self.widget_icon_top_bar.setObjectName(u"widget_icon_top_bar")
        self.widget_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.widget_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")

        self.horizontalLayout_10.addWidget(self.widget_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
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
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
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
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(80, 94, 134);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color:black; ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: black;")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color:#2D354C;")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.frame_menus)

        self.frame_menus_bottom = QFrame(self.frame_left_menu)
        self.frame_menus_bottom.setObjectName(u"frame_menus_bottom")
        sizePolicy3.setHeightForWidth(self.frame_menus_bottom.sizePolicy().hasHeightForWidth())
        self.frame_menus_bottom.setSizePolicy(sizePolicy3)
        self.frame_menus_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_menus_bottom.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_menus_bottom)
        self.layout_menu_bottom.setSpacing(0)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.frame_menus_bottom)

        self.widget_quickChange = QWidget(self.frame_left_menu)
        self.widget_quickChange.setObjectName(u"widget_quickChange")
        self.widget_quickChange.setMinimumSize(QSize(0, 45))
        self.widget_quickChange.setMaximumSize(QSize(16777215, 45))
        self.widget_quickChange.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_quickChange)
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(4, 0, 4, 4)
        self.comboBox_ChainID = QComboBox(self.widget_quickChange)
        self.comboBox_ChainID.setObjectName(u"comboBox_ChainID")
        self.comboBox_ChainID.setMinimumSize(QSize(0, 40))
        self.comboBox_ChainID.setMaximumSize(QSize(55, 40))
        self.comboBox_ChainID.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_ChainID.setStyleSheet(u"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: None;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.comboBox_ChainID)


        self.verticalLayout_12.addWidget(self.widget_quickChange)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(63, 73, 105) ;")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_wallet = QWidget()
        self.page_wallet.setObjectName(u"page_wallet")
        self.horizontalLayout_20 = QHBoxLayout(self.page_wallet)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.page_wallet)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_27 = QVBoxLayout(self.widget_11)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_11)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setContextMenuPolicy(Qt.PreventContextMenu)
        self.widget_17.setStyleSheet(u"background-color:transparent;")
        self.verticalLayout_35 = QVBoxLayout(self.widget_17)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_38 = QVBoxLayout(self.widget_19)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(203, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)

        self.widget_26 = QWidget(self.widget_20)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_wallet_address = QTextEdit(self.widget_26)
        self.label_wallet_address.setObjectName(u"label_wallet_address")
        self.label_wallet_address.setMinimumSize(QSize(410, 0))
        self.label_wallet_address.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.label_wallet_address.setStyleSheet(u"border:transparent;")
        self.label_wallet_address.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.label_wallet_address)

        self.pushButton_copy_wallet_address = QPushButton(self.widget_26)
        self.pushButton_copy_wallet_address.setObjectName(u"pushButton_copy_wallet_address")
        self.pushButton_copy_wallet_address.setMinimumSize(QSize(50, 25))
        self.pushButton_copy_wallet_address.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_copy_wallet_address.setFocusPolicy(Qt.WheelFocus)
        self.pushButton_copy_wallet_address.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_copy_wallet_address.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_copy_wallet_address)


        self.horizontalLayout_23.addWidget(self.widget_26)

        self.horizontalSpacer_13 = QSpacerItem(203, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_13)


        self.verticalLayout_38.addWidget(self.widget_20)

        self.widget_28 = QWidget(self.widget_19)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 250))
        self.widget_28.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_7)

        self.widget_qr_address = QWidget(self.widget_28)
        self.widget_qr_address.setObjectName(u"widget_qr_address")
        self.widget_qr_address.setMinimumSize(QSize(200, 100))
        self.verticalLayout_34 = QVBoxLayout(self.widget_qr_address)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_qr_address = QLabel(self.widget_qr_address)
        self.label_qr_address.setObjectName(u"label_qr_address")
        self.label_qr_address.setMinimumSize(QSize(250, 250))
        self.label_qr_address.setStyleSheet(u"border:transparent;")

        self.verticalLayout_34.addWidget(self.label_qr_address)


        self.horizontalLayout_29.addWidget(self.widget_qr_address)

        self.horizontalSpacer_11 = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_11)


        self.verticalLayout_38.addWidget(self.widget_28)

        self.widget_25 = QWidget(self.widget_19)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 50))
        self.widget_25.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_28.setSpacing(4)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(201, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_23)

        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_37 = QVBoxLayout(self.widget_27)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_27)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))

        self.verticalLayout_37.addWidget(self.label)

        self.label_6 = QLabel(self.widget_27)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_37.addWidget(self.label_6)


        self.horizontalLayout_28.addWidget(self.widget_27)

        self.horizontalSpacer_30 = QSpacerItem(201, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_30)


        self.verticalLayout_38.addWidget(self.widget_25)


        self.verticalLayout_35.addWidget(self.widget_19)


        self.verticalLayout_27.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_36 = QVBoxLayout(self.widget_16)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_wallet_assets = QScrollArea(self.widget_16)
        self.scrollArea_wallet_assets.setObjectName(u"scrollArea_wallet_assets")
        self.scrollArea_wallet_assets.setStyleSheet(u"border:none;")
        self.scrollArea_wallet_assets.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_wallet_assets.setWidgetResizable(True)
        self.scrollArea_wallet_assets_widget = QWidget()
        self.scrollArea_wallet_assets_widget.setObjectName(u"scrollArea_wallet_assets_widget")
        self.scrollArea_wallet_assets_widget.setGeometry(QRect(0, 0, 866, 285))
        self.scrollArea_wallet_assets.setWidget(self.scrollArea_wallet_assets_widget)

        self.verticalLayout_36.addWidget(self.scrollArea_wallet_assets)


        self.verticalLayout_27.addWidget(self.widget_16)


        self.horizontalLayout_20.addWidget(self.widget_11)

        self.widget_13 = QWidget(self.page_wallet)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(50, 16777215))
        self.widget_13.setContextMenuPolicy(Qt.NoContextMenu)
        self.widget_13.setLayoutDirection(Qt.LeftToRight)
        self.widget_13.setStyleSheet(u"background-color: rgb(28, 33, 47);")
        self.verticalLayout_25 = QVBoxLayout(self.widget_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_add_wallet = QPushButton(self.widget_13)
        self.pushButton_add_wallet.setObjectName(u"pushButton_add_wallet")
        self.pushButton_add_wallet.setMinimumSize(QSize(35, 35))
        self.pushButton_add_wallet.setMaximumSize(QSize(35, 35))
        self.pushButton_add_wallet.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-image:url(:/20x20/icons/20x20/cil-plus.png);\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_add_wallet.setIconSize(QSize(20, 20))

        self.verticalLayout_25.addWidget(self.pushButton_add_wallet)

        self.widget_Wallets = QWidget(self.widget_13)
        self.widget_Wallets.setObjectName(u"widget_Wallets")
        self.layout_wallet_buttons = QVBoxLayout(self.widget_Wallets)
        self.layout_wallet_buttons.setSpacing(5)
        self.layout_wallet_buttons.setObjectName(u"layout_wallet_buttons")
        self.layout_wallet_buttons.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_25.addWidget(self.widget_Wallets)

        self.verticalSpacer = QSpacerItem(20, 562, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer)


        self.horizontalLayout_20.addWidget(self.widget_13)

        self.stackedWidget.addWidget(self.page_wallet)
        self.page_add_wallet = QWidget()
        self.page_add_wallet.setObjectName(u"page_add_wallet")
        self.verticalLayout_28 = QVBoxLayout(self.page_add_wallet)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_add_wallet_header = QWidget(self.page_add_wallet)
        self.widget_add_wallet_header.setObjectName(u"widget_add_wallet_header")
        self.widget_add_wallet_header.setMinimumSize(QSize(0, 250))
        self.widget_add_wallet_header.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_30 = QVBoxLayout(self.widget_add_wallet_header)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_logo_8 = QLabel(self.widget_add_wallet_header)
        self.label_logo_8.setObjectName(u"label_logo_8")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(40)
        self.label_logo_8.setFont(font4)
        self.label_logo_8.setStyleSheet(u"color:rgba(30, 136, 229, 255);")
        self.label_logo_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_logo_8)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_30.addItem(self.verticalSpacer_2)

        self.widget_Reset_2 = QWidget(self.widget_add_wallet_header)
        self.widget_Reset_2.setObjectName(u"widget_Reset_2")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_Reset_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_22 = QSpacerItem(220, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_22)

        self.button_import_wallet = QPushButton(self.widget_Reset_2)
        self.button_import_wallet.setObjectName(u"button_import_wallet")
        self.button_import_wallet.setMinimumSize(QSize(120, 40))
        self.button_import_wallet.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.button_import_wallet)

        self.horizontalSpacer_18 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_18)

        self.button_create_new_wallet = QPushButton(self.widget_Reset_2)
        self.button_create_new_wallet.setObjectName(u"button_create_new_wallet")
        self.button_create_new_wallet.setMinimumSize(QSize(120, 40))
        self.button_create_new_wallet.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.button_create_new_wallet)

        self.horizontalSpacer_29 = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_29)

        self.button_add_wallet_cancel = QPushButton(self.widget_Reset_2)
        self.button_add_wallet_cancel.setObjectName(u"button_add_wallet_cancel")
        self.button_add_wallet_cancel.setMinimumSize(QSize(120, 40))
        self.button_add_wallet_cancel.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.button_add_wallet_cancel)


        self.verticalLayout_30.addWidget(self.widget_Reset_2)


        self.verticalLayout_28.addWidget(self.widget_add_wallet_header)

        self.stackedWidget_2 = QStackedWidget(self.page_add_wallet)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_import_wallet_key = QWidget()
        self.page_import_wallet_key.setObjectName(u"page_import_wallet_key")
        self.verticalLayout_26 = QVBoxLayout(self.page_import_wallet_key)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_15 = QWidget(self.page_import_wallet_key)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_29 = QVBoxLayout(self.widget_15)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_4 = QLabel(self.widget_15)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_29.addWidget(self.label_4)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(244, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_19)

        self.plainTextEdit_import_wallet_priv = QPlainTextEdit(self.widget_18)
        self.plainTextEdit_import_wallet_priv.setObjectName(u"plainTextEdit_import_wallet_priv")
        self.plainTextEdit_import_wallet_priv.setMinimumSize(QSize(400, 0))
        self.plainTextEdit_import_wallet_priv.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit_import_wallet_priv.setStyleSheet(u"background-color: rgb(28, 33, 47);\n"
"border-radius: 15px;\n"
"border: 4px solid #2D354C;\n"
"\n"
"")

        self.horizontalLayout_24.addWidget(self.plainTextEdit_import_wallet_priv)

        self.horizontalSpacer_20 = QSpacerItem(244, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_20)


        self.verticalLayout_29.addWidget(self.widget_18)

        self.widget_Reset_3 = QWidget(self.widget_15)
        self.widget_Reset_3.setObjectName(u"widget_Reset_3")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_Reset_3)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_24 = QSpacerItem(201, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_24)

        self.button_import_wallet_key = QPushButton(self.widget_Reset_3)
        self.button_import_wallet_key.setObjectName(u"button_import_wallet_key")
        self.button_import_wallet_key.setMinimumSize(QSize(120, 40))
        self.button_import_wallet_key.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_26.addWidget(self.button_import_wallet_key)

        self.horizontalSpacer_26 = QSpacerItem(201, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_26)


        self.verticalLayout_29.addWidget(self.widget_Reset_3)


        self.verticalLayout_26.addWidget(self.widget_15)

        self.stackedWidget_2.addWidget(self.page_import_wallet_key)
        self.page_import_wallet_name = QWidget()
        self.page_import_wallet_name.setObjectName(u"page_import_wallet_name")
        self.verticalLayout_33 = QVBoxLayout(self.page_import_wallet_name)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_21 = QWidget(self.page_import_wallet_name)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_32 = QVBoxLayout(self.widget_21)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalSpacer_4 = QSpacerItem(20, 101, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.widget_21)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_32.addWidget(self.label_5)

        self.widget_24 = QWidget(self.widget_21)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_27 = QSpacerItem(279, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)

        self.lineEdit_add_wallet_name = QLineEdit(self.widget_24)
        self.lineEdit_add_wallet_name.setObjectName(u"lineEdit_add_wallet_name")
        self.lineEdit_add_wallet_name.setMinimumSize(QSize(150, 50))
        self.lineEdit_add_wallet_name.setStyleSheet(u"border-radius:15px;\n"
"font-size: 18pt;\n"
"")
        self.lineEdit_add_wallet_name.setClearButtonEnabled(True)

        self.horizontalLayout_27.addWidget(self.lineEdit_add_wallet_name)

        self.horizontalSpacer_28 = QSpacerItem(279, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_28)


        self.verticalLayout_32.addWidget(self.widget_24)

        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_21 = QSpacerItem(375, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_21)

        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_31 = QVBoxLayout(self.widget_23)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.button_add_wallet_done = QPushButton(self.widget_23)
        self.button_add_wallet_done.setObjectName(u"button_add_wallet_done")
        self.button_add_wallet_done.setMinimumSize(QSize(120, 40))
        self.button_add_wallet_done.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_31.addWidget(self.button_add_wallet_done)

        self.verticalSpacer_3 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)


        self.horizontalLayout_25.addWidget(self.widget_23)

        self.horizontalSpacer_25 = QSpacerItem(375, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_25)


        self.verticalLayout_32.addWidget(self.widget_22)


        self.verticalLayout_33.addWidget(self.widget_21)

        self.stackedWidget_2.addWidget(self.page_import_wallet_name)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_2.addWidget(self.page)

        self.verticalLayout_28.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_add_wallet)
        self.page_create_password = QWidget()
        self.page_create_password.setObjectName(u"page_create_password")
        self.verticalLayout_5 = QVBoxLayout(self.page_create_password)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_OuterLogin_3 = QWidget(self.page_create_password)
        self.widget_OuterLogin_3.setObjectName(u"widget_OuterLogin_3")
        self.verticalLayout_13 = QVBoxLayout(self.widget_OuterLogin_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 20, 0, 0)
        self.widget_UnlockWelcome_2 = QWidget(self.widget_OuterLogin_3)
        self.widget_UnlockWelcome_2.setObjectName(u"widget_UnlockWelcome_2")
        self.verticalLayout_16 = QVBoxLayout(self.widget_UnlockWelcome_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_logo_2 = QLabel(self.widget_UnlockWelcome_2)
        self.label_logo_2.setObjectName(u"label_logo_2")
        self.label_logo_2.setFont(font4)
        self.label_logo_2.setStyleSheet(u"color:rgba(30, 136, 229, 255);")
        self.label_logo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_logo_2)

        self.label_logo_3 = QLabel(self.widget_UnlockWelcome_2)
        self.label_logo_3.setObjectName(u"label_logo_3")
        self.label_logo_3.setFont(font4)
        self.label_logo_3.setStyleSheet(u"color:RGB(211, 211, 211);")
        self.label_logo_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_logo_3)

        self.label_logo_4 = QLabel(self.widget_UnlockWelcome_2)
        self.label_logo_4.setObjectName(u"label_logo_4")
        self.label_logo_4.setFont(font4)
        self.label_logo_4.setStyleSheet(u"color:RGB(211, 211, 211);")
        self.label_logo_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_logo_4)


        self.verticalLayout_13.addWidget(self.widget_UnlockWelcome_2)

        self.widget_OuterUnlock_2 = QWidget(self.widget_OuterLogin_3)
        self.widget_OuterUnlock_2.setObjectName(u"widget_OuterUnlock_2")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_OuterUnlock_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(242, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.widget_5 = QWidget(self.widget_OuterUnlock_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(400, 0))
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_3)

        self.lineEdit_create_password = QLineEdit(self.widget_10)
        self.lineEdit_create_password.setObjectName(u"lineEdit_create_password")
        self.lineEdit_create_password.setMinimumSize(QSize(150, 50))
        self.lineEdit_create_password.setStyleSheet(u"border-radius:15px;\n"
"font-size: 18pt;\n"
"")
        self.lineEdit_create_password.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.lineEdit_create_password)


        self.verticalLayout_14.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_2)

        self.lineEdit_repeat_password = QLineEdit(self.widget_9)
        self.lineEdit_repeat_password.setObjectName(u"lineEdit_repeat_password")
        self.lineEdit_repeat_password.setMinimumSize(QSize(150, 50))
        self.lineEdit_repeat_password.setStyleSheet(u"border-radius:15px;\n"
"font-size: 18pt;\n"
"")
        self.lineEdit_repeat_password.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_repeat_password)


        self.verticalLayout_14.addWidget(self.widget_9)


        self.verticalLayout_15.addWidget(self.widget_6)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_20 = QVBoxLayout(self.widget_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.button_create_password_submit = QPushButton(self.widget_8)
        self.button_create_password_submit.setObjectName(u"button_create_password_submit")
        self.button_create_password_submit.setMinimumSize(QSize(120, 40))
        self.button_create_password_submit.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_20.addWidget(self.button_create_password_submit)

        self.button_create_password_cancel = QPushButton(self.widget_8)
        self.button_create_password_cancel.setObjectName(u"button_create_password_cancel")
        self.button_create_password_cancel.setMinimumSize(QSize(120, 40))
        self.button_create_password_cancel.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_20.addWidget(self.button_create_password_cancel)


        self.verticalLayout_15.addWidget(self.widget_8)


        self.horizontalLayout_15.addWidget(self.widget_5)

        self.horizontalSpacer_14 = QSpacerItem(241, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)


        self.verticalLayout_13.addWidget(self.widget_OuterUnlock_2)


        self.verticalLayout_5.addWidget(self.widget_OuterLogin_3)

        self.stackedWidget.addWidget(self.page_create_password)
        self.page_reset_password = QWidget()
        self.page_reset_password.setObjectName(u"page_reset_password")
        self.verticalLayout_21 = QVBoxLayout(self.page_reset_password)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_OuterLogin_4 = QWidget(self.page_reset_password)
        self.widget_OuterLogin_4.setObjectName(u"widget_OuterLogin_4")
        self.verticalLayout_17 = QVBoxLayout(self.widget_OuterLogin_4)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 20, 0, 0)
        self.widget_UnlockWelcome_3 = QWidget(self.widget_OuterLogin_4)
        self.widget_UnlockWelcome_3.setObjectName(u"widget_UnlockWelcome_3")
        self.verticalLayout_18 = QVBoxLayout(self.widget_UnlockWelcome_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_logo_5 = QLabel(self.widget_UnlockWelcome_3)
        self.label_logo_5.setObjectName(u"label_logo_5")
        self.label_logo_5.setFont(font4)
        self.label_logo_5.setStyleSheet(u"color:rgba(30, 136, 229, 255);")
        self.label_logo_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_logo_5)

        self.label_logo_6 = QLabel(self.widget_UnlockWelcome_3)
        self.label_logo_6.setObjectName(u"label_logo_6")
        self.label_logo_6.setFont(font4)
        self.label_logo_6.setStyleSheet(u"color:RGB(211, 211, 211);")
        self.label_logo_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_logo_6)

        self.label_logo_7 = QLabel(self.widget_UnlockWelcome_3)
        self.label_logo_7.setObjectName(u"label_logo_7")
        self.label_logo_7.setFont(font4)
        self.label_logo_7.setStyleSheet(u"color:RGB(211, 211, 211);")
        self.label_logo_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_logo_7)


        self.verticalLayout_17.addWidget(self.widget_UnlockWelcome_3)

        self.widget_OuterUnlock_3 = QWidget(self.widget_OuterLogin_4)
        self.widget_OuterUnlock_3.setObjectName(u"widget_OuterUnlock_3")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_OuterUnlock_3)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(242, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)

        self.widget_7 = QWidget(self.widget_OuterUnlock_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(400, 0))
        self.verticalLayout_19 = QVBoxLayout(self.widget_7)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_7)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_24 = QVBoxLayout(self.widget_14)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_confirm = QWidget(self.widget_14)
        self.widget_confirm.setObjectName(u"widget_confirm")
        self.verticalLayout_23 = QVBoxLayout(self.widget_confirm)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_logo_9 = QLabel(self.widget_confirm)
        self.label_logo_9.setObjectName(u"label_logo_9")
        self.label_logo_9.setFont(font4)
        self.label_logo_9.setStyleSheet(u"color:red;")
        self.label_logo_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_logo_9)

        self.widget_12 = QWidget(self.widget_confirm)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.button_reset_password_submit_go = QPushButton(self.widget_12)
        self.button_reset_password_submit_go.setObjectName(u"button_reset_password_submit_go")
        self.button_reset_password_submit_go.setMinimumSize(QSize(120, 40))
        self.button_reset_password_submit_go.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	color:red;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"	font: bold 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.button_reset_password_submit_go)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_17)

        self.button_reset_password_submit_reset = QPushButton(self.widget_12)
        self.button_reset_password_submit_reset.setObjectName(u"button_reset_password_submit_reset")
        self.button_reset_password_submit_reset.setMinimumSize(QSize(120, 40))
        self.button_reset_password_submit_reset.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	color:green;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"	font: bold 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.button_reset_password_submit_reset)


        self.verticalLayout_23.addWidget(self.widget_12)


        self.verticalLayout_24.addWidget(self.widget_confirm)

        self.widget_Reset = QWidget(self.widget_14)
        self.widget_Reset.setObjectName(u"widget_Reset")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_Reset)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.button_reset_password_submit = QPushButton(self.widget_Reset)
        self.button_reset_password_submit.setObjectName(u"button_reset_password_submit")
        self.button_reset_password_submit.setMinimumSize(QSize(120, 40))
        self.button_reset_password_submit.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.button_reset_password_submit)

        self.horizontalSpacer_15 = QSpacerItem(127, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.button_reset_password_cancel = QPushButton(self.widget_Reset)
        self.button_reset_password_cancel.setObjectName(u"button_reset_password_cancel")
        self.button_reset_password_cancel.setMinimumSize(QSize(120, 40))
        self.button_reset_password_cancel.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.button_reset_password_cancel)


        self.verticalLayout_24.addWidget(self.widget_Reset)


        self.verticalLayout_19.addWidget(self.widget_14)


        self.horizontalLayout_19.addWidget(self.widget_7)

        self.horizontalSpacer_16 = QSpacerItem(241, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_16)


        self.verticalLayout_17.addWidget(self.widget_OuterUnlock_3)


        self.verticalLayout_21.addWidget(self.widget_OuterLogin_4)

        self.stackedWidget.addWidget(self.page_reset_password)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget.addWidget(self.page_widgets)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout_8 = QVBoxLayout(self.page_login)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_OuterLogin_2 = QWidget(self.page_login)
        self.widget_OuterLogin_2.setObjectName(u"widget_OuterLogin_2")
        self.verticalLayout_11 = QVBoxLayout(self.widget_OuterLogin_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 20, 0, 0)
        self.widget_UnlockWelcome = QWidget(self.widget_OuterLogin_2)
        self.widget_UnlockWelcome.setObjectName(u"widget_UnlockWelcome")
        self.label_logo = QLabel(self.widget_UnlockWelcome)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(150, 10, 575, 94))
        self.label_logo.setFont(font4)
        self.label_logo.setStyleSheet(u"color:rgba(30, 136, 229, 255);")
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.widget_UnlockWelcome)

        self.widget_OuterUnlock = QWidget(self.widget_OuterLogin_2)
        self.widget_OuterUnlock.setObjectName(u"widget_OuterUnlock")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_OuterUnlock)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(242, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.widget_OuterUnlock)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_12 = QHBoxLayout(self.widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_6 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.lineEdit_UnlockPwd = QLineEdit(self.widget)
        self.lineEdit_UnlockPwd.setObjectName(u"lineEdit_UnlockPwd")
        self.lineEdit_UnlockPwd.setMinimumSize(QSize(400, 100))
        self.lineEdit_UnlockPwd.setStyleSheet(u"border-radius:15px;\n"
"font-size: 18pt;\n"
"")
        self.lineEdit_UnlockPwd.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.lineEdit_UnlockPwd)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_10.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_Unlock = QPushButton(self.widget_3)
        self.button_Unlock.setObjectName(u"button_Unlock")
        self.button_Unlock.setMinimumSize(QSize(140, 80))
        self.button_Unlock.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.button_Unlock)

        self.horizontalSpacer_3 = QSpacerItem(54, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_22 = QVBoxLayout(self.widget_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.button_createPW = QPushButton(self.widget_4)
        self.button_createPW.setObjectName(u"button_createPW")
        self.button_createPW.setMinimumSize(QSize(120, 40))
        self.button_createPW.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_22.addWidget(self.button_createPW)

        self.button_resetPW = QPushButton(self.widget_4)
        self.button_resetPW.setObjectName(u"button_resetPW")
        self.button_resetPW.setMinimumSize(QSize(120, 40))
        self.button_resetPW.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:  rgb(27, 29, 35);\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_22.addWidget(self.button_resetPW)


        self.verticalLayout_10.addWidget(self.widget_4)


        self.horizontalLayout_9.addWidget(self.widget_2)

        self.horizontalSpacer_4 = QSpacerItem(241, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addWidget(self.widget_OuterUnlock)


        self.verticalLayout_8.addWidget(self.widget_OuterLogin_2)

        self.stackedWidget.addWidget(self.page_login)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(80, 94, 134);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color:black;")

        self.horizontalLayout_7.addWidget(self.label_credits)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_popup = QFrame(self.frame_grip)
        self.frame_popup.setObjectName(u"frame_popup")
        self.frame_popup.setMaximumSize(QSize(300, 20))
        self.frame_popup.setLayoutDirection(Qt.LeftToRight)
        self.frame_popup.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_popup.setFrameShape(QFrame.NoFrame)
        self.frame_popup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_popup)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(267, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.label_version = QLabel(self.frame_popup)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: black;")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_popup)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(15, 20))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"background-position:  bottom;\n"
"background-repeat: no-reperat;\n"
"")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_7.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_wallet_address.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">0x20f21D732c9e82fA3E58A948329D16D3A4192119</span></p></body></html>", None))
        self.pushButton_copy_wallet_address.setText(QCoreApplication.translate("MainWindow", u"COPY", None))
        self.label_qr_address.setText(QCoreApplication.translate("MainWindow", u"QRCODE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Total Balance:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">0.00$</span></p></body></html>", None))
        self.pushButton_add_wallet.setText("")
        self.label_logo_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Import or create wallet</span></p></body></html>", None))
        self.button_import_wallet.setText(QCoreApplication.translate("MainWindow", u"Import Wallet", None))
        self.button_create_new_wallet.setText(QCoreApplication.translate("MainWindow", u"New Wallet", None))
        self.button_add_wallet_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">Please enter your private key or mnemonic phrase to access your wallet.</span></p></body></html>", None))
        self.button_import_wallet_key.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">Please enter a short Name for your wallet</span></p></body></html>", None))
        self.lineEdit_add_wallet_name.setText("")
        self.button_add_wallet_done.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.label_logo_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Synarix</span></p></body></html>", None))
        self.label_logo_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Create Password to protect your assets.</span></p></body></html>", None))
        self.label_logo_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Your imported wallets are encrypted with your password, so if you lose it, you will never be able to access your wallet</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter password", None))
        self.lineEdit_create_password.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Repeat password", None))
        self.lineEdit_repeat_password.setText("")
        self.button_create_password_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.button_create_password_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_logo_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Synarix</span></p></body></html>", None))
        self.label_logo_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Reset Password</span></p></body></html>", None))
        self.label_logo_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">If you reset your password, it will create a backup of your settings and wallets. You can only import them again with your password.</span></p></body></html>", None))
        self.label_logo_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Reset Password</span></p><p><span style=\" font-size:9pt; font-weight:700;\">Are you sure Reset your Wallets and Password?</span></p></body></html>", None))
        self.button_reset_password_submit_go.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.button_reset_password_submit_reset.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.button_reset_password_submit.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.button_reset_password_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Synarix</span></p></body></html>", None))
        self.lineEdit_UnlockPwd.setText("")
        self.button_Unlock.setText(QCoreApplication.translate("MainWindow", u"Unlock", None))
        self.button_createPW.setText(QCoreApplication.translate("MainWindow", u"Create Password", None))
        self.button_resetPW.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Synarix", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

