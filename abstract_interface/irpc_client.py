from common.common_defs import *

from typing import Type
from abstract_interface import irpc_client_xport


# A Concrete imolemeentation will be provided for a specific protocol.
# The Call method  will marshall the parameters and  the methods in ipc_xport_class to sned hte data.
# The transport handles post me
class IRpcClient():
    def __init__(self, i_rpc_xport_class: Type[irpc_client_xport.IRpcClientTransport], *args, **kwargs):
        self.rpc_client_xport: irpc_client_xport.IRpcClientTransport = i_rpc_xport_class(*args, **kwargs)

    def dispatch_payload(self, fxn_name: str, *args) -> RpcReturnDesc:
        pass
