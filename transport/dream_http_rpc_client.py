import requests
from common import Packers
from common.common_defs import *
from core import rpc_client
from common import log


class DreamRpcHttpClient(rpc_client.RpcClient):
    def __init__(self, server_url: str, rpc_port_name: str):
        super().__init__(server_url,rpc_port_name)
        self.rpc_url = f'http://{server_url}/{rpc_port_name}'
        log.simple_log(f"Debug:Initialized  client with {self.rpc_url} ")

    def call(self, fxn_name: str, *args) -> RpcReturnDesc:
        packer_byte = Packers.PackerByte()
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        fn_data_as_byte = packer_byte.marshall_func_object(fxn_name, arg_list)
        log.simple_log(f"DEBUG: in call calling the function with json as {fn_data_as_byte}")
        resp_as_bytes = requests.post(self.rpc_url, data=fn_data_as_byte).content
        resp_as_return_type = packer_byte.unmarshall_return_value(resp_as_bytes)
        log.simple_log(resp_as_return_type)
        return resp_as_return_type


if __name__ == "__main__":
    rpc_client = DreamRpcHttpClient("localhost:8000", "RPC0")
    response = rpc_client.call("add", 1, 2)
    log.simple_log(f"Final {response}")
    response = rpc_client.call("hello", "hello world")
    log.simple_log(f"Final {response}")
