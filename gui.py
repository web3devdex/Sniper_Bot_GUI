import sys, os

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
        self.settings = initSettings()
        self.encryption = Encryption()
        print(self.settings.settings)
        self.chain_instance = chain_mod(self.settings.settings["cache:ChainID"])
        self.WF = WalletFunctions(self)
        self.w3 = interfaceWeb3(self.chain_instance, self.settings)
        self.setup_ui()
        UIFunctions.removeTitleBar(True)
        self.setWindowTitle(WindowTitle)
        UIFunctions.labelTitle(self, WindowTitle)
        UIFunctions.labelDescription(self, '')
        self.ui.label_version.setText(version)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)


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



    def setup_ui(self):
        UIFunctions.populate_chain_combobox(self)
        UIFunctions.connectButtons(self)
        self.ui.lineEdit_UnlockPwd.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_UnlockPwd.setPlaceholderText("Enter your password")
        self.ui.lineEdit_create_password.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_repeat_password.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_create_password.setPlaceholderText("Enter Password")
        self.ui.lineEdit_repeat_password.setPlaceholderText("Repeat Password")
        self.unlockPage()
        
        
    def unlockPage(self):
        self.settings.initSettingsFile()
        if str(self.settings.settings["cache:refferenceHash"]) == "":
            self.ui.button_createPW.show()
        else:
            self.ui.button_createPW.hide()
        if str(self.settings.settings["cache:refferenceHash"]) == "":
            self.ui.button_resetPW.hide()
        else:
            self.ui.button_resetPW.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        UIFunctions.labelPage(self, "Unlock Wallet")
            
        
        

                

    def unlockWallet(self):
        if UIFunctions.verify_password(self, self.ui.lineEdit_UnlockPwd.text()):
            self.Login()
            UIFunctions.show_popup(self.ui.frame_popup, "Welcome! ", "green")


    def Login(self):
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Wallet", "menu_btn_wallet", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Swap", "menu_btn_swap", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Sniper", "menu_btn_sniper", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Stake", "menu_btn_stake", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Preferences", "menu_btn_preferences", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        UIFunctions.selectStandardMenu(self, "menu_btn_wallet")
        UIFunctions.labelPage(self, "Wallet")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_wallet)
        

    def Button(self):
        btnWidget = self.sender()
        if btnWidget.objectName() != None:
            print(btnWidget.objectName())
            pass

        
        #MENU BUTTONS
        if btnWidget.objectName() == "menu_btn_wallet":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_wallet)
            UIFunctions.resetStyle(self, "menu_btn_wallet")
            UIFunctions.labelPage(self, "Wallet")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "menu_btn_swap":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_wallet)
            UIFunctions.resetStyle(self, "menu_btn_swap")
            UIFunctions.labelPage(self, "Swap Tokens")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == "menu_btn_sniper":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "menu_btn_preferences")
            UIFunctions.labelPage(self, "Snip Token Launche")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            


            
            
        #UNLOCKPAGE BUTTONS
        if btnWidget.objectName() == "button_createPW":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_password)
            UIFunctions.labelPage(self, "Create Password")    
            self.ui.lineEdit_create_password.clear()
            self.ui.lineEdit_repeat_password.clear()
        if (btnWidget.objectName() == "button_create_password_cancel" 
            or btnWidget.objectName() == "button_reset_password_cancel" 
            or btnWidget.objectName() == "button_reset_password_submit_reset"
            ):
            self.unlockPage()
        if btnWidget.objectName() == "button_reset_password_submit":
            self.ui.widget_confirm.show()
            self.ui.widget_Reset.hide()            
        if btnWidget.objectName() == "button_resetPW":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_reset_password)
            UIFunctions.labelPage(self, "Reset Password")
            self.ui.widget_confirm.hide()
            self.ui.widget_Reset.show()
        if btnWidget.objectName() == "button_create_password_submit":
            UIFunctions.createPassword(self, self.ui.lineEdit_create_password.text(), self.ui.lineEdit_repeat_password.text())

        
        if btnWidget.objectName() == "button_reset_password_submit_go":
            self.settings.backupSettings()
            self.settings.updateSetting("cache:refferenceHash", "")
            self.settings.updateSetting("wallets", [{}])
            UIFunctions.show_popup(self.ui.frame_popup, "Backup Saved @ Documents", "green")
            self.unlockPage()
            
            
            
            
        #WALLETPAGE BUTTONS
        if btnWidget.objectName() == "pushButton_add_wallet":
            UIFunctions.labelPage(self, "Add Wallet")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_wallet)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page)
        
        if btnWidget.objectName() == "button_import_wallet":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_import_wallet_name)
                        
        if btnWidget.objectName() == "button_create_new_wallet":
            self.EncryptedWallet, status = self.newWallet()
            if status:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_import_wallet_name)
            
        
        if btnWidget.objectName() == "button_import_wallet_key":
            self.EncryptedWallet, status = self.importWallet()
            if status:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_import_wallet_name)
              
              
        if btnWidget.objectName() == "button_add_wallet_done":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_wallet)        
            
            
              

        if btnWidget.objectName() == "button_add_wallet_cancel":
            UIFunctions.labelPage(self, "Wallet")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_wallet)
        



        #comboboxes
        if btnWidget.objectName() == "comboBox_ChainID":
            ChainID = self.w3.initChain(self.ui.comboBox_ChainID.currentIndex())
            print(ChainID)
            self.settings.updateSetting("cache:ChainID", ChainID)
            
            
    def newWallet(self):
        try:
            json_account = self.WF.create_new_wallet()
            address = json_account["address"]
            priv_key =self.encryption.encrypt(json_account["key"], self.encryption.masterkey)
            del json_account
            return  {
                "name": "NotJetSet",
                "address": address,
                "key": priv_key
            }, True
        except Exception as e:
            UIFunctions.show_popup(self.ui.frame_popup, "Cant generate private key")
            return {}, False
        
    def importWallet(self):
        isMnomic = self.WF.isMnomic(self.ui.plainTextEdit_import_wallet_priv.text())
        if isMnomic:
            try:
                json_account = self.WF.import_wallet_from_mnemonic(self.ui.plainTextEdit_import_wallet_priv.text())
            except:
                UIFunctions.show_popup(self.ui.frame_popup, "Mnomic is invalid")
                UIFunctions.show_incorrect_animation(self, self.ui.plainTextEdit_import_wallet_priv)
                return {}, False
        else:
            try:
                json_account = self.WF.import_wallet_from_private_key(self.ui.plainTextEdit_import_wallet_priv.text())
            except:
                UIFunctions.show_popup(self.ui.frame_popup, "Private key is invalid")
                UIFunctions.show_incorrect_animation(self, self.ui.plainTextEdit_import_wallet_priv)
                return {}, False
        address = json_account["address"]
        priv_key =self.encryption.encrypt(json_account["key"], self.encryption.masterkey)
        del json_account
        return {
            "name": "NotJetSet",
            "address": address,
            "key": priv_key
        }, True
        
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
        print(f"Version: {version}")
    else: 
        print("Running GUI")
        app = QApplication(sys.argv)
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
        window = MainWindow()
        sys.exit(app.exec())
