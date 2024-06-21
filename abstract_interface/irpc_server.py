from common.Packers import *
from common import log
from typing import Callable
from typing import Type
from abc import ABC


class IRpcServer(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def register_rpc_fxn(self, fxn_name: str, fxn: Callable):
        pass

    def get_rpc_fxn(self, fxn_name: str) -> Callable:
        pass

    def execute_rpc_fxn(self, func_obj_in_bytes: bytes) -> bytes:
        pass



