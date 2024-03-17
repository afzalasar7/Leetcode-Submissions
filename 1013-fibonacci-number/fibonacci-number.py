class Solution:
    def fib(self, n: int,a =0, b=1) -> int:
        if n ==0:
            return a    
        return self.fib(n-1,b, a+b)
