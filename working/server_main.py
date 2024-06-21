
from http.server import HTTPServer
from http_server import *
from http_rpc_app_server import *
import functools


from sys import argv


def add(num_1: int, num_2: int) -> int:
    print("Debug: Calling add")
    return num_1 + num_2


if __name__ == '__main__':
    # def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    def run(port=8000):
        '''
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)

        httpd.serve_forever()
        rpc_server_http: RpcServer = RpcServerHttp( httpd.RequestHandlerClass, "json")
        rpc_server_http.register_rpc_fxn("add", add)
        '''

        print("staring the server")
        rpc_server_http = RpcServerHttp("RPC0")
        rpc_server_http.register_rpc_fxn("add", add)
        handler = functools.partial(SimpleRequestHandler, [rpc_server_http])
        server = HTTPServer(('', port), handler)

        server.serve_forever()


    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
