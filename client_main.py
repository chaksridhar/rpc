from transport import dream_http_rpc_client


if __name__ == "__main__":
    rpc_port_name="RPC0"
    http_rpc_client = dream_http_rpc_client.DreamRpcHttpClient("localhost:8000", rpc_port_name)
    val_1=1
    val_2=2
    response = http_rpc_client.call("add", val_1,val_2)
    print(f"Response of add ({val_1}, {val_2})=  {response.result}")
    response = http_rpc_client.call("greetings")
    print(f"Response of   greetings()=  {response.result}")
