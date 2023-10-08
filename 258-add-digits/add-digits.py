class Solution:
    def addDigits(self, num: int) -> int:
        # while num>9:
        #     rem,ans = 0,0
        #     while num>0:
        #         rem = num %10
        #         num = num//10
        #         ans+=rem
        #     num = ans
        # return num
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9