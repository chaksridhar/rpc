from common.common_defs import *
from abc import ABC
from common import log
from common import Packers

from typing import Type


class IRpcClientTransport(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def post_sync_request(self, data_in_bytes: bytes) -> bytes:
        pass


class RpcClient():
    def __init__(self, i_rpc_xport_class: Type[IRpcClientTransport], *args, **kwargs):
        self.rpc_client_xport: IRpcClientTransport = i_rpc_xport_class(*args, **kwargs)

    def call(self, fxn_name: str, *args) -> RpcReturnDesc:
        packer_byte = Packers.PackerByte()
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        fn_data_as_byte = packer_byte.marshall_func_object(fxn_name, arg_list)
        log.simple_log(f"DEBUG: in call calling the function with json as {fn_data_as_byte}")
        resp_as_bytes = self.rpc_client_xport.post_sync_request(fn_data_as_byte)
        resp_as_return_type = packer_byte.unmarshall_return_value(resp_as_bytes)
        log.simple_log(resp_as_return_type)
        return resp_as_return_type
