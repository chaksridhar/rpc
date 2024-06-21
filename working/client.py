import requests
from Packers import *
from common_defs import *
import Packers


class RpcClientHttpJson:
    def __init__(self, server_url: str, rpc_port_name: str):
        self.server_url = server_url
        self.rpc_port_name = rpc_port_name
        self.rpc_url = f'http://{server_url}/{rpc_port_name}'
        print(f"Debug:Initialized  client with {self.rpc_url} ")

    def call(self, fxn_name: str, *args) -> RpcReturnDesc:
        packer_byte = Packers.PackerByte()
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        fn_data_as_byte = packer_byte.marshall_func_object(fxn_name, arg_list)
        print(f"DEBUG: in call calling the function with json as {fn_data_as_byte}")
        resp_as_bytes = requests.post(self.rpc_url, data=fn_data_as_byte).content
        resp_as_return_type = packer_byte.unmarshall_return_value(resp_as_bytes)
        print(resp_as_return_type)
        return resp_as_return_type


if __name__ == "__main__":
    rpc_client = RpcClientHttpJson("localhost:8000", "RPC0")
    response = rpc_client.call("add", 1, 2)
    print(f"Final {response}")
