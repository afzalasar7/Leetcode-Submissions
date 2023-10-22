class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(x**0.5)
        # for i in range(5000000):
        #     if i*i > x:
        #         return i-1
        start = 1
        end = x
        ans = 0
        if x<2:
            return x
        
        while start <= end:
            mid = start + (end-start)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                ans = mid
                start=mid+1
            elif mid*mid >x:
                end = mid-1
        return ans
                  