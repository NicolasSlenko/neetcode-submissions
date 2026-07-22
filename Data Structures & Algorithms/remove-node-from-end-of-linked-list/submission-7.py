# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # 2. Move fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # 3. Move both pointers until fast hits the end of the list
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # 4. slow is now right before the target node. Skip it!
        slow.next = slow.next.next
        
        # 5. Return the true head of the list
        return dummy.next
    

        




        

