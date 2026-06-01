class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        seen = defaultdict(int)
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])

        print(len(bucket))

        for i, num in enumerate(nums):
            seen[num] += 1
        
        for num, freq in seen.items():
            bucket[freq].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    return res


        
        return res
        
    

        
        



