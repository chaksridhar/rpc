from common.common_defs import *

from typing import Type
from abstract_interface import irpc_xport_adapter


# A Concrete imolemeentation will be provided for a specific protocol.
# The Call method  will marshall the parameters and  the methods in ipc_xport_class to sned hte data.
# The transport handles post me
class IRpcClient():
    def __init__(self, i_rpc_xport_class_adapter: Type[irpc_xport_adapter.IRpcClientTransportAdapter], *args, **kwargs):
        self.rpc_client_xport_adapter: irpc_xport_adapter.IRpcClientTransportAdapter = i_rpc_xport_class_adapter(*args, **kwargs)

    def dispatch_payload(self, fxn_name: str, *args) -> RpcReturnDesc:
        pass
