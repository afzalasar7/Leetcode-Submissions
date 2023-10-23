class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return True if n>0 and log(n, 4) %1==0 else False
        