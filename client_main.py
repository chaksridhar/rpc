from dream_rpc  import dream_rpc_client
from  adapter.http.bad_dream_adapter import dream_rpc_adapter

if __name__ == "__main__":
    rpc_client_object:dream_rpc_client.DreamRpcClient = dream_rpc_client.DreamRpcClient(dream_rpc_adapter.DreamRpcClientAdapter,
                                                                                        "localhost:8000")
    val_1=1
    val_2=2
    response = rpc_client_object.dispatch_payload("add", val_1,val_2)
    print(f"Response of add ({val_1}, {val_2})=  {response.result}")
    response = rpc_client_object.dispatch_payload("greetings")
    print(f"Response of   greetings()=  {response.result}")
