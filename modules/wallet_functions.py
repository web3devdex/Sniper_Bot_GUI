from mnemonic import Mnemonic
from bip44 import Wallet
from eth_account import Account
from gui import *


class WalletFunctions(QMainWindow):

    def create_new_wallet(self):
        mnemo = Mnemonic("english")
        mnemonic_phrase = mnemo.generate(strength=256)
        wallet = Wallet(mnemonic_phrase)
        private_key_bytes, _ = wallet.derive_account("eth") 
        eth_account = Account.from_key(private_key_bytes)
        return {"address": eth_account.address, "key": private_key_bytes.hex()}

    def isMnomic(self, input_string, language):
        if Mnemonic("english").check(input_string):
            return True
        try:
            Account.from_key(input_string)
            return False
        except ValueError:
            return None

    def import_wallet_from_private_key(self, private_key):
        account = Account.from_key(private_key)
        return {
            "address": account.address,
            "key": private_key,
        }

    def import_wallet_from_mnemonic(self, mnemonic, language):
        if not Mnemonic(language).check(mnemonic):
            return "Invalid mnemonic phrase"
        wallet = Wallet(mnemonic)
        private_key_bytes, _ = wallet.derive_account("eth") 
        eth_account = Account.from_key(private_key_bytes)
        return {
            "address": eth_account.address,
            "key": private_key_bytes.hex(),
        }
