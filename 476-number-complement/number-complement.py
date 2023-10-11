class Solution:
    def findComplement(self, num: int) -> int:
        ans, mul =0,1
        if num == 0:
            return 1
        while num :
            ans += (num%2 ^ 1) * mul
            num = num //2
            mul = mul*2
        return ans
            
