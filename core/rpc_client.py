from common.common_defs import *
from abc import ABC


class RpcClient(ABC):
    def __init__(self, server_url: str, rpc_port_name: str):
        self.server_url = server_url
        self.rpc_port_name = rpc_port_name

    def call(self, fxn_name: str, *args) -> RpcReturnDesc:
        pass
