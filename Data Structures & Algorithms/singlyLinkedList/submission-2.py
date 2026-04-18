class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def get(self, index: int) -> int:

        if index < 0 or not self.head:
            return -1
        
        curr = self.head
        count = 0
        while(curr):
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:

        head = ListNode(val)

        if self.head:
            head.next = self.head
        else:
            self.head = self.tail = head

        self.head = head
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)

        if not self.tail:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
    def remove(self, index: int) -> bool:

        if index < 0 or not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        
        curr = self.head

        for i in range(index-1):
            if not curr.next:
                return False
            curr = curr.next

        if not curr.next:
            return False
        
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True
            
    def getValues(self) -> List[int]:
        if not self.head:
            return []
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
