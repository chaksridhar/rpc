from abc import ABC
from typing import Dict
from common.common_defs import *
from common import  log


class PortServer(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def payload_handler(self, transport_layer_hdl: any):
        pass


class RpcServer(PortServer, ABC):

    def __init__(self, port_name: str):
        self.port_name = port_name
        self.rpc_name_fxn_map: Dict[RpcFxnNameType, RpcFxnType] = {}
        super().__init__(port_name)

    def register_rpc_fxn(self, fxn_name: str, fxn: Callable):
        log.simple_log(f"Debug: Registered rpc_fxn {fxn_name}")
        self.rpc_name_fxn_map[fxn_name] = fxn

    def get_rpc_fxn(self, fxn_name: str) -> Callable:
        return self.rpc_name_fxn_map[fxn_name]
