import requests
from core import rpc_client
from common import log


class BadDreamHttpRpcClientTansport(rpc_client.IRpcClientTransport):
    def __init__(self, server_url: str):
        super().__init__(self, server_url)
        self.rpc_url = f'http://{server_url}'
        log.simple_log(f"Debug:Initialized  client with {self.rpc_url} ")

    def post_sync_request(self, data_in_bytes: bytes) -> bytes:
        resp_as_bytes = requests.post(self.rpc_url, data=data_in_bytes).content
        return resp_as_bytes


