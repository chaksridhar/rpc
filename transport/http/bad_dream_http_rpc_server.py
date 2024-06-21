
from http.server import BaseHTTPRequestHandler
from common import log
from typing import Callable

PacketHandlerCallback = Callable[[any, bytes], bytes]


class HttpServer(BaseHTTPRequestHandler):

    def __init__(self, packet_handler: PacketHandlerCallback, packet_handler_cookie: any, *args, **kwargs):
        print("calling BadDreamHttpRpcServerTransport")
        # self.partial_handle = functools.partial(BadDreamHttpRpcServerTransport, rpc_server_obj)
        self.packet_handler = packet_handler
        self.packet_handler_cookie = packet_handler_cookie
        print(kwargs)
        super().__init__(*args, **kwargs)

    def do_POST(self):
        log.simple_log("Entering doPost")
        length = int(self.headers.get('content-length'))
        packet: bytes = self.rfile.read(length)
        return_value = self.packet_handler(self.packet_handler_cookie, packet)

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
