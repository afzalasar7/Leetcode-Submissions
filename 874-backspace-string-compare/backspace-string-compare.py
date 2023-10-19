class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.processString(s)
        t = self.processString(t)
        return s == t
    
    def processString(self, text: str) -> str:
        result = []
        for char in text:
            if char != '#':
                result.append(char)
            elif result:
                result.pop()  # Remove the last character if there is one
        return ''.join(result)
