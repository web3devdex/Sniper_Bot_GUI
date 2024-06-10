from PySide6.QtCore import QObject
from mnemonic import Mnemonic
from eth_account import Account
import qrcode
from PIL import Image, ImageQt
from gui import *
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask

default_language = "english" #Change here your Wallet Mnomic language!
Account.enable_unaudited_hdwallet_features()

def genQrImage(data):
    size = 250
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(
                        image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer(),
                        eye_drawer=RoundedModuleDrawer(),
                        color_mask=SolidFillColorMask(back_color=(63, 73, 105), front_color=(0, 0, 0)),
                        )
    img = img.resize((size, size), Image.LANCZOS)
    return img


class WalletFunctions(QMainWindow):

    def setWalletQR(self, address):
        qrcode_image = genQrImage(address)
        qr_img_pixmap = QPixmap.fromImage(ImageQt.ImageQt(qrcode_image))
        self.ui.label_qr_address.setPixmap(qr_img_pixmap)
        
    def create_new_wallet(language: str = default_language):
        mnemo = Mnemonic(language)
        mnemonic_phrase = mnemo.generate(strength=256)
        account = Account.from_mnemonic(mnemonic_phrase)
        return {"address": account.address, "key": account.key.hex()}

    def isMnemonic(self, input_string, language: str = default_language):
        mnemo = Mnemonic(language)
        print(input_string)
        print(mnemo.check(input_string))
        if mnemo.check(input_string):
            return True
        try:
            Account.from_key(input_string)
            return False
        except Exception as e:
            print(e)
            return None

    def import_wallet_from_private_key(private_key):
        account = Account.from_key(private_key)
        return {
            "address": account.address,
            "key": private_key,
        }

    def import_wallet_from_mnemonic(mnemonic, language: str = default_language):
        if not Mnemonic(language).check(mnemonic):
            return "Invalid mnemonic phrase"
        account = Account.from_mnemonic(mnemonic)  # Uses mnemonic to create account
        print(account)
        return {
            "address": account.address,
            "key": account.key,
        }
