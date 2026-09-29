class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**3)]

    def add(self, key: int) -> None:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        prev = self.set[key % len(self.set)]
        curr = prev.next
        while curr:
            if curr.key == key:
                prev.next = curr.next 
                return
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)