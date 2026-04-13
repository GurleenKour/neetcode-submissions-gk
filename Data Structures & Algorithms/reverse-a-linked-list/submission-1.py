# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        p = head
        n = head.next
        head.next = None
        
        while n:
            ah = n.next
            n.next = p
            p = n
            n = ah
        
        return p
             