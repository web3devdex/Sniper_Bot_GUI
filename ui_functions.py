## ==> GUI FILE
from gui import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

popup_width = 130
popup_height = 50


class UIFunctions(QMainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True
    popup = None
    animation_in = None
    animation_out = None

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.previous_cursor_pos = QCursor.pos()
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(
                QtGui.QIcon(":/16x16/icons/16x16/cil-window-restore.png")
            )
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            QCursor.setPos(self.previous_cursor_pos)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(
                QtGui.QIcon(":/16x16/icons/16x16/cil-window-maximize.png")
            )
            self.ui.frame_top_btns.setStyleSheet(
                "background-color: rgba(27, 29, 35, 200)"
            )
            self.ui.frame_size_grip.show()

    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enableMaximumSize(self, width, height):
        if width != "" and height != "":
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumWidth"
            )
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily("Segoe UI")
        button = QPushButton(str(count), self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace("ICON_REPLACE", icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)
        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)


    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(63, 73, 105); }")
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace(
            "QPushButton { border-right: 7px solid rgb(63, 73, 105); }", ""
        )
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def labelPage(self, text):
        newText = "| " + text.upper()
        self.ui.label_top_info_2.setText(newText)

   
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(
                    250, lambda: UIFunctions.maximize_restore(self)
                )

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = (
                dobleClickMaximizeRestore
            )
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "width: 20px; height: 20px; margin 0px; padding: 0px;"
        )

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(
            lambda: UIFunctions.maximize_restore(self)
        )

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def show_incorrect_animation(self, component):
        original_geometry = component.geometry()
        animation = QPropertyAnimation(component, b"geometry")
        animation.setDuration(500)
        original_style = component.styleSheet()
        keyframes = [
            (0.0, original_geometry),
            (
                0.1,
                QRect(
                    original_geometry.x() - 10,
                    original_geometry.y(),
                    original_geometry.width(),
                    original_geometry.height(),
                ),
            ),
            (
                0.2,
                QRect(
                    original_geometry.x() + 10,
                    original_geometry.y(),
                    original_geometry.width(),
                    original_geometry.height(),
                ),
            ),
            (
                0.3,
                QRect(
                    original_geometry.x() - 10,
                    original_geometry.y(),
                    original_geometry.width(),
                    original_geometry.height(),
                ),
            ),
            (
                0.4,
                QRect(
                    original_geometry.x() + 10,
                    original_geometry.y(),
                    original_geometry.width(),
                    original_geometry.height(),
                ),
            ),
            (0.5, original_geometry),
        ]
        for kf in keyframes:
            animation.setKeyValueAt(kf[0], kf[1])
        animation.setEndValue(original_geometry)
        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(animation)
        component.setStyleSheet(original_style + "border: 2px solid red;")
        animation_group.start()

        def reset_style():
            self.ui.lineEdit_UnlockPwd.setStyleSheet(original_style)

        QTimer.singleShot(500, reset_style)
        self.animation_group = animation_group

    @staticmethod
    def show_popup(parent, message, color):
        if UIFunctions.popup is not None:
            UIFunctions.remove_popup()
        UIFunctions.popup = Popup(message, color, parent)
        popup_x_center = (parent.width() - popup_width) // 2
        popup_y_center = (parent.height() - popup_height) // 2
        start_rect = QRect(popup_x_center, popup_y_center, popup_width, popup_height)
        UIFunctions.popup.setGeometry(start_rect)
        UIFunctions.popup.show()
        UIFunctions.animate_popup_in(UIFunctions.popup, parent)
        QTimer.singleShot(3000, UIFunctions.animate_popup_out)

    @staticmethod
    def animate_popup_in(widget, parent):
        UIFunctions.animation_in = QPropertyAnimation(widget, b"geometry")
        UIFunctions.animation_in.setDuration(1000)
        popup_x_center = (parent.width() - popup_width) // 2
        popup_y_center = (parent.height() - popup_height) // 2
        end_rect = QRect(popup_x_center, popup_y_center, popup_width, popup_height)
        UIFunctions.animation_in.setStartValue(widget.geometry())
        UIFunctions.animation_in.setEndValue(end_rect)
        UIFunctions.animation_in.start()

    @staticmethod
    def animate_popup_out():
        if UIFunctions.popup:
            UIFunctions.animation_out = QPropertyAnimation(
                UIFunctions.popup, b"geometry"
            )
            UIFunctions.animation_out.setDuration(1000)
            popup_x_end = UIFunctions.popup.parent().width()
            end_rect = QRect(
                popup_x_end,
                UIFunctions.popup.geometry().y(),
                UIFunctions.popup.geometry().width(),
                UIFunctions.popup.geometry().height(),
            )
            UIFunctions.animation_out.setStartValue(UIFunctions.popup.geometry())
            UIFunctions.animation_out.setEndValue(end_rect)
            UIFunctions.animation_out.start()
            UIFunctions.animation_out.finished.connect(UIFunctions.remove_popup)

    @staticmethod
    def remove_popup():
        if UIFunctions.popup:
            UIFunctions.popup.hide()
            UIFunctions.popup.deleteLater()
            UIFunctions.popup = None


class Popup(QFrame):
    def __init__(self, message, color, parent=None):
        super().__init__(parent)
        self.setStyleSheet("border-radius:5%; background:#1C212F;")
        layout = QVBoxLayout(self)
        label = QLabel(message, self)
        label.setStyleSheet(f"color: {color};")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
