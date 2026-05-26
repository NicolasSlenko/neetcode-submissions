class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        output = []

        for word in strs:
            currCount = [0] * 26
            for c in word:
                currCount[ord(c) - ord('a')] += 1

            key = tuple(currCount)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        for arr in groups.values():
            output.append(arr)
        
        return output 

        

            


        