from common.common_defs import *
from abc import ABC

from typing import Type


# A TCP/HTTP  adapter will implement this.
# The args/kwargs will enable passing of  transport specific connecting parameter,
# Connect will latter post to server.
class IRpcClientTransport(ABC):
    def __init__(self, *args, **kwargs):
        pass

    def send_request(self, data_in_bytes: bytes) -> bytes:
        pass
