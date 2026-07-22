"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_new = {}
        if not head:
            return None
        
        #first pass, intialize list
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        #second pass, update the pointers using the references
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]

            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            else:
                old_to_new[curr].random = None
            curr = curr.next
        
        return old_to_new[head]