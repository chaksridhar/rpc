from http.server import HTTPServer
from transport.bad_dream_http_server import *
from transport.dream_http_rpc_server import *
import logging
import functools

from sys import argv
from user_app import *

if __name__ == '__main__':
    # def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    def run(port=8000):

        rpc_port_name="RPC0"
        print(f"Debug: Initializing the DreamRpcServer at port:{rpc_port_name}")
        rpc_server_http = DreamRpcHttpServer("RPC0")
        rpc_server_http.register_rpc_fxn("add", add)
        rpc_server_http.register_rpc_fxn("greetings", greetings)
        handler = functools.partial(BadDreamHttpHandler, [rpc_server_http])
        server = HTTPServer(('', port), handler)

        server.serve_forever()


    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
