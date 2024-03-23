from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s1 = Counter(s)
        # s2 = Counter(t)
        return True if sorted(s)==sorted(t) else False
        # for char in s:
        #     if s.count(char) = t.count(char):
        #         pass
        #     else: 
        #         return False
        # return True