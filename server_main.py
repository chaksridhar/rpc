from transport import dream_http_rpc_server
from core import rpc_server
import user_app
import functools
from http.server import HTTPServer

from transport import dream_http_rpc_server

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
        rpc_server_obj = rpc_server.RpcServer()
        rpc_server_obj.register_rpc_fxn("add", user_app.add)
        rpc_server_obj.register_rpc_fxn("greetings", user_app.greetings)
        handler = functools.partial(dream_http_rpc_server.BadDreamHttpRpcServerTransport, rpc_server.callback_handler,rpc_server_obj)
        server = HTTPServer(('', port), handler)

        server.serve_forever()


    run()
