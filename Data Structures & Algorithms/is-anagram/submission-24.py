class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}

        for let in s:
            letters_s[let] = letters_s.get(let, 0) + 1 # get value if it exists, else ret 0
        
        for let in t:
            letters_t[let] = letters_t.get(let, 0) + 1

        return letters_s == letters_t