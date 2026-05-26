class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) == 1:
            return 1
        l = 0
        cnt = Counter()
        res = 0

        for r in range(len(s)):
            cnt[s[r]] += 1
            length = r - l + 1
            if (length) - max(cnt.values()) <= k:
                res = max(res, length)
            else:
                while r - l + 1 - max(cnt.values()) > k:
                    cnt[s[l]] -= 1
                    l += 1
        return res
            

                

        


        