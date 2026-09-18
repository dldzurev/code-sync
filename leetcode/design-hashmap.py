class Node:
    def __init__(self,key=-1,val=-1,nxt=None):
        self.key = key
        self.val = val
        self.next = nxt
class MyHashMap:

    def __init__(self):
        self.mymap = [Node() for i in range (1000)]
    def put(self, key: int, value: int) -> None:
        curr = self.mymap[key%1000]
        while curr.next != None:
            if(curr.next.key == key):
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node()
        curr.next.val = value
        curr.next.key = key
        return
        

    def get(self, key: int) -> int:
        curr = self.mymap[key%1000]
        while(curr.next != None):
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.mymap[key%1000]
        while(curr.next != None):
            if (curr.next.key == key):
                curr.next = curr.next.next
                return
            curr = curr.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)