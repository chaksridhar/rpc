import user_app
import functools

from abstract_interface import irpc_xport_adapter
from adapter.http.bad_dream_adapter import dream_rpc_adapter
from transport.http import bad_dream_http_rpc_server

from http.server import HTTPServer
from dream_rpc import dream_rpc_server

if __name__ == '__main__':
    # def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    def run(port=8000):
        print("staring the server")
        rpc_server_obj = dream_rpc_server.RpcServer()
        rpc_server_obj.register_rpc_fxn("add", user_app.add)
        rpc_server_obj.register_rpc_fxn("greetings", user_app.greetings)
        rpc_server_obj.register_rpc_fxn("max_array", user_app.max_array)
        dream_rpc_server_adapter_obj: irpc_xport_adapter.IRpcServerTransportAdapter = \
           dream_rpc_adapter.DreamRpcServerAdapter(rpc_server_obj)
        handler = functools.partial(bad_dream_http_rpc_server.HttpServer, dream_rpc_server_adapter_obj)
        server = HTTPServer(('', port), handler)

        server.serve_forever()


    run()
