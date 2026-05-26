
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        globalMap = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord('a')] += 1
            globalMap[tuple(temp)].append(word)
        
        return list(globalMap.values())


