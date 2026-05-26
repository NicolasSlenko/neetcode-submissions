# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 0
        while(current):
            size+=1
            current = current.next   
        
        if n == size:
            temp = head.next
            head.next = None
            head = temp

        else:
            current = head
            counter = size - n
            prev = None
            for i in range(counter):
                prev = current
                current = current.next
            nxt = current.next
            current.next = None
            prev.next = nxt
            
                



        return head 

        

        

