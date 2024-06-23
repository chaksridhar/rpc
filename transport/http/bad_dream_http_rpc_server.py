from http.server import BaseHTTPRequestHandler
from common import log
from abstract_interface import irpc_xport_adapter
from typing import Type


class HttpServer(BaseHTTPRequestHandler):

    def __init__(self, rpc_xport_adapter_obj: Type[irpc_xport_adapter.IRpcServerTransportAdapter], *args, **kwargs):
        # self.partial_handle = functools.partial(BadDreamHttpRpcServerTransport, rpc_server_obj)
        self.rpc_xport_adapter: Type[irpc_xport_adapter.IRpcServerTransportAdapter] = rpc_xport_adapter_obj
        super().__init__(*args, **kwargs)

    def do_POST(self):
        log.simple_log("Entering doPost")
        length = int(self.headers.get('content-length'))
        packet: bytes = self.rfile.read(length)
        return_value = self.rpc_xport_adapter.execute_fxn_payload(packet)
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
