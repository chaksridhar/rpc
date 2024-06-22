import requests
from common import log
from common import common_defs
from common import Packers
from abstract_interface import irpc_xport_adapter
from dream_rpc import dream_rpc_server


class DreamRpcServerAdapter(irpc_xport_adapter.IRpcServerTransportAdapter):
    def __init__(self, dream_rpc_server_obj: dream_rpc_server.RpcServer):
        self.rpc_server_obj = dream_rpc_server_obj
        super().__init__()

    def execute_fxn_payload(self, func_obj_in_bytes: bytes) -> bytes:
        [fxn_name, fxn_args] = Packers.PackerByte().unmarshall_func_object(func_obj_in_bytes)
        return_val = self.rpc_server_obj.execute_rpc_fxn(fxn_name, fxn_args)
        return_val_in_bytes: bytes = Packers.PackerByte().marshall_return_value(return_val)
        return return_val_in_bytes


class DreamRpcClientAdapter(irpc_xport_adapter.IRpcClientTransportAdapter):
    def __init__(self, server_url: str):
        super().__init__(self, server_url)
        self.rpc_url = f'http://{server_url}'
        log.simple_log(f"Debug:Initialized  client with {self.rpc_url} ")

    def execute_fxn_payload(self, fxn_name: str, fxn_arg_list:list) -> common_defs.RpcReturnDesc:
        fxn_obj_as_bytes = Packers.PackerByte().marshall_func_object(fxn_name, fxn_arg_list)
        resp_as_bytes: bytes = requests.post(self.rpc_url, data=fxn_obj_as_bytes).content
        return_val: common_defs.RpcReturnDesc = Packers.PackerByte().unmarshall_return_value(resp_as_bytes)
        return return_val
