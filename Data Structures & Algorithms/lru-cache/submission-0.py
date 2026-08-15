class Node:
    def __init__(self, key: int = 0, val: int = 0, nxt = None, prv = None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prv = prv

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = Node()
        self.mru = Node()
        self.lru.prv = self.mru
        self.mru.nxt = self.lru

    def remove(self, node: Node):
        prv = node.prv
        nxt = node.nxt
        prv.nxt = nxt
        nxt.prv = prv

    def add(self, node: Node):
        node.nxt = self.mru.nxt
        self.mru.nxt = node
        node.nxt.prv = node
        node.prv = self.mru

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return
        
        if len(self.cache) == self.capacity:
            # eviction
            evic = self.lru.prv
            self.remove(evic)
            del self.cache[evic.key]
        
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        
