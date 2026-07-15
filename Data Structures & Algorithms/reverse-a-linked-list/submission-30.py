# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return
        
        if head and not head.next:
            return head 

    
       
        prev = None
        nxt = head.next
        while head and nxt:
            head.next = prev
            prev = head
            head = nxt
            nxt = nxt.next

        head.next = prev   
        
        return head
        
        

        
