from core import rpc_server
from http.server import BaseHTTPRequestHandler
import functools
from common import log


class BadDreamHttpRpcServerTransport(BaseHTTPRequestHandler):

    def __init__(self, rpc_server_obj: rpc_server.RpcServer, *args, **kwargs):
        print("calling BadDreamHttpRpcServerTransport")
        self.partial_handle = functools.partial(BadDreamHttpRpcServerTransport, rpc_server_obj)
        self.rpc_server_obj = rpc_server_obj
        print(kwargs)
        super().__init__(*args, **kwargs)

    def do_POST(self):
        log.simple_log("Entering doPost")
        length = int(self.headers.get('content-length'))
        payload: bytes = self.rfile.read(length)
        print(f"payload = {payload}")
        return_value = self.rpc_server_obj.execute_payload(payload)

        self.send_response(200)
        self.send_header('Content-type', 'application/text')
        self.end_headers()
        self.wfile.write(return_value)
        return

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        self.wfile.write('{!r}\n'
                         .format("Server up")
                         .encode('utf8'))
