from typing import Type
from dream_rpc import  dream_rpc_server

def  dream_rpc_server_adapter (rpc_server_obj: Type[dream_rpc_server.RpcServer],
                                              packet: bytes) -> bytes:
    return rpc_server_obj.execute_rpc_fxn(packet)
