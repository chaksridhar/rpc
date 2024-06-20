from core import rpc_server
from http.server import BaseHTTPRequestHandler
import functools
from common import log
from typing import Callable

PacketHandlerCallback = Callable[[any, bytes], bytes]


class BadDreamHttpRpcServerTransport(BaseHTTPRequestHandler):

    def __init__(self, call_back_fxn: PacketHandlerCallback, fxn_cookie: any, *args, **kwargs):
        print("calling BadDreamHttpRpcServerTransport")
        # self.partial_handle = functools.partial(BadDreamHttpRpcServerTransport, rpc_server_obj)
        self.call_back_fxn = call_back_fxn
        self.call_back_fxn_cookie = fxn_cookie
        print(kwargs)
        super().__init__(*args, **kwargs)

    def do_POST(self):
        log.simple_log("Entering doPost")
        length = int(self.headers.get('content-length'))
        payload: bytes = self.rfile.read(length)
        print(f"payload = {payload}")
        return_value = self.call_back_fxn(self.call_back_fxn_cookie, payload)

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
