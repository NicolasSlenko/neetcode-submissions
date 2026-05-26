class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = {}
        for char in t:
            chars[char] = chars.get(char, 0) + 1

        required = len(chars)
        formed = 0
        window_counts = {}
        l = 0
        res = float('inf')
        output = ""

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in chars and window_counts[char] == chars[char]:
                formed += 1

            while formed == required:
                if r - l + 1 < res:
                    res = r - l + 1
                    output = s[l:r+1]

                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in chars and window_counts[left_char] < chars[left_char]:
                    formed -= 1
                l += 1

        return output
