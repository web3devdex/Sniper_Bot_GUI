
from .imports import * 
from .libs.W3Utils import *
from .libs.IERC20 import *
from .libs.RixSwapOracle import *


class interfaceWeb3:
    
    def __init__(self, chain_mod, settings):
        self.settings = settings.settings
        try:
            self.address, self.key = self.settings["wallets"][0]["address"], self.settings["wallets"][0]["key"]
        except:
            self.address, self.key = None, None
            
        self.chain_mod = chain_mod
        self.initChain()
        self.initProvider()
        self.initWeb3()
        
        
    def initSettings(self, settings):
        self.settings = settings.settings
        
    def initWeb3(self):
        self.w3U = W3Utils(self.settings, self.w3)
        self.IERC20 = IERC20(self.address, self.key, self.settings, self.w3, None, self.w3U)
        self.RixSwapOracle = RixSwapOracle(self.address, self.key, self.settings, self.w3, self.IERC20, self.w3U, self.chain_mod)
        

    def setWallet(self, WalletIndex: int = 0):
        self.address, self.key = self.settings["wallets"][WalletIndex]["address"], self.settings["wallets"][WalletIndex]["key"]
        self.RixSwapOracle.setNewWallet(self.address, self.key)


    def initChain(self, ChainIndex: int = 0):
        self.CurrentProvider = self.chain_mod.get_supported_chains()
        self.ChainID = self.CurrentProvider[ChainIndex]["ChainID"]
        self.ProviderURI = self.CurrentProvider[ChainIndex]["RPC"]
        self.initProvider()
        return self.ChainID
        
    def initProvider(self):
        if self.ProviderURI[:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(self.ProviderURI, websocket_timeout=self.settings["timeout"]))
        else:
            w3 = Web3(Web3.HTTPProvider(self.ProviderURI,  request_kwargs={'timeout': self.settings["timeout"]}))
        self.w3 =  w3
        self.initWeb3()
    
    
    #SELL self.TokenSlot0 for self.TokenSlot1
    def initTokenSlot0(self, tokenAddress):
        self.IERC20 = IERC20(self.settings, self.w3, Web3.to_checksum_address(tokenAddress), self.w3U)
        self.TokenSlot0 = self.IERC20
        #print(self.Token0)