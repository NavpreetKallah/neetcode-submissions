class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0, prev=self.head)
        self.head.next = self.tail

    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_to_tail(self, node: ListNode) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._insert_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._remove(node)
            self._insert_to_tail(node)
            return

        if len(self.hashmap) == self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            self.hashmap.pop(lru_node.key)

        new_node = ListNode(key, value)
        self._insert_to_tail(new_node)
        self.hashmap[key] = new_node