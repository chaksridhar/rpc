from typing import List
from rpc_app_server import *


class SimpleRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, port_server_map_list: List[PortServer], *args, **kwargs):
        print("INFO:  Server Started")

        self.message_handler_map: Dict[str, PortServer] = {}
        port_server: "RpcServer"

        for port_server in port_server_map_list:
            print(f"Debug: Register the  handler for the port {port_server.port_name}")
            self.message_handler_map[port_server.port_name] = port_server
        print (args, kwargs)
        super().__init__(*args, **kwargs)

    def get_message_handler(self, handler_port_name: str) -> PortServer:
        return self.message_handler_map[handler_port_name]

    def do_POST(self):
        print("Debug:in post")

        try:
            port_end_idx = self.path[1:].index("/")
        except ValueError:
            print("Warning:Terminating slash for port not found, trying without")
            port_end_idx = len(self.path)

        port_name = self.path[1:port_end_idx]
        print(f"Debug: Received port name as {port_name}, Determining   payload handler")
        try:
            message_handler: PortServer = self.get_message_handler(port_name)
            message_handler.payload_handler(self)
        except KeyError:
            error_msg = f"Warning: Port name:{port_name} handler not found"
            print(error_msg)
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
