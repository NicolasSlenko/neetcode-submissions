class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num,0) + 1

        l = []

        for num, cnt in hmap.items():
            l.append((cnt,num))
            print((cnt, num))

        l.sort(reverse = True)

        res = []
       
        while len(l) > k:
            l.pop()
      
        for val in l:
            res.append(val[1])
        return res


