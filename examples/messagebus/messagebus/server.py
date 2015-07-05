from __future__ import print_function
import sys
from . import PYRO_MSGBUS_NAME
from .messagebus import make_messagebus, MessageBus
import Pyro4


Pyro4.config.COMMTIMEOUT = 30.0
Pyro4.config.POLLTIMEOUT = 10.0
Pyro4.config.MAX_MESSAGE_SIZE = 256*1024     # 256 kb
Pyro4.config.MAX_RETRIES = 3

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("provide storage type as argument (sqlite/memory)")
    if sys.argv[1] not in ("sqlite", "memory"):
        raise ValueError("invalid storagetype")
    make_messagebus.storagetype = sys.argv[1]
    Pyro4.Daemon.serveSimple({
        MessageBus: PYRO_MSGBUS_NAME
    })
