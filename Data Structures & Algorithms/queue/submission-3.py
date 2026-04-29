class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        node = ListNode(value)
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
        
    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        temp = self.head.next
        temp.prev = node
        node.next = temp
        node.prev = self.head
        self.head.next = node
        
    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            node = self.tail.prev
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            return node.val
             
    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            node = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            return node.val
        

        
