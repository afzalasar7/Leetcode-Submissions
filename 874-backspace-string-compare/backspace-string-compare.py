# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s = self.processString(s)
#         t = self.processString(t)
#         return s == t
    
#     def processString(self, text: str) -> str:
#         result = []
#         for char in text:
#             if char != '#':
#                 result.append(char)
#             elif result:
#                 result.pop()  # Remove the last character if there is one
#         return ''.join(result)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1 = []
        res2 = []
        for c in s:
            if c=="#":
                if res1:
                    res1.pop()
            else:
                res1.append(c)
        for c in t:
            if c=="#":
                if res2:
                    res2.pop()
            else:
                res2.append(c)
        return res1==res2