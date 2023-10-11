class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans, mul =0,1
        if n == 0:
            return 1
        while n :
            ans += (n%2 ^ 1) * mul
            n = n //2
            mul = mul*2
        return ans
            
