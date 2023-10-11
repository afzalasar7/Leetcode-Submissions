class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(x**0.5)
        for i in range(5000000):
            if i*i > x:
                return i-1