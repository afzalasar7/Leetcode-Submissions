class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = [2**x for x in range (31)]
        if n in power:
            return True
        