from ..imports import *

class RixSwapOracle:
    def __init__(self, address, key, settings, w3, IERC20, w3U, chain_mod):
        self.user_address, self.priv_key = address, key
        self.settings, self.w3, self.IERC20, self.w3U = settings, w3, IERC20, w3U
        self.constants = chain_mod
        self.RixSwapOracle = self.initRouter()

    def setNewWallet(self, address, key):
        self.user_address, self.priv_key = address, key
        
    def initRouter(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
            RixSwapOracleABI_path = os.path.join(application_path, "ABIS", "RixSwapOracleV1.json")
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
            RixSwapOracleABI_path = os.path.join(application_path, "..", "..", "..", "ABIS", "RixSwapOracleV1.json")   
                     
        with open(RixSwapOracleABI_path) as f:
            contract_abi = json.load(f)
        RixSwapOracle = self.w3.eth.contract(
            address=self.constants.RixSwapOracle, abi=contract_abi)
        return RixSwapOracle
    
    def getAmountsOutV3(self, pools, path, amountIn):
        return self.RixSwapOracle.functions.getAmountsOutV3(
            pools, path, amountIn
            ).call()
    
    def getAmountsOutV2(self, amountIn, path, dexPath):
        return self.RixSwapOracle.functions.getAmountsOutV2(
            amountIn, path, dexPath
            ).call()
    
    def getUSDPrice(self):
        return self.RixSwapOracle.functions.getUSDPrice(
            self.IERC20.get_token_address()
            ).call()
    
    def getProtocollVersion(self):
        return self.RixSwapOracle.functions.getSwapPathV3(self.constants.WETH, self.IERC20.get_token_address()).call()

    def getTokenInfos(self):
        function_signature = self.RixSwapOracle.encodeABI(fn_name="getTokenInfos", args=[self.IERC20.get_token_address()])
        data = {
            "to": self.RixSwapOracle.address,
            "data": function_signature,
            "from": self.constants.ZERO
        }
        
        _data = self.w3.eth.call(data)
        call = abi.decode(
            ['uint256', 'uint256', 'uint256', 'uint256', 'bool', 'bool', 'bool', 'bool', 'string'],
            _data
        )
        buy_tax = round(
            ((call[0] - call[1]) / (call[0]) * 100) - 0.77, 3)
        sell_tax = round(
            ((call[2] - call[3]) / (call[2]) * 100) - 0.77, 3)

        if call[4] and call[5] and call[6] and call[7] == True:
            honeypot = False
        else:
            honeypot = True
        return buy_tax, sell_tax, honeypot
    
    def getWalletTokenDATA(self, tokenList):
        tokenList = [Web3.to_checksum_address(address) for address in tokenList]
        tokenBalances ,tokenDecimals ,tokenPrice ,tokensVersion ,tokenAddress = self.RixSwapOracle.functions.getWalletTokenDATA(self.user_address, tokenList).call()
        print(tokenBalances ,tokenDecimals ,tokenPrice ,tokensVersion ,tokenAddress)
        return tokenBalances ,tokenDecimals ,tokenPrice ,tokensVersion ,tokenAddress

    def getETHtoTokenVersion(self):
        return self.RixSwapOracle.functions.checkVersion(self.constants.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHVersion(self):
        return self.RixSwapOracle.functions.checkVersion(self.IERC20.get_token_address(), self.constants.WETH).call()
        
    def getTokentoTokenVersion(self, tokenIn, tokenOut):
        return self.RixSwapOracle.functions.checkVersion(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    def getETHtoTokenPathV3(self):
        return self.RixSwapOracle.functions.getSwapPathV3(self.constants.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHPathV3(self):
        return self.RixSwapOracle.functions.getSwapPathV3(self.IERC20.get_token_address(),self.constants.WETH).call()
        
    def getTokentoTokenPathV3(self, tokenIn, tokenOut):
        print("getTokentoTokenPathV3:tokenIn,tokenOut",tokenIn, tokenOut)
        return self.RixSwapOracle.functions.getSwapPathV3(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    def getETHtoTokenPathV2(self):
        return self.RixSwapOracle.functions.getSwapPathV2(self.constants.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHPathV2(self):
        return self.RixSwapOracle.functions.getSwapPathV2(self.IERC20.get_token_address(),self.constants.WETH).call()
        
    def getTokentoTokenPathV2(self, tokenIn, tokenOut):
        return self.RixSwapOracle.functions.getSwapPathV2(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    def SwapFromETHtoTokenV3(self, inputAmount: int, trys: int = 1):
        while trys:
            try:
                path, dexIdents, pools, poolFees = self.getETHtoTokenPathV3()
                print("getETHtoTokenPathV3:path, dexIdents, pools, poolFees",path, dexIdents, pools, poolFees )
                amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
                minOutput = int(amountOut - (amountOut * self.settings.settings["Slippage"]) / 100)
                txn = self.RixSwapOracle.functions.swapETHtoTokenV3(
                    path,
                    pools,
                    poolFees,
                    minOutput
                ).build_transaction(
                    {'from': self.user_address,
                     'gasPrice': int(self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"], "ether")),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': int(inputAmount)}
                )
                txn.update({'gas': int(self.w3U.estimateGas(txn))})
                signed_txn = self.w3.eth.account.sign_transaction(
                    txn,
                    self.priv_key
                )
                txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                    txn, timeout=self.settings.settings["timeout"])
                if txn_receipt["status"] == 1:
                    return True, txn.hex()
                else:
                    return False, txn.hex()
                
            except Exception as e:
                print(e)
                trys -= 1
                print("SwapFromETHtoTokenV3 Failed!")
                time.sleep(1)


    def SwapFromTokentoETHV3(self, inputAmount: int, trys: int = 1):
        while trys:
            try:
                path, _, pools, poolFees = self.getTokentoETHPathV3()
                amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
                amountOutMinimum = int(amountOut - (amountOut * self.settings.settings["Slippage"]) / 100)
                txn = self.RixSwapOracle.functions.swapTokenToETHV3(
                    path,
                    pools,
                    poolFees,
                    inputAmount,
                    amountOutMinimum
                ).build_transaction(
                    {'from': self.user_address,
                     'gasPrice': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"],"ether"),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': 0
                     }
                )
                txn.update({'gas': int(self.w3U.estimateGas(txn))})
                signed_txn = self.w3.eth.account.sign_transaction(
                    txn,
                    self.priv_key
                )
                txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                    txn, timeout=self.settings.settings["timeout"])
                if txn_receipt["status"] == 1:
                    return True, txn.hex()
                else:
                    return False, txn.hex()

            except Exception as e:
                print(e)
                trys -= 1
                print("SwapFromTokentoETHV3 Failed!")
                time.sleep(1)


    def SwapFromTokentoTokenV3(self, tokenIn, tokenOut, inputAmount: int, trys: int = 1):
        while trys:
            path, dexIdents, pools, poolFees = self.getTokentoTokenPathV3(tokenIn, tokenOut)
            amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
            amountOutMinimum = int(amountOut - (amountOut * self.settings.settings["Slippage"]) / 100)
            try:
                txn = self.RixSwapOracle.functions.swapTokentoTokenV3(
                    path,
                    pools,
                    poolFees,
                    inputAmount,
                    amountOutMinimum
                ).build_transaction(
                    {'from': self.user_address,
                     'gasPrice': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"],"ether"),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': 0}
                )
                txn.update({'gas': int(self.w3U.estimateGas(txn))})
                signed_txn = self.w3.eth.account.sign_transaction(
                    txn,
                    self.priv_key
                )
                txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                    txn, timeout=self.settings.settings["timeout"])
                if txn_receipt["status"] == 1:
                    return True, txn.hex()
                else:
                    return False, txn.hex()
            except Exception as e:
                print(e)
                trys -= 1
                print("SwapFromTokentoTokenV3 Failed!")
                time.sleep(1)
    
    def SwapFromETHtoTokenV2(self, inputAmount: int, trys: int = 1):
        while trys:
            try:
                path, dexIdents  = self.getETHtoTokenPathV2()
                amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
                amountOutMinimum = int(amountOut - (amountOut * self.settings.settings["Slippage"]) / 100)
                txn = self.RixSwapOracle.functions.swapETHtoTokenV2(
                    path,
                    dexIdents,
                    amountOutMinimum
                ).build_transaction(
                    {'from': self.user_address,
                     'gasPrice': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"],"ether"),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': int(inputAmount)}
                )
                txn.update({'gas': int(self.w3U.estimateGas(txn))})
                signed_txn = self.w3.eth.account.sign_transaction(
                    txn,
                    self.priv_key
                )
                txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                    txn, timeout=self.settings.settings["timeout"])
                if txn_receipt["status"] == 1:
                    return True, txn.hex()
                else:
                    return False, txn.hex()
                
            except Exception as e:
                print(e)
                trys -= 1
                print("SwapFromETHtoTokenV2 Failed!")
                time.sleep(1)


    def SwapFromTokentoETHV2(self, inputAmount: int, trys: int = 1):
        while trys:
            try:
                path, dexIdents = self.getTokentoETHPathV2()
                amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
                amountOutMinimum = int(amountOut - (amountOut * self.settings.settings["Slippage"]) / 100)
                txn = self.RixSwapOracle.functions.swapTokentoETHV2(
                    path,
                    dexIdents,
                    inputAmount,
                    amountOutMinimum
                ).build_transaction(
                    {'from': self.user_address,
                     'gasPrice': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"],"ether"),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': 0}
                )
                txn.update({'gas': int(self.w3U.estimateGas(txn))})
                signed_txn = self.w3.eth.account.sign_transaction(
                    txn,
                    self.priv_key
                )
                txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                    txn, timeout=self.settings.settings["timeout"])
                if txn_receipt["status"] == 1:
                    return True, txn.hex()
                else:
                    return False, txn.hex()

            except Exception as e:
                print(e)
                trys -= 1
                print("SwapFromTokentoETHV2 Failed!")
                time.sleep(1)


    def SwapFromTokentoTokenV2(self, tokenIn, tokenOut, inputAmount: int, trys: int = 1):
        while trys:
            path, dexIdents = self.getTokentoTokenPathV2(tokenIn, tokenOut)
            amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
            amountOutMinimum = int(amountOut - (amountOut * self.settings.settings["Slippage"]) / 100)
            try:
                txn = self.RixSwapOracle.functions.swapTokentoTokenV2(
                    path,
                    dexIdents,
                    inputAmount,
                    amountOutMinimum
                ).build_transaction(
                    {'from': self.user_address,
                     'gasPrice': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"],"ether"),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': 0}
                )
                txn.update({'gas': int(self.w3U.estimateGas(txn))})
                signed_txn = self.w3.eth.account.sign_transaction(
                    txn,
                    self.priv_key
                )
                txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                    txn, timeout=self.settings.settings["timeout"])
                if txn_receipt["status"] == 1:
                    return True, txn.hex()
                else:
                    return False, txn.hex()
            except Exception as e:
                print(e)
                trys -= 1
                print("SwapFromTokentoTokenV2 Failed!")
                time.sleep(1)