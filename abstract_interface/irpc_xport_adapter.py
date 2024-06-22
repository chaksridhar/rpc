
from abc import ABC
from common import common_defs


# A TCP/HTTP  adapter will implement this.
# The args/kwargs will enable passing of  transport specific connecting parameter,
# Connect will latter post to server.
class IRpcClientTransportAdapter(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def execute_fxn_payload(self, *args, **kwargs) -> common_defs.RpcReturnDesc:
        pass


class IRpcServerTransportAdapter(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def execute_fxn_payload(self, *args, **kwargs) -> any:
        pass
