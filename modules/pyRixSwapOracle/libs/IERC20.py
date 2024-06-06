from ..imports import *
from typing import Optional, Union

class IERC20:
    def __init__(self, address: str, key: str, settings: dict, w3: Web3, token: Optional[str], w3U: any):
        script_path = os.path.abspath(__file__)
        self.dir = os.path.dirname(script_path)
        self.user_address = address
        self.priv_key = key
        self.settings = settings
        self.w3 = w3
        self.token = token
        self.w3U = w3U
        self.token_Instance = self.init_token_instance() if token else None

    def get_raw_ETH_balance(self) -> int:
        return self.w3.eth.get_balance(self.user_address)

    def get_ETH_balance(self) -> float:
        balance_wei = self.w3.eth.get_balance(self.user_address)
        return Web3.from_wei(balance_wei, "ether")

    def init_token_instance(self):
        if not self.token:
            return None
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
            IERC20_abi_path = os.path.join(application_path, "ABIS", "IERC20.json")
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
            IERC20_abi_path = os.path.join(application_path,"..", "..", "..", "ABIS", "IERC20.json")
        with open(IERC20_abi_path) as f:
            IERC20_abi = json.load(f)
        token_Instance = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.token), abi=IERC20_abi
        )
        return token_Instance

    def get_token_address(self) -> Optional[str]:
        if self.token_Instance:
            return Web3.to_checksum_address(self.token_Instance.address)
        return None

    def get_token_decimals(self) -> Optional[int]:
        if self.token_Instance:
            return self.token_Instance.functions.decimals().call()
        return None

    def get_token_Name(self) -> Optional[str]:
        if self.token_Instance:
            return self.token_Instance.functions.name().call()
        return None

    def get_token_Symbol(self) -> Optional[str]:
        if self.token_Instance:
            return self.token_Instance.functions.symbol().call()
        return None

    def get_token_balance(self, address: str) -> Optional[int]:
        if self.token_Instance:
            return self.token_Instance.functions.balanceOf(
                Web3.to_checksum_address(address)
            ).call()
        return None

    def get_token_allowance(self, spender: str) -> Optional[int]:
        if self.token_Instance:
            return self.token_Instance.functions.allowance(
                self.user_address, spender
            ).call()
        return None

    def is_approved(self, spender: str, amountIn: int) -> bool:
        if not self.token_Instance:
            return False
        allowance = self.get_token_allowance(spender)
        if int(allowance) <= int(amountIn):
            return False
        else:
            return True

    def approve(self, spender: str, amountIn: int) -> Optional[tuple[bool, str]]:
        if self.token_Instance and not self.is_approved(spender, amountIn):
            txn = self.token_Instance.functions.approve(
                Web3.to_checksum_address(spender), 2**256 - 1
            ).build_transaction(
                {
                    "from": self.user_address,
                    "gasPrice": self.w3.eth.gas_price
                    + Web3.to_wei(self.settings["GWEI_OFFSET"], "gwei"),
                    "nonce": self.w3.eth.get_transaction_count(self.user_address),
                    "value": 0,
                }
            )
            txn.update({"gas": int(self.w3U.estimateGas(txn))})
            signed_txn = self.w3.eth.account.sign_transaction(txn, self.priv_key)
            txn_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn_hash, timeout=self.settings["timeout"]
            )
            if txn_receipt["status"] == 1:
                return True, txn_hash.hex()
            else:
                return False, txn_hash.hex()
        return None