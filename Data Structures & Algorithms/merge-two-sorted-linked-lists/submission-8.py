# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2
        

        l1 = list1
        l2 = list2
        head = None
        curr = None

        if l1.val < l2.val:
            head = l1
            curr = head
            l1 = l1.next
        else:
            head = l2
            curr = head
            l2 = l2.next

        while l1 and l2:
            if (l1.val < l2.val):
                curr.next = l1
                l1 = l1.next   
            else:
               curr.next = l2
               l2 = l2.next 
            curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return head 
            

        