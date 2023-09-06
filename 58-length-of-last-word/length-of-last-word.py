class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # length = 0
        # s=s.strip()
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == ' ':
        #         break
        #     length += 1
    
        # return length

        return len( s.split()[-1])