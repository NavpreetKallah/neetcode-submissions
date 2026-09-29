class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hmap = [ListNode(0,0) for _ in range(10**3)]

    def put(self, key: int, value: int) -> None:
        curr = self.hmap[key % len(self.hmap)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.hmap[key % len(self.hmap)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        prev = self.hmap[key % len(self.hmap)]
        curr = prev.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)