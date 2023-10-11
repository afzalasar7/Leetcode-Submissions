class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # power = [2**x for x in range (31)]

        
        # high = len(power)-1
        # low = 0
        # while True:
        #     mid = (high + low)//2
        #     if power[mid] == n:
        #         return True
        #     if high == low:
        #         return 0
        #     elif power[mid] > n:
        #         high = mid - 1
        #     elif power[mid] < n:
        #         low = mid + 1 
            
        # if n in power:
        #     return True
        if n==0 or n == -abs(n):
            return False
        while n > 1:
            if n%2==0:
                n = n/2
            elif n%2 != 0:
                return False
        return True   
            