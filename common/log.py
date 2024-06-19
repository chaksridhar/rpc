import logging

logger = logging.getLogger("ZeissRpc")
logging.basicConfig(filename='example.log',  level=logging.DEBUG)


def  simple_log(*args):
    logging.debug(args)
