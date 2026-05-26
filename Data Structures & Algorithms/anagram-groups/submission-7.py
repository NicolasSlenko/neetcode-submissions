class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        output = []

        for i in range(len(strs)):
            counter = [0] * 26
            for char in strs[i]:
                index = ord(char) - ord('a')
                counter[index] +=1 
            final = tuple(counter)

            if group.get(final, None) != None:
                group[final].append(strs[i])
            else:
                group[final] = [strs[i]]
        

        for anagram in group:
            curr = []
            for word in group[anagram]:
                curr.append(word)
            output.append(curr)
        return output 
            



        

            


        