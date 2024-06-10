## ==> GUI FILE
from gui import *
from ui_assets import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1
## ==> COUT INITIAL WALLET
count_wallet = 1

popup_width = 200
popup_height = 60



class UIFunctions(QMainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True
    popup = None
    animation_in = None
    animation_out = None
    

    def connectButtons(self):
        #UnlockPage:
        self.ui.button_Unlock.clicked.connect(self.unlockWallet)
        self.ui.button_createPW.clicked.connect(self.Button)
        self.ui.button_resetPW.clicked.connect(self.Button)
        self.ui.button_create_password_cancel.clicked.connect(self.Button)
        self.ui.button_create_password_submit.clicked.connect(self.Button)
        self.ui.button_reset_password_cancel.clicked.connect(self.Button)
        self.ui.button_reset_password_submit.clicked.connect(self.Button)
        self.ui.button_reset_password_submit_go.clicked.connect(self.Button)
        self.ui.button_reset_password_submit_reset.clicked.connect(self.Button)
        self.ui.lineEdit_UnlockPwd.returnPressed.connect(self.unlockWallet)
        
        #ImportWalletPage:
        self.ui.button_import_wallet.clicked.connect(self.Button)
        self.ui.pushButton_add_wallet.clicked.connect(self.Button)
        self.ui.button_create_new_wallet.clicked.connect(self.Button)
        self.ui.button_add_wallet_cancel.clicked.connect(self.Button)
        self.ui.button_add_wallet_done.clicked.connect(self.Button)
        self.ui.button_import_wallet_key.clicked.connect(self.Button)
        self.ui.comboBox_ChainID.currentIndexChanged.connect(self.Button)

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
        
       
                
    def selectWalletStyle(getStyle):
        select = getStyle + ("QPushButton { border-left: 3px solid rgb(85, 170, 255); }")
        return select

    def deselectWalletStyle(getStyle):
        deselect = getStyle.replace("QPushButton { border-left: 3px solid rgb(85, 170, 255); }", "")
        return deselect

    def addWalletButtons(self, wallet_data):
        global count_wallet
        layout = self.ui.widget_Wallets.layout()

        if layout is None:
            layout = QVBoxLayout(self.ui.widget_Wallets)
            self.ui.widget_Wallets.setLayout(layout)
        else:
            # Clear existing layout
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    layout.removeItem(item)

        # Create new buttons and add them to the layout
        for wallet in wallet_data:
            button = QPushButton(wallet["name"])
            button.setObjectName("select_wallet_" + wallet["name"])
            button.setMinimumHeight(30)
            button.setStyleSheet(Style.style_bt_wallet)
            sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            sizePolicy3.setHorizontalStretch(0)
            sizePolicy3.setVerticalStretch(0)
            sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy3)
            button.setMinimumSize(QSize(10, 30))
            button.setLayoutDirection(Qt.LeftToRight)
            button.clicked.connect(self.Button)
            layout.addWidget(button)
            count_wallet += 1  # Increment the global counter if needed
            self.ui.widget_Wallets.setLayout(layout)



    def selectWallet(self, widget):
        for w in self.ui.widget_Wallets.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectWalletStyle(w.styleSheet()))

    def resetWalletStyle(self, widget):
        for w in self.ui.widget_Wallets.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectWalletStyle(w.styleSheet()))


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
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximize_restore.clicked.connect(
            lambda: UIFunctions.maximize_restore(self)
        )
        self.ui.btn_close.clicked.connect(lambda: self.close())
        
    

    def createPassword(self, password0, password1):
        if str(password0) == str(password1):
            if len(str(password0)) > 6:
                self.encryption.encrypt(self.settings.settings["cache:refferenceClear"], password0)
                encrypted_text = self.encryption.encrypt(self.settings.settings["cache:refferenceClear"], password0)
                self.settings.updateSetting("cache:refferenceHash", encrypted_text)
                UIFunctions.show_popup(self.ui.frame_popup,"Success!", "green")
                self.unlockPage()
            else:
                UIFunctions.show_incorrect_animation(self, self.ui.lineEdit_repeat_password)
                UIFunctions.show_incorrect_animation(self, self.ui.lineEdit_create_password)
                UIFunctions.show_popup(self.ui.frame_popup,"Min Length 6", "red") 
        else:
            UIFunctions.show_incorrect_animation(self, self.ui.lineEdit_create_password)
            UIFunctions.show_popup(self.ui.frame_popup,"Password not matching", "red")
            
            
    def verify_password(self, entered_password):
        stored_clear = self.settings.settings["cache:refferenceClear"]
        stored_hash = self.settings.settings["cache:refferenceHash"]
        if stored_hash == "":
                UIFunctions.show_incorrect_animation(self, self.ui.button_createPW)
                UIFunctions.show_popup(self.ui.frame_popup, "First create password", "red")
                return False
        try:
            test_hash = self.encryption.decrypt(self.settings.settings["cache:refferenceHash"], entered_password)
            if test_hash == stored_clear:
                self.encryption.generate_masterkey(str(entered_password).encode())
                self.ui.lineEdit_UnlockPwd.clear()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            UIFunctions.show_incorrect_animation(self, self.ui.lineEdit_UnlockPwd)
            UIFunctions.show_popup(self.ui.frame_popup,"Wrong Password", "red")
            return False 
        

    def add_assets_to_scroll_area(self):
        scroll_area = self.ui.scrollArea_wallet_assets
        inner_widget = scroll_area.widget()
        if inner_widget is None:
            inner_widget = QWidget()
            scroll_area.setWidget(inner_widget)
            inner_layout = QVBoxLayout(inner_widget)
        else:
            inner_layout = inner_widget.layout()
            if inner_layout is None:
                inner_layout = QVBoxLayout(inner_widget)

        if inner_layout is not None:
            while inner_layout.count():
                item = inner_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        if not hasattr(self, 'spinner') or self.spinner is None:
            self.spinner = SvgSpinnerWidget(UIAssets.SpinnerSVG(), inner_widget)
            self.spinner.setMinimumSize(50, 50)
            self.spinner.setMaximumSize(50, 50)
            self.spinner.setObjectName("spinner")
            inner_layout.addWidget(self.spinner, alignment=Qt.AlignCenter)
        elif self.spinner.parent() != inner_widget:
            self.spinner.setParent(inner_widget)
            inner_layout.addWidget(self.spinner, alignment=Qt.AlignCenter)

        if hasattr(self, 'spinner') and self.spinner:
            self.spinner.show()

        def load_assets_and_remove_spinner():
            UIFunctions.load_assets(self, inner_layout)
            if hasattr(self, 'spinner') and self.spinner:
                self.spinner.hide()
                self.spinner.deleteLater()
                self.spinner = None

        QTimer.singleShot(200, load_assets_and_remove_spinner)
        

    def load_assets(self, layout):          
        asset_data = [
            ("BTC", "25598.45", "2.3", "0.1", "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"),
            ("ETH", "1500.32", "-1.8", "300.54", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"),
            ("ETH", "1500.32", "-1.8", "300.54", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"),
            ("ETH", "1500.32", "-1.8", "300.54", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"),
            ("ETH", "1500.32", "-1.8", "300.54", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"),
            ("ETH", "1500.32", "-1.8", "300.54", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"),
            ("ETH", "1500.32", "-1.8", "300.54", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png")
        ]
        
        for index, data in enumerate(asset_data):
            
            asset_widget = QWidget()
            asset_layout = QHBoxLayout(asset_widget)
            asset_widget.setStyleSheet("background-color: #2D354C; border-radius: 5px; max-height: 50px;")

            # Icon label
            icon_label = QLabel()
            unique_identifier = f"{data[0]}_{index}"
            self.icon_labels[unique_identifier] = icon_label  # Store the label with the URL as the identifier
            asset_layout.addWidget(icon_label)
            UIFunctions.load_image(self, data[4], unique_identifier)

            # Name label
            name_label = QLabel(data[0])
            name_label.setStyleSheet("font-weight: bold; font-size: 16px; color: white;")
            asset_layout.addWidget(name_label)

            # USD value label
            symbol = '▲' if float(data[2]) >= float(0) else '▼'
            color = 'lightgreen' if float(data[2]) >= float(0) else 'red'
            
            usd_label = QLabel(f"${data[1]}")
            usd_label.setStyleSheet(f"font-size: 14px; color: {color};")
            asset_layout.addWidget(usd_label)

            percentage_label = QLabel(f"{symbol} {data[2]}%")
            percentage_label.setStyleSheet(f"font-size: 14px; color: {color};")
            asset_layout.addWidget(percentage_label)

            asset_balance = QLabel(f"{data[3]} {data[0]}")
            asset_balance.setStyleSheet(f"font-size: 14px; color: black; font-weight: bold;")
            asset_layout.addWidget(asset_balance)

            balance_usd = float(data[1]) * float(data[3])  # Calculating the USD value of the balance
            balance_usd_label = QLabel(f"${self.w3.w3U.custom_round(balance_usd)}")
            balance_usd_label.setStyleSheet("font-size: 14px; font-weight: bold; color: lightgray;")
            asset_layout.addWidget(balance_usd_label)
            layout.addWidget(asset_widget)


    def load_image(self, url, unique_identifier):
        request = QNetworkRequest(QUrl(url))
        reply = self.net_manager_Icons.get(request)
        reply.finished.connect(lambda:UIFunctions.on_finished(self, reply, unique_identifier))

    def on_finished(self, reply, unique_identifier):
        data = reply.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        if unique_identifier in self.icon_labels:
            label = self.icon_labels[unique_identifier]
            label.setPixmap(pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def populate_chain_combobox(self):
        chains = self.chain_instance.get_supported_chains()
        preferred_chain_id = self.settings.settings.get("cache:ChainID", None)
        preferred_chain_data = None
        for chain in chains:
            if chain["ChainID"] == preferred_chain_id:
                preferred_chain_data = chain
                break
        if preferred_chain_data:
            pixmap = QPixmap()
            pixmap.loadFromData(preferred_chain_data["LogoBase64"])
            icon = QIcon(pixmap)
            self.ui.comboBox_ChainID.addItem(preferred_chain_data["ShortName"], preferred_chain_data["ChainID"])
            self.ui.comboBox_ChainID.setItemIcon(0, icon)
        for chain in chains:
            if chain["ChainID"] != preferred_chain_id:
                pixmap = QPixmap()
                pixmap.loadFromData(chain["LogoBase64"])
                icon = QIcon(pixmap)
                self.ui.comboBox_ChainID.addItem(chain["ShortName"], chain["ChainID"])
                self.ui.comboBox_ChainID.setItemIcon(self.ui.comboBox_ChainID.count() - 1, icon)
        if preferred_chain_data:
            self.ui.comboBox_ChainID.setCurrentIndex(0)



    def show_incorrect_animation(self, component):
        original_geometry = component.geometry()
        original_style = component.styleSheet()
        animation = QPropertyAnimation(component, b"geometry")
        animation.setDuration(500) 
        movements = [-10, 10] * 5  
        num_moves = len(movements)
        for i, offset in enumerate(movements):
            step = (i + 1) / num_moves
            if step < 1.0: 
                new_rect = QRect(
                    original_geometry.x() + offset,
                    original_geometry.y(),
                    original_geometry.width(),
                    original_geometry.height()
                )
                animation.setKeyValueAt(step, new_rect)
        animation.setEndValue(original_geometry)
        component.setStyleSheet(component.styleSheet() + "border: 2px solid red;")
        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(animation)
        animation_group.start()
        def reset_style():
            component.setStyleSheet(original_style)
        QTimer.singleShot(3000, reset_style)
        self.animation_group = animation_group

    @staticmethod
    def show_popup(parent, message, color):
        if UIFunctions.popup is not None:
            UIFunctions.remove_popup()
        UIFunctions.popup = Popup(message, color, parent)
        orginal_style = UIFunctions.popup.styleSheet()
        UIFunctions.popup.setStyleSheet(orginal_style +"font-weight: bold;" )
        popup_x_center = (parent.width() - popup_width) // 2
        popup_y_center = (parent.height() - popup_height) // 2
        start_rect = QRect(popup_x_center, popup_y_center, popup_width, popup_height)
        UIFunctions.popup.setGeometry(start_rect)
        UIFunctions.popup.show()
        UIFunctions.animate_popup_in(UIFunctions.popup, parent)
        QTimer.singleShot(3000, UIFunctions.animate_popup_out)

    @staticmethod
    def animate_popup_in(widget, parent):
        if not widget.isVisible():
            widget.show()
        widget.raise_()
        UIFunctions.animation_in = QPropertyAnimation(widget, b"geometry")
        UIFunctions.animation_in.setDuration(600) 
        popup_width = widget.width()
        popup_height = widget.height()
        popup_x_center = (parent.width() - popup_width) // 2
        popup_y_center = (parent.height() - popup_height) // 2
        end_rect = QRect(popup_x_center, popup_y_center, popup_width, popup_height)
        start_rect = QRect(parent.width(), popup_y_center, popup_width, popup_height) 
        UIFunctions.animation_in.setStartValue(start_rect)
        UIFunctions.animation_in.setEndValue(end_rect)
        UIFunctions.animation_in.start()
        
    @staticmethod
    def animate_popup_out():
        if UIFunctions.popup:
            UIFunctions.animation_out = QPropertyAnimation(
                UIFunctions.popup, b"geometry"
            )
            UIFunctions.animation_out.setDuration(600)
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
        
        
        
class SvgSpinnerWidget(QWidget):
    def __init__(self, svg_data, parent=None):
        super().__init__(parent)
        self.renderer = QSvgRenderer(svg_data.encode('utf-8'))
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_rotation)
        self.timer.start(50)  # Animation speed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        transform = QTransform()
        transform.translate(self.width() / 2, self.height() / 2)
        transform.rotate(self.angle)
        transform.translate(-self.width() / 2, -self.height() / 2)
        painter.setTransform(transform)
        self.renderer.render(painter, QRect(0, 0, self.width(), self.height()))

    def update_rotation(self):
        self.angle = (self.angle + 10) % 360
        self.update()  # Triggers a repaint

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
