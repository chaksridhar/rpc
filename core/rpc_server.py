from common.Packers import *
from common import log
from typing import Callable
from typing import Type


class RpcServer():
    def __init__(self, *args, **kwargs):
        self.rpc_name_fxn_map: Dict[RpcFxnNameType, RpcFxnType] = {}

    def register_rpc_fxn(self, fxn_name: str, fxn: Callable):
        log.simple_log(f"Debug: Registered rpc_fxn {fxn_name}")
        self.rpc_name_fxn_map[fxn_name] = fxn

    def get_rpc_fxn(self, fxn_name: str) -> Callable:
        return self.rpc_name_fxn_map[fxn_name]

    def execute_payload(self, func_obj_in_bytes: bytes) -> bytes:
        [fxn_name, fxn_args] = PackerByte().unmarshall_func_object(func_obj_in_bytes)
        fxn = self.get_rpc_fxn(fxn_name)
        result = fxn(*fxn_args)
        return_desc: RpcReturnDesc = RpcReturnDesc()
        return_desc.result = result
        return_value_in_bytes = PackerByte().marshall_return_value(return_desc)
        return return_value_in_bytes


def callback_handler(rpc_server_obj: Type[RpcServer], packet: bytes) -> bytes:
    return rpc_server_obj.execute_payload(packet)
