class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            outputList = count.get(tuple(arr), [])
            outputList.append(word)
            count[tuple(arr)] = outputList

        return list(count.values())

        