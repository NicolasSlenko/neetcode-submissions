class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += s
            string += '123_231'

        return string 

    def decode(self, s: str) -> List[str]:
        decoded = []
        start = 0
        current = 0
        
        def checkNextSix(s: str, startIndex: int) -> bool:
            finishIndex = startIndex + 7
            substr = s[startIndex:finishIndex]

            if len(substr) != 7:
                return False
            else:
                if substr == '123_231':
                    return True
                return False 

        while(current < len(s)):
            if checkNextSix(s, current):
                # Add the substring from `start` to `current` to the decoded list
                decoded.append(s[start:current])
                # Skip over the delimiter
                current += 7
                # Move start to the new position after the delimiter
                start = current
            else:
                # Move to the next character
                current += 1

        return decoded
                    
            


        
