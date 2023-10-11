# class Solution:
#     def reverse(self, x: int) -> int:
#         MIN = float('-inf')
#         MAX = float('inf')
#         ans = 0
#         y = x
#         while x !=0:
#             if ans*10 < MAX and ans*10 > MIN:
#                 ans= ans*10 + x%10
#             else:
#                 return 0     
#             x = x//10
#         return ans

class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)

        flag = -1 if x < 0 else 1
        ans = 0
        x = abs(x)

        while x > 0:
            digit = x %10
            if ans > max_int/10:
                return 0
            ans = (ans*10) + digit
            x //=10
        
        return ans * flag