class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = set()
        hashMapT = set()
        
        for letters in hashMapS and hashMapT:
            if letters in hashMapS not in hashMapT:
                return False
        else: return True