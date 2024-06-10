import json, os, sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QFileDialog

class initSettings:
    def __init__(self):
        self.settings = self.initSettingsFile()
        self.wallets = self.loadWallets()

    def initSettingsFile(self):
        if getattr(sys, 'frozen', False):
            self.application_path = os.path.dirname(sys.executable)
            self.settings_path = os.path.join(self.application_path, 'modules', 'pyRixSwapOracle', 'Settings.json')
        else:
            self.application_path = os.path.dirname(os.path.abspath(__file__))
            self.settings_path = os.path.join(self.application_path, 'Settings.json')
            
        if not os.path.isfile(self.settings_path):
            raise FileNotFoundError(f"No such file or directory: '{self.settings_path}'")
        with open(self.settings_path, 'r') as f:
            settings = json.load(f) 
        return settings
    
    def checkSettings(self):
        pass

    def updateSetting(self, setting, new_setting):
        self.settings[setting] = new_setting
        with open(self.settings_path, "w") as f:
            json.dump(self.settings, f)
            
        
    def loadWallets(self):
        return self.settings.get('wallets', [])

    def addWallet(self, name, address, private_key_hex):
        try:
            new_wallet = {
                "name": name,
                "address": address,
                "key": private_key_hex
            }
            self.wallets.append(new_wallet)
            self.updateSetting('wallets', self.wallets)
            return True
        except Exception as e:
            print(e)
            return False
        
            
            
    def backupSettings(self):
        filepath, _ = QFileDialog.getSaveFileName(
            None,
            "Save Settings File",
            os.path.expanduser("~"), 
            "JSON files (*.json)"
        )
        if filepath:
            try:
                with open(filepath, 'w') as file:
                    json.dump(self.settings, file, indent=4)
                return True
            except PermissionError:
                return False
        
