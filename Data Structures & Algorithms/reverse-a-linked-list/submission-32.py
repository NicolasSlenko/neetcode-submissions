# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
        # 1. Save the next node so we don't lose the rest of the list
            nxt = curr.next  
            
            # 2. Reverse the link (point current node backward)
            curr.next = prev  
            
            # 3. Move 'prev' one step forward to the current node
            prev = curr       
            
            # 4. Move 'curr' one step forward to the saved next node
            curr = nxt
        
        return prev 
        
        
        

        
