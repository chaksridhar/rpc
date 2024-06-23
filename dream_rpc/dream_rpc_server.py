
from common.Packers import *
from common import log
from typing import Callable
from abstract_interface import irpc_server


class  RpcServer(irpc_server.IRpcServer):
    def __init__(self, *args, **kwargs):
        self.rpc_name_fxn_map: Dict[RpcFxnNameType, RpcFxnType] = {}
        super().__init__(*args, **kwargs)

    def register_rpc_fxn(self, fxn_name: str, fxn: Callable):
        log.simple_log(f"Debug: Registered rpc_fxn {fxn_name}")
        self.rpc_name_fxn_map[fxn_name] = fxn

    def get_rpc_fxn(self, fxn_name: str) -> Callable:
        return self.rpc_name_fxn_map[fxn_name]

    def execute_rpc_fxn(self, fxn_name:str, fxn_args:list ) -> RpcReturnDesc:
        return_desc: RpcReturnDesc = RpcReturnDesc()
        try:
            fxn = self.get_rpc_fxn(fxn_name)
            result = fxn(*fxn_args)
            return_desc.result = result
        except Exception as e:
            return_desc.status=False
            return_desc.error_msg = e.__str__()
        return return_desc



