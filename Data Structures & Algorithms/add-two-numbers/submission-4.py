# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = tail = ListNode()
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry

            if val >= 10:
                rem = val % 10
                carry = 1
                newNode = ListNode(rem)           
            else:
                newNode = ListNode(val)
                carry = 0

            tail.next = newNode 
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        
        while l1 or l2 or carry:
            val = 0
            if l1:
                val = l1.val
            elif l2:
                val = l2.val
            print(val)
            finalVal = val + carry

            if finalVal >= 10:
                rem = finalVal % 10
                print(rem)
                carry = 1
                newNode = ListNode(rem)
            else:
                carry = 0
                newNode = ListNode(finalVal)
            tail.next= newNode
            tail= tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next



        