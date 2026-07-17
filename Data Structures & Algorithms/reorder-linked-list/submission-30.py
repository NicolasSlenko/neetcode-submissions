# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        
        
        left = head
        right = head
        nodeMap = {}
      

      
        while right.next:
            nodeMap[right.next] = right
            right = right.next
        

        while True:
            #even node case
            if left == right:
                left.next = None
                break

            if left.next == right:
                right.next = None
                break

            tempL = left.next
            left.next = right
            left = tempL

            tempR = nodeMap[right]
            right.next = left
            right = tempR

            

       



        