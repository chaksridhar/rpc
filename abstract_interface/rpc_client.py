from common.common_defs import *
from abc import ABC


from typing import Type


class IRpcClientTransport(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def post_sync_request(self, data_in_bytes: bytes) -> bytes:
        pass

class IRpcClient():
    def __init__(self, i_rpc_xport_class: Type[IRpcClientTransport], *args, **kwargs):
        self.rpc_client_xport: IRpcClientTransport = i_rpc_xport_class(*args, **kwargs)

    def call(self, fxn_name: str, *args) -> RpcReturnDesc:
       pass

