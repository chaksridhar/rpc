from abstract_interface import irpc_client
from abstract_interface import irpc_client_xport
from common import Packers
from common import common_defs
from common import log
from typing import Type


class DreamRpcClient(irpc_client.IRpcClient):
    def __init__(self, i_rpc_xport_class: Type[irpc_client_xport.IRpcClientTransport], *args, **kwargs):
        super().__init__(i_rpc_xport_class, *args, **kwargs)

    def dispatch_payload(self, fxn_name: str, *args) -> common_defs.RpcReturnDesc:
        packer_byte = Packers.PackerByte()
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        fn_data_as_byte = packer_byte.marshall_func_object(fxn_name, arg_list)
        log.simple_log(f"DEBUG: in call calling the function with json as {fn_data_as_byte}")
        resp_as_bytes = self.rpc_client_xport.send_request(fn_data_as_byte)
        resp_as_return_type = packer_byte.unmarshall_return_value(resp_as_bytes)
        log.simple_log(resp_as_return_type)
        return resp_as_return_type
