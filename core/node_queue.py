from queue import SimpleQueue

from core.singleton import Singleton
from app.settings import VIDEO_NODES


class NodeQueue(metaclass=Singleton):
    def __init__(self):
        if not hasattr(self, '__node_queue'):
            self.__node_queue = SimpleQueue()
            self.__init_queue()

    def __init_queue(self):
        for node in VIDEO_NODES:
            self.__node_queue.put(node)

    def get_node(self):
        node = self.__node_queue.get()
        self.__node_queue.put(node)
        return node
