from rpc_app_server import *
import Packers


class RpcServerHttp(RpcServer):
    def __init__(self, port_name: str):
        print(f"INFO: RPC server populated with name {port_name}")
        super().__init__(port_name)

    def payload_handler(self, transport_hdl: BaseHTTPRequestHandler):
        print("Debug: IN payload handler Unpacking payload")
        length = int(transport_hdl.headers.get('content-length'))
        func_obj_bytes = transport_hdl.rfile.read(length)
        print(f"Debug: IN payload handler Unpacking payload {func_obj_bytes}")

        packer_bytes: Packers.PackerByte = Packers.PackerByte()
        [fxn_name, fxn_args] = packer_bytes.unmarshall_func_object(func_obj_bytes)
        print(f"Debug: In payload_handler obtained fxn  {fxn_name} with  params {fxn_args}")
        return_desc = RpcReturnDesc()
        try:
            print(f"Debug calling the  rpc function {fxn_name}")
            fxn = self.get_rpc_fxn(fxn_name)
            result = fxn(*fxn_args)
            return_desc.result = result
        except KeyError:
            return_desc.status = False
            return_desc.error_msg = f"{fxn_name} not found"

        transport_hdl.send_response(200)
        transport_hdl.send_header('Content-type', 'application/json')
        transport_hdl.end_headers()
        print(f"value returned = {return_desc}")
        data_in_bytes: RpcPacketMarshalledReturnType = packer_bytes.marshall_return_value(return_desc)
        transport_hdl.wfile.write(data_in_bytes)