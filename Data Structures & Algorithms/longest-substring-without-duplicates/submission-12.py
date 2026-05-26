class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        cnt = Counter()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            if cnt[s[r]] > 1:
                maxLength = max(r - l, maxLength)
                while cnt[s[r]] > 1:
                    cnt[s[l]] -= 1
                    l += 1 
        maxLength = max(len(s) - l, maxLength)
        return maxLength 

    
