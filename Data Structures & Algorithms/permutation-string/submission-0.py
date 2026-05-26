class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False 
        
        s1_count = Counter(s1)
        window = Counter()

        for i in 'abcdefghijklmnopqrstuvwxyz':
            window[i] = 0
            s1_count[i] = s1_count.get(i,0)
            

        r = len(s1) - 1 

        for l in range(r+1):
            window[s2[l]] += 1
        
        if s1_count == window:
            return True 

        l = 0
        while r < len(s2) - 1:
            window[s2[l]] -= 1
            l+=1
            r+=1 
            window[s2[r]] += 1

            if window == s1_count:
                return True 

        return False 



        