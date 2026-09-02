class Node:
    def __init__(self,key = 0,value = 0):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left

    def insert(self,node):#insert at right
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev

    def remove(self,node):#remove
        prev = node.prev
        next_ = node.next
        prev.next = next_
        next_.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        else: 
            self.cache[key] = Node()
            node = self.cache[key]
            node.key = key
            node.val = value
            self.insert(node)
        if(len(self.cache) > self.cap):
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)