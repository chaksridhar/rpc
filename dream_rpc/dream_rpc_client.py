from abstract_interface import irpc_client
from abstract_interface import irpc_xport_adapter
from common import Packers
from common import common_defs
from common import log
from typing import Type


class DreamRpcClient(irpc_client.IRpcClient):
    def __init__(self, i_rpc_xport_class_adapter: Type[irpc_xport_adapter.IRpcClientTransportAdapter], *args, **kwargs):
        super().__init__(i_rpc_xport_class_adapter, *args, **kwargs)

    def dispatch_payload(self, fxn_name: str, *args) -> common_defs.RpcReturnDesc:
        packer_byte = Packers.PackerByte()
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        resp_as_return_type= self.rpc_client_xport_adapter.execute_fxn_payload(fxn_name,arg_list)
        log.simple_log(resp_as_return_type)
        return resp_as_return_type
