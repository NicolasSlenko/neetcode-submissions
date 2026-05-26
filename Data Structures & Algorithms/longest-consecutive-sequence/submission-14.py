class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        visited = set()
        maxCount = 1

        if not nums:
            return 0

        for i in nums:
            seen.add(i)
        
        for i in nums:
            count = 1
            if i in visited:
                continue 
            while i + 1 in seen:
                count += 1
                visited.add(i+1)
                i+=1
            
            if count > maxCount:
                maxCount = count 

        
        return maxCount 
