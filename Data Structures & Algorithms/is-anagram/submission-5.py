class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = set()
        for char in str(s) and str(t):
            if str(s).length != str(t).length:
                return False
            if s.char in t.char:
                return True
            else:
                return False 