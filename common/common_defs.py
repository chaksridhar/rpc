from typing import TypeVar, Callable, NewType

from dataclasses import dataclass

PacketDictValueType = TypeVar("PacketDictValueType", str, Callable)

RpcPacketMarshalledReturnType = TypeVar("RpcPacketMarshalledReturnType", str, bytes, dict)
RpcSerVer = NewType("RpcServer", None)
RpcFxnType = Callable
RpcFxnNameType = str
RpcFxnArgsAsList = list



@dataclass
class RpcReturnDesc:
    result: any = None
    status: bool = True
    error_msg: str = ""
