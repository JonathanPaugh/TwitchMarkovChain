import threading, logging
from typing import Callable

logger = logging.getLogger(__name__)

class LoopingTimer(threading.Thread):
    """
    Thread that will continuously run `target(*args, **kwargs)`
    every `interval` seconds, until program termination.
    """
    def __init__(self, getInterval, target: Callable[[], None], *args, **kwargs) -> None:
        threading.Thread.__init__(self)
        self.getInterval = getInterval
        self.target = target
        self.args = args
        self.kwargs = kwargs

        self.stopped = threading.Event()
        self.daemon = True
    
    def run(self):
        while not self.stopped.wait(self.getInterval()):
            self.target(*self.args, **self.kwargs)