class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if len(s) != len(t):
                return False
            if s.count(char) == t.count(char):
                pass
            else: 
                return False
        return True