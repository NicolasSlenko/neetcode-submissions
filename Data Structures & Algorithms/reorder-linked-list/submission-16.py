# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        dummy = head

        #find halfway point
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        #set halfway
        secondHalf = slow.next
        slow.next = None

        #reverse second half of list
        prev = None
        current = secondHalf
        
        while(current):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        #get new connections using head and prev pointers
        while(prev):
            temp = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp
            head = temp
            prev = temp2
        
        

            




       