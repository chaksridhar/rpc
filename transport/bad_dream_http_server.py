from typing import List
from core import rpc_server
from http.server import BaseHTTPRequestHandler
from typing import Dict

from common import log

class BadDreamHttpHandler(BaseHTTPRequestHandler):

    def __init__(self, port_server_map_list: List[rpc_server.PortServer], *args, **kwargs):
        log.simple_log("Info:  Server Started")

        self.message_handler_map: Dict[str, rpc_server.PortServer] = {}
        port_server: rpc_server.RpcServer

        for port_server in port_server_map_list:
            log.simple_log(f"Debug: Register the  handler for the port {port_server.port_name}")
            self.message_handler_map[port_server.port_name] = port_server

        super().__init__(*args, **kwargs)

    def get_message_handler(self, handler_port_name: str) -> rpc_server.PortServer:
        return self.message_handler_map[handler_port_name]

    def do_POST(self):
        log.simple_log("Debug:in dPost")

        try:
            port_end_idx = self.path[1:].index("/")
        except ValueError:
            log.simple_log("Debug:Terminating slash for port not found, trying without")
            port_end_idx = len(self.path)

        port_name = self.path[1:port_end_idx]
        log.simple_log(f"Debug: Received port name as {port_name}, Determining   payload handler")
        try:
            message_handler: rpc_server.PortServer = self.get_message_handler(port_name)
            message_handler.payload_handler(self)
        except KeyError:
            error_msg = f"Debug: Port name:{port_name} handler not found"
            log.simple_log(error_msg)
            self.do_HEAD()
            self.wfile.write('{!r}\n'
                             .format(error_msg)
                             .encode('utf8'))

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
