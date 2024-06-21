
import user_app
import functools
from http.server import HTTPServer
from dream_rpc import  dream_rpc_server
from adapter.http.bad_dream_adapter import dream_rpc_adapter
from transport.http import bad_dream_http_rpc_server


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
        rpc_server_obj = dream_rpc_server.RpcServer()
        rpc_server_obj.register_rpc_fxn("add", user_app.add)
        rpc_server_obj.register_rpc_fxn("greetings", user_app.greetings)
        handler = functools.partial(bad_dream_http_rpc_server.HttpServer, dream_rpc_adapter.dream_rpc_server_adapter, rpc_server_obj)
        server = HTTPServer(('', port), handler)

        server.serve_forever()


    run()
