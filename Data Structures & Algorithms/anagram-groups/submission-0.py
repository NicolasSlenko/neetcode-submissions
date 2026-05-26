from typing import List

class Solution:
    def checkA(self, str1: str, str2: str) -> bool:
        str1 = sorted(str1)
        str2 = sorted(str2)

        if str1 == str2:
            return True
        else:
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = []

        for i in range(len(strs)):
            temp = []
            for j in range(len(strs)): 
                if self.checkA(strs[i], strs[j]):
                    temp.append(strs[j])
            if sorted(temp) not in total:
                total.append(sorted(temp))

        return total
