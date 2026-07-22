# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        nxt = curr.next
        count = 0


        if not head or n == 1 and not head.next:
            return None 

        while curr:
            count+=1
            prev = curr
            curr = curr.next 
        
        curr = head
        if count == n:
            curr.next = None
            return nxt
        prev = None
        pos = 0

        while pos != count - n:
            prev = curr
            curr = nxt
            nxt = nxt.next
            pos += 1 
        
        prev.next = nxt
        curr.next = None
    
        return head
    

        




        

