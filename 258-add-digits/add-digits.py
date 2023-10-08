class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            rem,ans = 0,0
            while num>0:
                rem = num %10
                num = num//10
                ans+=rem
            num = ans
        return num