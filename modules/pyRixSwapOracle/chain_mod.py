import json, requests, base64, sys, os
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, QBuffer

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None
    except Exception as e:
        print(e)
        return None

def download_image_as_base64(url) -> bytes:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image = QImage()
            image.loadFromData(response.content)
            buffer = QBuffer()
            buffer.open(QBuffer.ReadWrite)
            image.save(buffer, "PNG")
            base64_data = base64.b64encode(buffer.data()).decode()
            return base64_data
    except Exception as e:
        return None

class chain_mod:
    
    def __init__(self, chainID: int = 0):
        self.chainID = str(chainID)
        self.RixSwapOracle = None
        self.RixFeeUtils = None
        self.ZERO = "0x0000000000000000000000000000000000000000"  # This is constant across all chains
        self.WETH = None
        self.Name = None
        self.ShortName = None
        self.LogoURI = None
        self.RPC = None
        self.NativeName = None
        self.NativeSymbol = None
        self.config = None
        
        if getattr(sys, 'frozen', False):
            self.application_path = os.path.dirname(sys.executable)
            self.chain_conf_path = os.path.join(self.application_path, 'chain_config.json',)
        else:
            self.application_path = os.path.dirname(os.path.abspath(__file__))
            self.chain_conf_path = os.path.join(self.application_path, '..', '..', 'chain_config.json',)
        
        with open(self.chain_conf_path, 'r') as f:
            self.config = json.load(f)
        
        if self.chainID not in self.config:
            self.chainID = "56"  # Fallback to BSC
        
        self.initialize_chain(self.chainID)
        print(f"Connected to ChainID: {self.chainID}")

    def initialize_chain(self, chainID):
        chain_config = self.config.get(chainID)
        if not chain_config:
            raise SystemExit("ChainID not Supported!")
        self.RixSwapOracle = chain_config.get("RixSwapOracle")
        self.WETH = chain_config.get("WETH")
        self.RPC = chain_config.get("RPC")
        self.Name = chain_config.get("Name")
        self.ShortName = chain_config.get("ShortName")
        self.LogoURI = chain_config.get("LogoURI")
        self.NativeName = chain_config.get("NativeName")
        self.NativeSymbol = chain_config.get("NativeSymbol")

    def get_supported_chains(self):
        chains = []
        for chain_id, chain_info in self.config.items():
            chains.append({
                "ChainID": chain_id,
                "Name": chain_info["Name"],
                "ShortName": chain_info["ShortName"],
                "LogoURI": chain_info["LogoURI"],
                "LogoBase64": download_image(chain_info["LogoURI"]),
                "RPC": chain_info["RPC"],
                "NativeName": chain_info["NativeName"],
                "NativeSymbol": chain_info["NativeSymbol"]
            })
        return chains

    def save_new_rpc(self, chainID, rpc_url):
        chainID = str(chainID)
        if chainID in self.config:
            self.config[chainID]['RPC'] = rpc_url
            with open('chain_config.json', 'w') as f:
                json.dump(self.config, f, indent=4)
            print(f"RPC URL for ChainID {chainID} has been updated to {rpc_url}")
            self.initialize_chain(chainID)
        else:
            raise ValueError(f"ChainID {chainID} not found in the configuration. New entries are not allowed.")
