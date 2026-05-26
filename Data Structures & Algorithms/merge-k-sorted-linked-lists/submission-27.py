class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        headptrs = []
        minVal = float('inf')

        # append all heads to list
        for i in range(len(lists)):
            if lists[i]:
                headptrs.append(lists[i])

        # find initial smallest value to be head of final list
        globalheadptr = None
        min_index = -1
        for i in range(len(headptrs)):
            currentVal = headptrs[i].val
            if currentVal < minVal:
                globalheadptr = headptrs[i]
                minVal = currentVal
                min_index = i
        
        # advance the pointer in the list that provided the head
        if min_index != -1:
            headptrs[min_index] = headptrs[min_index].next
            if headptrs[min_index] is None:
                del headptrs[min_index]
        
        globaltailptr = globalheadptr
        
        while headptrs:
            smallest = float('inf')
            current = None
            min_index = -1
            for i in range(len(headptrs)):
                if headptrs[i] is not None:
                    currentVal = headptrs[i].val
                    if currentVal < smallest:
                        current = headptrs[i]
                        smallest = currentVal
                        min_index = i

            if current is None:
                break

            globaltailptr.next = current
            globaltailptr = current  # Move the tail forward

            headptrs[min_index] = headptrs[min_index].next
            if headptrs[min_index] is None:
                del headptrs[min_index]

        return globalheadptr