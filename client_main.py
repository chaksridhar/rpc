from transport import dream_http_rpc_client
from core import rpc_client



if __name__ == "__main__":
    rpc_port_name="RPC0"
    rpc_client_transport_http = dream_http_rpc_client.BadDreamHttpRpcClientTansport ("localhost:8000")
    rpc_client_object = rpc_client.RpcClient(rpc_client_transport_http)
    val_1=1
    val_2=2
    response = rpc_client_object.call("add", val_1,val_2)
    print(f"Response of add ({val_1}, {val_2})=  {response.result}")
    response = rpc_client_object.call("greetings")
    print(f"Response of   greetings()=  {response.result}")
