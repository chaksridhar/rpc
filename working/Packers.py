from abc import ABC
from typing import List, Union
import json
from common_defs import *
from typing import Dict


class Packers(ABC):
    def marshall_func_object(self, fxn_name_params: RpcFxnNameType, fxn_params: List) -> RpcPacketMarshalledReturnType:
        pass

    def unmarshall_func_object(self, pkt: RpcReturnDesc) -> List[Union[str, List]]:
        pass

    def marshall_return_value(self, result: RpcReturnDesc) -> RpcPacketMarshalledReturnType:
        pass

    def unmarshall_return_value(self, result: Dict[str, RpcReturnDesc]) -> RpcReturnDesc:
        pass


class PackerDict(Packers):
    def marshall_func_object(self, fxn_name_params: RpcFxnNameType, fxn_params_param: RpcFxnArgsAsList) -> dict:
        data = {"fxn_name": fxn_name_params, "fxn_params": fxn_params_param}
        return data

    def unmarshall_func_object(self, data_dict: dict) -> List[Union[RpcFxnNameType, RpcFxnArgsAsList]]:
        fxn_name_as_str = data_dict["fxn_name"]
        fxn_params = data_dict["fxn_params"]
        return [fxn_name_as_str, fxn_params]

    def marshall_return_value(self, result_as_rpc_desc: RpcReturnDesc) -> Dict[str, RpcReturnDesc]:
        return_value_as_json = {"status": result_as_rpc_desc.status, "result": result_as_rpc_desc.result,
                                "error_msg": result_as_rpc_desc.error_msg}
        return return_value_as_json

    def unmarshall_return_value(self, return_value_as_json: dict) -> RpcReturnDesc:
        result_as_rpc_desc = RpcReturnDesc(return_value_as_json["status"],
                                           return_value_as_json["result"],
                                           return_value_as_json["error_msg"])

        return result_as_rpc_desc


class PackerByte(Packers):
    def marshall_func_object(self, fxn_name_param: RpcFxnNameType, fxn_args: RpcFxnArgsAsList) -> bytes:
        fxn_data_as_dict: dict = PackerDict().marshall_func_object(fxn_name_param, fxn_args)
        return json.dumps(fxn_data_as_dict).encode("utf-8")

    def unmarshall_func_object(self, data_in_bytes_param: bytes) -> List[Union[RpcFxnNameType, RpcFxnArgsAsList]]:
        data_str = data_in_bytes_param.decode("utf-8")
        print ("in unmarshall")
        print(data_str)
        data_dict = json.loads(data_str)
        return PackerDict().unmarshall_func_object(data_dict)

    def marshall_return_value(self, result: RpcReturnDesc) -> RpcPacketMarshalledReturnType:
        data_dict: any = PackerDict().marshall_return_value(result)
        data_in_bytes_return = json.dumps(data_dict).encode("utf-8")
        return data_in_bytes_return

    def unmarshall_return_value(self, data_in_bytes_param: bytes) -> RpcReturnDesc:
        data_as_str: str = data_in_bytes_param.decode("utf-8")
        fxn_data_as_dict: dict = json.loads(data_as_str)
        data_any: any = PackerDict().unmarshall_return_value(fxn_data_as_dict)
        return data_any


if __name__ == "__main__":
    fxn_name_ref = "fn1"
    fxn_list_ref = [1, "3,", {"3": [8, 9]}]
    return_value = RpcReturnDesc(144, True, "OK")

    data_as_dict = PackerDict().marshall_func_object(fxn_name_ref, fxn_list_ref)
    [fxn_name, fxn_list] = PackerDict().unmarshall_func_object(data_as_dict)
    rv_as_dict = PackerDict().marshall_return_value(return_value)
    rv_from_dict = PackerDict().unmarshall_return_value(rv_as_dict)
    print(f"{rv_from_dict} ={fxn_name}, {fxn_list}")

    data_as_bytes = PackerByte().marshall_func_object(fxn_name_ref, fxn_list_ref)
    [fxn_name, fxn_list] = PackerByte().unmarshall_func_object(data_as_bytes)
    print(data_as_bytes, fxn_name, fxn_list)
