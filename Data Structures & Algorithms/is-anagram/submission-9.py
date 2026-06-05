class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        HashMapS, HashMapT = {}, {}
        for letter in range(len(s)):
            HashMapS[s[letter]] = 1 + HashMapS.get(s[letter], 0)
            HashMapT[t[letter]] = 1 + HashMapT.get(t[letter], 0)
        for count in HashMapS:
            if HashMapS[count] != HashMapT.get(count, 0):
                return False
        return True

            