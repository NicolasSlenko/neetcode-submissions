class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #bucketsort list (n appears c amount of times)
        freq = [[] for i in range(len(nums) + 1 )]

        #initailize hashmap 
        for n in nums:
            count[n] = 1 + count.get(n, 0)


        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res




            

        
        
        